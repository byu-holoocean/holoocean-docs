.. _`turtle-agent`:

===========
TurtleAgent
===========

.. image:: images/turtle.png
   :scale: 30%


Description
===========
A simple turtle-bot agent with an arrow pointing forwards. Its radius is 
approximately 25cm and is approximately 10cm high.

The TurtleAgent moves when forces are applied to it - so it has momentum and
mass, compared to the sphere-agent which teleports around. The 
TurtleAgent is subject to gravity and can climb ramps and slopes.

See :class:`~holoocean.agents.TurtleAgent` for more details.


Control Schemes
===============

**Sphere continuous** (``0``)
  A 2-length floating point vector used to specify
  the agent's forward force (index 0) and rotation force (index 1).

Sockets
=======
All sockets have standard orientation unless stated otherwise. Standard orientation is NWU, which has 
the x-axis pointing towards the front of the vehicle, the y-axis pointing starboard, and the z-axis 
pointing upwards. 

Socket Definitions
------------------
- ``CameraSocket`` located at the front of the body.
- ``Viewport`` located behind the agent.

Socket Frames
-------------
.. image:: images/turtle-sockets.png
   :scale: 30%
