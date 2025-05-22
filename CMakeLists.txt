cmake_minimum_required(VERSION 3.0.2)
project(touchlab_driver_ros)

find_package(catkin REQUIRED COMPONENTS
  rospy
  touchlab_msgs
  std_srvs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/touchlab_driver
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
