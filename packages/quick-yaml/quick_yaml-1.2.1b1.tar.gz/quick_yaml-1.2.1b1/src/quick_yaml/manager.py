__all__ = ['QYAMLDB', 'QYAMLDBCoarse', 'MetaData', 'QYAMLDBFine']

import logging
import os
import time
from cryptography.fernet import InvalidToken
from threading import Semaphore, Lock
from .data_structures import BYAML, NestedDict, RecordLockManager
from .parser import QueryProcessor
import pandas as pd
import copy



class MetaData:
    """
    A class for storing table metadata

    Attributes:
        - version (float): The version of the metadata.
        - unique_columns (list): A list of unique columns for the table.
        - indexes (list): A list of indexes for the table.
    """

    def __init__(self):
        """
        Initialize the object with an empty dictionary for storing tables.
        """
        self.tables = {}  # A dictionary to hold table-specific metadata
        self._lock = Lock()  # Internal Semaphore for synchronizing access to the metadata.

    def add_table(self, table_name, default_values=None, unique_columns=None, indexes=None):
        """
        Add a new table to the metadata.
        Parameters:
            table_name (str): The name of the table.
            default_values: A dictionary of default values for the table.
            unique_columns (list): A list of unique columns for the table.
            indexes (list): A list of indexes for the table.
        Returns:
            None

        """

        with self._lock:
            self.tables[table_name] = {
                'version': 1.1,
                'unique_columns': unique_columns or [],
                'default_values': default_values or {},
                'indexes': indexes or []
            }

    def to_dict(self):
        """
        Return a dictionary representation of the object.
        """
        return self.tables

    def get_unique_columns(self, table_name):
        """Returns the unique columns for the given table."""
        with self._lock:
            data = self.tables[table_name]['unique_columns']
        return data

    def get_indexes(self, table_name):
        """Returns the indexes for the given table."""
        with self._lock:
            data = self.tables[table_name]['indexes']

        return data

    def __deepcopy__(self, memo):
        # Create a new instance of the same class
        new_obj = type(self)()
        # Explicitly copy the dictionary to the new instance
        new_obj.tables = copy.deepcopy(self.tables, memo)
        # Do not copy the lock, just create a new lock
        new_obj._lock = Lock()
        return new_obj

    def add_default_values(self, table_name, default_values):
        """Adds default key and value to the table
        Parameters:
            table_name (str): The name of the table.
            default_values: A dictionary of default values for the table to be added.
        Returns:
            None
         """
        # Get table MetaDATA
        with self._lock:
            meta = self.tables[table_name]
            # check if default Values is declared if not add it
            if 'default_values' not in self.tables[table_name]:
                self.tables[table_name]['default_values'] = {}

            # Now for each key in default_values check if the key is in unique_columns
            for k, v in default_values.items():
                if k in meta['unique_columns']:
                    raise ValueError(f"Default value for {k} is not allowed as it is a unique column")

            self.tables[table_name]['default_values'].update(default_values)

    def add_unique_column(self, table_name, unique_columns):
        """Adds unique column to the table
        Parameters:decent
            table_name (str): The name of the table.
            unique_columns: A list of unique columns for the table to be added.
        Returns:
            None
         """

        with self._lock:
            # check if default Values is declared if not add it
            if 'unique_columns' not in self.tables[table_name]:
                self.tables[table_name]['unique_columns'] = []

            self.tables[table_name]['unique_columns'].extend(unique_columns)


class QYAMLDB:
    """
    A simple and easy-to-use database manager without thread safety

    Attributes:
        - path (str) : path of database
        - key_file (str): path of key file
        - encrypted (bool): flag indicating if encryption is enabled
        - byaml (BYAML): BYAML instance
        - log_file (str): path of log file
        - enable_logging (bool): flag indicating if logging is enabled
        - log_level (int): level of logging
        - silent (bool): flag indicating if logging is silent

    Methods:
        - __init__: Initialize the database.
        - add_table: Add a table to the database.
        - insert_data: Insert data into a specified table.
        - execute_query: Query data from a specified table.
        - delete_data: Delete data from a specified table.
    """

    def __init__(self, path, key_file='key.file', encrypted=False, auto_load=True, **kwargs):
        """
        Initializes the quick_yaml instance.
        Parameters:
              path (str): The file path for the database.
              key_file (str): The file path for the encryption key. Defaults to 'key.file'.
              encrypted (bool): Flag indicating whether encryption is enabled. Defaults to False.
              auto_load (bool): Flag indicating whether to automatically load the database, Failing to load will not
              raise an exception. Defaults to True.

        Keyword Args:
              enable_logging (bool): Flag indicating whether logging is enabled. Defaults to False.
              log_file (str): The file path for the log file. Defaults to 'qyaml.log'.
              log_level (int): The level of logging. Defaults to logging.DEBUG.
              byaml (BYAML): An existing BYAML instance. If not provided, a new BYAML instance is created.
              silent (bool): Flag indicating whether logging is silent. Defaults to False.
              backup_dir (str): The directory to store backup files. Defaults to /home/<user>/.config/quick_yaml/backups.
          Raises:
              ValueError: If the file format is invalid.
          Returns:
              None
          """

        if not path.endswith('.ezdb'):
            raise ValueError('Invalid file format. Must use ".ezdb" extension.')
        backup_dir = kwargs.get('backup_dir', None)
        if backup_dir is None:
            # Set the default backup dir
            user_home = os.path.expanduser('~')

            backup_dir = os.path.join(user_home, '.config', 'quick_yaml', 'backups')
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

        self.path = path
        self.key_file = key_file
        self.encrypted = encrypted
        self.logger_enabled = kwargs.get('enable_logging', False)
        self.log_file = kwargs.get('log_file', 'qyaml.log')
        self.log_level = kwargs.get('log_level', logging.DEBUG)
        self.silent = kwargs.get('silent', False)
        self.backup_dir = backup_dir
        self._backup_table = None
        self.tables: dict = {} # Variable to store the data in memory.
        self._commit_mode = False  # flag to indicate transaction mode
        self.byaml = kwargs.get('byaml'
                                , BYAML(self.path, encryption_enabled=self.encrypted, key_file=self.key_file,
                                        backup_dir=self.backup_dir))
        if self.logger_enabled:
            self._setup_logger(self.log_file, self.log_level, not self.silent)
        else:
            self._logger = logging.getLogger('QYAMLDB')
            self._logger.addHandler(logging.NullHandler())

        if auto_load:
            self.load_db(ignore_errors=True)

        # Logging Operations


    def _setup_logger(self, log_file, log_level, print_to_console):
        self._logger = logging.getLogger('QYAMLDB')
        self._logger.setLevel(log_level)
        # Include milliseconds in the formatter
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        self._logger.addHandler(fh)
        if print_to_console:
            ch = logging.StreamHandler()
            ch.setLevel(log_level)
            ch.setFormatter(formatter)
            self._logger.addHandler(ch)

    def _log(self, message, level='debug'):
        if self.logger_enabled:
            getattr(self._logger, level)(message)

    def save_db(self, override_commit=False):
        """Saves the current state of the database to a file.

        Args:
            override_commit (bool, optional): If True, the commit mode will be ignored. Defaults to False. Intended for
            use in the context of a transaction. Please note that this feature will work only if the database is in commit mode.
        """
        if self._commit_mode and not override_commit:
            return
        self._log(f"Saving database to {self.path}", 'info')

        try:
            if not os.path.exists(os.path.dirname(self.path)):
                os.makedirs(os.path.dirname(self.path))
            to_save = {table_name: {'metadata': table_info['metadata'].to_dict(),
                                    'data': table_info['data'].to_dict()} for table_name, table_info in
                       self.tables.items()}

            self.byaml.encode_to_binary_yaml(to_save)

            self._log(f"Saved database to {self.path}", 'info')
        except Exception as e:
            self._log(f"Failed to save database: {e}", 'error')

    def make_backup(self):
        """Creates a backup copy of the database."""
        file_name = os.path.basename(self.path)
        file_name = file_name.replace('.ezdb', f'_backup_{time.time()}.ezdb')
        path = self.byaml.make_backup(file_name)
        self._log(f"Created backup copy of database at {file_name}", 'info')
        return path

    def restore_backup(self, **kwargs):
        """Restores a backup copy of the database."""
        backup_file = kwargs.get('backup_file', None)
        if backup_file is None:
            self._log('Backup file not provided, Restoring the last backup copy of the database...')
            backup_file = self.list_backups()[-1]

        self._log(f"Restoring backup copy of database from {backup_file}", 'info')
        new_byaml = BYAML(backup_file, encryption_enabled=self.encrypted, key_file=self.key_file)
        self.byaml = new_byaml  # replace the old byaml instance with newer one.
        self.tables = new_byaml.decode_from_binary_yaml(type_dict='dict')  # load the new table
        self._log(f"Restored backup copy of database from {backup_file}", 'info')

    def list_backups(self):
        """Lists all backup copies of the database."""
        backup_files = [os.path.join(self.backup_dir, file) for file in os.listdir(self.backup_dir)]
        return backup_files.sort()

    # TCL operations
    def start_transaction(self):
        self._commit_mode = True
        self._backup_table = copy.deepcopy(self.tables)

    def end_transaction(self, commit_transactions=False):
        """Ends the current transaction.

        Parameters:
            commit_transactions (bool, optional): Whether to commit the transaction. Defaults to False.
        """
        if commit_transactions:
            self.save_db()
        else:
            self.tables = self._backup_table  # rollback the transaction
        self._commit_mode = False

    def get_commit_mode(self):
        return self._commit_mode

    def roll_back(self):
        """Rolls back the current transaction.

        **NOTE: This functionality is not supported yet.**
        """
        self.tables = self._backup_table
        self._log("Rolled back transaction.", 'info')

    def commit(self):
        """
         Commits the current transaction.
         **NOTE: This functionality is not supported yet.**
        """
        self.save_db(True)
        self._log("Committed transaction.", 'info')

    def create_table(self, table_name, unique_columns=None, indexes=None):
        """
        Creates a new table in the database.

        Parameters:
            table_name (str): The name of the table to create.
            unique_columns (list, optional): List of column names that should be unique. Defaults to None.
            indexes (list, optional): List of column names to index. Defaults to None.
        Returns:
            str: "done." if the table is created successfully.
        Raises:
            ValueError: If the table already exists.
        """
        if table_name in self.tables:
            self._log(f"Table '{table_name}' already exists.", 'error')
            raise ValueError(f"Table '{table_name}' already exists.")
        metadata = MetaData()
        metadata.add_table(table_name, unique_columns, indexes)
        self.tables[table_name] = {
            'metadata': metadata,
            'data': NestedDict()
        }
        self.save_db()
        self._log(f"Created table '{table_name}'.", 'info')
        return "done."

    def load_db(self, ignore_errors=False):
        """
        Load the database by decoding the contents from binary YAML and populating the tables dictionary with metadata
         and data.

        Parameters:
            ignore_errors (bool, optional): When set to True the function ignores FileNotFoundError. Defaults to False.

        Returns:
            None
        """
        try:
            contents = self.byaml.decode_from_binary_yaml(type_dict='dict')
            for table_name, table_info in contents.items():
                #  Load the table into memory.
                metadata = MetaData()
                metadata.tables[table_name] = table_info['metadata']
                self.tables[table_name] = {
                    'metadata': metadata,
                    'data': NestedDict(table_info['data'])
                }
        except FileNotFoundError:
            if not ignore_errors:
                raise FileNotFoundError("Database file not found.")
            self._log('File not found, creating a new file.')
        except PermissionError:
            raise PermissionError("Permission denied to access database file.")
        except IndexError:
            raise ValueError("Cannot load the metadata")
        except InvalidToken:
            if not ignore_errors:
                raise InvalidToken("Invalid Token. Data is corrupted.")
            print('Warning Invalid Token, A new database will be created')


    def _generate_new_id(self, table_name):
        """
        Generates new ID for records
        """
        # Get existing IDs as integers
        existing_ids = [int(key) for key in self.tables[table_name]['data'].get_dict().keys()]
        # Find missing IDs if there are any gaps
        missing_ids = [i for i in range(1, max(existing_ids) + 1) if i not in existing_ids] if existing_ids else []
        # Use the first missing ID if available; otherwise, use the next highest ID
        entry_id = str(missing_ids[0]) if missing_ids else str(max(existing_ids) + 1 if existing_ids else 1)
        return entry_id

    def insert_new_data(self, table_name, data):
        """
        Insert new data into the specified table.

        Parameters:
            table_name (str): Name of the table to insert data into.
            data (dict): Data to be inserted into the table.

        Returns:
            str: A message indicating the insertion operation is done.

        Raises:
            ValueError: If the table does not exist or if a unique constraint is violated.
        """
        # TODO: Work using Default meta data
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        # Check for unique constraints
        unique_columns = self.tables[table_name]['metadata'].get_unique_columns(table_name)
        for column in unique_columns:
            if column in data and any(
                    data[column] == row.get(column) for row in self.tables[table_name]['data'].get_dict().values()):
                raise ValueError(f"Unique constraint violated for column: {column}")

        entry_id = self._generate_new_id(table_name)
        # Insert the data with the new entry_id
        self.tables[table_name]['data'][entry_id] = data
        self.save_db()
        return 'done'

    def insert_many(self, table_name, list_of_values):
        """
        Insert multiple values into the specified table.
        Parameters:
            table_name (str): Name of the table to insert data into.
            list_of_values (list): List of values to be inserted into the table.
        Returns:
            str: A message indicating the insertion operation is done.
        """
        try:
            for i in list_of_values:
                if type(i) is dict or isinstance(i, NestedDict):
                    self.insert_new_data(table_name, i)

            return 'done'
        except Exception as e:
           self._log('Error in insert_many: {}'.format(e), 'error')

    def get_data_by_id(self, table_name, entry_id):
        """
        A function that retrieves data by ID from a specific table.

        Parameters:
            table_name (str): The name of the table to retrieve data from.
            entry_id (int): The ID of the entry to retrieve.

        Returns:
            contents: The data associated with the provided entry ID in the specified table.
        """
        if table_name not in self.tables:
            raise ValueError(f"Table Not found.")
        contents = self.tables[table_name]['data'].get(str(entry_id), None)
        return contents

    def update_entry(self, table_name, entry_id, updated_data):
        """Updates the data by given ID.
        Parameters:
            table_name (str): Name of the table
            entry_id (str): ID of the entry
            updated_data (NestedDict/Dict): Data to be updated.
        """
        if table_name not in self.tables or entry_id not in self.tables[table_name]['data'].get_dict():
            raise ValueError("Table or entry does not exist.")
        print(
            f"DEBUG Table {self.tables[table_name]['data'][entry_id]} type{type(self.tables[table_name]['data'][entry_id])}")
        if entry_id not in self.tables[table_name]['data'].keys():
            return KeyError("Entry does not exist.")
        self.tables[table_name]['data'][entry_id].update(updated_data)
        self.save_db()
        return 'done'

    def update_many(self, table_name, condition, update_data, flags=None):
        """
        Updates data based on given condition

        Parameters:
            condition (dict): Filtering Conditions.
            update_data (dict): Data to be updated
            flags: Additional flags (Supported: { add_missing_values : 'True'/False})
            table_name: name of table

        Returns:
            str: A message indicating the update operation is done.
            """
        if flags is None:
            flags = {'add_missing_values': True}
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        # Retrieve the metadata to check for unique constraints
        unique_columns = self.tables[table_name]['metadata'].get_unique_columns(table_name)
        qp = QueryProcessor(self.tables[table_name]['data'])
        qp.filter(condition,index_only=True)
        matching_ids = qp.results

        if not matching_ids:
            return None  # No data matching the condition

        for entry_id in matching_ids:
            current_entry = self.tables[table_name]['data'].get(str(entry_id))

            for key, value in update_data.items():
                # Check if the key exists in the entry or if missing keys should be added
                if key in current_entry or flags.get('add_missing_keys', False):
                    # Check for unique constraints
                    if key in unique_columns and any(
                            value == row.get(key) for row in self.tables[table_name]['data'].get_dict().values()
                            if row.get(key) is not None and str(row.get('id')) != entry_id):
                        raise ValueError(f"Unique constraint violated for column: {key}")

                    # Update or add the key-value pair
                    if isinstance(value, dict) and isinstance(current_entry.get(key, None), dict):
                        # For nested dicts, update sub-keys
                        current_entry[key].update(value)
                    else:
                        current_entry[key] = value

            # Update the entry in the dataset
            self.tables[table_name]['data'][str(entry_id)] = current_entry

        self.save_db()
        return 'done'

    def delete_entry(self, table_name, entry_id):
        """
        Delete an entry from a specified table.
        Parameters:
            table_name (str): The name of the table to delete the entry from.
            entry_id (str): The unique identifier of the entry to be deleted.

        Raises:
            ValueError: If the table or entry does not exist.
            KeyError: If the entry does not exist.

        Returns:
            str: "done" if the deletion is successful.
        """
        if table_name not in self.tables or entry_id not in self.tables[table_name]['data'].get_dict().keys():
            raise ValueError("Table or entry does not exist.")
        if entry_id not in self.tables[table_name]['data']:
            return KeyError("Entry does not exist.")
        del self.tables[table_name]['data'][entry_id]
        self.save_db()
        return "done"

    def delete_many(self, table_name, condition):
        """
           Delete multiple records from a table based on a given condition.
           Parameters:
               table_name (str): The name of the table to delete records from.
               condition (dict): The condition to filter the records to be deleted.
           Raises:
               ValueError: If the table does not exist in the database.
           Returns:
               str: A message confirming the deletion process is done.
           """
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        # Retrieve the metadata to check for unique constraints
        qp = QueryProcessor(self.tables[table_name]['data'])
        qp.filter(condition,index_only=True)
        matching_ids = qp.results
        # for each matching records, delete the record
        for entry_id in matching_ids:
            del self.tables[table_name]['data'][entry_id]
        self.save_db()
        return "done"

    def execute_query(self, table_name, query):
        """
           Executes a query on a specific table and returns the results.

           Parameters:
               table_name (str): The name of the table to execute the query on.
               query (dict): The query to be executed.

           Returns:
               dict: The results of the query execution.
           """
        # check if table exists
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        data = self.tables[table_name]['data'].to_dict()
        executor = QueryProcessor(data)
        executor.process_query(query)

        return executor.results

    def find(self, table_name, query):
        """
           Finds and filters data in the specified table based on a query.
           Parameters:
               table_name (str): The name of the table to search in.
               query (dict): The query to filter the data.
           Returns:
               dict: The filtered results based on the query.
           """
        data = self.tables[table_name].to_dict()
        executor = QueryProcessor(data)
        executor.filter(query)
        return executor.results

    def get_all_data(self, table_name):
        """
        Returns all the data in the specified table.
        Parameters:
            table_name (str): The name of the table to search in.
        Returns:
            list: The results of the query execution.
        """
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        return self.tables[table_name]['data'].values()

    def to_pandas(self, table_name):
        """
        Converts the specified table data into a pandas DataFrame.

        Parameters:
            table_name (str): The name of the table to convert.

        Returns:
            pandas.DataFrame: The converted DataFrame.

        Raises:
            ValueError: If the table does not exist in the database.
        """
        if table_name not in self.tables:
            self._log(f"Executed method to_pandas. Table '{table_name}' does not exist.", 'error')
            raise ValueError(f"Table '{table_name}' does not exist.")

        # Extract data from the specified table
        data = self.tables[table_name]['data'].to_dict()

        # Flatten the data and convert it into a format suitable for DataFrame creation
        flattened_data = []
        for entry_id, entry_data in data.items():
            entry_data_flat = {'obj_id': entry_id}
            for key, value in entry_data.items():
                if isinstance(value, list):
                    entry_data_flat[key] = ', '.join(map(str, value))  # Convert lists to comma-separated strings
                else:
                    entry_data_flat[key] = value
            flattened_data.append(entry_data_flat)

        # Create and return the DataFrame
        df = pd.DataFrame(flattened_data)
        self._log(f'Result {df}')
        return df

    # MetaData Methods
    def get_metadata(self, table_name):
        return copy.deepcopy(self.tables[table_name]['metadata'])

    def update_meta_data(self, table_name, data):
        # Update Metadata
        self.tables[table_name]['metadata'].update(data)

    def batch_process(self, data):
        """
        Process bulk commands.

        Parameters:
            data (dict): Dictionary data to be processed.

        Raises:
            ValueError: If the error strategy is not one of the valid values.

        Returns:
            dict: A dictionary containing the status, error message, and transaction details.
        """

        def rollback():
            self.tables = self._backup_table
            self.save_db()

        # Create a backup copy of the tables
        self._backup_table = copy.deepcopy(self.tables)

        # Initialize transaction report
        transaction_report = {
            'successful_operations': 0,
            'failed_operations': 0,
            'results': [],
            'list_of_failed_operations_id': []
        }

        transactional_data = data.get('$commands', [])
        error_strategy = data.get('$error_strategy', 'rollback')
        on_invalid_command = data.get('$on_invalid_command', 'rollback')

        # Validate error_strategy
        if error_strategy not in ('rollback', 'continue', 'break'):
            error_strategy = 'rollback'

        for transaction_id, operation in enumerate(transactional_data, start=1):
            try:
                status = self.execute_command(operation)
                transaction_report['results'].append(status)

                if status == 'Invalid command':
                    if on_invalid_command == 'rollback':
                        rollback()
                        return {'status': 'Failure', 'error_message': 'Invalid command', 'details': transaction_report}
                    elif on_invalid_command == 'break':
                        return {'status': 'Failure', 'error_message': 'Invalid command', 'details': transaction_report}
                    transaction_report['list_of_failed_operations_id'].append(transaction_id)

                else:
                    transaction_report['successful_operations'] += 1

            except Exception as e:
                if error_strategy == 'rollback':
                    rollback()
                transaction_report['failed_operations'] += 1
                transaction_report['list_of_failed_operations_id'].append(transaction_id)

                if error_strategy == 'break':
                    return {'status': 'Failure', 'error_message': str(e), 'details': transaction_report}
                else:
                    continue

        stat = "Success" if not transaction_report['list_of_failed_operations_id'] else "Finished with errors"
        return {'status': stat, 'error_message': None, 'details': transaction_report}

    def execute_command(self, i):
        """
        Execute a command based on the given input type.

        Parameters:
            i (dict): The input command to be executed.
        Returns:
            str: The result of the executed command.
        """
        operations_map = {
            '$insert': (self.insert_new_data, ['$table_name', '$data']),
            '$insert_many': (self.insert_many, ['$table_name', '$data']),
            '$query': (self.execute_query, ['$table_name', '$data']),
            '$find': (self.find, ['$table_name', '$data']),
            '$get_by_id': (self.get_data_by_id, ['$table_name', '$obj_id']),
            '$update': (self.update_entry, ['$table_name', '$obj_id', '$data']),
            '$update_many': (self.update_many, ['$table_name', '$condition', '$data', '$flags']),
            '$delete': (self.delete_entry, ['$table_name', '$obj_id']),
            '$del': (self.delete_entry, ['$table_name', '$obj_id']),
            '$delete_many': (self.delete_many, ['$table_name', '$condition']),
            '$del_many': (self.delete_many, ['$table_name', '$condition']),
            '$create_table': (self.create_table, ['$table_name', '$unique_columns', '$default_values']),
            '$backup': (self.make_backup, []),
            '$list_backups': (self.list_backups, [])
        }

        # Retrieve the operation type
        op_type = i.get('$type', None) or i.get('type', None)
        if op_type not in operations_map:
            return "Invalid operation detected."

        # Retrieve the method and the expected arguments for this operation type
        method, expected_args = operations_map[op_type]

        # Gather the arguments from the input dictionary
        args = [i.get(arg) for arg in expected_args]

        # Handle operations without return values separately
        if op_type in ['$backup', '$list_backups']:
            method()  # Directly call the backup method
            return 'success'

        # Call the method with the gathered arguments and return the result
        return method(*args)


class QYAMLDBCoarse(QYAMLDB):
    """
     A subclass designed to handle locks in a coarse-grained manner. This is ideal for environments
     where simplicity and preventing race conditions are prioritized over operation throughput. Inherits from QYAMLDB.

    Attributes:
        _mutex (threading.Semaphore): A semaphore used to synchronize access to the database.
        _writers_lock (threading.Semaphore): A semaphore used to synchronize access t  Inherits from:
        _readers (int): The number of _readers currently accessing the database.
    """

    READ_OPERATIONS = ["find", "get_all_data", "execute_query", "get_data_by_id", "to_pandas",'get_all_data','make_backup']
    WRITE_OPERATIONS = ["insert_many", "insert_new_data", "update_entry", "update_many", "delete_entry",
                        "delete_many", "create_table", "update_meta_data", "insert_meta_data",'restore_backup']

    # include all the arguments from base class
    def __init__(self, path, key_file='key.file', encrypted=False, auto_load=True, **kwargs):
        super().__init__(path, key_file,encrypted, auto_load, **kwargs)

        self._mutex = Semaphore(1)
        self._writers_lock = Semaphore(1)
        self._readers = 0
        self._writers_waiting = False
        self._data_lock = Lock()

    def _start_write(self, agent='Writer'):
        """
        Function to acquire the writer lock.
        """
        self._log(f'{agent} Waiting to acquire writer lock. With {self._readers} _readers', 'debug')
        with self._mutex:
            self._writers_waiting = True

        self._log(f'{agent} Acquired writer lock. With {self._readers} _readers', 'debug')
        self._writers_lock.acquire()

    def _end_write(self, agent='Writer'):
        """
        Function to release the writer lock.
        """
        self._log(f'Releasing writer lock. With {self._readers} _readers', 'debug')
        self._writers_lock.release()

        with self._mutex:
            self._writers_waiting = False

        self._log(f'Released writer lock.With {self._readers} _readers', 'debug')

    def _start_read(self):
        """
        Function to acquire the reader lock.
        """
        self._log('Waiting to acquire reader lock', 'debug')
        self._mutex.acquire()  # Acquire mutex lock to synchronize readers attaining lock
        while self._writers_waiting:
            # Release all the readers until writers are finished.
            self._log(f'Lock Released due to waiting of writers. No of _readers {self._readers}')
            self._mutex.release()  # Release mutex in favor of writers
            time.sleep(0.1)  # Sleep to prevent busy waiting
            self._mutex.acquire()  # Again Try to acquire locks.

        self._log('Acquired reader lock', 'debug')
        self._readers += 1

        if self._readers == 1:
            self._log('Waiting for writers lock by _readers', 'debug')
            self._writers_lock.acquire()
            self._log('Writers Lock acquired by _readers.', 'debug')
        self._mutex.release()
        self._log(f'No of _readers {self._readers}', 'debug')

    def _end_read(self):
        """Function to release reader lock."""
        self._log('Releasing reader lock', 'debug')
        self._mutex.acquire()

        self._readers -= 1
        self._log(f'Released reader lock. No of Readers {self._readers}', 'debug')
        if self._readers == 0:
            self._writers_lock.release()
        self._mutex.release()

    def __getattr__(self, item):
        """Override the getattr method to add read/write locks to the database operations."""
        f = getattr(super(), item)

        if item in QYAMLDBCoarse.WRITE_OPERATIONS:
            def wrapped(*args, **kwargs):
                # modify the function to add locks
                try:
                    self._start_write()
                    return f(*args, **kwargs)
                finally:
                    self._end_write()

            return wrapped

        elif item in QYAMLDBCoarse.READ_OPERATIONS:
            def wrapped(*args, **kwargs):
                try:
                    self._start_read()
                    return f(*args, **kwargs)
                finally:
                    self._end_read()

            return wrapped
        else:
            return f


class QYAMLDBFine(QYAMLDB):
    """
    A subclass of QYAMLDB that implements fine-grained locking. It implements read/write lock in record level.

    """

    def __init__(self, path, key_file='key.file',encrypted=False, auto_load=True, **kwargs):

        super().__init__(path, key_file,encrypted,auto_load, **kwargs)
        self._lock_manager = RecordLockManager(create_logger=self.logger_enabled, logger=self._logger)

    def insert_new_data(self, table_name, data):
        """
        Insert new data into the table in a thread-safe manner.

        Parameters:
            table_name (str): Name of the table.
            data (dict): Data to insert.

        Returns:
            str: A message indicating the insertion operation is done.

        Raises:
            ValueError: If the table does not exist, the entry does not exist, or a unique constraint is violated.
        """
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")

        # Generate a unique Record ID for the new data
        entry_id = self._generate_new_id(table_name)

        # Acquire a write lock for the newly generated ID
        self._lock_manager.acquire_writer_lock(table_name, entry_id)

        try:
            # Check for unique constraints
            unique_columns = self.tables[table_name]['metadata'].get_unique_columns(table_name)
            if any(data.get(column) in [row.get(column) for row in self.tables[table_name]['data'].values()] for column
                   in unique_columns):
                raise ValueError("Unique constraint violated.")

            # Insert the data
            self.tables[table_name]['data'][entry_id] = data
            self.save_db()
            self._logger.debug(f"Inserted data for record {entry_id} into table {table_name}")
        except Exception as e:
            raise e
        finally:
            # Release the write lock
            self._lock_manager.release_writer_lock(table_name, entry_id)

        return "done."

    def update_entry(self, table_name, entry_id, updated_data):
        """"""
        if table_name not in self.tables or entry_id not in self.tables[table_name]['data'].keys():
            raise ValueError("Table or entry does not exist.")
        try:
            self._lock_manager.acquire_writer_lock(table_name, entry_id)
            self.tables[table_name]['data'][entry_id].update(updated_data)
            self.save_db()

        except Exception as e:
            raise e
        finally:
            # Release the lock
            self._lock_manager.release_writer_lock(table_name, entry_id)

        return "done."

    def update_many(self, table_name, condition, update_data, flags=None):
        """
        Updates data based on given condition.
        Parameters:
            condition (dict): Filtering Conditions.
            update_data (dict): Data to be updated.
            flags: Additional flags (Supported: { add_missing_values : 'True'/False}).
            table_name: Name of table.
        """
        if flags is None:
            flags = {'add_missing_values': True}
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        self._log('Updating table.........')
        # Retrieve the metadata to check for unique constraints
        self._lock_for_read(table_name)
        qp = QueryProcessor(self.tables[table_name]['data'])
        qp.filter(condition,index_only=True)
        matching_ids = qp.results
        self._release_read(table_name)
        if not matching_ids:
            return None  # No data matching the condition

        # Sort IDs to avoid deadlock
        matching_ids.sort()

        locked_ids = []
        try:
            # Acquire locks for all relevant records
            # print('Acquiring lock for ids.........')
            for entry_id in matching_ids:
                self._lock_manager.acquire_writer_lock(table_name, entry_id)
                locked_ids.append(entry_id)
            # Perform updates
            super().update_many(table_name, condition, update_data, flags)
        except Exception as e:
            raise e
        finally:
            # Release locks
            for entry_id in locked_ids:
                self._lock_manager.release_writer_lock(table_name, entry_id)

        return "done"

    def delete_entry(self, table_name, entry_id):
        """"""
        if table_name not in self.tables or entry_id not in self.tables[table_name]['data'].keys():
            raise ValueError("Table or entry does not exist.")
        try:
            self._lock_manager.acquire_writer_lock(table_name, entry_id)
            del self.tables[table_name]['data'][entry_id]

            self.save_db()
        except Exception as e:
            raise e
        finally:
            # Release the lock
            self._lock_manager.release_writer_lock(table_name, entry_id)
            self._lock_manager.delete_lock_id(table_name, entry_id)

        return "done"

    def delete_table(self, table_name):
        """"""

        if table_name not in self.tables:
            raise ValueError("Table does not exist.")

        # Acquire lock for entire id
        for i in self.tables[table_name]['data'].keys():
            self._lock_manager.acquire_writer_lock(table_name, i)
        del self.tables[table_name]

        self.save_db()

        self._lock_manager.delete_lock_table(table_name)

        return "done"

    def delete_many(self, table_name, condition):
        """
        Delete multiple records from a table based on a given condition.
        Threadsafe
        Parameters:
            table_name (str): The name of the table to delete records from.
            condition (dict): The condition to filter the records to be deleted.
        Raises:
            ValueError: If the table does not exist in the database.
        Returns:
            str: A message confirming the deletion process is done.
        """
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        # Retrieve the metadata to check for unique constraints
        qp = QueryProcessor(self.tables[table_name]['data'])
        qp.filter(condition,index_only=True)
        matching_ids = qp.results

        if not matching_ids:
            return None  # No data matching the condition

        # Sort IDs to avoid deadlock
        matching_ids.sort()

        locked_ids = []
        try:
            # Acquire locks for all relevant records
            for entry_id in matching_ids:
                self._lock_manager.acquire_writer_lock(table_name, entry_id)
                locked_ids.append(entry_id)

            # Perform updates
            for entry_id in matching_ids:
                del self.tables[table_name]['data'][entry_id]

            self.save_db()

        except Exception as e:
            raise e
        finally:
            # Release locks
            for entry_id in locked_ids:
                self._lock_manager.release_writer_lock(table_name, entry_id)
                # remove all the locks associated with id
                self._lock_manager.delete_lock_id(table_name, entry_id)

        return "done"

    def get_all_data(self, table_name):
        """
        Returns all the record.
        Returns:
            list: A list of all the records in the table.
        Raises:
            ValueError: If the table does not exist in the database.
        """
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")

        self._lock_for_read(table_name)
        results = self.tables[table_name]['data'].values()
        self._release_read(table_name)
        return results

    def find(self, table_name, query):
        """
        Find for specific records based on $filter query

        Parameters:
            table_name (str): The name of the table to search in.
            query (dict): The query to filter the data.

        Returns:
            list: The results of the query execution.
        Raises:
            ValueError: If the table does not exist in the database.
        """
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")

        self._lock_for_read(table_name)
        qp = QueryProcessor(self.tables[table_name])
        results = qp.filter(query)
        self._release_read(table_name)
        return results

    def get_data_by_id(self, table_name, entry_id):
        """Gets Data by Object ID"""

        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        if isinstance(entry_id, int):
            # convert it to string
            entry_id = str(entry_id)
        try:
            self._lock_manager.acquire_reader_lock(table_name, entry_id)

            data = self.tables[table_name]['data'][entry_id]

        except Exception as e:
            raise e
        finally:
            # Release the lock
            self._lock_manager.release_reader_lock(table_name, entry_id)
        return data

    def execute_query(self, table_name, query):
        """Executes the query on the table.
        Parameters:
            table_name (str): The name of the table to execute the query on.
            query (dict): The query to be executed.
        """

        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        self._lock_for_read(table_name)
        qp = QueryProcessor(self.tables[table_name])
        results = qp.process_query(query)
        self._release_read(table_name)
        return results

    def _lock_for_read(self, table_name):
        """
        Lock All the record in the table for reading

       **DO NOT USE THIS FUNCTION. IT IS MEANT FOR INTERNAL PURPOSES.**

        Parameters:
            table_name (str): The name of the table to lock.

        Returns:
            None
        """
        self._log('Waiting to acquire reader lock for entire table.', 'debug')

        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        k = self.tables[table_name]['data'].keys()
        # lock for all data
        for i in k:
            self._lock_manager.acquire_reader_lock(table_name, i)
        pass

    def _release_read(self, table_name):
        """
        Release All the record in the table for reading

       **DO NOT USE THIS FUNCTION.
       IT IS MEANT FOR INTERNAL PURPOSES.**

        Parameters:
            table_name (str): The name of the table to lock.

        Returns:
            None
        """

        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        self._log('Releasing reader lock for entire table.', 'debug')
        # lock for all data
        for i in self.tables[table_name]['data'].keys():
            self._lock_manager.release_reader_lock(table_name, i)

        self._log(f"Released reader lock for the table. {table_name}", 'debug')

    # _lock_write

    def _lock_for_write(self, table_name):
        """
        Lock All the record in the table for writing

       **DO NOT USE THIS FUNCTION. IT IS MEANT FOR INTERNAL PURPOSES.**

        Parameters:
            table_name (str): The name of the table to lock.

        Returns:
            None
        """
        self._log('Waiting to acquire writer lock for entire table.', 'debug')
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        key_list = list(self.tables[table_name]['data'].keys())

        self._log('Waiting to acquire writer lock for entire table.', 'debug')
        key_list.sort()
        # lock for all data
        for i in key_list:
            self._lock_manager.acquire_writer_lock(table_name, i)

        self._log(f'Acquired writer lock for the table. {table_name}', 'debug')

    def _release_write(self, table_name):
        """
        Release All the record in the table for writing

       **DO NOT USE THIS FUNCTION. IT IS MEANT FOR INTERNAL PURPOSES.**

        Parameters:
            table_name (str): The name of the table to lock.

        Returns:
            None
        """
        print('Releasing write lock for all table')
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")

        self._log('Releasing writer lock for entire table.', 'debug')
        # lock for all data
        for i in self.tables[table_name]['data'].keys():
            self._lock_manager.release_writer_lock(table_name, i)

        self._log(f"Released writer lock for the table. {table_name}", 'debug')
