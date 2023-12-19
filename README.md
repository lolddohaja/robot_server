
# Run rmf

```bash
docker run --rm --network=host -it \
open-rmf/rmf_deployment_template/rmf-web-rmf-server:latest
```

```bash
docker run --rm --network=host --gpus all -it \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
open-rmf/rmf_deployment_template/rmf-simulation:latest \
bash -c "ros2 launch rmf_demos_gz_classic hotel.launch.xml \
server_uri:=ws://localhost:8000/_internal"
```

```bash
docker run --rm -p 3000:80 \
-it open-rmf/rmf_deployment_template/rmf-web-dashboard-local:latest
```

# Build turtlebot3
#### install vcstool
```bash
# These commands are executed on your local system to setup ROS 2 and RMF environment
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install python3-vcstool -y
```

#### Build turtlebot3 image
```bash
# Build turtlebot3 Docker image
docker build -f turtlebot3.Dockerfile -t open-rmf/rmf_deployment_template/turtlebot3 .

mkdir -p ~/.gazebo/models
```

# Run turtlebot3

#### run Empty World
```bash
# Run turtlebot3 Docker image
docker run --network=host -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/home/progryu/.gazebo/models:/root/.gazebo/models" \
           --privileged \
           --runtime=nvidia \
           open-rmf/rmf_deployment_template/turtlebot3:latest \
           bash -c "export TURTLEBOT3_MODEL=waffle && \
           ros2 launch turtlebot3_gazebo empty_world.launch.py"
```
#### run TurtleBot3 World
```bash
# Run turtlebot3 Docker image
docker run --network=host -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/home/progryu/.gazebo/models:/root/.gazebo/models" \
           --privileged \
           --runtime=nvidia \
           open-rmf/rmf_deployment_template/turtlebot3:latest \
           bash -c "export TURTLEBOT3_MODEL=waffle && \
           ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"
```
#### run TurtleBot3 House
```bash
# Run turtlebot3 Docker image
docker run --network=host -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/home/progryu/.gazebo/models:/root/.gazebo/models" \
           --privileged \
           --runtime=nvidia \
           open-rmf/rmf_deployment_template/turtlebot3:latest \
           bash -c "export TURTLEBOT3_MODEL=waffle && \
           ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py"
```
#### run TurtleBot3 Move
```bash
# Run turtlebot3 Docker image
docker run --network=host -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/home/progryu/.gazebo/models:/root/.gazebo/models" \
           --privileged \
           --runtime=nvidia \
           open-rmf/rmf_deployment_template/turtlebot3:latest \
           bash -c "ros2 run turtlebot3_teleop teleop_keyboard"
```

#### run 
```bash
# Run turtlebot3 Docker image
docker run --network=host -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/home/progryu/.gazebo/models:/root/.gazebo/models" \
           --privileged \
           --runtime=nvidia \
           open-rmf/rmf_deployment_template/turtlebot3:latest \
           bash -c "export TURTLEBOT3_MODEL=waffle && \
           export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models && \
           ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False"
```



