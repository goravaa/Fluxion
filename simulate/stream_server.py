# simulate/stream_server.py
import asyncio
import websockets
import json
import random
from simulation.simulator import PipelineNetwork
from simulation.pipeline import Pipeline, FluidType
from simulation.sensor import Sensor  # Your basic pressure sensor implementation
from simulation.leak import Leak

async def sensor_data(websocket, path=None):
    # Instantiate the simulation network.
    network = PipelineNetwork()
    # Create a pipeline (for example, named "Pipe1" with a length of 100 metres).
    pipeline = Pipeline(name="Pipe1", length=100, fluid_type=FluidType.LIQUID)
    network.add_pipeline(pipeline)
    
    # Create two sensors (start and end).
    sensor_start = Sensor(location=0, sensor_type="pressure", noise_std=0.02)
    sensor_end = Sensor(location=pipeline.num_segments - 1, sensor_type="pressure", noise_std=0.02)
    
    # Create a leak. We'll randomize its location when triggered.
    leak = Leak(pipeline_name="Pipe1", location=50, leak_coefficient=0.05)
    network.add_leak(leak)
    # Initially, no leak is active.
    leak.active = False

    dt = 0.1  # time step in seconds
    while True:
        # Randomly trigger a leak if none is active.
        if not leak.active and random.random() < 0.005:  # approx. one event every 20 sec
            # Choose a random segment for the leak
            leak.location = random.randint(0, pipeline.num_segments - 1)
            leak.active = True
            print(f"Leak triggered at segment {leak.location}")
        
        # Here you could add logic to trigger repairs or further evolution.
        # For now, once a leak is active, it remains active.
        
        network.update(dt)
        # Gather sensor readings.
        data = {
            "pipe": "Pipe1",
            "start_pressure": sensor_start.read(pipeline),
            "end_pressure": sensor_end.read(pipeline),
            "leak_active": leak.active,
            "leak_location": leak.location,
            "leak_pressure": pipeline.pressure_profile[leak.location],
            "leak_flow": pipeline.flow_profile[leak.location]
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(dt)

async def main():
    async with websockets.serve(sensor_data, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
