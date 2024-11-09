from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    # Első robot indítása
    robot1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            os.getenv('TURTLEBOT3_GAZEBO_MODEL_PATH'), 'turtlebot3_world.launch.py')]),
        launch_arguments={'robot_name': 'robot1', 'robot_namespace': '/robot1'}.items()
    )

    # Második robot indítása
    robot2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            os.getenv('TURTLEBOT3_GAZEBO_MODEL_PATH'), 'turtlebot3_world.launch.py')]),
        launch_arguments={'robot_name': 'robot2', 'robot_namespace': '/robot2'}.items()
    )

    return LaunchDescription([robot1, robot2])
