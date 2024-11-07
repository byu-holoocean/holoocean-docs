.. _`blue-rov-agent`:

BlueRov2
============

Images
------

.. image:: images/blue-rov.PNG
   :scale: 100%

Description
-----------
An implementation of the BlueRov2.

See the :class:`~holoocean.agents.BlueROV2`.

Control Schemes
---------------

**AUV Thrusters (``0``)**
  An 8-length floating point vector used to specify the control on each thruster. They begin with the front right vertical thrusters, then goes around counter-clockwise, then repeat the last four with the sideways thrusters.

**PD Controller (``1``)**
   A 6-length floating point vector of desired position in the global frame and roll, pitch, and yaw. A basic PD controller has been implementing to move the vehicle to that position and orientation using the needed forces and torques.

**Custom Dynamics (``2``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This is to be used for implementing custom dynamics. Besides collisions, all other forces and torques - including gravity, buoyancy, and damping - have been disabled in the simulator to allow for a clean slate for custom dynamics.

Sockets
-------

- ``COM`` Center of mass
- ``SonarSocket`` A socket on the top of the AUV.
- ``CameraSocket`` Location of the camera sensor.
- ``Socket`` A socket on the bottom of the AUV.

.. image:: images/blue-rov-sockets.PNG
   :scale: 50%

.. image:: images/blue-rov-sockets-top.PNG
   :scale: 47%

.. image:: images/blue-rov-sockets-left.PNG
   :scale: 65%

.. image:: images/blue-rov-sockets-front.PNG
   :scale: 63%