ROS2 Wrapper
============

After installing holoocean, you can clone this ros package into your ros workspace:
https://github.com/byu-holoocean/holoocean-ros

.. warning:: 

    - CURRENTLY ROS2 SETUP ONLY WORKS WITH SINGLE AGENT SCENARIOS
    - Running holoocean and ros2 in a virtual environment (ie. conda) may cause dependency issues
    - The speed of the simulation will max out which may cause timing errors.

ROS workspace for holoocean works with ros2 humble installation
Follow the ROS2 installation tutorials: https://docs.ros.org/en/humble/Tutorials

The example controller can be run after building the package in your ros workspace:

.. code::

    source /opt/ros/humble/setup.bash
    colcon build
    source install/setup.bash

    ros2 launch holoocean_main torpedo_launch.py

Follow the ROS2 Documentation to build nodes to control the holoocean environment

The holoocean_main node:
    - Subscribes to Controller commands
    - Publishes the sensor data retuned in holoocean state
    - Creates a timer to tick the environment

    The holoocean publishers will use the namespace holoocean (View Documentation on namespaces)
    the name of the topic will follow the scenario name for the sensor 
    If there is no name given it will be the same as sensor type. 

Holoocean Interface package:
    - Holds the messages and service used for publishing sensor data

command_example node:
    - Publishes random HSD commands at specific intervals
    - Or publishes a preprogrammed sequence of HSD commands


Publishing your own sensor
--------------------------

After  implementing in your sensor Python and Cpp with the holoocean package:

    - Make msg file in holoocean_interfaces (ex. SensorData.msg)
    - Add msg file to Cmake list (ex. "msg/SesnorData.msg")

    - In sensor data converter file: 
        
        - Add an elif statement in convert_to_msg function
        
        - Add a Key to sensor_keys 
        
        - Import the message object in first line of the file (ex. from holoocean_interfaces.msg import SensorData)
        
        - Add function to encode the data into a ros message
	
Run the following code to rebuild your ros2 workspace

.. code::

    source /opt/ros/humble/setup.bash
    colcon build
    source install/setup.bash


Record your data
----------------

To record sensor data or commands with ros2bag installed you can run a command like this
from your ros2_ws folder

.. code::

    source install/setup.bash
    ros2 bag record /holoocean/desiredHSD /holoocean/RotationSensor /holoocean/LocationSensor -o /path/to/save_data

You can read more on the ros2 Documentation here to record and play back ros2 bag data:
https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html
