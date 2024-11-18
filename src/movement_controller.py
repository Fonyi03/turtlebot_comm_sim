import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class MovementController(Node):
    def __init__(self):
        super().__init__('movement_controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            String,
            'robot_communication',
            self.listener_callback,
            10
        )
        self.timer = self.create_timer(1.0, self.move_robot)

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.5  # Haladás előre
        msg.angular.z = 0.1  # Fordulás
        self.publisher_.publish(msg)
        self.get_logger().info('Moving robot with linear velocity 0.5 and angular velocity 0.1')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received command: "{msg.data}"')
        # A parancs alapján módosítható a robot mozgása vagy viselkedése

def main(args=None):
    rclpy.init(args=args)
    movement_controller = MovementController()
    rclpy.spin(movement_controller)
    movement_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
