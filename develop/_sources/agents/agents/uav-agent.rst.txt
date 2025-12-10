.. _`uav-agent`:

=========
UAV Agent
=========

.. image:: images/uav-perspective.png
   :scale: 20%

.. image:: images/uav-top.png
   :scale: 20%

.. image:: images/uav-side.png
   :scale: 20%


Description
===========
A quadcopter UAV agent. 

See the :class:`~holoocean.agents.UavAgent` class. 


Control Schemes
===============

**UAV Torques (``0``)**
  A 4-length floating point vector used to specify the pitch torque,
  roll torque, yaw torque and thrust with indices 0, 1, 2 and 3 respectively.

**UAV Roll / Pitch / Yaw Targets(``1``)**
  A 4-length floating point vector used to specify the pitch,
  roll, yaw, and altitude targets. The values are specified in
  indices 0, 1, 2, and 3 respectively.

Sockets
=======
All sockets are oriented in the agent's body frame (right-handed NWU, with the x-axis pointing forward, 
the y-axis pointing to the left, and the z-axis pointing upward) unless stated otherwise. See 
:ref:`sockets` for details. 

Socket Definitions
------------------
- ``CameraSocket`` located underneath the uav body.
- ``Viewport`` located behind the agent.

Socket Frames
-------------
.. image:: images/uav-sockets.png
   :scale: 30%
