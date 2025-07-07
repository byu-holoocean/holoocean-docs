.. _`surface-vessel-agent`:

=============
SurfaceVessel
=============

.. image:: images/surface.png
   :scale: 40%


Description
===========
A simple surface vessel with 2 thrusters in the rear for propulsion.

See the :class:`~holoocean.agents.SurfaceVessel`.


Control Schemes
===============

**Thrusters (``0``)**
  A 2-length floating point vector specifying the force on each thruster. The vector is in the 
  format [Left Thruster, Right Thruster].

**PD Controller (``1``)**
   A 2-length floating point vector of desired x and y coordinates in the global frame. A basic PD 
   controller has been implemented to move the vehicle to that position.

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
- ``Payload`` where the payload with sensors will be in the water. Rotated 270 on y-axis, so x pointed downward.
- ``Platform`` sensors placed on platform.
- ``Viewport`` where the robot is viewed from.

Socket Frames
-------------
.. image:: images/surface-sockets.png
   :scale: 50%