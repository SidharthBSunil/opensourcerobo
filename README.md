# 🤖 Raju Brain: My AI Robot Project!

Welcome! This is a simple project to give a robot a "brain" using **Ollama** (an AI engine) and **Phi-3** (a smart AI model). It can also track your hand movements using your webcam!

---

## 🌟 What does this do?
1. **The Brain (`raju_brain`)**: It uses the Phi-3 AI model to answer questions. If you send it text, it replies back!
2. **The Hand Controller (`hand_servo_publisher`)**: It uses your webcam to see your hand. It counts your fingers and sends an angle to control a robot's motor (servo)!

---

## 🚀 How to set it up (Easy Mode)

If you are on a new Linux computer, follow these simple steps:

### 1. Open your Terminal
Press `Ctrl + Alt + T` on your keyboard to open the command line.

### 2. Go to the project folder
Type this and press Enter:
```bash
cd ~/Downloads/ros2/opensourcerobo
```

### 3. Run the installer
This magic script will install everything you need (Python libraries, Ollama, and the Phi-3 model).
```bash
bash setup_dependencies.sh
```
*Note: This might take a few minutes because the AI model is about 2GB.*

---

## 🎮 How to run it

Once the installer is finished, you can start the robot with one command:

```bash
bash run_raju.sh
```

### What happens now?
- **Ollama** starts in the background.
- Your **Webcam** will open. Try showing 2 fingers or 5 fingers to move the robot's "hand"!
- The **AI Brain** starts waiting for text messages.

---

## ✨ For Curious Minds (How it works)

- **Ollama**: Think of this as the "engine" that runs the AI. 
- **Phi-3**: This is the "knowledge" inside the brain. It's a small but very smart AI model made by Microsoft.
- **ROS 2**: This is the "skeleton" of the robot. it helps different parts (like the camera and the brain) talk to each other.
- **Mediapipe**: This is what the robot uses to "see" your hand. It's made by Google!

---

### 🛠️ Troubleshooting
- **Webcam not opening?** Make sure no other apps (like Zoom or Teams) are using it.
- **AI not responding?** Make sure you have an internet connection during the first setup so it can download Phi-3.

Have fun building! 🚀
