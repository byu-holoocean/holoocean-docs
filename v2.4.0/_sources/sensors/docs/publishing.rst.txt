======================
Publishing Sensor Data
======================

.. _`ros`:

Publishing Data Using ROS2 Bridge
=================================

ROS2 (Robot Operating System) is a popular middleware for robotics development. We have created 
the ROS2 Bridge package to allow users to connect ROS2 with other middleware systems, such as LCM 
and HoloOcean. This allows you to use ROS2 to control HoloOcean agents and publish sensor data to 
ROS2 topics. 

Installation
------------
Using the ROS2 Bridge requires downloading a separate package. 
For more information see the README on the repository: https://github.com/byu-holoocean/holoocean-ros


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
