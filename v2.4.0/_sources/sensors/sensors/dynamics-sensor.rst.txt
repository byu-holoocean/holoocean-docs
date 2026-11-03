.. _dynamics-sensor:

===============
Dynamics Sensor
===============

A sensor that returns ground truth values needed to implement custom dynamics. The dynamics sensor 
returns linear acceleration, velocity, and position, followed by angular acceleration, velocity, and 
position, in that order.
 
.. note::
    This sensor always returns values at the **COM of the vehicle**, with values given in the **global 
    frame**, regardless of the socket it is placed in. 

See :py:class:`~holoocean.sensors.DynamicsSensor` for the Python API and more details.

Example sensor definition::
    
    {
        "sensor_type": "DynamicsSensor",
        "socket": "COM",
        "configuration": {
           "UseCOM": true,
           "UseRPY": true
        }
    }

