cmake_minimum_required(VERSION 3.5)
project(turtlebot_comm_sim)

# ROS2 alapcsomagok hozzáadása
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# Python fájlok telepítése
install(
  DIRECTORY src/
  DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
)

# Python fájlok végrehajtási jogosultságának biztosítása
install(
  PROGRAMS
  src/communication_node.py
  src/movement_controller.py
  DESTINATION lib/${PROJECT_NAME}
)

# Launch mappa telepítése
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
