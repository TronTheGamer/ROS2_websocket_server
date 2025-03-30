import asyncio
import json
import websockets
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class WebSocketBridge(Node):
    def __init__(self):
        super().__init__("websocket_bridge")
        # Add any initialization here (e.g., service clients) if needed

    async def publish_on_topic(self, topic: str, value: dict):
        self.publisher_top = self.create_publisher(Twist, topic, 10)
        msg = Twist()
        msg.linear.x = float(value.get("linear_x", 0.0))
        msg.linear.y = float(value.get("linear_y", 0.0))
        msg.linear.z = float(value.get("linear_z", 0.0))
        msg.angular.x = float(value.get("angular_x", 0.0))
        msg.angular.y = float(value.get("angular_y", 0.0))
        msg.angular.z = float(value.get("angular_z", 0.0))
        self.publisher_top.publish(msg)

    async def handle_client(self, websocket):
        self.get_logger().info("New Client Connected")
        try:
            while True:
                message = await websocket.recv()
                self.get_logger().info(f"Received message: {message}")
                try:
                    data = json.loads(message)
                    topic = data.get("topic")
                    if not topic:
                        await websocket.send(
                            json.dumps(
                                {"error": "Topic is required: 'topic': some_topic"}
                            )
                        )
                        continue
                    value = data.get("value")
                    if not value:
                        await websocket.send(
                            json.dumps(
                                {"error": "Value is required: 'value': some_value"}
                            )
                        )
                        continue
                    await self.publish_on_topic(topic, value)
                except json.JSONDecodeError:
                    self.get_logger().error("Invalid JSON message")
                    continue
        except websockets.ConnectionClosed:
            self.get_logger().info("Client disconnected")
        except Exception as e:
            self.get_logger().error(f"Error: {e}")
            await websocket.send(json.dumps({"error": "Server error"}))


async def ros_spin(node):
    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec=0.1)
        await asyncio.sleep(0.01)


async def async_main(node):
    ros_task = asyncio.create_task(ros_spin(node))
    async with websockets.serve(node.handle_client, "0.0.0.0", 8080):
        print("WebSocket server started at ws://localhost:8080")
        await asyncio.Future()  # Run forever
    ros_task.cancel()


def main(args=None):
    rclpy.init(args=args)
    node = WebSocketBridge()
    try:
        asyncio.run(async_main(node))
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
