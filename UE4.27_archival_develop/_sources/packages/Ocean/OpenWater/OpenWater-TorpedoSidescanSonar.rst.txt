OpenWater-TorpedoSidescanSonar
===============================

This scenario starts with a TorpedoAUV near a submarine. This is identical to the base version, only with a sonar mounted.
Octree leaf size is 2cm. Unless otherwise specified, all sensors are named the same as their class name, ie IMUSensor is named "IMUSensor".

- ``auv0``: Main :ref:`TorpedoAUV <hovering-auv-agent>` agent
    - :class:`~holoocean.sensors.IMUSensor` configured with noise, bias, and returns bias.
    - :class:`~holoocean.sensors.GPSSensor` gets measurements with N(1, 0.25) of the surface, actual measurement also has noise.
    - :class:`~holoocean.sensors.DVLSensor` configured with an elevation of 22.5 degrees, noise, and returns 4 range measurements.
    - :class:`~holoocean.sensors.SidescanSonar` configured with an azimuth of 170 degrees, 2000 range bins, range from 0.5 to 40 meters, and noise.
    - :class:`~holoocean.sensors.PoseSensor` for ground truth.
    - :class:`~holoocean.sensors.VelocitySensor` for ground truth.

.. image:: starting.png
