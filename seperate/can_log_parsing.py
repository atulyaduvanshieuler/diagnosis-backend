import codecs
from updated_stark_parser import stark_parser

with codecs.open("CAN1_log_160222_Test_Vehicle.trc", "r", "UTF8") as inputFile:
    inputFile = inputFile.readlines()

can_ids = []
can_ids_set = set()
counter = 0
can_data = []
exact_time = [0]

for line in inputFile[14:]:
    req = []
    req = [s for s in line.split(" ") if s != ""]
    exact_time.append(float(req[1]))
    can_ids.append(req[3])
    can_data.append(req[5:-1])

sleeping_time = []
for i in range(1, len(exact_time)):
    sleeping_time.append(exact_time[i] - exact_time[i - 1])

trimmed_can_ids = []
for s in can_ids:
    if s[0] == "0":
        for i in range(len(s)):
            if s[i] != "0":
                trimmed_can_ids.append(s[i:])
                break
    else:
        trimmed_can_ids.append(s)


cdata = []
for c in can_data:
    cdata.append("".join(c))

hex_format_can_data = []
for lst in can_data:
    new_lst = []
    for i in range(len(lst)):
        new_lst.append("0x" + lst[i])
    hex_format_can_data.append(new_lst)

new_can_ids = []
for s in can_ids:
    if s[0] == "0":
        for i in range(len(s)):
            if s[i] != "0":
                new_can_ids.append("0x" + s[i:])
                break
    else:
        new_can_ids.append("0x" + s)

can_ids_for_expected_output = []
can_data_for_expected_output = []

prev = 0
exact_time = exact_time[1:]
mapp = {}
for i in range(len(exact_time)):
    if exact_time[i] // 5000 > prev:
        mapp[str(prev)] = stark_parser(
            can_ids_for_expected_output, can_data_for_expected_output
        )
        prev = exact_time[i] // 5000
        can_ids_for_expected_output = [trimmed_can_ids[i]]
        can_data_for_expected_output = [cdata[i]]
    else:
        can_ids_for_expected_output.append(trimmed_can_ids[i])
        can_data_for_expected_output.append(cdata[i])
    if i == len(exact_time) - 1:
        mapp[str(prev)] = stark_parser(
            can_ids_for_expected_output, can_data_for_expected_output
        )
print(mapp["0"])

# can_ids_for_expected_output=trimmed_can_ids
can_ids_for_real_output = new_can_ids
# can_data_for_expected_output=cdata
can_data_for_real_output = hex_format_can_data


# print(neww)


# 110-118
# 11A-11E
# 705,706,708,710,715,716,717,724,726
#
# Not included 20,12a,259,725,1806E5F4
# 728 not in can1 but in can2


# with codecs.open("CAN2_LOG_160222_TestVehicle.trc", "r", "UTF8") as inputFile:
#    inputFile=inputFile.readlines()
# can2_ids=[]
# can2_ids_set=set()
# counter=0
# can2_data=[]
#
##print(inputFile[14])
# for line in inputFile[14:]:
#    #print(line)
#    req=[]
#    req=[s for s in line.split(" ") if s!='']
#    #print(req)
#    can2_ids.append(req[3])
#    can2_ids_set.add(req[3])
#    can2_data.append(req[5:-1])
##print(can2_ids)
# can2_ids_set=list(can2_ids_set)
# can2_ids_set.sort()
##print(can2_data)
##print(can2_ids_set)
# new_can2_ids_set=[]
# for s in can2_ids_set:
#    if s[0]=="0":
#        for i in range(len(s)):
#            if s[i]!="0":
#                new_can2_ids_set.append(s[i:])
#                break
#    else:
#        new_can2_ids_set.append(s)
# print(new_can2_ids_set)
