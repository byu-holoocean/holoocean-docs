====================
Range Finder Sensor
====================

The Range Finder is a laser sensor. It returns distances to nearest collisions in the directions 
specified by the parameters. Or if the sensor does not detect anything whithin the operational range, 
a negative value is returned. As an example, if an agent had two range sensors at different 
angles with 24 lasers each, the RangeFinder debug traces would look something like this:

.. image:: ../images/UAVRangeFinder.PNG

That is, for one laser, you'd have one laser facing forward; for three, you'd have one forward, with the 
other two distributed evenly along the circle, at 120 degree intervals; and for 24, you'd have a laser 
spaced every 15 degrees.

See :py:class:`~holoocean.sensors.RangeFinderSensor` for the Python API and more details.


Example sensor definition::

    {
        "socket": "COM",
        "configuration": {
            "LaserMaxDistance": 10,
            "LaserCount": 1,
            "LaserAngle": 0,
            "LaserDebug": false
        }
    }
