.. _`surface-vessel-agent`:

SurfaceVessel
===============

Images
------

.. image:: images/surface.png
   :scale: 40%

Description
-----------
A simple surface vessel with 2 thrusters for propolsion.

See the :class:`~holoocean.agents.SurfaceVessel`.

Control Schemes
---------------

**Thrusters (``0``)**
  An 2-length floating point vector used to specify the control on each thruster. First one is left, second is right.

**PD Controller (``1``)**
   A 2-length floating point vector of desired x and y position in the global frame. A basic PD controller has been implemented to move the vehicle to that position using the correct thruster forces.

**Custom Dynamics (``2``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This is to be used for implementing custom dynamics. Besides collisions, all other forces and torques - including gravity, buoyancy, and damping - have been disabled in the simulator to allow for a clean slate for custom dynamics.

Sockets
-------

- ``Payload`` where the payload with sensors will be in the water. Pointed downward.
- ``Platform`` sensors placed on platform.
- ``Viewport`` where the robot is viewed from.

.. image:: images/surface-sockets.png
   :scale: 50%