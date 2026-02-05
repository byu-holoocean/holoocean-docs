============
Depth Camera
============

Capture a depth image from the camera.

The image below shows the comparison between the RGB camera output with the corresponding Depth Camera output. 

.. image:: ../images/depth_camera_w_comparison.png

See :ref:`visualizing_depthcamera_output` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.DepthCamera` for the Python API.
Example sensor definition (from a BlueROV2)::
    
    {
        "sensor_type": "DepthCamera",
        "sensor_name": "DepthForwardCamera",
        "socket": "CameraSocket",
        "Hz": 5,
        "configuration": {
            "CaptureWidth": 512,
            "CaptureHeight": 512
        }
    }

If you would like use the Depth Camera in a custom level, please reference :ref:`depth-camera-custom`.
