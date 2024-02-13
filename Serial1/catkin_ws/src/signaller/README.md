roslaunch rplidar_ros rplidar_a1.launch
rosrun rosserial_python serial_node.py /dev/ttyACM0
rosrun signaller publisher.py
