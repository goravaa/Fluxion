# simulation/leak.py
class Leak:
    def __init__(self, location, leak_coefficient):
        self.location = location
        self.leak_coefficient = leak_coefficient
        self.active = False
    
    def inject(self, pipeline, current_time):
        if self.active:
            # Modify the pipeline state at the leak location:
            # Example: pressure drop proportional to leak_coefficient
            pipeline.pressure_profile[self.location] *= (1 - self.leak_coefficient)
