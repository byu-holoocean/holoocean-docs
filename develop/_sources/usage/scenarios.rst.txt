.. _scenarios:

=========
Scenarios
=========

When you call ``holoocean.make()`` to create an environment, you pass in the
name of a scenario, eg. ``holoocean.make("Pier-Hovering")``. A scenario tells 
HoloOcean:

* Which world to load
* What agents are present
* Where they are
* What sensors they have

HoloOcean worlds are meant to be configurable by changing out the scenario. 
Scenarios allow the same world to be used for different purposes. For different 
senarios using the same world, the world or map itself doesn't change, but the 
things in the world and your objective can change.

We provide several pre-built scenarios in :ref:`all-packages` for common underwater 
robotics tasks, distributed as ``.json`` files. 

HoloOcean is intended to be used with user-created scenarios as well. Custom scenarios 
can be created using a dictionary in a Python script or by creating a ``.json`` file. 
Both methods follow the same format, described below. 


.. _`scenario-files`:

Scenario File Format
====================

Scenario ``.json`` files are distributed in packages (see :ref:`package-contents`), and 
must be named ``{WorldName}-{ScenarioName}.json``. By default they are stored in the
``worlds/{PackageName}`` directory (see :ref:`package-locations`). 

Scenarios can be defined using a ``.json`` file or in a Python script using a dictionary. 
Both methods follow the same format using key-value pairs. An example dictionary is given below: 

.. code-block:: json

   {
      "name": "{Scenario Name}",
      "world": "{world it is associated with}",
      "package_name": "{package it is associated with}",
      "agents":[
         "array of agent objects"
      ],
      "ticks_per_sec": 30,
      "frames_per_sec": 30,
      "env_min": [-10, -10, -10],
      "env_max": [10, 10, 10],
      "octree_min": 0.1,
      "octree_max": 5,
      "window_width":  1280,
      "window_height": 720,
      "lcm_provider": "provider name"
   }

.. note::

   At a minimum, a scenario must contain ``name``, ``world``, and ``package_name`` keys, and at 
   least one agent object. All other keys are optional and will default to a set value if not 
   provided.

Below is a description of some of the keys in the scenario dictionary. 


Name and World
--------------
- ``name`` is a string that specifies the name of the scenario.
   This name is part of the string passed to ``holoocean.make()`` to create an environment.
- ``world`` is a string that specifies the world to load.
   It must match the name of the world file in the package folder (see :ref:`packages`).
- ``package_name`` is a string that specifies the package the world is associated with.


Agent Objects
-------------
HoloOcean agents are declared in a list in the scenario dictionary. Each agent is defined using a
new dictionary in the list. 

Below is an example of an agent configuration. For detailed descriptions of the keys and values, 
see :ref:`agent-configuration`. 

.. code-block:: json

   "agents":[
      {
         "agent_name": "uav0",
         "agent_type": "{agent types}",
         "sensors": [
            "array of sensor objects"
         ],
         "control_scheme": "{control scheme type}",
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0],
         "location_randomization": [1, 2, 3],
         "rotation_randomization": [10, 10, 10]
      }
   ]


Sensor Objects
--------------
Each agent can be equipped with one or more sensors, including cameras and sonar. Sensor definition
happens within each agent definition. 

Below is an example of a sensor definition. For detailed descriptions of the keys and values, see
:ref:`sensor-configuration`.

.. code-block:: json

   "sensors":[
      {
         "sensor_type": "RGBCamera",
         "sensor_name": "FrontCamera",
         "socket": "socket name",
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0],
         "Hz": 5,
         "lcm_channel": "channel_name",
         "configuration": {
            "array of sensor configurations"
         }
      }
   ]
   

.. _`configure-framerate`:

Frame Rates
-----------
The frame rate in HoloOcean is controlled using two parameters: ``ticks_per_sec`` and 
``frames_per_sec``.

- ``ticks_per_sec`` changes how many ticks are in a simulation second.
   This must be higher than any "Hz" sampling rate used by any sensors. Defaults to 30.

- ``frames_per_sec`` is the max FPS the environment can run at.

   - If ``true``, it will match ``ticks_per_sec``.
   - If ``false``, FPS will not be capped, and the environment will run as fast as possible.
   - If a number is given, the simulation will attempt to reach that frame rate, but no higher. 
   - Defaults to `true`.

For running the simulation in real time (for example, when :ref:`manual-control`), set 
``frames_per_sec`` to true. For running HoloOcean :ref:`headless<headless>`, you'll likely want the 
simulation to run as fast as possible, so ``frames_per_sec`` should be set to false. When using a 
GPU, simulations can run much faster than realtime, making things difficult to control when the 
framerate is unlimited. In this case, capping ``frames_per_sec`` at a specific value can be useful.


.. _`configure-octree`:

Octree Configuration
--------------------
When using a form of sonar sensor and initializing the world, an Octree will either be
created or loaded from a cache. The parameters of these can be set using the ``env_min``,
``env_max``, ``octree_min``, and ``octree_max``. The octrees are cached in the ``Linux/Holodeck/Octrees`` folder
in the worlds folder (see :ref:`package-locations`).

``env_min``/``env_max`` are used to set the upper/lower bounds of the environment. They should 
be set in :ref:`package-structure`, but the values set here will override it.

``octree_min``/``octree_max`` are used to set the minimum/mid-level size of the octree. ``octree_min``
can go as low as .01 (1cm), and then the octree will double in size until it reaches ``octree_max``.

For more information about Octrees, see :ref:`octree`.


Other Scenario Parameters
-------------------------

- ``window_width/height`` control the size of the viewport window opened when an environment is created. 
   Sizes are in pixels. 
- ``lcm_provider`` is an optional parameter that specifies where to publish LCM messages. 
   For more detail, see :ref:`lcm`.


Accessing and Modifying Pre-Built Scenarios
===========================================

Configurations for pre-built scenarios can be found by reading the associated ``.json`` file. 
These are located in the worlds package folder (see :ref:`package-locations`). 

Sometimes it is helpful to extract specific parameters from a pre-made scenario for use within 
a Python script (ex. for plotting data). Rather than having to copy data manually from the 
``.json``, you can use the HoloOcean :ref:`packagemanager` to extract the scenario configuration. 

For example, the following code extracts the azimuth angle from the sidescan sonar sensor in the 
``OpenWater-TorpedoSidescanSonar`` scenario.

.. code-block:: python

   import holoocean

   scenario = holoocean.packagemanager.get_scenario("OpenWater-TorpedoSidescanSonar")
   sidescan_config = scenario['agents'][0]['sensors'][-1]["configuration"]
   azi = sidescan_config['Azimuth']

You may find that the provided pre-built scenarios in the :ref:`Ocean package <all-packages>` 
meet some but not all of your needs. Rather than create a new scenario from scratch, you can 
modify the pre-built scenarios to adjust specific parameters using a similar method as above. 

The code below demonstrates how to modify the ``ticks_per_sec`` parameter in the ``Pier-Hovering``
scenario:

.. code-block:: python

   import holoocean

   scenario = holoocean.packagemanager.get_scenario("Pier-Hovering")
   scenario["ticks_per_sec"] = 60

   env = holoocean.make(scenario_cfg=scenario)


.. _`custom-scenarios`:

Making Custom Scenarios
=======================

You can create custom scenarios in two ways: with a dictionary in a Python script, or by
creating a ``.json`` file. Both methods follow the same format as described in the section above.

Using a Dictionary for a Scenario Config
----------------------------------------

Create a dictionary in Python that matches the structure specified in :ref:`scenario-files`, 
and pass it in to :func:`holoocean.make` using the ``scenario_cfg`` variable.

An example is given below: 

.. code-block:: python

    import holoocean

    scenario = {
        "name": "test_rgb_camera",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 60,
        "agents": [
            {
                "agent_name": "auv0",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "RGBCamera",
                        "socket": "CameraSocket",
                        "configuration": {
                            "CaptureWidth": 512,
                            "CaptureHeight": 512
                        }
                    }
                ],
                "control_scheme": 0,
                "location": [0, 0, -10]
            }
        ]
    }

    with holoocean.make(scenario_cfg=scenario) as env:
        for _ in range(200):
            env.tick()


Using a ``.json`` file for a Scenario Config
--------------------------------------------

You can specify a custom scenario by creating a ``.json`` file that follows
the format given in :ref:`scenario-files` and either:

1. Loading it yourself in a Python script and parsing it into a dictionary, then 
   using that dictionary as described above. 
2. Placing it in HoloOcean's scenario search path.

When you give a scenario name to :func:`holoocean.make`, HoloOcean will search 
each package folder (see :ref:`package-locations`) until it finds a
``.json`` file that matches the scenario name. 

To use custom scenario ``.json`` files, place them in the Oceans package folder 
(or the package folder that contains the world your scenario uses). For details 
on package folder locations, see :ref:`package-locations`. HoloOcean 
will automatically find and use ``.json`` scenario files in the package folder.

.. warning::
   If you remove and reinstall a package, HoloOcean will clear the contents of
   that folder. Be sure to remove any custom scenario ``.json`` files from the 
   package folder before uninstalling and reinstalling a package.
