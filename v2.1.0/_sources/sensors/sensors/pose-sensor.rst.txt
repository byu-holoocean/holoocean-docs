.. _pose-sensor:

============
Pose Sensor
============
Returns the orientation (see :py:class:`~holoocean.sensors.OrientationSensor`) and position of the 
**sensor** in a 4x4 homogenous matrix in the **global frame**. If the sensor is placed in a socket 
other than the COM socket, it will return the global pose of the socket it is placed in (the
location of the vehicle plus the offset from vehicle COM to socket).

The 4x4 matrix is in the following form:
::

    [R, p]
    [0, 1]

Where R is a 3x3 rotation matrix and p is a 3x1 position vector. The last row is always [0, 0, 0, 1].

See :py:class:`~holoocean.sensors.PoseSensor` for the Python API and more details.

Example sensor definition::
    
     {
         "sensor_type": "PoseSensor",
         "socket": "COM"
     }
