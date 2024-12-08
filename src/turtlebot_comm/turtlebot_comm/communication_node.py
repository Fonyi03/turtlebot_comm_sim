import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class CommunicationNode(Node):
    def __init__(self):
        super().__init__('communication_node')
        self.publisher = self.create_publisher(Marker, '/communication_marker', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info("Communication Node Started")

    def publish_status(self):
        msg = Marker()
        msg.header.frame_id = "map"
        msg.ns = "communication"
        msg.id = 2
        msg.type = Marker.TEXT_VIEW_FACING
        msg.action = Marker.ADD
        msg.pose.position.x = 1.0
        msg.pose.position.y = 1.0
        msg.pose.position.z = 1.5
        msg.scale.z = 0.5  # Text size
        msg.color.a = 1.0  # Alpha
        msg.color.r = 0.0
        msg.color.g = 0.0
        msg.color.b = 1.0
        msg.text = "Communication Active"
        self.publisher.publish(msg)
        self.get_logger().info("Published Communication Marker")

def main(args=None):
    rclpy.init(args=args)
    node = CommunicationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
