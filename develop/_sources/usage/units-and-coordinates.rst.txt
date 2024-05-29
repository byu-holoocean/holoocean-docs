==================================
Units and Coordinates in HoloOcean
==================================

HoloOcean uses **meters** for units and a **right-handed coordinate system** for
all locations, distances, and offsets.


.. _`coordinate-system`:

Coordinate System
=================

Unreal Engine uses a left handed coordinate system by default, however
to keep with general robotics conventions, we use a right handed coordinate 
system with positive ``z`` being up.

So, when you need to specify a location in HoloOcean, the format is as follows

``[x, y, z]`` where:

- Positive ``x`` is **forward**
- Positive ``y`` is **left**
- Positive ``z`` is **up**

Remember that the units for ``[x, y, z]`` are in meters (Unreal Engine
defaults to centimeters, we've changed this to make things a bit easier).

.. _`rotations`:

Rotations
=========

Rotations are specified in ``[roll, pitch, yaw]`` / ``[x, y, z]`` format, in degrees (usually). This means

- **Roll**: Rotation around the fixed forward (``x``) axis
- **Pitch**: Rotation around the fixed right (``y``) axis
- **Yaw**: Rotation around the fixed up (``z``) axis

In that order.