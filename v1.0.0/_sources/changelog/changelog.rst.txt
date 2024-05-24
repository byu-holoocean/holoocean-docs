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

HoloOcean 1.0.0
----------------
*4/29/2024*

Migrating to GitHub, and updating license phrasing.

HoloOcean 0.5.8
---------------
*4/3/2/2024*

Added custom dynamics and updated installation instructions to reflect current installation process to comply with Unreal Engine EULA.
(Note that the version numbers 0.5.1-0.5.7 are absent because of some difficulties with updating the PyPI package. So 0.5.8 is the first release after 0.5.0)

Highlights
~~~~~~~~~~
- Added magnetometer
- Added dynamics sensor
- Simple PD controller for HoveringAUV
- Added SurfaceVessel agent
- misc bug fixes and documentation improvements

HoloOcean 0.5.0
----------------
*3/22/2022*

Large sonar upgrade!

Highlights
~~~~~~~~~~
- 3 new sonar sensors
- Upgraded noise modeling in Imaging and Profiling Sonar
- Lots of misc bug fixes!
- Upgrade to Unreal Engine 4.27

New Features
~~~~~~~~~~~~
- Added many new sonar sensors, including

  - :class:`~holoocean.sensors.ImagingSonar`
  - :class:`~holoocean.sensors.SidescanSonar`
  - :class:`~holoocean.sensors.ProfilingSonar`
  - :class:`~holoocean.sensors.SinglebeamSonar`

- ImagingSonar now has significantly improved noise modeling
- Can now specify a lifetime parameter to draw functions
- Now based on Unreal Engine 4.27

Changes
~~~~~~~
- SonarSensor is now ImagingSonar
- Rotations are now a correct [roll, pitch, yaw].
- step function no longer returns terminal, reward and info. Only state.
- Environments no longer publish over lcm in pre-start ticks.

Bug Fixes
~~~~~~~~~
- Timeouts are turned off for sonars to prevent premature termination of the simulation.
- Specifying a number of ticks to execute at once now ticks for all of them.


HoloOcean 0.4.1
----------------
*9/21/2021*

Bug Fixes
~~~~~~~~~
- Required pywin32 <= 228 for easier Windows install.


HoloOcean 0.4.0
----------------
*9/17/2021*

First official release!

Highlights
~~~~~~~~~~
- New Ocean environment package.
- 2 new agents and 7 new sensors, along with updating of all previous sensors.
- Complete rebranding to HoloOcean.  

New Features
~~~~~~~~~~~~
- Added agents :class:`~holoocean.agents.HoveringAUV` and :class:`~holoocean.agents.TorpedoAUV`
- Added a plethora of new sensors, all with optional noise configurations

  - :class:`~holoocean.sensors.ImagingSonar`
  - :class:`~holoocean.sensors.DVLSensor`
  - :class:`~holoocean.sensors.DepthSensor`
  - :class:`~holoocean.sensors.GPSSensor`
  - :class:`~holoocean.sensors.PoseSensor`
  - :class:`~holoocean.sensors.AcousticBeaconSensor`
  - :class:`~holoocean.sensors.OpticalModemSensor`
- New :ref:`Ocean <ocean>` package.
- Added frame rate capping option.
- Added ticks_per_sec and frames_per_sec to scenario config, see :ref:`configure-framerate`.

Changes
~~~~~~~
- Everything is now rebranded from Holodeck -> HoloOcean.

Bug Fixes
~~~~~~~~~
- Sensors now return values from their location, not the agent location.
- IMU now returns angular velocity instead of linear velocity.
- Various integer -> float changes in scenario loading.


Pre-HoloOcean
--------------
See `Holodeck changelog <https://holodeck.readthedocs.io/en/latest/changelog/changelog.html>`_