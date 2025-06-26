===============
Rotation Sensor
===============

Gets the [roll, pitch, yaw] rotation of the **sensor** in the **global frame**. If the sensor is 
placed in a socket other than the vehicle COM, it will return the global rotation of the socket
it is placed in (the rotation of the vehicle plus the rotation offset from vehicle COM to socket).

Angles are in degrees.

See :py:class:`~holoocean.sensors.RotationSensor` for the Python API.

Example sensor definition::
    
    {
        "sensor_type": "RotationSensor",
        "socket": "COM",
    }