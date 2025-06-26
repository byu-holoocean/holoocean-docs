.. _`sphere-agent`:

===========
SphereAgent
===========

.. image:: images/sphere.png
   :scale: 30%


Description
===========

A basic sphere robot that moves along a plane. The SphereAgent does not have 
physics - it simply computes its next location and teleports there, as 
compared to other agents which have mass and momentum.

See :class:`~holoocean.agents.SphereAgent` for more details.


Control Schemes
===============

**Sphere Discrete** (``0``)
  A single-length integer vector that accepts one of four
  possible numbers; 0: move forward, 1: move backward, 
  2: turn right, 3: turn left.

**Sphere Continuous** (``1``)
  A 2-length floating point vector used to specify 
  the agent's forward speed (index 0) and rotational speed (index 1).

Sockets
=======
All sockets have standard orientation unless stated otherwise. Standard orientation has the x-axis 
pointing towards the front of the vehicle, the y-axis pointing starboard, and the z-axis pointing 
upwards.

Socket Definitions
------------------
- ``CameraSocket`` located at the front of the sphere body.
- ``Viewport`` located behind the agent.


Socket Frames
-------------
.. image:: images/sphere-sockets.png
   :scale: 30%