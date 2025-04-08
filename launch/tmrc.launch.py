from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    config_file = '' # your config file path

    return LaunchDescription([
        Node(
            namespace='hardware_layer', 
            package='rslidar_sdk', 
            executable='rslidar_sdk_node', 
            output='screen', 
            parameters=[{'config_path': config_file}],
            remappings=[('/rslidar_imu_data ','imu/data'),
                        ('/rslidar_points ', 'scan/lidar_3d')],)
    ])
