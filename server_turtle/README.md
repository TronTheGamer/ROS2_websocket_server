<h1 align='center'> 🤖 ROS2 Websocket Server for Turtlebot3 </h1> 

This is a Websocket based server written in python for controlling a Turtlebot3 remotely

# 1. 📔 Table of Contents

- [1. 📔 Table of Contents](#1--table-of-contents)
- [2. :link: Pre-Requisites](#2-link-pre-requisites)
- [3. :gear: Installation:](#3-gear-installation)
    - [Exposing the server to Public IP:](#exposing-the-server-to-public-ip)

# 2. :link: Pre-Requisites

- Make sure that ROS2 humble is installed on your system.

# 3. :gear: Installation:

- Clone the repository using `git clone ...`
- go to the cloned folder
  
  ```bash
  cd server_turtle/
  ```

- Build the package:
  
  ```bash
  colcon build --symlink-install
  ```

- source the package:
  
  ```bash
  source install/setup.bash
  ```

- Make sure that the Turtlebot3 is connected to your system and you can see it's messages by:

  ```bash
  ros2 topic list
  ```

- run the server node:
  
  ```bash
  ros2 run server_turtle websocket_bridge
  ```

- You should be able to see that the websocket server has been started in localhost:8080.

### Exposing the server to Public IP:

[WIP]