=========
Changelog
=========

.. Changelog Style Guide
  - Each release should have a New Features / Changes / Bug Fixes section.
  - Keep the first sentence of each point short and descriptive
  - The passive voice should be avoided
  - Try to make the first word a verb in past tense. Bug fixes should use
    "Fixed"
  - Add a link to the issue describing the change or the pull request that
    merged it at the end in parentheses
  - see https://github.com/BYU-PCCL/holodeck/wiki/Holodeck-Release-Notes-Template


HoloOcean 2.2.1
===============
*10/31/2025*

New Features
------------

- Added delete octree command to delete all octrees for worlds or one specific world

Bug Fixes
---------

- Fixed Torpedo AUV and CougUV fin control bug that prevented vehicle from turning
- API docs Fixed
- Edge case for Octree sidescan range binning fixed.

HoloOcean 2.2.0
===============
*10/22/2025*

New Features
------------

- Added underwater currents
- Added biomass, salinity, and temperature (BST) sensor

Bug Fixes
---------

- Fixed RangeFinder sensor returning max range value when nothing was in range of the sensor. Now it returns -1 if nothing is in range of the sensor.

HoloOcean 2.1.0
===============
*9/29/2025*

New Features
------------

- Added develop install for Windows, as we've automated the world build process.
- Added Flashlight for underwater illumination.
- Add weather commands, including rain, time of day and tide, air and water fog, water color.

Changes
-------

- Updated Logo
- Changed drone CI/CD steps for internal improvements.

Bug Fixes
---------

- Fixed PID instability for the hovering and BlueROV vehicles.

HoloOcean 2.0.1
===============
*6/27/2025*

New Features
------------

- Updated Fossen based dynamics with new interface for easier use and multi-agent support, and expanded torpedo model with additional fin configurations.
- Official Docker support for both runtime and development containers.

Changes
-------

- Expanded documentation on creating environments and developing with the Unreal Editor.
- Dropped support for Python 3.7 and 3.8; added support for Python 3.12 and 3.13.
- Improved installation instructions, including a new Docker installation guide.
- Grammar fixes throughout the documentation.

Bug Fixes
---------

- Improved rise time and damping in the Torpedo depth controller when using Fossen based dynamics.


HoloOcean 2.0.0
===============
*5/10/2025*

New Features
------------
- Improved rendering with Unreal Engine 5.3
- Advanced vehicle dynamics using models from Fossen
- ROS2 Bridge for communication with external systems
- New vehicles: BlueROV Heavy, CougUV

Changes
-------
- Huge update to documentation to improve overall readability and clarity
- Updated numpy to v2.0.0 to work with UE 5.3
- Added extra test cases to several sensors to improve coverage

Bug Fixes
---------
- **Temporarily disabled materials in worlds to prevent sonar issue in Linux**
- Fixed bugs in some world files that caused incorrect sonar data
- Removed Git LFS from repository to prevent bandwidth limitation that prevented committing
- Overhauled implementation of thruster/fin control to fix issues with vehicle dynamics (TorpedoAUV 
  now turns properly, no issues with uncontrollable spinning)
- Fixed memory allocation bug that sometimes prevented world from loading properly
- Added post-process materials to prevent error message when launching Unreal

HoloOcean 2.0.0 PreRelease
==========================
*11/8/2024*

Updating from Unreal Engine 4.27 to 5.3

HoloOcean 1.0.0
===============
*4/29/2024*

Migrating to GitHub, and updating license phrasing

HoloOcean 0.5.8
===============
*4/3/2024*

New Features
------------
- Added custom dynamics for vehicles
- Added magnetometer
- Added dynamics sensor
- Simple PD controller for HoveringAUV
- Added SurfaceVessel agent

Changes
-------
- Updated installation instructions to comply with Unreal Engine EULA
- Misc bug fixes and documentation improvements

(Note that the version numbers 0.5.1-0.5.7 are absent because of some difficulties with updating the 
PyPI package. 0.5.8 is the first release after 0.5.0.)

HoloOcean 0.5.0
===============
*3/22/2022*

Large sonar upgrade!

Highlights
----------
- 3 new sonar sensors
- Upgraded noise modeling in Imaging and Profiling Sonar
- Lots of misc bug fixes!
- Upgrade to Unreal Engine 4.27

New Features
------------
- Added many new sonar sensors, including

  - :class:`~holoocean.sensors.ImagingSonar`
  - :class:`~holoocean.sensors.SidescanSonar`
  - :class:`~holoocean.sensors.ProfilingSonar`
  - :class:`~holoocean.sensors.SinglebeamSonar`

- ImagingSonar now has significantly improved noise modeling
- Can now specify a lifetime parameter to draw functions
- Now based on Unreal Engine 4.27

Changes
-------
- SonarSensor is now ImagingSonar
- Rotations are now a correct [roll, pitch, yaw]
- Step function no longer returns terminal, reward and info. Only state
- Environments no longer publish over lcm in pre-start ticks

Bug Fixes
---------
- Timeouts are turned off for sonars to prevent premature termination of the simulation
- Specifying a number of ticks to execute at once now ticks for all of them


HoloOcean 0.4.1
===============
*9/21/2021*

Bug Fixes
---------
- Required pywin32 <= 228 for easier Windows install


HoloOcean 0.4.0
===============
*9/17/2021*

First official release!

Highlights
----------
- New Ocean environment package
- 2 new agents and 7 new sensors, along with updating of all previous sensors
- Complete rebranding to HoloOcean

New Features
------------
- Added agents :class:`~holoocean.agents.HoveringAUV` and :class:`~holoocean.agents.TorpedoAUV`
- Added a plethora of new sensors, all with optional noise configurations

  - :class:`~holoocean.sensors.ImagingSonar`
  - :class:`~holoocean.sensors.DVLSensor`
  - :class:`~holoocean.sensors.DepthSensor`
  - :class:`~holoocean.sensors.GPSSensor`
  - :class:`~holoocean.sensors.PoseSensor`
  - :class:`~holoocean.sensors.AcousticBeaconSensor`
  - :class:`~holoocean.sensors.OpticalModemSensor`
- New :ref:`Ocean <ocean>` package
- Added frame rate capping option
- Added ticks_per_sec and frames_per_sec to scenario config, see :ref:`configure-framerate`

Changes
-------
- Everything is now rebranded from Holodeck -> HoloOcean

Bug Fixes
---------
- Sensors now return values from their location, not the agent location
- IMU now returns angular velocity instead of linear velocity
- Various integer -> float changes in scenario loading


Pre-HoloOcean
=============
See `Holodeck changelog <https://holodeck.readthedocs.io/en/latest/changelog/changelog.html>`_
