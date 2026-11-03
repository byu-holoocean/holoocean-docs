==============================
Semantic Segmentation Camera
==============================

A camera sensor for getting semantically labelled camera data.

The image below shows the comparison between the RGB camera output with the corresponding semantic 
segmentation camera output. 

.. image:: ../images/semantic_output_w_comparison.png

See :ref:`visualizing_semanticsegcamera_output` for an example of how to use this sensor.

.. note::

    All HoloOcean levels already have semantic labels applied. If you are making a custom level, you must 
    enable semantic labels and define any new labels. Please reference :ref:`semantic-segmentation` for 
    instructions and our current list of semantic labels.


See :py:class:`~holoocean.sensors.SemanticSegmentationCamera` for the Python API.

Example sensor definition::

    {
        "sensor_type": "SemanticSegmentationCamera",
        "sensor_name": "SemanticForwardFacingCamera",
        "socket": "CameraSocket",
        "configuration": {
            "CaptureWidth": 512,
            "CaptureHeight": 512,
        }
    }
