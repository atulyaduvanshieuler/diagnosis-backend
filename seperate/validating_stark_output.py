expected_output = [
    4053.1,
    4062.8,
    42949073.1,
    87.1,
    100.0,
    81.2,
    3.0,
    22.0,
    23.0,
    21.0,
    21.0,
    20.0,
    20.0,
    150.6,
    8.0,
    4053.2,
    4053.5,
    4053.7,
    4053.8,
    4053.8,
    4053.4,
    4053.4,
    4053.7,
    4053.3,
    0.0,
    0.0,
    0,
    0,
    0,
    0,
    0,
    0,
    4062.5,
    4062.6,
    4062.4,
    4062.7,
    4062.6,
    4062.6,
    4062.7,
    4062.6,
    0.0,
    4062.8,
    0.0,
    0.0,
    0,
    0,
    0,
    0,
    0,
    0,
    "dataType_bms",
    24.0,
    39.0,
    0.0,
    0.0,
    332.0,
    4.0,
    0.0,
    0.0,
    0.0,
    332.0,
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    0.0,
    0.0,
    0.0,
    19.0,
    19.0,
    21.7,
    0.7,
    81.0,
    81.0,
    0.0,
    520706.1,
    3.0,
    0.0,
    0.0,
    10.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    100.0,
    100.0,
    0.0,
    1,
    2.0,
    100098.0,
    1.0,
    14.0,
    37.0,
    0.0,
    0,
    0,
    0,
    0,
    0,
    False,
    1.0,
    0,
    0,
    4062.8,
    0.0,
    0.0,
    2.0,
    5.0,
    50.0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    96.6,
    250.0,
    0,
    0,
    0,
    0,
]

key_names = [
    "String Index",
    "dataType",
    'bmsData["Cell_V_Min_Val"]',
    ' bmsData["Cell_V_Max_Val"]',
    ' bmsData["Pack_I_Master"]',
    ' bmsData["Pack_Q_SOC_Trimmed"]',
    ' bmsData["SOH"]',
    ' bmsData["Pack_V_Sum_of_Cells"]',
    ' bmsData["BMSStatus"] ',
    'bmsData["Aux_T"][0]',
    ' bmsData["Aux_T"][1]',
    'bmsData["Aux_T"][2]',
    'bmsData["Aux_T"][3]',
    'bmsData["Aux_T"][4]',
    'bmsData["Aux_T"][5]',
    ' bmsData["BatteryCapacity"]',
    ' bmsData["CMU1_Cell_Vtgs"][0]',
    ' bmsData["CMU1_Cell_Vtgs"][1]',
    ' bmsData["CMU1_Cell_Vtgs"][2]',
    ' bmsData["CMU1_Cell_Vtgs"][3]',
    ' bmsData["CMU1_Cell_Vtgs"][4]',
    ' bmsData["CMU1_Cell_Vtgs"][5]',
    ' bmsData["CMU1_Cell_Vtgs"][6]',
    ' bmsData["CMU1_Cell_Vtgs"][7]',
    ' bmsData["CMU1_Cell_Vtgs"][8]',
    ' bmsData["CMU1_Cell_Vtgs"][9]',
    ' bmsData["CMU1_Cell_Vtgs"][10]',
    ' bmsData["CMU1_Cell_Vtgs"][11]',
    ' bmsData["CMU1_Cell_Vtgs"][12]',
    ' bmsData["CMU1_Cell_Vtgs"][13]',
    ' bmsData["CMU1_Cell_Vtgs"][14]',
    ' bmsData["CMU1_Cell_Vtgs"][15]',
    ' bmsData["CMU1_Cell_Vtgs[16]"]',
    ' bmsData["CMU1_Cell_Vtgs[17]"]',
    ' bmsData["CMU2_Cell_Vtgs"][0]',
    ' bmsData["CMU2_Cell_Vtgs"][1]',
    ' bmsData["CMU2_Cell_Vtgs"][2]',
    ' bmsData["CMU2_Cell_Vtgs"][3]',
    ' bmsData["CMU2_Cell_Vtgs"][4]',
    ' bmsData["CMU2_Cell_Vtgs"][5]',
    ' bmsData["CMU2_Cell_Vtgs"][6]',
    ' bmsData["CMU2_Cell_Vtgs"][7]',
    ' bmsData["CMU2_Cell_Vtgs"][8]',
    ' bmsData["CMU2_Cell_Vtgs"][9]',
    ' bmsData["CMU2_Cell_Vtgs"][10]',
    ' bmsData["CMU2_Cell_Vtgs"][11]',
    ' bmsData["CMU2_Cell_Vtgs"][12]',
    ' bmsData["CMU2_Cell_Vtgs"][13]',
    ' bmsData["CMU2_Cell_Vtgs"][14]',
    ' bmsData["CMU2_Cell_Vtgs"][15]',
    ' bmsData["CMU2_Cell_Vtgs[16]"]',
    ' bmsData["CMU2_Cell_Vtgs[17]"] ',
    " dataType_bms",
    'ControllerDATA["MotorTemp"]',
    ' ControllerDATA["Controller_Temp"]',
    ' ControllerDATA["SOC"]',
    ' ControllerDATA["Batt_Discharge_Current_Rate"]',
    ' ControllerDATA["Odometer"]',
    ' ControllerDATA["Vehicle_Status"]',
    ' ControllerDATA["AssistLevelGear"]',
    ' ControllerDATA["AlarmFault"]',
    ' ControllerDATA["SpeedLowHigh"]',
    ' ControllerDATA["TripLowHigh"]',
    ' ControllerDATA["FaultStatus"]',
    ' ControllerDATA["ThrottleCommand"]',
    ' ControllerDATA["ThrottleMultiplier"]',
    ' ControllerDATA["MappedThrottle"]',
    ' ControllerDATA["BrakeCommand"]',
    ' ControllerDATA["MappedBrake"]',
    ' ControllerDATA["Potential2Row"]',
    ' ControllerDATA["ThrottlePotentiometer"]',
    ' ControllerDATA["BatteryCapacityVoltage"]',
    ' ControllerDATA["BatteryKeyswitchVoltage"]',
    ' ControllerDATA["MotorRPM"]',
    ' ControllerDATA["ControllerMasterTimer"]',
    ' ControllerDATA["ControllerCurrentRMS"]',
    ' ControllerDATA["ControllerModulationDepth"]',
    ' ControllerDATA["ControllerFrequency"]',
    ' ControllerDATA["ControllerMainState"]',
    ' ControllerDATA["MotorTorqueEstimated"]',
    ' ControllerDATA["BatteryPowerConsumed"]',
    ' ControllerDATA["BatteryEnergyConsumed"]',
    ' ControllerDATA["AccelerationRate"]',
    ' ControllerDATA["AccelerationReleaseRate"]',
    ' ControllerDATA["BrakeRate"]',
    ' ControllerDATA["DriveCurrentLimit"]',
    ' ControllerDATA["RegenCurrentLimit"]',
    ' ControllerDATA["BrakeCurrentLimit"]',
    ' ControllerDATA["RegenOff"]',
    ' ControllerDATA["ControllerResetCANBaudRate"]',
    ' ControllerDATA["ControllerSerialNumber"]',
    ' ControllerDATA["VCLVersion"]',
    ' ControllerDATA["VCLBuildNumber"]',
    ' ControllerDATA["OSVersion"]',
    ' ControllerDATA["OSBuildNumber"]',
    '"dataType_controller"',
    ' "Temperature Ambient"',
    ' "Temperature C3 Box"',
    ' "Temperature ON Board"',
    ' "Datatype_ADC"',
    ' bmsData["FullyChargeFlag"]',
    ' ControllerDATA["VehiclePowerMode"]',
    ' "vehicleState"',
    ' "vehicle_parameter_ar_Status"',
    ' bmsData["balancingLimit"]',
    ' bmsData["prechargeActive"]',
    ' bmsData["balancingActive"]',
    ' bmsData["FW_major"]',
    ' bmsData["FW_minor"]',
    ' bmsData["BUILD_Date"]',
    '"brakeCount"',
    ' bmsData["requested_current"]',
    ' bmsData["requested_voltage"]',
    ' "charger_param_requested_current"',
    ' "charger_param_requested_voltage"',
    ' "charger_param_output_current"',
    ' "charger_param_output_voltage"',
    ' "charger_param_status"',
    ' "liq_temp"',
    ' bmsData["dynamic_in_limit"]',
    ' bmsData["dynamic_out_limit"]',
    " HW",
    " SW",
    "dataType_Misc",
    "stringIndex",
]

serial_ouput = []

key_indices_not_validated = [
    0,
    1,
    2,
    3,
    4,
    52,
    63,
    75,
    77,
    85,
    86,
    88,
    89,
    95,
    96,
    97,
    98,
    99,
    118,
    121,
    122,
    123,
    124,
]


def match(serial_output):
    flag = False
    for i in range(len(expected_output)):
        if i not in key_indices_not_validated:
            if expected_output[i] != serial_output[i]:
                flag = True
                print(expected_output[i], serial_ouput[i], key_names[i])

    if flag == False:
        validate(serial_ouput)
    else:
        print("Above mentioned keys are not matching")


def validate(serial_output):
    if serial_output[53] < -50 and serial_output[54] > 200:
        print("The vaue of ControllerData Motor Temp is %s " % serial_ouput[53])

    if serial_output[54] < -50 and serial_output[54] > 200:
        print("The vaue of ControllerData Controller Temp is %s " % serial_ouput[54])

    if serial_ouput[61] < -60 and serial_ouput[61] > 60:
        print("The value of ControllerData SpeedhighLow is %s" % serial_ouput[61])

    if serial_ouput[77] < -500 and serial_ouput[77] > 500:
        print("The value of ControllerData Frequency is %s" % serial_ouput[77])

    if serial_ouput[79] < -100 and serial_ouput[79] > 100:
        print("The value of ControllerData Motor Torque is %s" % serial_ouput[79])

    if serial_ouput[82] < 1 and serial_ouput[82] > 250:
        print("The value of ControllerData Acceleration Rate is %s" % serial_ouput[82])

    if serial_ouput[83] < 1 and serial_ouput[83] > 250:
        print(
            "The value of ControllerData Acceleration Release Rate is %s"
            % serial_ouput[83]
        )

    if serial_ouput[84] < 1 and serial_ouput[84] > 250:
        print("The value of ControllerData Brake Rate is %s" % serial_ouput[84])

    if serial_ouput[85] < 10 and serial_ouput[85] > 100:
        print(
            "The value of ControllerData Drive Current Limit is %s" % serial_ouput[85]
        )

    if serial_ouput[86] < 5 and serial_ouput[86] > 100:
        print(
            "The value of ControllerData Regen Current Limit is %s" % serial_ouput[86]
        )

    if serial_ouput[87] < 5 and serial_ouput[87] > 100:
        print(
            "The value of ControllerData Brake Current Limit is %s" % serial_ouput[87]
        )

    if serial_ouput[5] < 0 and serial_ouput[5] > 100:
        print("The value of Pack Q SoC Trimmed is %s" % serial_ouput[5])
