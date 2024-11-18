from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_comm_sim',
            executable='communication_node',
            name='communication_node'
        ),
        Node(
            package='turtlebot_comm_sim',
            executable='movement_controller',
            name='movement_controller'
        ),
    ])
