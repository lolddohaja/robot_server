from __future__ import print_function

import roslibpy

import time


ros = roslibpy.Ros(host='192.168.50.92', port=9090)
ros.on_ready(lambda: print('Is ROS connected?', ros.is_connected))
ros.run()

print(ros.get_topics())
print(ros.get_topic_type(u'/ublox/fix'))

def print_message(message):
    print("What")
    print("Latitude: {}".format(message['latitude']))
    print("Longitude: {}".format(message['longitude']))
    print("Altitude: {}".format(message['altitude']))
    listener.unsubscribe()
    # Add more fields as neede

listener = roslibpy.Topic(ros, '/ublox/fix', 'sensor_msgs/NavSatFix')
print('go')

listener.subscribe(print_message)
time.sleep(4)

ros.close()
