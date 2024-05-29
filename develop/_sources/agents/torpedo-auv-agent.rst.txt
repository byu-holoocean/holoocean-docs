.. _`torpedo-auv-agent`:

TorpedoAUV
============

Images
------

.. image:: images/torpedo-auv.png
   :scale: 60%

Description
-----------
A generic AUV.

See the :class:`~holoocean.agents.TorpedoAUV`.

Control Schemes
---------------

**AUV Fins (``0``)**
  Takes in a 5 length vector. The first element is the right fin angle from -45 to 45 degrees, then top, left, and bottom. The last element is the "thruster" with a value of -100 to 100.

**Custom Dynamics (``1``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This is to be used for implementing custom dynamics. Besides collisions, all other forces and torques - including gravity, buoyancy, and damping - have been disabled in the simulator to allow for a clean slate for custom dynamics.

Sockets
-------

- ``COM`` Center of mass
- ``DVLSocket`` Location of the DVL
- ``IMUSocket`` Location of the IMU.
- ``DepthSocket`` Location of the depth sensor.
- ``SonarSocket`` Location of the sonar sensor.
- ``Viewport`` where the robot is viewed from.

.. image:: images/torpedo-angled.png
   :scale: 50%

.. image:: images/torpedo-top.png
   :scale: 50%

.. image:: images/torpedo-right.png
   :scale: 50%