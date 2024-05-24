PierHarbor-HoveringImagingSonar
================================

This scenario starts with a HoveringAUV near one of the larger docks. This is identical to the base version, only with a sonar mounted.
Octree leaf size is 2cm. Unless otherwise specified, all sensors are named the same as their class name, ie IMUSensor is named "IMUSensor".

- ``auv0``: Main :ref:`HoveringAUV <hovering-auv-agent>` agent
    - :class:`~holoocean.sensors.IMUSensor` configured with noise, bias, and returns bias.
    - :class:`~holoocean.sensors.GPSSensor` gets measurements with N(1, 0.25) of the surface, actual measurement also has noise.
    - :class:`~holoocean.sensors.DVLSensor` configured with an elevation of 22.5 degrees, noise, and returns 4 range measurements.
    - :class:`~holoocean.sensors.ImagingSonar` configured with an elevation of 20 degrees, azimuth 130, range 1-40m, an initial octree generation of 40m, and all noise turned on.
    - :class:`~holoocean.sensors.DepthSensor` configured with noise.
    - :class:`~holoocean.sensors.PoseSensor` for ground truth.
    - :class:`~holoocean.sensors.VelocitySensor` for ground truth.

.. image:: starting.png
