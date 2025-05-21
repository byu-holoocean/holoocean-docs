===============
Location Sensor
===============

Returns the [x,y,z] position of the **sensor** in the **global frame**. If the sensor is in a socket other 
than the COM socket, it will return the global position of the socket it is placed in (the location 
of the vehicle plus the offset from vehicle COM to socket).

See :py:class:`~holoocean.sensors.LocationSensor` for the python API.

Example sensor definition::

    {
        "sensor_type": "LocationSensor",
        "socket": "COM",
        "configuration": {
            "Sigma": 0
        }
    }