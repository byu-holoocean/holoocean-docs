===============================
Global Positioning System (GPS)
===============================

A simulated GPS sensor, including that signal caughts out under water. 

See :py:class:`~holoocean.sensors.GPSSensor` for the python API.

Example sensor definition::
    
    {
        "sensor_type": "GPSSensor",
        "socket": "IMUSocket",
        "Hz": 5,
        "configuration":{
            "Sigma": 0.5,
            "Depth": 1,
            "DepthSigma": 0.25
        }
    }