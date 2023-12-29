ARG BUILDER_NS="open-rmf/rmf_deployment_template"
ARG TAG="latest"
FROM $BUILDER_NS/rmf:$TAG

ARG NETRC

SHELL ["bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

RUN apt update && apt install -y \
    ros-humble-rviz2 \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    && rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/$ROS_DISTRO/setup.bash && apt update && apt install -y \
    ros-humble-turtlebot3-gazebo \
    && rm -rf /var/lib/apt/lists/*

# WORKDIR /opt/turtlebot3

# COPY zeta_demos_gz src/zeta_demos_gz

# RUN rosdep update --rosdistro $ROS_DISTRO

# RUN apt update && rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -y

# RUN . /opt/ros/$ROS_DISTRO/setup.sh \
#   && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release


# RUN sed -i '$isource "/opt/turtlebot3/install/setup.bash"' /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
