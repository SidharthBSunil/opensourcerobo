#!/bin/bash

# Exit on error
set -e

echo "--- Raju Brain: Dependency Setup ---"

# 1. Update system
echo "[1/4] Updating package list..."
sudo apt-get update

# 2. Install Python and ROS 2 build dependencies
echo "[2/4] Installing Python libraries and Build tools..."
sudo apt-get install -y python3-colcon-common-extensions
pip3 install requests opencv-python mediapipe

# 3. Check for Ollama
if command -v ollama &> /dev/null
then
    echo "[3/4] Ollama is already installed!"
else
    echo "[3/4] Installing Ollama (the AI engine)..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# 4. Pull the Phi-3 model
echo "[4/4] Downloading the Phi-3 AI model (This might take a while)..."
ollama pull phi3

echo ""
echo "--- Done! All dependencies installed. ---"
echo "You can now run 'bash run_raju.sh' to start the robot brain."
