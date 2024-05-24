Package Structure
=================

A holoocean package is a ``.zip`` file containing a build of `holoocean-engine`_
that contains worlds and :ref:`scenarios` for those worlds.

.. _`holoocean-engine`: https://bitbucket.org/frostlab/holoocean-engine

A package file is platform specific, since it contains a compiled binary of
HoloOcean.

.. _`package-contents`:

Package Contents
----------------

The ``.zip`` file must contain the following elements

1. A build of `holoocean-engine`_

2. A ``config.json`` file that defines the worlds present in the package

3. Scenario configs for those worlds

.. _`package-structure`:

Package Structure
-----------------

The package.zip contains a ``config.json`` file at the root of the archive, as
well as all of the scenarios for every world included in the package. The
scenario files must follow the format ``{WorldName}-{ScenarioName}.json``.

::

   +package.zip
   +-- config.json
   +-- materials.csv
   +-- WorldName-ScenarioName.json
   +-- LinuxNoEditor
       + UE4 build output

config.json
-----------

This configuration file contains the package-level configuration. Below is 
the format the config file is expected to follow:

``config.json``:

.. code-block:: json

   {
      "name": "{package_name}",
      "platform": "{Linux | Windows}",
      "version": "{package_version}",
      "path" : "{path to binary within the archive}",
      "worlds": [
         {
            "name": "{world_name}",
            "pre_start_steps": 2,
            "env_min": [-10, -10, -10],
            "env_max": [10, 10, 10]
         }
      ]
   }

The ``"pre_start_steps"`` attribute for a world defines how many ticks should 
occur before starting the simulation, to work around world idiosyncrasies.

The ``env_min``/``env_max`` attributes are used to set the upper/lower bounds of the environment,
used when an octree is made for a sonar sensor.

materials.csv
--------------

This file contains acoustic properties of the materials found in the environments, used for
computation of the sonar images. Below is the format the config file is expected to follow:

.. code-block::

   Material, Density kg/m^3, Speed of Sound m/s
   M_Landscape, 3200, 4500
   M_URockA, 3000, 5000

At the start of each simulation, this file is read so that it can be edited without needing to recompile the entire unreal binary.
The first line is ignored, and is just used for reference when editing the file. The first column
is the name of the material in UE4, the second is the material density in kg/m^3, and the third
is the speed of sound in m/s. These are used to compute the acoustic intensity of the various materials
found in the environment.

Note if a material is found in the environment that isn't found in the ``.csv`` file, it will be appended
to the csv file with a default density and speed of sound of 10,000 (which results in full acoustic reflection).
