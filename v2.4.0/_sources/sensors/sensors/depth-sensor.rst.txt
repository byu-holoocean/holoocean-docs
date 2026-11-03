===============
Depth Sensor
===============

A depth sensor, capable of simulating noiseless or noisy measurement of depth under the water level.

See :py:class:`~holoocean.sensors.DepthSensor` for more information.

Example sensor definition::

    {
        "sensor_type": "DepthSensor",
        "socket": "DepthSocket",
        "Hz": 100,
        "configuration": {
            "Sigma": 0.255
        }
    }
