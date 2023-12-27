cmake_minimum_required(VERSION 3.5)

project(zeta_demos_gz)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
