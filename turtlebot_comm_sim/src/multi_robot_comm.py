from geometry_msgs.msg import Pose
import rclpy
from rclpy.node import Node

class RobotCommunicator(Node):
    def __init__(self):
        super().__init__('robot_communicator')
        self.robot1_pose_sub = self.create_subscription(
            Pose, '/robot1/pose', self.robot1_pose_callback, 10)
        self.robot2_pose_pub = self.create_publisher(Pose, '/robot2/target_pose', 10)
    
    def robot1_pose_callback(self, msg):
        # Publikálja a célpontot robot2 számára
        self.robot2_pose_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    robot_comm = RobotCommunicator()
    rclpy.spin(robot_comm)
    robot_comm.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
