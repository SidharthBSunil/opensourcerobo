import cv2
import mediapipe as mp
import os

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# Silence TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


class HandServoPublisher(Node):
    def __init__(self):
        super().__init__('hand_servo_publisher')
        self.pub = self.create_publisher(Int32, '/servo_angle', 10)

        self.cap = cv2.VideoCapture(0)

        self.value = 90  # start at center (0–180)
        self.VALUE_MIN = 0
        self.VALUE_MAX = 180
        self.MAX_SPEED = 5.0

        self.hands = mp_hands.Hands(
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.timer = self.create_timer(0.05, self.loop)  # 20 Hz


    def count_open_fingers(self, hand_landmarks):
        tips = [8, 12, 16, 20]
        pips = [6, 10, 14, 18]

        count = 0
        for tip, pip in zip(tips, pips):
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                count += 1
        return count


    def loop(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                open_fingers = self.count_open_fingers(hand_landmarks)

                # Map fingers (0–4) → control (-1 to +1)
                control = (open_fingers - 2) / 2.0

                if abs(control) < 0.2:
                    control = 0.0

                self.value += control * self.MAX_SPEED
                self.value = max(self.VALUE_MIN, min(self.VALUE_MAX, self.value))

                msg = Int32()
                msg.data = int(self.value)
                self.pub.publish(msg)

                self.get_logger().info(f"Servo angle: {msg.data}")

                cv2.putText(
                    frame, f"Fingers: {open_fingers}",
                    (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2
                )

        cv2.putText(
            frame, f"Angle: {int(self.value)}",
            (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
            1.4, (0, 255, 0), 3
        )

        cv2.imshow("Hand Servo Control", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            self.cap.release()
            cv2.destroyAllWindows()
            rclpy.shutdown()


def main():
    rclpy.init()
    node = HandServoPublisher()
    rclpy.spin(node)
