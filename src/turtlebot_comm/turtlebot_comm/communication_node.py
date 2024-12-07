#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommunicationNode(Node):
    def __init__(self):
        super().__init__('communication_node')
        self.publisher = self.create_publisher(String, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info("Communication Node Started")

    def publish_status(self):
        msg = String()
        msg.data = "Robot is active"
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")

def main(args=None):
    try:
        rclpy.init(args=args)
        node = CommunicationNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
