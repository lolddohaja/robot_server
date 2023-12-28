from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'fleet_adapter_turtlebot3'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # config 디렉토리 및 하위 디렉토리의 모든 파일 포함
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'config/glhd'), glob('config/glhd/*')),
        # launch 디렉토리의 모든 파일 포함
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.xml')),
    ],
    install_requires=['setuptools', 'fastapi>=0.79.0', 'uvicorn>=0.18.2'],
    zip_safe=True,
    maintainer='lolddohaja',
    maintainer_email='lolddohaja@zetabank.co.kr',
    description='A turtlebot for an RMF fleet adapter',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_adapter=fleet_adapter_turtlebot3.fleet_adapter:main',
            'fleet_manager=fleet_adapter_turtlebot3.fleet_manager:main',
            'easy_fleet_adapter='
            'fleet_adapter_turtlebot3.easy_fleet_adapter:main',
        ],
    },
)