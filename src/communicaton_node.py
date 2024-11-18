import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommunicationNode(Node):
    def __init__(self):
        super().__init__('communication_node')
        self.publisher_ = self.create_publisher(String, 'robot_communication', 10)
        self.subscription = self.create_subscription(
            String,
            'robot_communication',
            self.listener_callback,
            10
        )
        self.timer = self.create_timer(2.0, self.publish_message)
    
    def publish_message(self):
        msg = String()
        msg.data = "Hello from Communication Node"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sent message: "{msg.data}"')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    communication_node = CommunicationNode()
    rclpy.spin(communication_node)
    communication_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
