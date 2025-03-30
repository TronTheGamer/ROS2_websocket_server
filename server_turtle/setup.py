from setuptools import setup

package_name = "server_turtle"

setup(
    name=package_name,
    version="0.0.1",  # Ensure this is a string
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=[
        "setuptools>=61.0.0",  # Specify a minimum version to avoid compatibility issues
        "websockets",  # For your WebSocket dependency
    ],
    zip_safe=True,
    maintainer="Your Name",
    maintainer_email="your.email@example.com",
    description="A ROS 2 node bridging WebSocket and ROS 2 topics",
    license="Apache License 2.0",
    # Remove tests_require; handle testing separately if needed
    entry_points={
        "console_scripts": [
            "websocket_bridge = server_turtle.server_turtle_node:main",  # Adjust if filename differs
        ],
    },
)
