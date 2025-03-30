#!/bin/bash

# Source the build environment
source ./server_turtle/install/setup.bash

# Start the server
ros2 run server_turtle websocket_bridge
