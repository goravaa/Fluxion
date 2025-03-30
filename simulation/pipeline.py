# simulation/pipeline.py
import numpy as np
from enum import Enum
from simulation.logger import log_action

class FluidType(Enum):
    LIQUID = "liquid"
    GAS = "gas"

class Pipeline:
    @log_action
    def __init__(self, name, length, fluid_type=FluidType.LIQUID, friction_factor=0.02):
        self.name = name
        self.length = length  # in metres
        self.fluid_type = fluid_type
        self.friction_factor = friction_factor
        self.num_segments = int(length)  # 1 segment per metre
        
        # Initialize profiles: starting pressure ~90 and flow ~10 for each segment.
        self.pressure_profile = [90.0] * self.num_segments  
        self.flow_profile = [10.0] * self.num_segments
        
        # Automatically assign sensors at the start and end segments
        self.sensors = {
            "start": {"name": f"{name}_start", "location": 0},
            "end": {"name": f"{name}_end", "location": self.num_segments - 1}
        }

    @log_action
    def update_state(self, dt):
        if self.fluid_type == FluidType.LIQUID:
            self._update_liquid(dt)
        else:
            self._update_gas(dt)

    def _update_liquid(self, dt):
        # Simplified placeholder: simulate friction loss
        self.pressure_profile = [p * 0.999 for p in self.pressure_profile]
        self.flow_profile = [q * 0.999 for q in self.flow_profile]

    def _update_gas(self, dt):
        # Simplified placeholder for gas
        self.pressure_profile = [p * 0.998 for p in self.pressure_profile]
        self.flow_profile = [q * 0.998 for q in self.flow_profile]
