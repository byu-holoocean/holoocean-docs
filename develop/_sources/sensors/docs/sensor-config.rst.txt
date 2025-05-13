.. _`sensor-configuration`:

====================
Sensor Configuration
====================
Sensors are defined in the ``sensors`` array of an agent object. Each sensor is defined using a new 
dictionary in the list.

.. code-block:: json
   
   "sensors":[
      {
         "sensor_name": "FrontCamera",
         "sensor_type": "RGBCamera",
         "socket": "socket name",
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0],
         "Hz": 5,
         "lcm_channel": "channel_name",
         "ros_publish": "False",
         "configuration": {
            "array of sensor configurations"
         }
      }
   ]


Sensor Placement
================

Sensor placement can be defined in several ways:

1. **Provide a socket name**

   This will place the sensor in the given socket.

   .. code-block:: json

      {
         "sensor_type": "RGBCamera",
         "socket": "CameraSocket"
      }

2. **Provide a socket, location and/or rotation**

   The sensor will be placed offset to the socket by the location and rotation. 
   The rotation is ``[roll, pitch, yaw]`` in degrees, rotated about XYZ fixed axes,
   ie R_z R_y R_x.


   .. code-block:: json

      {
         "sensor_type": "RGBCamera",
         "socket": "CameraSocket"
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0],
      }

3. **Provide just a location and/or rotation**

   The sensor will be placed at the given coordinates, offset from the root of
   the agent.

   .. code-block:: json

      {
         "sensor_type": "RGBCamera",
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0]
      }


Sensor Sample Rate
==================

The sensor will be sampled at the rate specified in ``Hz``. Note this must be less then ``ticks_per_sec``, and
preferably a divisor of ``ticks_per_sec`` as well. See :ref:`configure-framerate` for more info
on ``ticks_per_sec``.

.. code-block:: json

   {
      "sensor_type": "RGBCamera",
      "Hz": 20
   }


Publish Message
===============

HoloOcean supports publishing sensor messages and data to LCM. A HoloOcean-ROS2 Bridge package 
is also available.

To publish sensor data to LCM, specify the type to publish and the channel to publish to:

.. code-block:: json

   {
      "sensor_type": "RGBCamera",
      "lcm_channel": "CAMERA"
   }
   

To publish sensor data to ROS2, set ``ros_publish`` to ``True``:

.. code-block:: json

   {
      "sensor_type": "RGBCamera",
      "ros_publish": "True"
   }
   

See :ref:`ros` for more information on the ROS2 Bridge.


.. _`configuration-block`:

Configuration Block
===================

The contents of the ``configuration`` block are sensor-specific. The configuration block is
passed verbatim to the sensor itself, which parses it.

For example, the docstring for :class:`~holoocean.sensors.RGBCamera` states that
it accepts ``CaptureWidth`` and ``CaptureHeight`` parameters, so an example
sensor configuration would be:

.. code-block:: json

   "sensors": [
      {
         "sensor_name": "RBGCamera",
         "sensor_type": "RGBCamera",
         "socket": "CameraSocket",
         "configuration": {
            "CaptureHeight": 1920,
            "CaptureWidth": 1080
         }
      }   
   ]