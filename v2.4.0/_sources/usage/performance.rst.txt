.. _`improving-performance`:

=====================
Improving Performance
=====================

HoloOcean is fairly performant by default, but you can also sacrifice features to increase your 
frames per second.

Frame Rate
==========
The frame rate can have a large impact on performance. The frame rate is set in the scenario 
configuration. See :ref:`configure-framerate` for details on how to set the ``ticks_per_sec`` and 
``frames_per_sec`` to optimize performance for your specific task. 

Sonar Sensors
=============

The sonar sensors can be taxing on performance. There's a number of things that can be done to help 
improve their performance as well.

Lowering Octree Resolution
--------------------------

The Octree resolution has a large impact on sonar performance. The higher ``octree_min`` is, the less 
leaves there are to search through, and the faster it'll run. This will have an impact on image 
quality, especially at close distances. If most objects that are being inspected are a ways away, 
this parameter can be safely increased quite a bit.

See :ref:`configure-octree` for info on how to do that.

Changing Ticks-Per-Capture
--------------------------

The sonar sample rate can be reduced to increase the average frames per second.
See :ref:`sensor-configuration` and the ``Hz`` parameter for more info.


Camera Sensors
==============

If using a ``Camera`` or ``RGBCamera`` sensor, rendering the camera frames each tick will 
significantly impact performance. Rendering the camera every frame causes a context switch deep in 
the rendering code of the engine, which has a significant performance penalty. 

This chart shows how much performance you can expect to gain or lose by adjusting or disabling the 
Camera (left column is frame time in milleseconds). 

.. note::
    The following tests were performed in the original Holodeck, but the results should be similar 
    for HoloOcean.

+------------+----------+---------+-----------+---------+----------+---------+
| Resolution | UrbanCity          | MazeWorld           | AndroidPlayground  |
+============+==========+=========+===========+=========+==========+=========+
| No Camera  | 8.55 ms  | 117 fps | 4.69  ms  | 213 fps | 2.47 ms  | 405 fps |
+------------+----------+---------+-----------+---------+----------+---------+
| 64         | 17   ms  | 59 fps  | 11    ms  | 91 fps  | 4.87 ms  | 205 fps |
+------------+----------+---------+-----------+---------+----------+---------+
| 128        | 20   ms  | 50 fps  | 11.6  ms  | 86 fps  | 5.59 ms  | 179 fps |
+------------+----------+---------+-----------+---------+----------+---------+
| 256        | 22   ms  | 45 fps  | 14.71 ms  | 68 fps  | 9.02 ms  | 111 fps |
+------------+----------+---------+-----------+---------+----------+---------+
| 512        | 35   ms  | 29 fps  | 30.8  ms  | 32 fps  | 24.81 ms | 40 fps  |
+------------+----------+---------+-----------+---------+----------+---------+
| 1024       | 89   ms  | 11 fps  | 84.2  ms  | 12 fps  | 94.55 ms | 11 fps  |
+------------+----------+---------+-----------+---------+----------+---------+
| 2048       | 410  ms  | 2  fps  | 383   ms  | 3  fps  | 366   ms | 3  fps  |
+------------+----------+---------+-----------+---------+----------+---------+

Removing the Camera
--------------------
Removing the camera entirely will significantly improve performance. For custom scenarios, simply 
remove the camera from the scenario configuration file you are using. To modify pre-made scenarios,
the easiest method is simply to create a new custom scenario based on the one you want to use, and 
remove the camera from the configuration.

See :ref:`custom-scenarios`.

Lowering the Camera Resolution
------------------------------

Lowering the resolution of the ``RGBCamera`` or ``Camera`` can also help speed things up. 
Create a :ref:`custom scenario <custom-scenarios>`, and in the 
:ref:`configuration block <configuration-block>` for the ``RGBCamera`` or ``Camera``, set the
``CaptureWidth`` and ``CaptureHeight``.

See :class:`~holoocean.sensors.RGBCamera` and :class:`~holoocean.sensors.Camera` for more details.

Changing Ticks-Per-Capture
--------------------------

The camera sample rate can be reduced to increase the average frames per second.
See :ref:`sensor-configuration` and the ``Hz`` parameter for more info.


Disable Viewport Rendering
==========================

Rendering the viewport window can be unnecessary when running simulations sequentially, 
such as when using HoloOcean for reinforcement learning. You can disable the viewport with 
the :meth:`~holoocean.environments.HoloOceanEnvironment.should_render_viewport` method (see 
:ref:`headless` for details).

At lower camera resolutions, disabling the viewport can improve framerates by up to 40%.

Change Render Quality
=====================

You can adjust HoloOcean to render at a lower (or higher) quality to improve
performance. See the 
:meth:`~holoocean.environments.HoloOceanEnvironment.set_render_quality` method.

Below is a comparison of render qualities and the frame time in ms.

========= =========== =========== ==================
 Quality   MazeWorld   UrbanCity   AndroidPlayground
========= =========== =========== ==================
 ``0``       10.34       12.33       6.63
 ``1``       10.53       15.06       6.84
 ``2``       14.81       19.19       8.66
 ``3``       15.58       21.78       9.2
========= =========== =========== ==================
