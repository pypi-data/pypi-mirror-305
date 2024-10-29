"""
    A module for parsing and executing queries on a dataset.
"""
import json
import statistics
from collections import defaultdict
from .data_structures import NestedDict
import re

filter_options = {
    '$gte': lambda val, thr: val >= thr,
    '$lte': lambda val, thr: val <= thr,
    '$gt': lambda val, thr: val > thr,
    '$lt': lambda val, thr: val < thr,
    '$eq': lambda val, thr: val == thr,
    '$neq': lambda val, thr: val != thr,
    '$range': lambda val, thr: thr[0] <= val < thr[1],
    '$not_in_range': lambda val, thr: val < thr[0] or val >= thr[1],
    '$in': lambda val, thr: val in thr,
    '$not_in': lambda val, thr: val not in thr,
    '$like': lambda val, thr: bool(re.match(re.compile(thr), val)) if val is not None else False,
    '$not_like': lambda val, thr: not bool(re.match(re.compile(thr), val)) if val is not None else False,
    '$matches': lambda val, thr: bool(re.match(re.compile(thr), val)) if val is not None else False,
    '$not_matches': lambda val, thr: not bool(re.match(re.compile(thr), val)) if val is not None else False,
    '$contains': lambda val, thr: bool(re.findall(re.compile(thr), val)) if val is not None else False,
    '$not_contains': lambda val, thr: not bool(re.findall(re.compile(thr), val)) if val is not None else False
}

aggregate_functions = {
    '$sum': sum,
    '$avg': lambda vals: sum(vals) / len(vals) if vals else 0,
    '$count': len,
    '$max': max,
    '$min': min,
    '$median': lambda vals: statistics.median(vals) if vals else 0,
    '$mode': lambda vals: statistics.mode(vals) if vals else None,
    '$stddev': lambda vals: statistics.stdev(vals) if len(vals) > 1 else 0,
    '$variance': lambda vals: statistics.variance(vals) if len(vals) > 1 else 0,
}


class QueryFormatError(Exception):
    def __init__(self, data, message="Invalid Query Data"):
        self.data = data
        self.message = message
        super().__init__(self.message)


class KeywordNotFoundError(Exception):
    def __init__(self, data, message="Invalid Keyword found"):
        self.data = data
        self.message = message
        super().__init__(self.message)


class QueryOptimizer:

    @staticmethod
    def flatten_condition_list_iterative(condition_lists, condition):
        final_list = []
        stack = [iter(condition_lists)]  # Initialize the stack with an iterator over the initial list

        while stack:
            try:
                i = next(stack[-1])  # Get the next item from the current iterator
                if condition in i:
                    # If 'condition' is in the dictionary, push an iterator over 'i[condition]' onto the stack
                    stack.append(iter(i[condition]))
                else:
                    # If 'condition' is not in the dictionary, append it to 'final_list'
                    final_list.append(i)
            except StopIteration:
                # If the current iterator is exhausted, pop it from the stack
                stack.pop()

        return final_list

    def filter_flatten_query(data):

        def flatten_condition_list(condition_lists, condition):
            final_list = []
            for i in condition_lists:
                if condition in i:
                    final_list.extend(flatten_condition_list(i[condition], condition))
                else:
                    final_list.append(i)
            return final_list

        final_dict = dict()
        for k, v in data.items():
            if k == '$and':
                final_dict[k] = flatten_condition_list(v, '$and')

            elif k == '$or':
                final_dict[k] = flatten_condition_list(v, '$or')

            else:
                final_dict[k] = v
        return final_dict


class QueryProcessor(object):
    """
       Initializes the QueryProcessor with a dataset.

       Attributes:
           results (list): A list of records in the dataset.

    """

    def __init__(self, data: NestedDict, disable_optimization=False):
        self.disable_optimization = disable_optimization
        self.results = list(data.values())

    def process_query(self, query):
        """
           Processes a structured query and applies the specified operations on the dataset.


           Args:
               query (dict): A structured query dict containing operations like $filter, $groupby, $sort, $select, and
                $operations.

           Raises:
               QueryFormatError: If 'select' and aggregate functions are requested in the same query.

           Returns: The result set after applying the query operations on the dataset. It Returns the entire dataset
           if no query is given.
        """
        operation_order = ('$filter', '$groupby', '$sort', '$select', '$operations')

        sorted_operations = sorted(query.items(), key=lambda item: operation_order.index(item[0]))
        if '$select' in query and '$operations' in query:
            # Handle the situation where both operations are requested together
            raise QueryFormatError(query, "Combining 'select' and aggregate functions in the same query is not "
                                          "supported.")
        for operation, parameters in sorted_operations:
            if operation == '$filter':
                self.filter(parameters)
            elif operation == '$groupby':
                self.group_by(parameters)
            elif operation == '$sort' and '$operations' not in query:
                self.sort(parameters)
            elif operation == '$select':
                self.select(parameters)
            elif operation == '$operations':
                self.execute_operations(parameters)

        return self.results  # Or the modified dataset

    def filter(self, filter_data, index_only=False,disable_optimization=False):
        """
        Filters the dataset based on the conditions specified in the data argument.

        Args:
            data (dict): A dictionary containing field names as keys and conditions as values.
            index_only (bool) : Return the indexes of result. Defaults to False
            disable_optimization (bool) : Disables optimization on queries. Defaults to false.

        Raises:
            KeywordNotFoundError: If an invalid filter condition is specified.


        """
        # Pre-Process data
        if not self.disable_optimization or not disable_optimization:
            optimized_query = QueryOptimizer.filter_flatten_query(filter_data)
        else:
            optimized_query = filter_data
        if index_only:
            self.results = [index for index, record in enumerate(self.results, start=1) if
                            self.logical_operations(filter_data, record)]
        else:

            self.results = [record for record in self.results if self.logical_operations(optimized_query, record)]
        return self.results

    def logical_operations(self, filter_constraints, record):
        """
        Recursively evaluates logical operations within filter constraints on a single record.

        :param filter_constraints: Dict containing the filter conditions and logical operators.
        :param record: The record to be evaluated against the filter constraints.
        :return: Boolean indicating whether the record satisfies the filter constraints.
        """

        if isinstance(filter_constraints, list):
            # This is a nested list of constraints under an operator.
            return filter_constraints

        result_array = []

        # Check for logical operators and process accordingly
        for operator, conditions in filter_constraints.items():
            if operator == '$or':
                # Recurse and evaluate OR condition
                result_array.append(any(self.logical_operations(condition, record) for condition in conditions))
            elif operator == '$and':
                # Recurse and evaluate AND condition
                result_array.append(all(self.logical_operations(condition, record) for condition in conditions))
            else:
                # Handle other filter condition
                key = operator
                value = conditions

                # Check for nested filter conditions
                print(value)
                sub_operator, constraint = next(iter(value.items())) if isinstance(value, dict) else ('$eq', value)

                if sub_operator not in filter_options:
                    raise KeywordNotFoundError(sub_operator,
                                               f"This keyword is invalid. Supported keywords are: {list(filter_options.keys())}")
                filter_func = filter_options[sub_operator]
                result_array.append(filter_func(record.get(key, None), constraint))

        # If there are no explicit logical operators at the root, default to AND logic
        return all(result_array)

    def group_by(self, key):
        """
          Groups the dataset based on a specified key.

          Args:
              key (str): The key to group the data by.

          Raises:
              ValueError: If the group by key is None.
          """
        if not key:
            raise ValueError("Group by key cannot be None")

        grouped_results = defaultdict(list)
        for item in self.results:
            group_key_value = item.get(key)  # Get the key value for grouping
            grouped_results[group_key_value].append(item)  # append the item into the group

        self.results = dict(grouped_results)

    def sort(self, data):
        """
          Sorts the dataset or grouped data based on specified fields and directions.

          Args:
              data (list of tuples): Each tuple contains the field to sort by and the direction ('asc' or 'desc').
          """

        if isinstance(self.results, list):  # Ungrouped data

            sort_keys = [item[0] for item in data]
            sort_directions = [item[1] for item in data]
            # Build a list of tuples based on the sort keys and directions
            self.results = sorted(self.results, key=lambda x: tuple(
                x[k] * (-1 if d == 'desc' else 1) for k, d in zip(sort_keys, sort_directions)))

        elif isinstance(self.results, dict):  # Grouped data

            for group_key, records in self.results.items():
                sort_keys = [item[0] for item in data]
                sort_directions = [item[1] for item in data]
                # Sort each group individually
                self.results[group_key] = sorted(records, key=lambda x: tuple(
                    x[k] * (-1 if d == 'desc' else 1) for k, d in zip(sort_keys, sort_directions)))

    def select(self, fields):
        """
        Projects only the specified fields in the results.

        Args:
            fields (list): A list of fields to include in the output.
        """
        # If the data is grouped (dict), iterate through groups
        if type(self.results) is dict:
            selected_results = {}
            for group_key, group_items in self.results.items():
                # Apply selection on each item within the group
                selected_results[group_key] = [{field: item.get(field) for field in fields} for item in group_items]
        elif isinstance(self.results, list):
            # Directly apply selection on the list of items
            selected_results = [{field: item.get(field) for field in fields} for item in self.results]
        else:
            # Handle other types or raise an error
            raise TypeError("Unsupported data type for selection operation.")

        self.results = selected_results

    def execute_operations(self, operations):
        """
           Executes specified aggregate operations on the dataset or grouped data.

           Args:
               operations (list[dict]): Each dictionary contains an aggregate op to perform and the field it operates on.

           Note:
               Supported operations include sum, average (avg), count, max, min, median, mode, standard deviation (stddev), and variance.
        """
        # Define aggregate functions

        # Initialize a variable to hold the aggregated results
        # The structure will depend on whether the data is grouped or not
        aggregated_results = {}

        # Helper function to perform the aggregation
        def perform_aggregation(items, op):

            op_action = op['$action']
            op_field = op['$on']
            if op_action not in aggregate_functions:
                raise QueryFormatError({op_action}, '')
            values = [item.get(op_field, 0) for item in items]
            try:
                result = aggregate_functions[op_action](values)
            except Exception:
                result = 0
            return result

        # Check if results are grouped (dict) or ungrouped (list)
        if isinstance(self.results, dict):
            # Grouped data: iterate over each group
            for group_key, group_items in self.results.items():
                group_aggregates = {}
                for operation in operations:
                    aggregated_value = perform_aggregation(group_items, operation)
                    # Store each op result in a dictionary under the group key
                    group_aggregates[operation['$action']] = aggregated_value
                aggregated_results[group_key] = group_aggregates
        elif isinstance(self.results, list):
            # Ungrouped data: apply operations directly on the list of results
            for operation in operations:
                aggregated_value = perform_aggregation(self.results, operation)
                # Store each op result directly in the results dictionary
                aggregated_results[operation['$action']] = aggregated_value

        # Update self.results with the final aggregated results
        self.results = aggregated_results
