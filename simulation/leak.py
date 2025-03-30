# simulation/leak.py
from simulation.logger import log_action

class Leak:
    @log_action
    def __init__(self, pipeline_name, location, leak_coefficient=0.05):
        self.pipeline_name = pipeline_name  # identifies which pipeline
        self.location = location  # segment index where leak occurs
        self.leak_coefficient = leak_coefficient  # fraction reduction per injection
        self.active = False  # not active by default

    @log_action
    def inject(self, pipeline):
        if self.active:
            # Reduce the pressure and flow at the leak location
            pipeline.pressure_profile[self.location] *= (1 - self.leak_coefficient)
            pipeline.flow_profile[self.location] *= (1 - self.leak_coefficient)
            # Propagate the flow drop downstream to mimic leak effect
            for i in range(self.location + 1, len(pipeline.flow_profile)):
                pipeline.flow_profile[i] *= (1 - self.leak_coefficient)
