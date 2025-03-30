# simulation/simulator.py
from simulation.pipeline import Pipeline, FluidType
from simulation.leak import Leak
from simulation.logger import log_action

class PipelineNetwork:
    @log_action
    def __init__(self):
        self.pipelines = {}
        self.leaks = []  # list of Leak objects

    @log_action
    def add_pipeline(self, pipeline):
        self.pipelines[pipeline.name] = pipeline
    
    @log_action
    def add_leak(self, leak):
        self.leaks.append(leak)
    
    @log_action
    def update(self, dt):
        # Update all pipelines
        for pipeline in self.pipelines.values():
            pipeline.update_state(dt)
        # Apply active leaks to their respective pipelines
        for leak in self.leaks:
            if leak.pipeline_name in self.pipelines:
                leak.inject(self.pipelines[leak.pipeline_name])
