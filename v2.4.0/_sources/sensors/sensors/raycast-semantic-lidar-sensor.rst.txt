=============================
Raycast Semantic LIDAR Sensor
=============================

Simulates a LIDAR sensor using raycasting. Returns a point cloud of "hit" objects within the sensor's
range as well as semantic data about each object being hit, including the unique object ID of the 
object being hit and the semantic tag/category of the object. Points are classified into semantic 
categories based on the environment's semantic map. Also returns the intensity and ring/channel for 
each point. 

See :ref:`raycast_lidar_sensor` for more information on the parameters and how to use this sensor.

See :ref:`visualizing_raycast_lidar` for an example of how to use the base non-semantic sensor. Change
the sensor type to `RaycastSemanticLidar` to have semantics returned.

.. note::

    All HoloOcean levels already have semantic labels applied. If you are making a custom level, you must 
    enable semantic labels and define any new labels. Please reference :ref:`semantic-segmentation` for 
    instructions and our current list of semantic labels.

See :py:class:`~holoocean.sensors.RaycastSemanticLidar` for the python API.

Example sensor definition::

    {
        "sensor_type": "RaycastSemanticLidar",
        "configuration": {
            "socket": "CameraSocket",
            "Channels": 128,                    
            "Range": 200,                        
            "PointsPerSecond": 20000,           
            "RotationFrequency": 10,               
            "UpperFovLimit": 10,                 
            "LowerFovLimit": -30,                 
            "HorizontalFov": 360.0,               
            "AtmospAttenRate": 0.4,             
            "RandomSeed": 42,                      
            "DropOffGenRate": 0.45,                
            "DropOffIntensityLimit": 0.8,        
            "DropOffAtZeroIntensity": 0.4,        
            "ShowDebugPoints": True,              
            "NoiseStdDev": 0.0            
        },
        "Hz": 10
    }
