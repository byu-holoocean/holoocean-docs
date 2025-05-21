===============
Viewport Sensor
===============

Captures what the viewport is seeing (what the simulation window displays). This is faster than the 
camera, but there can be only one viewport capture. It may be useful to move the viewport with 
:meth:`~holoocean.environments.HoloOceanEnvironment.move_viewport`. Note that the dimesions set in 
the configuration must match the viewports dimensions. Default settings match the default viewport 
resolution.

See :py:class:`~holoocean.sensors.ViewportCapture` for the python API.

Example sensor definition::

    {
        "sensor_type": "ViewportCapture",
        "socket": "Viewport",
        "configuration": {
            "Width": 1280,
            "Height": 7200,
        }
    }