===============
Sidescan Sonar
===============

Simulates a sidescan sonar with octrees. Has a narrow elevation and wide asimuth, and simulates both 
sides being scanned. 

See :ref:`visualizing_sidescan_sonar` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.SidescanSonar` for the python API.

Example sensor definition::
    
    {
        "sensor_type": "SidescanSonar",
        "socket": "SonarSocket",
        "Hz": 10,
        "configuration": {
            "Azimuth": 170,
            "Elevation": 0.25,
            "RangeMin": 0.5,
            "RangeMax": 40,
            "RangeBins": 2000,
            "AddSigma": 0.05,
            "MultSigma": 0.05,
            "ShowWarning": true,
            "InitOctreeRange": 50,
            "ViewRegion": false,
            "ViewOctree": -10,
            "WaterDensity": 997,
            "WaterSpeedSound": 1480,
            "UseApprox": true
        }
    }