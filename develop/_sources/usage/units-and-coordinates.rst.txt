.. _`units-and-coordinates`:

==================================
Units and Coordinates in HoloOcean
==================================

HoloOcean uses **meters** for units and a **right-handed coordinate system** for all locations, 
distances, and offsets.

HoloOcean coordinates differ from coordinates within the Unreal Engine Editor. To see specific 
coordinates for HoloOcean levels, please refer to the :ref:`ocean` page.


.. _`coordinate-system`:

Coordinate System
=================

Unreal Engine uses a left-handed coordinate system by default. However, to keep with general robotics 
conventions, we use a right-handed coordinate system, with positive ``z`` being up. 

Locations and translations in HoloOcean worlds are specified as ``[x, y, z]`` where:

- Positive ``x`` is **forward**
- Positive ``y`` is **left**
- Positive ``z`` is **up**

Remember that the units for ``[x, y, z]`` are in meters (Unreal Engine defaults to centimeters).


.. _`rotations`:

Rotations
=========

Rotations are specified in ``[roll, pitch, yaw]`` / ``[x, y, z]`` format, in degrees.

- **Roll**: Rotation around the fixed forward (``x``) axis
- **Pitch**: Rotation around the fixed right (``y``) axis
- **Yaw**: Rotation around the fixed up (``z``) axis

Agent, Socket, & Sensor Frames
==============================
Agents each have a coordinate frame located at their center (usually the center of mass, rarely the 
center of the mesh if different). This coordinate frame is always aligned with the agent's forward, 
left, and up directions in a right-handed coordinate system. 

Agents are equiped with sockets to hold sensors. Each socket has its own coordinate frame that is 
usually in the same orientation as the agent frame. See the individual Agent pages in :ref:`agents`
for details on the location and orientation of sockets for each agent.  

Sensors can be placed in sockets with an offset in position or orientation. With some rare exceptions, 
sensors return their data in the coordinate frame defined by this offset from the socket frame. Users 
are responsible for keeping track of the coordinate frame in which sensor data is reported. See the 
individual sensor pages in :ref:`sensors` for details on the coordinate frame in which each sensor
returns data.


