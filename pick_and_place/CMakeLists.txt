cmake_minimum_required(VERSION 3.0.2)
project(pick_and_place)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  geometry_msgs
)

catkin_python_setup()


add_message_files(
  FILES
  Grasp.msg
  # Message2.msg
)


generate_messages(
  DEPENDENCIES std_msgs geometry_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES pick_and_place
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
CATKIN_DEPENDS message_runtime rospy
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


