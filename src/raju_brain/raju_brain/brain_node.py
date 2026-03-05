import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests


class RajuBrain(Node):
    def __init__(self):
        super().__init__('raju_brain')

        self.sub = self.create_subscription(
            String,
            '/stt/text',
            self.callback,
            10
        )

        self.pub = self.create_publisher(
            String,
            '/tts/text',
            10
        )

        self.get_logger().info("RAJU BRAIN started (Ollama model: raju)")

    def ask_raju(self, text):
        try:
            r = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "phi3",
                    "prompt": text,
                    "stream": False,
                    "context": [],          # clears memory
                    "options": {
                        "num_predict": 60   # limits output length
                    }
                },
                timeout=30
            )
            return r.json().get("response", "").strip()
        except Exception as e:
            self.get_logger().error(str(e))
            return "Sorry, enikku manasilayilla."

    def callback(self, msg):
        user_text = msg.data
        self.get_logger().info(f"From Pi: {user_text}")

        reply = self.ask_raju(user_text)

        out = String()
        out.data = reply
        self.pub.publish(out)

        self.get_logger().info(f"To Pi: {reply}")


def main():
    rclpy.init()
    node = RajuBrain()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
