"""
Add comments for what this file is doing
"""
import typing
#from testing_module import constants
import sys
print(sys.path)
from shared import sha256_converter 


def hash_expected_output(expected_output: typing.List) -> str:
    """
    hash_expected_output: Describe what this method is doing

    describe args
    describe return
    """
    expected_output_str = ",".join(expected_output)
    hashed_output = hash(expected_output_str)
    return hashed_output
