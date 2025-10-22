==============================
Doppler Velocity Log (DVL)
==============================

A Doppler Velocity Log Sensor, which simulates the emitting of sound waves to calculate relative vehicle velocity to the seafloor or other objects that the sound waves bounce off of. 

See :py:class:`~holoocean.sensors.DVLSensor` for the Python API.

Example sensor definition::

    {
        "sensor_type": "DVLSensor",
        "socket": "DVLSocket",
        "Hz": 20,
        "configuration": {
            "Elevation": 22.5,
            "DebugLines": false,
            "VelSigma": 0.02626,
            "ReturnRange": true,
            "MaxRange": 50,
            "RangeSigma": 0.1
        }
    }