.. _visualizing_rgbcamera_output:

Visualizing RGBCamera Output
============================

It can be useful to display the output of the RGB camera while an agent is 
training. Below is an example using the ``cv2`` library.

When the window is open, press the ``0`` key to tick the environment and show the
next window.

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