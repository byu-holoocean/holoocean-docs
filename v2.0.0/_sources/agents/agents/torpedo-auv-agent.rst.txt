.. _`torpedo-auv-agent`:

==========
TorpedoAUV
==========

.. image:: images/torpedo-auv.png
   :scale: 60%


Description
===========
A generic torpedo-style AUV with four fins.

See the :class:`~holoocean.agents.TorpedoAUV`.


Control Schemes
===============

**AUV Fins (``0``)**
  Takes in a 5 length vector of four fin angles and a thruster value. The format is 
  [Right Fin, Top Fin, Left Fin, Bottom Fin] Fins have a range of -45 to 45 degrees, and the 
  thruster has a range of -100 to 100 (percent of max thrust).

**Custom Dynamics (``1``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This 
   is to be used for implementing custom dynamics. Besides collisions, all other forces and torques 
   (including gravity, buoyancy, and damping) have been disabled in the simulator to allow for a 
   clean slate for custom dynamics.

.. note::

   Dynamics models from Thor Fossen are available for the TorpedoAUV to enable more realistic 
   simulations. To use Fossen dynmics, use the Custom Dynamics control scheme, then create a Fossen 
   vehicle controller and a Fossen dynamics manager. For details, see :ref:`fossen-dynamics`.

Sockets
=======
All sockets have standard orientation unless stated otherwise. Standard orientation has the x-axis 
pointing towards the front of the vehicle, the y-axis pointing starboard, and the z-axis pointing 
upwards.

Socket Definitions
------------------
- ``COM`` Center of mass.
- ``CameraSocket`` Location of camera, rotated -90 on y-axis.
- ``DVLSocket`` Location of the DVL
- ``IMUSocket`` Location of the IMU.
- ``DepthSocket`` Location of the depth sensor.
- ``SonarSocket`` Location of the sonar sensor, rotated -90 on y-axis.
- ``Viewport`` where the robot is viewed from.

Socket Frames
-------------
.. image:: images/torpedo-angled.png
   :scale: 50%

.. image:: images/torpedo-top.png
   :scale: 50%

.. image:: images/torpedo-right.png
   :scale: 50%