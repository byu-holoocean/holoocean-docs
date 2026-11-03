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
All sockets are oriented in the agent's body frame (right-handed NWU, with the x-axis pointing forward, 
the y-axis pointing to the left, and the z-axis pointing upward) unless stated otherwise. See 
:ref:`sockets` for details. 

Socket Definitions
------------------
- ``CameraSocket`` located at the front of the sphere body.
- ``Viewport`` located behind the agent.


Socket Frames
-------------
.. image:: images/sphere-sockets.png
   :scale: 30%