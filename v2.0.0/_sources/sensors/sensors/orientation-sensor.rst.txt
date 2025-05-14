===================
Orientation Sensor
===================

A sensor that returns the forward, right, and up vectors for the **sensor**, in form of 3x3 matrix, in 
the **global frame**. If the sensor is in a socket other than the COM, the returned matrix will 
reflect the global orientation of the socket (the orientation of the vehicle plus the orientation 
offset from vehicle to the socket used). 

.. note:: 
    In our provided configurations that use this sensor, the sensor is in the IMU socket, which is 
    oriented NED. 

See :py:class:`~holoocean.sensors.OrientationSensor` for the python API and more details.

Example sensor definition::
    
     {
         "sensor_type": "OrientationSensor",
         "socket": "IMUSocket",
     }