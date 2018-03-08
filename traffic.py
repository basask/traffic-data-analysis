from ctypes import cdll

traffic_lib = cdll.LoadLibrary('./libc/traffic.so')

# C
# vehicle_size = traffic_lib.vehicle_size

# C++
vehicle_size = traffic_lib._Z12vehicle_sizei