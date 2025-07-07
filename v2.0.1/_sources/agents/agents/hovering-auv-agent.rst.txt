.. _`hovering-auv-agent`:

===========
HoveringAUV
===========

.. image:: images/hovering-auv.png
   :scale: 40%


Description
===========
Our custom in-house hovering AUV.

See the :class:`~holoocean.agents.HoveringAUV`.


Control Schemes
===============

**AUV Thrusters (``0``)**
  An 8-length floating point vector used to specify the control on each thruster. They begin with 
  the front right vertical thrusters, then goes around counter-clockwise, then repeat the last four 
  with the sideways thrusters.

**PD Controller (``1``)**
   A 6-length floating point vector of desired position in the global frame and roll, pitch, and yaw. 
   A basic PD controller has been implementing to move the vehicle to that position and orientation 
   using the needed forces and torques.

**Custom Dynamics (``2``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This 
   is to be used for implementing custom dynamics. Besides collisions, all other forces and torques 
   (including gravity, buoyancy, and damping) have been disabled in the simulator to allow for a 
   clean slate for custom dynamics.

Sockets
=======
All sockets have standard orientation unless stated otherwise. Standard orientation has the x-axis 
pointing towards the front of the vehicle, the y-axis pointing starboard, and the z-axis pointing 
upwards.

Socket Definitions
------------------
- ``COM`` Center of mass.
- ``DVLSocket`` Location of the DVL.
- ``IMUSocket`` Location of the IMU. Rotated 180 on x-axis, i.e. in a NED frame instead of NWU.
- ``DepthSocket`` Location of the depth sensor.
- ``SonarSocket`` Location of the sonar sensor.
- ``CameraRightSocket`` Location of the right camera (when looking in the same direction that the AUV is facing).
- ``CameraLeftSocket`` Location of the left camera (when looking in the same direction that the AUV is facing).
- ``Origin`` True center of the robot.
- ``Viewport`` Where the robot is viewed from.

Socket Frames
-------------
.. image:: images/hovering-angled.png
   :scale: 50%

.. image:: images/hovering-top.png
   :scale: 50%

.. image:: images/hovering-right.png
   :scale: 50%

.. image:: images/hovering-front.png
   :scale: 50%