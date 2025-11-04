===============
Profiling Sonar
===============

A simulaiton of a profiling sonar using octrees. 

See :ref:`visualizing_profiling_sonar` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.ProfilingSonar` for the Python API.

Example sensor definition::
    
    {
        "sensor_type": "ProfilingSonar",
        "socket": "SonarSocket",
        "Hz": 2,
        "configuration": {
            "Azimuth": 120,
            "Elevation": 1,
            "RangeMin": 1,
            "RangeMax": 60,
            "RangeBins": 512,
            "AzimuthBins": 512,
            "AddSigma": 0.15,
            "MultSigma": 0.2,
            "MultiPath": true,
            "ClusterSize": 5,
            "ScaleNoise": true,
            "AzimuthStreaks": -1,
            "RangeSigma": 0.1,
            "ShowWarning": true,
            "InitOctreeRange": 70,
            "ViewRegion": false,
            "ViewOctree": -10,
        }
    }