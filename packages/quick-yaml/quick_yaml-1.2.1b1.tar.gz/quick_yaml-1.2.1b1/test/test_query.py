"""
Here we test  the query processor performance and the query correctness.

"""
import unittest
import time

from src.quick_yaml.data_structures import NestedDict
from src.quick_yaml.parser import QueryProcessor

from src.quick_yaml.mock_generator import DataGenerator
import yaml


class TestQueryProcessor(unittest.TestCase):
    # This data setup will be used for all tests

    sample_data = yaml.safe_load(DataGenerator.generate_sample_data(30))

    def test_filter(self):
        query_processor = QueryProcessor(self.sample_data['data'])
        query = {
            "$filter": {
                "key1": {"$gt": 11}
            }
        }

        query_processor.process_query(query)
        original_results = list()
        for i in self.sample_data['data'].values():
            if i['key1'] > 11:
                original_results.append(i)

        # Assert the length
        self.assertEqual(len(query_processor.results), len(original_results))

        # Assert the content
        for i in query_processor.results:
            self.assertIn(i, original_results)

    def test_sort_performance(self):
        query_processor = QueryProcessor(self.sample_data['data'])
        query = {
            "$sort": [("key4", "asc")],
        }

        start_time = time.time()
        query_processor.process_query(query)
        duration = time.time() - start_time

        print(f"Sort operation took {duration:.10f} seconds.")

    # Example threshold, adjust based on expected performance

    def test_aggregate_performance_simple(self):
        query_processor = QueryProcessor(TestQueryProcessor.sample_data['data'])
        query = {
            "$operations": [
                {"$action": "$sum", "$on": "key4"}

            ]
        }
        x = query_processor.process_query(query)
        print(x)

    def test_logical_non_recursive(self):
        query_processor = QueryProcessor(TestQueryProcessor.sample_data['data'])

        query = {

            '$and': [{
                "key1":
                    {"$gt": 11}
            }, {
                '$or': [
                    {
                        "key2": "A"
                    },
                    {
                        "key3": 55
                    }
                ]
            }

            ]
        }

        query_processor.filter(query)
        correct = 0
        # first result
        for i in query_processor.results:
            if i['key1'] > 11 and ((i['key2'] == 'A') or (i['key3'] == 55)):
                correct += 1

        if correct == len(query_processor.results):
            print('correct')

        py_correct = 0
        for i in TestQueryProcessor.sample_data['data'].values():
            if i['key1'] > 11 and ((i['key2'] == 'A') or (i['key3'] == 55)):
                py_correct += 1
                print(i)

        if py_correct == correct:
            print('py correct')

    def test_flatten_conditions(self):
        query = {

            '$and': [
                {'key1': {'$gt': 11}},
                {'key2': 'A'},
                {'$and': [
                    {'key4': {'$lt': 150}}
                    , {'key5': {'$gt': 1000}}
                ]}
            ]

        }

        def flatten_dict(data: dict):
            def f_list(l, k):
                final_list = []
                for i in l:
                    if k in i:
                        final_list.extend(f_list(i[k], k))
                    else:
                        final_list.append(i)
                return final_list

            final_dict = dict()
            for k, v in data.items():
                if k == '$and':
                    final_dict[k] = f_list(v, '$and')

                elif k == '$or':
                    final_dict[k] = f_list(v, '$or')

                else:
                    final_dict[k] = v
            return final_dict

        print(flatten_dict(query))


if __name__ == "__main__":
    unittest.main()
