import copy
import os
import socket
import json
import sys
import threading
from threading import Thread
from .manager import QYAMLDBCoarse, QYAMLDB, QYAMLDBFine
import logging
from cryptography.fernet import Fernet

READ_COMMANDS = ['$query']
WRITE_COMMANDS = ['$insert', '$insert_many', '$update', '$update_many', '$delete'
    , '$delete_many', '$del_many', '$del', '$create_table']


# Declare a class DaemonError to denote that daemon cannot start
class DaemonError(Exception):
    pass


class DatabaseDaemonBase:

    def __init__(self, dbpath, key, encrypted, encryption_key=None, **kwargs):

        """
        Initialize the DatabaseDaemon object.

        Parameters:
            dbpath (str): The path to the database.
            key (str): The encryption key.
            encrypted (bool): Flag indicating if the data is encrypted.
            encryption_key (str, optional): The encryption key to use. Defaults to None.
        Keyword Arguments:
            enable_logging (bool): Flag indicating whether logging is enabled. Defaults to False.
            log_file (str): The file path for the log file. Defaults to 'qyaml.log'.
            db_type (str, optional): The type of database. Defaults to 'Fine'. (Choices: 'Fine', 'Coarse', 'Normal')
            silent (bool): Flag indicating whether logging is silent. Defaults to False.
        Returns:
            None
        """
        self.db_path = dbpath
        self.key_path = key
        self.encrypted = encrypted
        self.encryption_key = encryption_key
        self.fernet = Fernet(encryption_key) if encryption_key else None
        self.running = False
        self._db_type = kwargs.get('db_type', 'Fine')
        self.enable_log = kwargs.get('enable_logging', True)
        self.silent = kwargs.get('silent', False)

        self.level = kwargs.get('level', logging.DEBUG)
        self.log_file = kwargs.get('log_file', 'daemon.log')
        self.mode = kwargs.get('mode', 'batch') # batch uses db.batch_process and 'single' uses db.execute_command in commit mode.
        # Setup logging
        self.logger = logging.getLogger('DatabaseDaemon')
        self.logger.setLevel(logging.DEBUG)
        if self.enable_log:
            fh = logging.FileHandler(self.log_file)
        else:
            fh = logging.NullHandler()

        formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')

        fh.setLevel(self.level)

        if not self.silent:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        self.logger.info("DatabaseDaemon initialized.")

    def _encrypt_message(self, message):
        if self.fernet:
            encrypted_message = self.fernet.encrypt(message.encode('utf-8'))
            self.logger.debug("Message encrypted.")
            return encrypted_message
        return message.encode('utf-8')

    def _decrypt_message(self, message):
        if self.fernet:
            decrypted_message = self.fernet.decrypt(message).decode('utf-8')
            self.logger.debug("Message decrypted.")
            return decrypted_message
        return message.decode('utf-8')

    def _setup_db(self):
        self.logger.info("Setting up database ...")
        print("Setting up database ....")
        if self._db_type == 'Normal':
            self.database = QYAMLDB(self.db_path, self.key_path, self.encrypted, enable_logging=self.enable_log,
                                    silent=self.silent,
                                    log_level=self.level, log_file=self.log_file)
        elif self._db_type == 'Coarse':
            self.database = QYAMLDBCoarse(self.db_path, self.key_path, self.encrypted, enable_logging=self.enable_log,
                                          silent=self.silent,
                                          log_level=self.level, log_file=self.log_file)
        else:
            self.database = QYAMLDBFine(self.db_path, self.key_path, self.encrypted, enable_logging=self.enable_log,
                                        silent=self.silent,
                                        log_level=self.level, log_file=self.log_file)
        # loading not required due to auto_load feature
        # try:
        #     self.database.load_db()
        #     self.logger.info("Database loaded successfully.")
        #     print("Database Loaded Successfully")
        # except Exception as e:
        #     self.logger.error(f"Initialization of the database failed: {e}")
        #     raise Exception(f"Initialization of the database failed: {e}")

    def start(self):
        self.running = True
        self._setup_db()
        self.logger.info("Database Daemon started.")

    def stop(self):
        self.running = False
        self.logger.info("Database Daemon stopped.")

    def _process_command(self, command):
        self.logger.info(f"Processing command: {command}")

    def run(self):
        self.logger.info("Daemon running.")
        # This should be implemented in subclass
        raise NotImplementedError("Daemon run loop not implemented.")


class DataBaseSocketDaemon(DatabaseDaemonBase):
    def __init__(self, dbpath, key, encrypted=False, **kwargs):
        # TODO Use KWARGS
        """
        Initializes Socket-Based Database Daemon
        Parameters:
            dbpath (str): The path to the database.
            key (str): The encryption key.
            encrypted (bool): Flag indicating if the data is encrypted.

        Keyword Arguments:
            socket_path (str): The path to the socket.
            socket_type (str): The type of socket (unix or inet).
            address (str): The address of the socket.
            port (int): The port of the socket.
        Returns:
            None
        """

        super().__init__(dbpath, key, encrypted, **kwargs)

        self.socket_type = kwargs.get('socket_type', 'unix')
        self.socket_path = kwargs.get('socket_path', None)  # For unix socket
        self.address = kwargs.get('address', None) # for inet
        self.port = kwargs.get('port', None)

        # Validate the socket type
        if self.socket_type not in ['unix', 'inet']:
            raise ValueError("Unsupported socket type")

        # Validate the socket path
        if self.socket_type == 'unix':
            if not self.socket_path:
                raise ValueError("Socket path must be specified for unix socket")
        elif self.socket_type == 'inet':
            if not self.address or not self.port:
                raise ValueError("Address and port must be specified for inet sockets")
        else:
            raise ValueError("Unsupported socket type")
        self.server_socket = None
        self._threads = []
        self.logger.info("DataBaseIPCDaemon initialized with socket type: " + self.socket_type)

    def start(self):
        """
        Starts the socket-based database daemon.
        """
        self._setup_db()

        if self.socket_type == 'unix':
            try:
                os.unlink(self.socket_path)
            except OSError:
                if os.path.exists(self.socket_path):
                    self.logger.error('Socket path already exists')
                    raise Exception('Socket path exists')
            self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            socket_bind_address = self.socket_path
        elif self.socket_type == 'inet':
            if not self.address or not self.port:
                raise ValueError("Address and port must be specified for inet sockets")
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_bind_address = (self.address, self.port)
        else:
            raise ValueError("Unsupported socket type")

        try:
            self.server_socket.bind(socket_bind_address)
            self.server_socket.listen(5)
            self.logger.info('Listening for client connections on {}'.format(socket_bind_address))
            while True:
                connection, address = self.server_socket.accept()
                self.logger.info("A client has been connected")
                ct = Thread(target=self._handle_client, args=(connection, address,))
                ct.start()
                self._threads.append(ct)
        except Exception as e:
            self.logger.error("Error in socket setup: {}".format(str(e)))
        finally:
            for t in self._threads:
                t.join()
            self.server_socket.close()
            self.logger.info('Socket connection has been terminated.')

    def _handle_client(self, client_socket, mask=None):
        """
        Handle the client connection by receiving, processing, and sending messages.

        Parameters:
            client_socket: the socket object for the client connection
            mask: optional parameter to be used for handling the client (default is None)

        Returns:
            None
        """
        # First, receive the length of the incoming message
        while True:
            data_length = client_socket.recv(8)

            print(data_length)

            if not data_length:
                continue
            # Convert the length to an integer
            message_length = int(data_length.decode('utf-8'))
            self.logger.info(f"Received message length: {message_length}")
            # Send ack after receiving length to signal
            client_socket.send("ACK".encode('utf-8'))
            # Now receive the rest of the message based on the length
            data = client_socket.recv(message_length)
            self.logger.debug('Received data: ' + data.decode('utf-8'))

            # Now that the complete message has been received, proceed with decryption and processing
            try:
                decrypted_command = self._decrypt_message(data)
                command = json.loads(decrypted_command)
                response = self._process_command(command)
                encrypted_response = self._encrypt_message(json.dumps(response))

                # send the length of data
                response_length = str(len(encrypted_response))
                client_socket.send(response_length.encode('utf-8'))
                # wait for acknowledgement from the client.
                ack = client_socket.recv(1024).decode('utf-8')
                self.logger.info(f"Received acknowledgement from client: {ack}")
                # Send actual response
                client_socket.send(encrypted_response)

            except Exception as e:
                print(f"Error processing command: {e}")
                error_response = self._encrypt_message(json.dumps({'error': str(e)}))
                client_socket.send(error_response)

    def _process_command(self, command):
        """Process the received command."""

        status = self.database.batch_process(command)
        return status

    def stop(self):
        """
        Stops the daemon. Closes the server socket.
        """
        # Close the connection
        self.running = False
        self.server_socket.close()


class DBDClientBase:
    """Base class that encompasses the client interface to communicate between the Daemon Socket"""

    def __init__(self):
        self._transaction = 0
        self._failed_transactions = 0
        self._success_transactions = 0
        self.results = None

    # Set of abstract methods
    def connect(self):
        raise NotImplementedError('Override this method.')

    def disconnect(self):
        raise NotImplementedError('Override this method.')

    def send(self, command):
        raise NotImplementedError('override this method.')


class DBDSSocketClient(DBDClientBase):
    """
    Client class for Unix/Inet socket for Socket Server.

    Attributes:
     socket_type: type of socket (unix or inet)
     socket_path: path of the socket
     address: address of the socket
     port: port of the socket
     client_socket: socket object
     encryption_key: encryption key to use to send or receive messages.

    """

    def __init__(self, socket_type, socket_path, address=None, port=None,
                 encryption_key: Fernet = None):
        self.socket_type = socket_type
        self.socket_path = socket_path
        self.address = address
        self.port = port
        self.client_socket = None
        self.encryption_key = encryption_key
        # A lambda function to encrypt data on transit.
        self.encrypt = lambda x: self.encryption_key.encrypt(x) if encryption_key is not None else x
        super().__init__()

    def connect(self):
        """
        Connects to the socket

        """
        if self.socket_type == 'unix':
            self.client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            socket_connect_address = self.socket_path
        elif self.socket_type == 'inet':
            if not self.address or not self.port:
                raise ValueError("Address and port must be specified for inet sockets")
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connect_address = (self.address, self.port)
        else:
            raise ValueError("Unsupported socket type")

        try:
            self.client_socket.connect(socket_connect_address)

        except Exception as e:
            raise e

    def disconnect(self):
        """Disconnect the socket"""
        self.client_socket.close()

    def send(self, command):
        """
        Send the command to the server and receives the response

        Parameters:
         command: the command to be sent in json format

        Returns:
         The response from the server as json

        Raises:
         ConnectionError: if there is an error in sending the command

         Exception: For any other error.

        """
        try:
            # send the length of data
            command = json.dumps(command).encode('utf-8')

            encrypted_command = self.encrypt(command)

            command_length = str(len(encrypted_command))
            encrypted_command_length = self.encrypt(command_length.encode())
            self.client_socket.send(encrypted_command_length)
            # wait for acknowledgement from the client.
            ack = self.client_socket.recv(1024).decode('utf-8')

            if ack == 'ACK':
                # Send actual response
                self.client_socket.send(command)
                # get the results length
                results_length = int(self.client_socket.recv(8).decode('utf-8'))
                # send ACK and get the actual result
                self.client_socket.send(b'ACK')
                result = self.client_socket.recv(results_length).decode('utf-8')
                return json.loads(result)

            else:
                raise ConnectionError('Did not receive the ACK from the server')

        except Exception as e:
            raise e
