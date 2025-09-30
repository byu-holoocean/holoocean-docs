==================
Single-Beam Sonar
==================

A sensor that simulates with octrees a single conical sonar beam, returning a 1D array of return 
strength at each range bin.

See :ref:`visualizing_singlebeam_sonar` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.SinglebeamSonar` for the python API.

Example sensor definition::
    
    {
        "sensor_type": "SinglebeamSonar",
        "socket": "SonarSocket",
        "Hz": 10,
        "configuration": {
            "OpeningAngle": 30,
            "RangeMin": 0.5,
            "RangeMax": 30,
            "RangeBins": 200,
            "AddSigma": 0,
            "MultSigma": 0,
            "RangeSigma": 0.1,
            "ShowWarning": true,
            "InitOctreeRange": 40,
            "ViewRegion": false,
            "ViewOctree": -10,
            "WaterDensity": 997,
            "WaterSpeedSound": 1480,
            "UseApprox": true
        }
    }