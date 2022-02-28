'''
This module will test controller_validator.py
'''
import pytest
from controller_testing_package import controller_validation_function
from shared.constants import TEST_STRINGS_FOR_CONTROLLER_VALIDATION

def test_controller_validator():
    for string in TEST_STRINGS_FOR_CONTROLLER_VALIDATION:
        assert controller_validation_function(string) == False
