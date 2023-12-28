import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    my_navigation_dir = get_package_share_directory('zeta_demos_gz')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')

    # Define launch configurations
    params_file = LaunchConfiguration('params_file')
    slam_config_file = LaunchConfiguration('slam_config_file')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Declare launch arguments
    turtlebot_param_argument = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(my_navigation_dir, 'param', 'waffle_pi.yaml'),
        description='Path to the navigation2 parameters file')

    slam_toolbox_config_argument = DeclareLaunchArgument(
        'slam_config_file',
        default_value=os.path.join(my_navigation_dir, 'config', 'mapper_params_online_async.yaml'),
        description='Path to the SLAM configuration file')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')

    # Include SLAM Toolbox launch
    online_async_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
        ),
        # launch_arguments={
        #     'slam_params': slam_config_file,
        #     'use_sim_time': use_sim_time
        # }.items()
        )


    # Include Navigation2 launch
    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
        ),
        # launch_arguments={
        #     'use_sim_time': use_sim_time,
        #     'params_file': params_file
        # }.items()
        )

    # Create LaunchDescription object
    ld = LaunchDescription()
    ld.add_action(turtlebot_param_argument)
    ld.add_action(slam_toolbox_config_argument)
    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(online_async_launch)
    ld.add_action(navigation_launch)

    return ld
