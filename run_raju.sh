#!/bin/bash

# This script builds the workspace and starts the robot brain!

# 1. Source ROS 2 (Assuming Humble/Iron/Jazzy - path may vary but standard is /opt/ros)
if [ -f "/opt/ros/humble/setup.bash" ]; then
    source /opt/ros/humble/setup.bash
elif [ -f "/opt/ros/iron/setup.bash" ]; then
    source /opt/ros/iron/setup.bash
elif [ -f "/opt/ros/jazzy/setup.bash" ]; then
    source /opt/ros/jazzy/setup.bash
else
    echo "[!] Warning: ROS 2 setup.bash not found in standard paths. Please source it manually."
fi

# 2. Build the workspace
echo "--- Building the Robot Brain ---"
colcon build

# 3. Source the local workspace
source install/setup.bash

# 4. Starting the nodes
echo "--- Starting Raju Brain & Hand Controller ---"
echo "Press Ctrl+C to stop everything."

# Run nodes in background/separate processes
# Note: In a real robot, we might use a launch file, but for a 14-year-old, scripts are clear.
ros2 run raju_brain brain_node &
BRAIN_PID=$!

ros2 run raju_brain hand_servo_publisher &
HAND_PID=$!

# Wait for Ctrl+C
trap "kill $BRAIN_PID $HAND_PID; exit" INT
wait
