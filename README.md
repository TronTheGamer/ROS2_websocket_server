
<h1 align='center'> 🤖 ROS2 - Websocket based server for Tutrtlebot3 🐢 </h1>

# 1. Table of Contents

- [1. Table of Contents](#1-table-of-contents)
- [2. 📔 Introduction](#2--introduction)
- [3. 📜 Instructions](#3--instructions)
  - [3.1. 🔨 Installation](#31--installation)
  - [3.2. ⚙️ Running the server](#32-️-running-the-server)
  - [3.3. ⌨️ Testing the server](#33-️-testing-the-server)
- [4. 🗒 Message Structure](#4--message-structure)

# 2. 📔 Introduction

This is a ROS2-Websocket server for communicating with the turtlebot sim via Websocket APIs.
This server only contains the server side code. You can test this code out by following the run instructions

# 3. 📜 Instructions

## 3.1. 🔨 Installation

- Clone this repository and `cd` to the cloned directory.
- Install the pre-requsites modules into your python3 env:

  ```bash
  ➡ pip install asyncio websockets
  ```

- Make sure that you have the ROS2 `Humble` installed in your system by:

   ```bash
   ➡ echo $ROS_DISTRO
   ```

  - This should result in `Humble`
- Now, build the package by:
  
  ```bash
  ➡ cd server_turtle/
  ➡ colcon build --symlink-install
  ```

- Source the package in the shell

    ```bash
    ➡ source ./install/setup.bash
    ```

## 3.2. ⚙️ Running the server

- Make sure the turtlebot3 is listening to your host pc and you are able to do teleop on the turtlebot

- Run the server using:

    ```bash
    ➡ ros2 run server_turtle websocket_bridge
    ```

-  You should now be able to see the server startup with the ip and port displayed in cli

## 3.3. ⌨️ Testing the server

- From some other pc / device connected to the same network, try running a websocket client at the server `ip:port`

# 4. 🗒 Message Structure

> [!IMPORTANT]
> The message structure for the server is in json as follows:
 
 ```json
 {
    "topic":"TOPIC_NAME",
    "val":{
        //ROS Topic valid values....
    } 
 }
 ```
 > [!NOTE]
 > The `TOPIC_NAME` can be found by:
 > ```bash
 > ➡ ros2 topic list 
 > ```