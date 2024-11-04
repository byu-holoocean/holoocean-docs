SimpleUnderwater-Torpedo
=============================

This scenario starts with a TorpedoAUV in the center of the basin. Unless otherwise specified,
all sensors are named the same as their class name, ie IMUSensor is named "IMUSensor".

- ``auv0``: Main :ref:`HoveringAUV <hovering-auv-agent>` agent
    - :class:`~holoocean.sensors.IMUSensor` configured with noise, bias, and returns bias.
    - :class:`~holoocean.sensors.GPSSensor` gets measurements with N(1, 0.25) of the surface, actual measurement also has noise.
    - :class:`~holoocean.sensors.DVLSensor` configured with an elevation of 22.5 degrees, noise, and returns 4 range measurements.
    - :class:`~holoocean.sensors.DepthSensor` configured with noise.
    - :class:`~holoocean.sensors.PoseSensor` for ground truth.
    - :class:`~holoocean.sensors.VelocitySensor` for ground truth.