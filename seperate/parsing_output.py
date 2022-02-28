from sha256_converter import converter

with open("./serial_log") as log:
    data = log.read()
    parsed_data = data.split("\n")
    for i in range(len(parsed_data)):
        data_points = parsed_data[i].split(",")
        if len(data_points) == 3:
            # hashed_data=converter(",".join(data_points[1:-1]))
            # print(hashed_data)
            if data_points[1] == "43794":
                print("Data Matched")
            else:
                print("Data Not Matched")

    # print(parsed_data)
    # print(data)
