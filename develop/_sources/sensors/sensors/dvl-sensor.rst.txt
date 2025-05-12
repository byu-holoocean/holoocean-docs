==============================
Doppler Velocity Log (DVL)
==============================

A Doppler Velocity Log Sensor. 

See :py:class:`~holoocean.sensors.DVLSensor` for the python API.

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