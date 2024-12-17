import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')

        # Marker-ek figyelése
        self.subscription = self.create_subscription(
            Marker,
            '/robot_burger/marker',
            self.listener_callback,
            10)
        self.subscription  # Prevent unused variable warning
        self.get_logger().info('Subscriber Node Started')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received Marker from Burger Robot: {msg.ns}')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()