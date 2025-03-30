import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:6789"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to the WebSocket server.")
            while True:
                message = await websocket.recv()
                try:
                    data = json.loads(message)
                    print("Received data:", data)
                except json.JSONDecodeError:
                    print("Received non-JSON data:", message)
    except Exception as e:
        print("Error connecting or receiving data:", e)

if __name__ == "__main__":
    asyncio.run(test_websocket())
