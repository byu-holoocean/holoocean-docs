.. _`blue-rov-agent`:

========
BlueROV2
========

.. image:: images/blue-rov.png
   :scale: 100%


Description
~~~~~~~~~~~
An implementation of the BlueROV2 Heavy vehicle from Blue Robotics. 

See the :class:`~holoocean.agents.BlueROV2`.


Control Schemes
~~~~~~~~~~~~~~~

**AUV Thrusters (``0``)**
  An 8-length floating point vector used to specify the control on each thruster. They begin with 
  the front right vertical thrusters, then goes around counter-clockwise, then repeat the last four 
  with the sideways thrusters.

**PID Controller (``1``)**
   A 6-length floating point vector of desired position in the global frame and roll, pitch, and yaw. 
   A basic PID controller is implemented to move the vehicle to that position and orientation 
   using the needed forces and torques.

**Custom Dynamics (``2``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This 
   is to be used for implementing custom dynamics. Besides collisions, all other forces and torques 
   (including gravity, buoyancy, and damping) have been disabled in the simulator to allow for a 
   clean slate for custom dynamics.

Sockets
~~~~~~~
All sockets have standard orientation unless stated otherwise. Standard orientation has the x-axis 
pointing towards the front of the vehicle, the y-axis pointing starboard, and the z-axis pointing 
upwards. 

Socket Definitions
------------------
- ``COM`` Center of mass.
- ``SonarSocket`` Location of the sonar sensor.
- ``DVLSocket`` Location of the DVL.
- ``IMUSocket`` Location of the IMU. Rotated 180 on x-axis, i.e. in a NED frame instead of NWU.
- ``DepthSocket`` Location of the depth sensor.
- ``CameraSocket`` Location of the camera.
- ``Origin`` True center of the robot.
- ``Viewport`` Where the robot is viewed from.

Socket Frames
-------------
.. image:: images/blue-rov-sockets.png
   :scale: 120%

.. image:: images/blue-rov-sockets-top.png
   :scale: 40%

.. image:: images/blue-rov-sockets-left.png
   :scale: 65%

.. image:: images/blue-rov-sockets-front.png
   :scale: 73%


.. _bluerov2-flashlights:

Flashlights
~~~~~~~~~~~

The BlueROV2 comes with four built-in flashlights positioned around the vehicle to provide illumination in various directions.

.. image:: images/blue_rov2_flashlight.png
   :scale: 70%

* `flashlight1`: (22, 19, 11)
* `flashlight2`: (22, -19, 11)
* `flashlight3`: (22, 19, -6)
* `flashlight4`: (22, -19, -6)

Please refer to :ref:`flashlights<flashlight>` for information on available control commands.
