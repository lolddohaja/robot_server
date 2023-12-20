from setuptools import setup

package_name = 'fleet_adapter_turtlebot3'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name,['config.yaml']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lolddohaja',
    maintainer_email='lolddohaja@zetabank.co.kr',
    description='A turtlebot for an RMF fleet adapter',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_adapter=fleet_adapter_turtlebot3.fleet_adapter:main'
        ],
    },
)
