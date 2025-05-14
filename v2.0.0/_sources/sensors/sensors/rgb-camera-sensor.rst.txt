===============
RGB Camera
===============

Capture an RGBA image from the camera.

See :ref:`visualizing_rgbcamera_output` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.RGBCamera` for the python API.
Example sensor definition (from a HoveringAUV)::
    
    {
        "sensor_type": "RGBCamera",
        "sensor_name": "RightCamera",
        "socket": "CameraRightSocket",
        "Hz": 5,
        "configuration": {
            "CaptureWidth": 512,
            "CaptureHeight": 512
        }
    }