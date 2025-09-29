.. _velocity-sensor:

================
Velocity Sensor
================

Returns the [x,y,z] velocity of the **sensor** in the **global frame**. If the sensor is placed in 
a socket other than the vehicle COM, it will return the velocity of the socket used (the vehicle 
velocity plus the relative velocity between vehicle COM and socket used).


See :py:class:`~holoocean.sensors.VelocitySensor` for the python API.

Example sensor definition::
    
    {
        "sensor_type": "VelocitySensor",
        "socket": "IMUSocket"
    }