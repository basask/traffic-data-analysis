import ctypes
from ctypes import cdll

try:
    traffic_lib = cdll.LoadLibrary('./lib/traffic.so')
    clib = True
except OSError as e:
    from . import mock_lib as traffic_lib
    clib = False

def vehicle_size(readings):
    param = readings
    if clib:
        param = ','.join(str(i) for i in param)
        param = ctypes.c_char_p(param.encode('utf-8'))
    return traffic_lib.replay_sensor_readings(param)
