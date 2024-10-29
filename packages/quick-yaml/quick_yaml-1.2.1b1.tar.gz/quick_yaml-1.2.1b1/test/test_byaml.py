import unittest
import os
import random

from src.quick_yaml.data_structures import BYAML


class TestBYAML(unittest.TestCase):

    def setUp(self):
        self.filepath = "sample.ezdb"
        self.key_file = "test.key"
        self.backup_file = os.getcwd()+'/backups'
        i = random.randint(1, 100)
        self.data = {'id': str(i),'name': random.choice(['sensor', 'fan', ' light', 'fridge']) + str(i),
                                     'status': 'active', 'value': random.randrange(10,100)}
        self.byaml = BYAML(self.filepath, encryption_enabled=True, key_file=self.key_file,backup_path=self.backup_file)
        self.byaml.encode_to_binary_yaml(self.data)

    def test_key_generation_and_loading(self):
        key = self.byaml.load_key()
        self.assertTrue(os.path.exists(self.key_file))
        self.assertIsNotNone(key)

    def test_encode_decode_binary_yaml(self):
        self.byaml.encode_to_binary_yaml(self.data)
        self.assertTrue(os.path.exists(self.filepath))
        decoded_data = self.byaml.decode_from_binary_yaml()

        self.assertEqual(decoded_data.to_dict(), self.data)

    def test_backup(self):

        self.byaml.make_backup('test_backup')

        print(self.byaml.list_backups())
        file,key = self.byaml.list_backups()
        new_byaml = BYAML(filepath=os.path.join(self.backup_file,file),
                          encryption_enabled=True,
                          key_file=os.path.join(self.backup_file,key),
                          backup_path=None)
        print(new_byaml.decode_from_binary_yaml('dict'))

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        if os.path.exists(self.key_file):
            os.remove(self.key_file)
        if os.path.exists(self.backup_file):
            for i in os.listdir(self.backup_file):
                os.remove(os.path.join(self.backup_file,i))
            os.removedirs(self.backup_file)


if __name__ == '__main__':
    unittest.main()
