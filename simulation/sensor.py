# simulation/sensor.py
import numpy as np

class Sensor:
    def __init__(self, location, sensor_type, noise_std=0.01):
        self.location = location
        self.sensor_type = sensor_type  # e.g., 'pressure', 'flow'
        self.noise_std = noise_std
    
    def read(self, pipeline):
        # Example for pressure sensor:
        raw_value = pipeline.pressure_profile[self.location]
        noise = np.random.normal(0, self.noise_std)
        return raw_value + noise
