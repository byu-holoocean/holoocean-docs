Camera Output Examples
======================

It can be useful to display camera output. Below are examples using the ``cv2`` library.

When the window is open, press the ``0`` key to tick the environment and show the
next window.

.. _visualizing_rgbcamera_output:

Visualizing RGBCamera Output
----------------------------

::

    import holoocean, cv2

    env = holoocean.make("Dam-HoveringCamera")
    env.act('auv0', [10,10,10,10,0,0,0,0])

    for _ in range(200):
        state = env.tick()

        if "LeftCamera" in state:
            pixels = state["LeftCamera"]
            cv2.namedWindow("Camera Output")
            cv2.imshow("Camera Output", pixels[:, :, 0:3])
            cv2.waitKey(0)
            cv2.destroyAllWindows()

.. _visualizing_depthcamera_output:

Visualizing Depth Camera Output
-------------------------------

::

    import holoocean, cv2

    env = holoocean.make("Dam-HoveringCamera")
    env.act('auv0', [10,10,10,10,0,0,0,0])

    for _ in range(200):
        state = env.tick()

        if "DepthForwardCamera" in state:
            data = state["DepthForwardCamera"]
            cv2.namedWindow("Depth Output")
            depth = data["depth"] #grab the depth data from the camera output
            cv2.imshow("Depth Output", depth) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.namedWindow("Depth Color Output")
            image = data["image"]
            cv2.imshow("Depth Color Output", image) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()


.. _visualizing_semanticsegcamera_output:

Visualizing Semantic Segmentation Camera Output
-----------------------------------------------

::

    import holoocean, cv2

    env = holoocean.make("Dam-HoveringCamera")
    env.act('auv0', [10,10,10,10,0,0,0,0])

    for _ in range(200):
        state = env.tick()

        if "SemanticForwardFacingCamera" in state:
            pixels = state["SemanticForwardFacingCamera"]
            cv2.namedWindow("Semantic Output")
            cv2.imshow("Semantic Output", pixels[:, :, 0:3])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
