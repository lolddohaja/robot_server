ARG BUILDER_NS="open-rmf/rmf_deployment_template"
ARG TAG="latest"
FROM $BUILDER_NS/builder-rosdep:$TAG

ARG NETRC

SHELL ["bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

RUN apt update && apt install -y \
    ros-humble-rviz2 \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    && rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/$ROS_DISTRO/setup.bash && apt update && apt install -y \
    ros-humble-turtlebot3-gazebo \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
