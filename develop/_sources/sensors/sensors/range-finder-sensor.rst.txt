====================
Range Finder Sensor
====================

The Range Finder is a laser sensor. It returns distances to nearest collisions in the directions 
specified by the parameters. For example, if an agent had two range sensors at different angles with 
24 lasers each, the RangeFinder debug traces would look something like this:

.. image:: ../UAVRangeFinder.PNG

That is, for 1 laser, you'd have 1 laser facing forward; for 3, you'd have one forward, with the 
other 2 distributed evenly along the circle, at 120 degree intervals; and for 24, you'd have a laser 
spaced every 15 degrees.

See :py:class:`~holoocean.sensors.RangeFinderSensor` for the python API and more details.


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