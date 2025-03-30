# simulation/sensor.py
import numpy as np

class Sensor:
    def __init__(self, location, sensor_type, noise_std=0.01):
        self.location = location
        self.sensor_type = sensor_type  # e.g., 'pressure'
        self.noise_std = noise_std
    
    def read(self, pipeline):
        # For example, read pressure at the sensor's location
        raw_value = pipeline.pressure_profile[self.location]
        noise = np.random.normal(0, self.noise_std)
        return raw_value + noise