========================
OpenWater-HoveringCamera
========================

This scenario starts with a HoveringAUV near a submarine. This is identical to the base version, only with cameras mounted.
Unless otherwise specified, all sensors are named the same as their class name, ie IMUSensor is named "IMUSensor".

- ``auv0``: Main :ref:`HoveringAUV <hovering-auv-agent>` agent
    - :class:`~holoocean.sensors.IMUSensor` configured with noise, bias, and returns bias.
    - :class:`~holoocean.sensors.GPSSensor` gets measurements with N(1, 0.25) of the surface, actual measurement also has noise.
    - :class:`~holoocean.sensors.DVLSensor` configured with an elevation of 22.5 degrees, noise, and returns 4 range measurements.
    - :class:`~holoocean.sensors.RGBCamera` named LeftCamera.
    - :class:`~holoocean.sensors.RGBCamera` named RightCamera.
    - :class:`~holoocean.sensors.DepthSensor` configured with noise.
    - :class:`~holoocean.sensors.PoseSensor` for ground truth.
    - :class:`~holoocean.sensors.VelocitySensor` for ground truth.

.. image:: starting.png
