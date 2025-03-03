cmake_minimum_required(VERSION 3.0.2)
project(coverage_planner)

# Add ROS dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  cv_bridge
  roslib
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES coverage_planner
  CATKIN_DEPENDS roscpp std_msgs sensor_msgs cv_bridge roslib
  DEPENDS Eigen3 OpenCV CGAL SQLite3
)

# Add your other dependencies
find_package(Eigen3 REQUIRED)
find_package(OpenCV 4 REQUIRED)
find_package(CGAL REQUIRED COMPONENTS Core)
find_package(SQLite3 REQUIRED)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${EIGEN_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${CGAL_DEFINITIONS}
  ${CGAL_INCLUDE_DIRS}
  ${SQLite3_INCLUDE_DIRS}
  include  # Your include directory
)

# Collect source files
file(GLOB_RECURSE srcs "src/*.cc" "src/*.cpp")
file(GLOB_RECURSE hdrs "include/*.h")
list(REMOVE_ITEM srcs "${CMAKE_CURRENT_SOURCE_DIR}/src/db_publisher_node.cpp")

#Add new subscriber node source file
set(db_publisher_srcs src/db_publisher_node.cpp)

# Define the ROS node
add_executable(coverage_planner_node ${srcs} ${hdrs})
add_executable(db_publisher_node ${db_publisher_srcs})

# Link libraries
target_link_libraries(coverage_planner_node
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
  CGAL::CGAL
  CGAL::CGAL_Core
  pthread
)

target_link_libraries(db_publisher_node
  ${catkin_LIBRARIES}
  ${SQLite3_LIBRARIES}
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)