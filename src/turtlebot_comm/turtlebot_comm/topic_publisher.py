import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotCommandPublisher(Node):
    def __init__(self):
        super().__init__('robot_command_publisher')

        # Topic a TurtleBot3 Burger számára
        self.burger_cmd_vel_publisher = self.create_publisher(
            Twist,
            '/robot_burger/cmd_vel',
            10
        )

        # Topic az Evata robot számára
        self.evata_cmd_vel_publisher = self.create_publisher(
            Twist,
            '/evata/cmd_vel',
            10
        )

        # Timer a rendszeres üzenetküldéshez
        self.timer = self.create_timer(1.0, self.publish_commands)

    def publish_commands(self):
        # Parancs a TurtleBot3 számára
        burger_cmd = Twist()
        burger_cmd.linear.x = 0.5
        burger_cmd.angular.z = 0.1
        self.burger_cmd_vel_publisher.publish(burger_cmd)
        self.get_logger().info('Published to /robot_burger/cmd_vel')

        # Parancs az Evata robot számára
        evata_cmd = Twist()
        evata_cmd.linear.x = 0.3
        evata_cmd.angular.z = 0.0
        self.evata_cmd_vel_publisher.publish(evata_cmd)
        self.get_logger().info('Published to /evata/cmd_vel')

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
