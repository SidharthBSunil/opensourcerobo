#!/bin/bash

# This script helps you connect your PC to your Raspberry Pi!
# ROS 2 uses "Domain IDs" to make sure the right computers talk to each other.

if [ -z "$1" ]; then
    echo "Usage: source setup_network.sh [DOMAIN_ID]"
    echo "Example: source setup_network.sh 42"
    echo ""
    echo "Please provide a Domain ID (a number between 0 and 101)."
    return 1 2>/dev/null || exit 1
fi

export ROS_DOMAIN_ID=$1
export ROS_LOCALHOST_ONLY=0

echo "✅ Success! ROS_DOMAIN_ID is now set to: $ROS_DOMAIN_ID"
echo "🌐 Your PC is now ready to talk to your Raspberry Pi on the same network."
echo "Remember: Both your PC and Raspberry Pi MUST use the SAME number!"
