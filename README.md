
<h1 align='center'> 🤖 ROS2 - Websocket based server </h1>

# 1. Table of Contents

- [1. Table of Contents](#1-table-of-contents)
- [2. 📔 Introduction](#2--introduction)
- [3. 📜 Instructions](#3--instructions)
  - [Installation](#installation)

# 2. 📔 Introduction

This is a ROS2-Websocket server for communcating with the turtlebot sim via Websocket APIs.
This server only contains the server side code. You can test this code out by following the run instructions

# 3. 📜 Instructions

## Installation

- Clone this repository and `cd` to the cloned directory.
- Make sure that you have the ROS2 `Humble` installed in your system by:

   ```bash
   echo $ROS_DISTRO
   ```

  - This should result in `Humble`
- Now, build the package by:
  
  ```bash
  colcon build --symlink-install
  ```

- Source the package in the shell

    ```bash
    source ./