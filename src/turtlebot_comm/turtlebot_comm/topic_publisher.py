import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class RobotCommandPublisher(Node):
    def __init__(self):
        super().__init__('robot_command_publisher')

        # Marker topicok a két robot számára
        self.burger_marker_publisher = self.create_publisher(
            Marker,
            '/robot_burger/marker',
            10
        )

        self.evata_marker_publisher = self.create_publisher(
            Marker,
            '/evata/marker',
            10
        )

        # Timer a rendszeres üzenetküldéshez
        self.timer = self.create_timer(1.0, self.publish_markers)

    def publish_markers(self):
        # Marker a TurtleBot3 Burger számára
        burger_marker = Marker()
        burger_marker.header.frame_id = "map"
        burger_marker.ns = "robot_burger"
        burger_marker.id = 0
        burger_marker.type = Marker.SPHERE
        burger_marker.action = Marker.ADD
        burger_marker.pose.position.x = 0.0
        burger_marker.pose.position.y = 0.0
        burger_marker.pose.position.z = 0.0
        burger_marker.scale.x = 0.5
        burger_marker.scale.y = 0.5
        burger_marker.scale.z = 0.5
        burger_marker.color.a = 1.0  # Alpha
        burger_marker.color.r = 1.0
        burger_marker.color.g = 0.0
        burger_marker.color.b = 0.0
        self.burger_marker_publisher.publish(burger_marker)
        self.get_logger().info('Published Burger Marker')

        # Marker az Evata számára
        evata_marker = Marker()
        evata_marker.header.frame_id = "map"
        evata_marker.ns = "evata"
        evata_marker.id = 1
        evata_marker.type = Marker.CUBE
        evata_marker.action = Marker.ADD
        evata_marker.pose.position.x = 2.0
        evata_marker.pose.position.y = 2.0
        evata_marker.pose.position.z = 0.0
        evata_marker.scale.x = 0.5
        evata_marker.scale.y = 0.5
        evata_marker.scale.z = 0.5
        evata_marker.color.a = 1.0  # Alpha
        evata_marker.color.r = 0.0
        evata_marker.color.g = 1.0
        evata_marker.color.b = 0.0
        self.evata_marker_publisher.publish(evata_marker)
        self.get_logger().info('Published Evata Marker')

def main(args=None):
    rclpy.init(args=args)
    node = RobotCommandPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
