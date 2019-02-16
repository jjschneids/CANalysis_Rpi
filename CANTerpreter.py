 #! Author: Justin Schneider
# Created: 12:21AM February 8, 2019
# Purpose: Ready important CAN status information for web server

import os

class CANStatus(object):
    "This object contains all the latest information from our CAN bus" # __doc__
    fault1 = 1
    fault2 = 1
    fault3 = 1
    fault4 = 1
    fault5 = 1
    fault6 = 1
    cell0Voltage = 0.0
    cell1Voltage = 0.0
    
    def updateStatus(line):
        splitTokens = line.split(" ")
        date_raw = splitTokens[0]
        timestamp_raw = splitTokens[1]
        can_bus_raw = splitTokens[2]
        can_id = splitTokens[3]
        can_num_bytes_raw = splitTokens[4]
        can_num_bytes = strip(can_num_bytes_raw)
        can_num_butes_int = stoi(can_num_bytes)
        for i=5, i<=12, i++:
            try:
                can_byte[i-5] = splitTokens[i]
            except:
                break

if __name__ == "__main__":
    logfile.open("CanReadings.txt", "r")
    CANStatus = CanStatus()
    while True:
        file_line = logfile.readline()
        if file_line is None or len(file_line) == 0:
            continue
        CANStatus = CANStatus.updateStatus(file_line) #splits the line into words
    
