===============
Magnetometer
===============

Returns the global x-axis (or configuration vector) in the local frame.

See :py:class:`~holoocean.sensors.MagnetometerSensor` for the python API and more details.

Example sensor definition::
    
     {
         "sensor_type": "MagnetometerSensor",
         "socket": "IMUSocket",
         "configuration": {
            "Sigma": 0,
            "MagnetixVector": [1,0,0]
         }
     }