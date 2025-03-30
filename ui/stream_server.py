# ui/stream_server.py
import asyncio
import websockets
import json
from simulation.pipeline import Pipeline
from simulation.sensor import Sensor

async def sensor_data(websocket, path):
    pipeline = Pipeline(length=1000, diameter=0.5, fluid_density=1000, friction_factor=0.02)
    sensor = Sensor(location=50, sensor_type='pressure')
    dt = 0.1
    while True:
        pipeline.update_state(dt)
        reading = sensor.read(pipeline)
        data = json.dumps({"pressure": reading})
        await websocket.send(data)
        await asyncio.sleep(dt)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(sensor_data, "localhost", 6789)
)
asyncio.get_event_loop().run_forever()
