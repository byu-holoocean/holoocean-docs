.. _develop-env:

Developing Environments
=========================

This article was loosely based on the information `here <https://github.com/BYU-PCCL/holodeck/wiki/Packaging-Project>`_.

An Unreal project needs to be packaged before it can be distributed. This 
process produces the engine executables and bundles up all of the assets that
are needed for the client to start up the engine by itself without starting it
from the editor or Visual Studio.

This process will compile the C++ code for Holodeck and "cook" the ``.uasset``
files (including blueprints!) into one large ``.pak`` file, and create the 
directory structure needed.

Adding HoloOcean Worlds
~~~~~~~~~~~~~~~~~~~~~~~~~

The finished package will only contain the worlds (called "levels" in the editor) that are added into the project. The ``holoocean`` repo only contains the example level. You can 
create new worlds by simply making a new level in unreal engine editor. See the `Unreal Engine documentation <https://docs.unrealengine.com/4.27/en-US/Basics/Levels/HowTo/WorkWithLevelAssets/>`_ for
more information.


.. note::
    
    Because the other packaged worlds distributed with HoloOcean contain purchased assets, they are only available to official BYU FRoStLab members. Others will have to develop their own worlds in the holoocean repo.

Cooking Content
~~~~~~~~~~~~~~~~
When you are running ``holodeck-engine`` from Visual Studio, you may need to cook
the content to "refresh" the assets, levels, and blueprints that 
``holodeck-engine`` reads. 

**From Unreal Editor:**

File ➡ Cook Content for Windows/Linux

Packaging holodeck-engine
~~~~~~~~~~~~~~~~~~~~~~~~~

**From Unreal Editor:**

1. File ➡ Package Project ➡ Windows x64/Linux

.. image:: images/package-project.png

2. Select an output folder
    
   I usually pick "dist" inside the root of the ``holodeck-engine`` repo

Place in install directory
~~~~~~~~~~~~~~~~~~~~~~~~~~


In order to be able to call ``holodeck.make()``, you will need to place the 
packaged engine in :ref:`package-locations`.

Make sure the version in the path matches the output of the 
``holdoeck.util.get_holodeck_version`` command.

1. Copy contents of ``dist`` folder into the package path found above.
   
   .. code::

    + worlds
    |--+ PackageName
        |-- config.json
        |-- WorldName-ScenarioName.json
        |--+ LinuxNoEditor (output from dist folder)
            | UE4 build output

2. Copy configurations from ``holodeck-configs`` following the file structure above.
   
   **IMPORTANT** The ``config.json`` file is written for Linux, and must be edited to work in windows.
   Edit the ``platform`` and ``path`` fields to the following:
   
    ``"platform": "windows"``
   
    ``"path": "WindowsNoEditor/Holodeck/Binaries/Win64/Holodeck.exe"``

Note on creating environment objects and Sonar:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sonar simulation relies upon the collision mesh for objects when generating the octree. If 
the collision mesh of an object is coarser than the visual mesh then the representation of
that object in a sonar image will be inaccurate. This issue can be addressed for the objects
by using the Unreal Engine editor and setting the “Collision Complexity” option in the 
details section of the static mesh editor to “use complex collision as simple”.
 