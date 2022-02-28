'''
This module will test bms_testing function
'''

import pytest
import dummy_serial
from shared.connections import ser
from bms_testing_package import test_bms
from shared.constants import TEST_STRINGS_FOR_BMS_TESTING

def test_wrong_input_for_test_bms(monkeypatch):
    #monkeypatch.setenv("ser",{})
    com = dummy_serial.Serial(
            port='COM1',
            baudrate=9600,
            ds_responses={powerCheck : powerCheck}
            )
    monkeypatch.setattr(ser, "write", True)
    #monkeypatch.setenv("ser.write",)
    monkeypatch.setenv("msg_buffer_size",20)
    monkeypatch.setenv("data","random")
    for string in TEST_STRINGS_FOR_BMS_TESTING:
        monkeypatch.setenv("info", string)
        assert test_bms() == False

