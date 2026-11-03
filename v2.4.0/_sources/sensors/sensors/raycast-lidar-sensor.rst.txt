.. _raycast_lidar_sensor:

===============
Raycast LIDAR
===============

Simulates a LIDAR sensor using raycasting. Returns a point cloud of "hit" objects within the sensor's
range. Also returns the intensity and ring/channel for each point. The intensity is currently based
only on atmospheric attenuation (set by the ``AtmospAttenRate`` parameter) and the distance to the
object.

A general drop off return rate for points can be set by changing the ``DropOffGenRate`` parameter.
Additionally an intensity-based drop-off rate can be applied to the points based on the parameters
``DropOffIntensityLimit`` and ``DropOffAtZeroIntensity``. These parameters create a linear drop-off
between ``DropOffIntensityLimit`` (the intensity at which intensity-based drop off starts) and
``DropOffAtZeroIntensity`` (the drop off rate at which the intensity is zero). To disable all drop off,
set ``DropOffGenRate`` to 0.0, and ``DropOffIntensityLimit`` to 0.0.

Note that to get an entire 360 degree scan (or a full horizontal field of view as set by
``HorizontalFov``), tuning of the ``RotationFrequency`` and ``TicksPerSecond`` parameters is required.
Setting them equal to each other will result in a full 360 degree scan. Alternatively, if you do not
wish your sensor to be running at the same frequency as your environment, you can change the ticks
per capture (see Example sensor definition below at the parameter listed as Hz). The ``Hz`` parameter
controls the ticks per capture rate at which the sensor captures and returns data. If ``Hz`` is set to
the same value as ``RotationFrequency``, the sensor will return a full 360 degree scan at each tick.

See :ref:`visualizing_raycast_lidar` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.RaycastLidar` for the python API.

Example sensor definition::

    {
        "sensor_type": "RaycastLidar",
        "configuration": {
            "socket": "CameraSocket",
            "Channels": 128,                    
            "Range": 200,                        
            "PointsPerSecond": 20000,           
            "RotationFrequency": 10,               
            "UpperFovLimit": 10,                 
            "LowerFovLimit": -30,                 
            "HorizontalFov": 360.0,               
            "AtmospAttenRate": 0.4,             
            "RandomSeed": 42,                      
            "DropOffGenRate": 0.45,                
            "DropOffIntensityLimit": 0.8,        
            "DropOffAtZeroIntensity": 0.4,        
            "ShowDebugPoints": True,              
            "NoiseStdDev": 0.0            
        },
        "Hz": 10 #TicksPerCapture
    }
