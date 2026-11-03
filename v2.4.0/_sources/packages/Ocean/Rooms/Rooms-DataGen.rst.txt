=============
Rooms-DataGen
=============

This scenario starts with a TurtleAgent equipped with Location, Rotation and RangeFinder sensors. 
No noise is included in any of the sensors.

- ``turtle0``: Main :ref:`Turtle <turtle-agent>` agent
    - :class:`~holoocean.sensors.LocationSensor` 
    - :class:`~holoocean.sensors.RotationSensor` 
    - :class:`~holoocean.sensors.RangeFinder` configured with 64 beams and a max distance of 20m. 
