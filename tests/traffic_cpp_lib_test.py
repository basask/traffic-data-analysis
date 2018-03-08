import unittest

from wrappers import traffic

class TrafficLibTest(unittest.TestCase):

    def test_detect_an_single_car_in_sensor_stream(self):
        readings = [0,0,0,0,0,34,65,76,56,24,0,0,1,0]
        vehicle_size = traffic.vehicle_size(readings)
        self.assertEqual(vehicle_size, 5)

    def test_detect_last_car_in_a_sensor_stream(self):
        readings = [0,0,34,65,76,56,24,0,0,1,0,20,24,45,12,0,0]
        vehicle_size = traffic.vehicle_size(readings)
        self.assertEqual(vehicle_size, 4)

    def test_no_detection_if_on_noisy_sensor_reading(self):
        readings = [0,0,2,0,40,2,0,0,67,7,0,0,0,0,12,6,0]
        vehicle_size = traffic.vehicle_size(readings)
        self.assertEqual(vehicle_size, 0)