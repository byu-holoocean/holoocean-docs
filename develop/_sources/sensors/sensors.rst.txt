.. _`sensors`:

=================
HoloOcean Sensors
=================

HoloOcean sensors are used to gather data from the environment. Sensors are attached to agents at 
specific locations called "sockets" (see :ref:`agents` for socket locations on each agent). Sensors 
publish data to the simulation state, which can be accessed as the return value of the environment's 
``.tick()`` and ``.step()`` functions.

Using Sensors
=============

.. toctree::
   :maxdepth: 1

   docs/sensor-config
   docs/octree
   docs/publishing


HoloOcean Sensors
=================
The following are inspired by real-world sensors and are intended to collect realistic data.
Most sensors here include parameters for adjusting noise, bias, and other characteristics to
simulate real-world sensor behavior.

Perception Sensors
------------------
.. toctree::
   :maxdepth: 1
   :glob:

   sensors/singlebeam-sonar-sensor
   sensors/sidescan-sonar-sensor
   sensors/imaging-sonar-sensor
   sensors/profiling-sonar-sensor
   sensors/dvl-sensor
   sensors/depth-sensor
   sensors/rgb-camera-sensor  
   sensors/camera-sensor
   sensors/imu-sensor
   sensors/gps-sensor
   sensors/magnetometer-sensor
   sensors/range-finder-sensor
   sensors/bst-sensor

Communication Sensors
---------------------
.. toctree::
   :maxdepth: 1
   :glob:

   sensors/acoustic-beacon-sensor
   sensors/optical-modem-sensor 

State Sensors
-------------
The following are not physical sensors, but are used to return information that is only available in 
simulation. They are helpful in debugging, collecting ground truth data, capturing simulation videos, 
and other applications where simulation information is helpful. Some of these have overlap with each 
other, but are provided for convenience for different use cases.

.. toctree::
   :maxdepth: 1
   :glob:

   sensors/viewport-capture-sensor
   sensors/location-sensor
   sensors/rotation-sensor
   sensors/orientation-sensor
   sensors/pose-sensor
   sensors/velocity-sensor
   sensors/dynamics-sensor

.. note::
   The location, rotation, orientation, pose, and velocity sensors return values relative to the 
   **global frame** for the pose of the socket they are placed in. 

   The dynamics sensor always returns values for the COM of the agent, with values given in the 
   **global frame**, regardless of the socket it is placed in.


.. Note: We are not yet including semantic segmentation camera, raycast lidar, or raycast semantic 
   lidar, as they are not fully tested yet. 

   Sensor pages that exist but aren't in a tree yet:
    
   sensors/rgbd-camera-sensor 
   sensors/semantic-segmentation-camera-sensor
   sensors/raycast-lidar-sensor
   sensors/raycast-semantic-lidar-sensor

  



