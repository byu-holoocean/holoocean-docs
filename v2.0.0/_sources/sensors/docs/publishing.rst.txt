======================
Publishing Sensor Data
======================

.. _`lcm`:

Publishing Data Using LCM
=========================

HoloOcean supports publishing data to LCM (Lightweight Communications and Marshalling), a messaging
system that is used to communicate between different processes. This allows you to publish sensor
data to LCM channels, which can be used to communicate with other systems.

LCM configuration happens in the :ref:`scenario <scenarios>` file. LCM publishes data to a 
medium called the provider. This can be local, over the network, a log file, etc. This can be 
specified in the header of the scenario file. See `here <https://lcm-proj.github.io/lcm/>`_ 
for options on this. If no provider is specified, HoloOcean uses the default LCM udqm.

.. code-block:: json

   {
      "name": "{Scenario Name}",
      "world": "{world it is associated with}",
      "lcm_provider": "file:///home/lcm.log"
      "agents":[
         "array of agent objects"
      ]
   }

Once the provider is chosen, HoloOcean publishes each sensor individually. The lcm_channel is 
set in the sensor configuration. If no channel is specified, the sensor will not be published.

.. code-block:: json

   {
      "sensor_type": "RGBCamera",
      "sensor_name": "FrontCamera",
      "lcm_channel": "CAMERA",
   }

.. _`ros`:

Publishing Data Using ROS2 Bridge
=================================
.. TODO: Flesh this out more, add examples and code snippets. 

ROS2 (Robot Operating System) is a popular middleware for robotics development. We have created 
the ROS2 Bridge package to allow users to connect ROS2 with other middleware systems, such as LCM 
and HoloOcean. This allows you to use ROS2 to control HoloOcean agents and publish sensor data to 
ROS2 topics. 

This feature is written specifically to work with the implementation of Fossen vehicle dynamics.   

Installation
------------
Using the ROS2 Bridge requires downloading a separate package. After installing HoloOcean, clone the 
following repository into a ROS2 workspace: https://github.com/byu-holoocean/holoocean-ros

.. warning:: 

    - Currently, the ROS2 Bridge only supports **single-agent scenarios**.
    - Running holoocean and ROS2 in a virtual environment (ie. conda) may cause dependency issues.
    - The speed of the simulation may max out, which may cause timing errors.

The ROS workspace for holoocean works with the Humble installation of ROS2. Follow the ROS2 
installation tutorials: https://docs.ros.org/en/humble/Tutorials

Usage 
-----
The example controller can be run after building the package in your ROS workspace:

.. code::

    source /opt/ros/humble/setup.bash
    colcon build
    source install/setup.bash

    ros2 launch holoocean_main torpedo_launch.py

Follow the ROS2 documentation to build nodes to control the holoocean environment.

The holoocean_main node:

- Subscribes to Controller commands
- Publishes the sensor data retuned in holoocean state
- Creates a timer to tick the environment

The holoocean publishers will use the namespace "holoocean" (see ROS documentation on namespaces). 
The name of the topic will follow the scenario name for the sensor. If there is no name given, it 
will be the same as sensor type. 

Holoocean Interface package:

- Holds the messages and service used for publishing sensor data

command_example node:

- Publishes random HSD commands at specific intervals
- Or publishes a preprogrammed sequence of HSD commands


Publishing Your Own Sensor
--------------------------
The ROS2 Bridge can be configured to work with custom sensors. After implementing your sensor in 
HoloOcean(see :ref:`develop-sensor`), follow these steps to publish your sensor data:
- Make a ``.msg`` file in ``holoocean_interfaces`` (ex. ``SensorData.msg``)
- Add ``.msg`` file to Cmake list (ex. ``msg/SesnorData.msg``)
- In the sensor data converter file: 
        
    - Add an elif statement in the ``convert_to_msg`` function
    - Add a Key to ``sensor_keys``
    - Import the message object in first line of the file (ex. ``from holoocean_interfaces.msg import SensorData``)
    - Add a function to encode the data into a ROS message
	
Run the following code to rebuild your ROS2 workspace:

.. code::

    source /opt/ros/humble/setup.bash
    colcon build
    source install/setup.bash


Record Your Data
----------------
You can record the data from the HoloOcean environment using ros2bag. With ros2bag installed, you can 
record sensor data or commands by running a command like this from your ros2_ws folder:

.. code::

    source install/setup.bash
    ros2 bag record /holoocean/desiredHSD /holoocean/RotationSensor /holoocean/LocationSensor -o /path/to/save_data

You can read more on the ros2 Documentation here to record and play back ros2 bag data:
https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html

