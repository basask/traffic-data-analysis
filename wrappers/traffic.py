import ctypes
from ctypes import cdll

traffic_lib = cdll.LoadLibrary('./lib/traffic.so')

def vehicle_size(readings):
    string_param = ','.join(str(i) for i in readings)
    param = ctypes.c_char_p(string_param.encode('utf-8'))
    return traffic_lib.replay_sensor_readings(param)
