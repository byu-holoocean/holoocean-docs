==============================
Installing & Managing Packages
==============================

.. _`package-locations`:

Package Installation Location
=============================

HoloOcean packages are by default saved in the current user profile, depending
on the platform.

========== ==================================================================
 Platform   Location
========== ==================================================================
Linux      ``~/.local/share/holoocean/{holoocean_version}/worlds/``
Windows    ``%USERPROFILE%\AppData\Local\holoocean\{holoocean_version}\worlds``
========== ==================================================================

Note that the packages are saved in different subfolders based on the version
of HoloOcean. This allows multiple versions of HoloOcean to coexist, without
causing version incompatibility conflicts.

This is the path returned by :func:`holoocean.util.get_holoocean_path`

Each folder inside the worlds folder is considered a seperate package, so it 
must match the format of the archive described in :ref:`package-contents`.

Overriding Location
-------------------

The environment variable ``HOLODECKPATH`` can be set to override the default
location given above.

.. caution::
   If ``HOLODECKPATH`` is used, it will override
   this version partitioning, so ensure that ``HOLODECKPATH`` only points to 
   packages that are compatible with your version of HoloOcean.


Managing World Packages
=======================

The default option for managing packages is to use ``holoocean.install()`` and 
``holoocean.remove()``. These functions can be used to install and remove any packages 
managed by the HoloOcean team (currently only the Ocean package). 

Install a Package Automatically
-------------------------------
The ``holoocean`` python package includes a :ref:`packagemanager` that can be used independently. 
Below are some example usages, but see :ref:`packagemanager` for complete documentation.
::

   >>> from holoocean import packagemanager
   >>> packagemanager.installed_packages()
   []
   >>> packagemanager.available_packages()
   ['Ocean']
   >>> packagemanager.install("Ocean")
   Installing Ocean ver. 0.1.0 from https://robots.et.byu.edu/holo/Ocean/v0.1.0/Linux.zip
   File size: 1.55 GB
   |â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ| 100%
   Unpacking worlds...
   Finished.
   >>> packagemanager.installed_packages()
   ['Ocean']

Manually Installing a Package
-----------------------------
Packages developed by users can be installed for use with the HoloOcean library. To manually 
install a package, you will be provided a ``.zip`` file. Extract it into the ``worlds`` folder 
in your HoloOcean installation location.

.. note::

   Ensure that the file structure is as follows:

   ::

      + worlds
      +-- YourManuallyInstalledPackage
      |   +-- config.json
      |    +-- etc...
      +-- AnotherPackage
      |   +-- config.json
      |   +-- etc...

   Not

   ::

      + worlds
      +-- YourManuallyInstalledPackage
      |   +-- YourManuallyInstalledPackage
      |       +-- config.json
      |   +-- etc...
      +-- AnotherPackage
      |   +-- config.json
      |   +-- etc...

Print Information
-----------------

There are several convenience functions provided to allow packages, worlds,
and scenarios to be easily inspected.

::

   >>> packagemanager.package_info("Ocean")
   Package: Ocean
      Platform: Linux
      Version: 0.1.0
      Path: Linux/Holodeck/Binaries/Linux/Holodeck
      Worlds:
      Rooms
            Scenarios:
            Rooms-DataGen:
               Agents:
                  Name: turtle0
                  Type: TurtleAgent
                  Sensors:
                     LocationSensor
                        lcm_channel: POSITION
                     RotationSensor
                        lcm_channel: ROTATION
                     RangeFinderSensor
                        lcm_channel: LIDAR
                        configuration
                           LaserCount: 64
                           LaserMaxDistance: 20
                           LaserAngle: 0
                           LaserDebug: True
            Rooms-IEKF:
               Agents:
                  Name: uav0
                  Type: UavAgent
                  Sensors:
                     PoseSensor
                     VelocitySensor
                     IMUSensor
      SimpleUnderwater
            Scenarios:
            SimpleUnderwater-AUV:
               Agents:
                  Name: auv0
                  Type: HoveringAUV
                  Sensors:
                     PoseSensor
                        socket: IMUSocket
                     VelocitySensor
                        socket: IMUSocket
                     IMUSensor
                        socket: IMUSocket
                     DVLSensor
                        socket: DVLSocket


You can also look for information for a specific world or scenario
::

   packagemanager.world_info("SimpleUnderwater")
   packagemanager.scenario_info("Rooms-DataGen")

