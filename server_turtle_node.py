import asyncio
import websockets
import rclpy
from rclpy.node import Node
from std_msgs.msg import Twist


class WebSocketBridge(Node):
    def __init__(self):
        super().__init__("websocket_bridge")
        self.cli = self.create_client(ControlTurtle, "control_turtle")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting...")

    async def publish_on_topic(self, topic: str, value: dict):
        self.publisher_top = self.create_publisher(Twist, topic, 10)
        self / publisher_top.publish(value)

    async def handle_client(self, websocket):
        self.get_logger().info("New Client Connected")
        try:
            while True:
                # Step 1: Receive message from client
                messsage = await websocket.recv()
                self.get_logger().info(f"Received message: {message}")

                # Step 2: Parse the JSON Message to publish on a ROS2 Topic
                try:
                    # Step 2.1: ID the topic
                    data = json.loads(message)
                    topic = data.get("topic")
                    if not topic:
                        await websocket.send(
                            json.dumps(
                                {
                                    "error": "Topic is required send the message 'topic': some_topic"
                                }
                            )
                        )

                        continue
                    # Step 2.2: Get the value set to publish
                    value = data.get("value")
                    if not value:
                        await websocket.send(
                            json.dumps(
                                {
                                    "error": "Value is required send the message 'value': some_value in a dictionary format"
                                }
                            )
                        )
                        continue

                except json.JSONDecodeError:
                    self.get_logger().error("Invalid JSON message")
                    continue
                # Step 3: Publish the message on a ROS2 Topic
                #
        except websockets.ConnectionClosed:
            self.get_logger().info("Client disconnected")
        except Exception as e:
            self.get_logger().error(f"Error: {e}")
            await websocket.send(json.dumps({"error": "Server error"}))


async def main():
    rclpy.init()
    node = WebSocketBridge()
    async with websockets.serve(node.handle_client, "0.0.0.0", 8080):
        print("WebSocket server started at ws://localhost:8080")
        await asyncio.Future()  # Run forever
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
