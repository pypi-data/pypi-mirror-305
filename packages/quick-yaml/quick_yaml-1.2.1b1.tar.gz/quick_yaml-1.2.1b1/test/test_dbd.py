"""
This is Work In Progress
"""
import random
import time
import unittest
import threading
import socket
import json
import os
from src.quick_yaml.DatabaseDaemon import DataBaseSocketDaemon
from src.quick_yaml.manager import QYAMLDB
from src.quick_yaml.mock_generator import SetupDeviceTable
from src.quick_yaml.DatabaseDaemon import DBDSSocketClient


class TestDatabaseDaemon(unittest.TestCase):
    db_path = 'sample.ezdb'
    key = 'sample.key'
    log = 'test_ipc.log'
    socket_path = "/tmp/test_dbd_socket"
    encrypted = False
    sample_data = None
    key_file = ""
    db = None
    dbd_thread = None
    t1 = None

    def test_transaction(self):
        import requests
        # To get a random word for unix socket path
        #r = requests.get('https://random-word-api.herokuapp.com/word?lang=en')
        # set the path
        #self.socket_path = "/tmp/" + r.json()[0] + "_socket"
        self.socket_path = '/tmp/test_dbd_socket'
        d = SetupDeviceTable()
        d.setup_db(self.db_path, self.key, self.encrypted)
        data = d.generate_random_data(random.randint(1, 20))
        transactions = {
            'transaction_id': 100,
            '$commands': [
                {'type': '$insert', '$table_name': 'devices_table',
                 '$data': data}
            ]
        }
        self.dbd_thread = DataBaseSocketDaemon(self.db_path, None, self.encrypted, self.socket_path,

                                               enable_logging=True, silent=False, log_file=self.log, db_type='Fine')
        # launch in a separate thread
        print(self.socket_path)
        t1 = threading.Thread(target=self.dbd_thread.start, daemon=True)
        t1.start()

        time.sleep(1)
        com = None

        if os.path.exists(self.socket_path):
            print('Path Found')
            com = DBDSSocketClient('unix', self.socket_path, self.log)
            com.connect()
        else:
            print('No Path Found')
            exit(1)
        # Send length of message and wait for ack

        msg = json.dumps(transactions).encode('utf-8')
        results = com.send(transactions)
        print(results)
        data = d.generate_random_data(random.randint(10, 100))
        transactions = {
            'transaction_id': 200,
            '$commands': [
                {'type': '$insert', '$table_name': 'devices_table',
                 '$data': data}
            ]
        }
        msg = json.dumps(transactions).encode('utf-8')
        results = com.send(transactions)
        print(results)
        # sock.close()
        com.disconnect()

        self.dbd_thread.stop()


# To Define additional class methods and tests here later


if __name__ == '__main__':
    unittest.main()
