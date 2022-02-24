"""
This module will validate the controller output.
"""
import time
import logging
from constants import SERIAL_DATA_LOG_FILENAME

def controller_validation_function(ser,controller_output):

    """This function will take controller_output as string and will parse it 
        and will match it to the expected ouput

    Args:
        controller_output (_str_): controller output as string
    """    

    try:
        controller_output_list = controller_output.split(",")
        try:
            with open(SERIAL_DATA_LOG_FILENAME, "a") as data_file:
                data_file.write(controller_output_list)
        except:
            logging.error("Controller log not added")

        flag = True

        if float(controller_output_list[1]) < -50 and float(controller_output_list[1]) > 200:
            flag = False
            print("The vaue of ControllerData Motor Temp is %s " % controller_output_list[1])

        if float(controller_output_list[2]) < -50 and float(controller_output_list[2]) > 200:
            flag = False
            print("The vaue of ControllerData Controller Temp is %s " % controller_output_list[2])

        if float(controller_output_list[9]) < -60 and float(controller_output_list[9]) > 60:
            flag = False
            print("The value of ControllerData SpeedhighLow is %s" % controller_output_list[61])

        if float(controller_output_list[25]) < -500 and float(controller_output_list[25]) > 500:
            flag = False
            print("The value of ControllerData Frequency is %s" % controller_output_list[25])

        if float(controller_output_list[27]) < -100 and float(controller_output_list[27]) > 100:
            flag = False
            print("The value of ControllerData Motor Torque is %s" % controller_output_list[27])

        if float(controller_output_list[30]) < 1 and float(controller_output_list[30]) > 250:
            flag = False
            print("The value of ControllerData Acceleration Rate is %s" % controller_output_list[30])

        if float(controller_output_list[31]) < 1 and float(controller_output_list[31]) > 250:
            flag = False
            print("The value of ControllerData Acceleration Release Rate is %s" % controller_output_list[31])

        if float(controller_output_list[32]) < 1 and float(controller_output_list[32]) > 250:
            flag = False
            print("The value of ControllerData Brake Rate is %s" % controller_output_list[32])

        if float(controller_output_list[33]) < 10 and float(controller_output_list[33]) > 100:
            flag = False
            print("The value of ControllerData Drive Current Limit is %s" % controller_output_list[33])

        if float(controller_output_list[34]) < 5 and float(controller_output_list[34]) > 100:
            flag = False
            print("The value of ControllerData Regen Current Limit is %s" % controller_output_list[34])

        if float(controller_output_list[35]) < 5 and float(controller_output_list[35]) > 100:
            flag = False
            print("The value of ControllerData Brake Current Limit is %s" % controller_output_list[35])

        if flag == False:
            return False
            
        return True
    except:
        ser.write("DIAG_CONTROLLER_STOP\t")
        time.sleep(0.1)






