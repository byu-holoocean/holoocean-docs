===============
Imaging Sonar
===============

Sometimes referred to as a forward-looking sonar, imaging sonar is a type of multi-beam sonar that 
projects the intensity onto the 2d time of return-azimuth plane. This allows for a 2d image to be 
created of the area in front of the sonar. This is useful for detecting objects in front of the sonar, 
and is often used in AUVs to detect obstacles in front of them.

Note that the Azimuth streaks parameter is used to control whether the simulator will add or remove 
streaks along the azimuth to the return, as those are common artifacts in sonar images.

See :ref:`visualizing_imaging_sonar` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.ImagingSonar` for the Python API.

Example sensor definition::

    {
        "sensor_type": "ImagingSonar",
        "socket": "SonarSocket",
        "Hz": 2,
        "configuration": {
            "Azimuth": 120,
            "Elevation": 20,
            "RangeMin": 1,
            "RangeMax": 40,
            "RangeBins": 512,
            "AzimuthBins": 512,
            "AddSigma": 0.15,
            "MultSigma": 0.2,
            "MultiPath": true,
            "ClusterSize": 5,
            "ScaleNoise": true,
            "AzimuthStreaks": -1,
            "RangeSigma": 0.1,
            "ShowWaring": true,
            "InitOctreeRange": 50,
            "ViewRegion": false,
            "ViewOctree" -10,
            "WaterDensity": 997,
            "WaterSoundSpeed": 1480,
            "UseApprox": true
        }
    }