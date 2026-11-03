.. _`fixed-wing-agent`:

=========
FixedWing
=========

.. warning::
   This agent is in active development, and any functionality or features are prototypical in nature
   and subject to change. At this time we cannot guarantee stable HoloOcean performance while using 
   this agent. 

.. image:: images/fixed-wing.png
   :scale: 40%


Description
===========
This custom agent is a fixed-wing, vertical takeoff and landing (VTOL) aircraft. It is being 
developed to model a specific real-world vehicle. 

Our implementation has some key differences from the image shown. First, the actual agent has only 
8 propellors (4 vertical and 4 horizontal) instead of 12. Second, while the asset shows the front 
row of horizontal prepellors pointing directly forward, on the agent they are angled outward from 
the vehicle in the XY plane by 45 degrees.

See :class:`~holoocean.agents.FixedWing`.


Control Schemes
===============

**Propellors (``0``)**
   An 8-length floating point vector used to specify the thrust force from each propellor. The order
   for specifying the propellors in the command is as follows: 
   [Vertical Front Starboard, Vertical Front Port, Vertical Back Port, Vertical Back Starboard, 
   Angled Front Starboard, Angled Front Port, Angled Back Port, Angled Back Starboard]
      
**PD Controller (``1``)**
   A 6-length floating point vector of desired position in the global frame and roll, pitch, and 
   yaw. A basic PD controller has been implementing to move the vehicle to that position and 
   orientation using the needed forces and torques.

**Custom Dynamics (``2``)**
   A 6-length floating point vector of linear and angular accelerations in the global frame. This 
   is to be used for implementing custom dynamics. Besides collisions, all other forces and torques 
   (including gravity, buoyancy, and damping) have been disabled in the simulator to allow for a 
   clean slate for custom dynamics.


Sockets
=======
This agent does not have any sockets yet.
