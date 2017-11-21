import pytest
import main
import hypothesis.strategies as st
from hypothesis import given


def my_test_factory(keys_strategies, values_strategies):
	@given(st.sets(keys_strategies), st.sets(values_strategies))
	def new_test_function(keys, values):
		keys = list(keys)
		values = list(values)

		dictionary = main.make_dict(keys, values)

		if len(keys) < len(values):
			values = values[0:len(keys):]
	
		if len(values) < len(keys):
			for i in range(len(keys) - len(values)):
				values.append(None)
	
		assert list(dictionary.keys()) == keys
		assert list(dictionary.values()) == values

	return new_test_function


strategies_list = [st.integers(), st.floats(), st.booleans(), st.none(), st.text(), st.binary()]

test_function_1 = my_test_factory(strategies_list[0], strategies_list[0])
test_function_2 = my_test_factory(strategies_list[1], strategies_list[1])
test_function_3 = my_test_factory(strategies_list[2], strategies_list[2])
test_function_4 = my_test_factory(strategies_list[3], strategies_list[3])
test_function_5 = my_test_factory(strategies_list[4], strategies_list[4])
test_function_6 = my_test_factory(strategies_list[5], strategies_list[5])
