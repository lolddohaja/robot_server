ARG BUILDER_NS="rmf_deployment_template"
ARG TAG="latest"

FROM $BUILDER_NS/iron-rmf:$TAG

SHELL ["bash", "-c"]

RUN apt update

WORKDIR /opt/rmf

# copy rmf-simulation source files
COPY rmf-simulation-src src

RUN python3 -m pip install flask-socketio fastapi uvicorn

RUN rosdep update --rosdistro $ROS_DISTRO
RUN rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO \
    --skip-keys roscpp  \
    --skip-keys actionlib \ 
    --skip-keys rviz \ 
    --skip-keys catkin \ 
    --skip-keys move_base \ 
    --skip-keys amcl \ 
    --skip-keys turtlebot3_navigation \ 
    --skip-keys turtlebot3_bringup \ 
    --skip-keys move_base_msgs \ 
    --skip-keys dwa_local_planner \ 
    --skip-keys map_server \
    -y

RUN apt update && apt install -y \
    ros-humble-rviz2 \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/$ROS_DISTRO/setup.sh \
  && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

RUN sed -i '$isource "/opt/rmf/install/setup.bash"' /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
