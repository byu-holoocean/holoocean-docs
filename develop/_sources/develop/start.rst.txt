.. _develop-start:

Getting Started
=====================

While unreal development is possible on Linux, I've found working on Windows to be much more straightforward and stable. Regardless of which one you use, you'll need the following dependencies:

* `Unreal Engine 4.27 <https://docs.unrealengine.com/4.27/en-US/Basics/InstallingUnrealEngine/>`_
* `Visual Studio 2019 <https://visualstudio.microsoft.com/vs/older-downloads/>`_ -- See UE `documentation <https://docs.unrealengine.com/4.26/en-US/ProductionPipelines/DevelopmentSetup/VisualStudioSetup/>`_ for setup
* git
* Some sort of python installation (conda is my preferred)

Cloning 
~~~~~~~~~~
For running holoocean live, you'll need to setup both the C++ and python portions of HoloOcean, which are now conveniently in the same repo.

 * Clone `holoocean <https://bitbucket.org/frostlab/holoocean>`_.
 * Navigate into that directory.
 * Checkout to the branch you want to develop on, likely the develop branch, which you can access through ``git checkout develop``, 

   * Alternatively create your own new branch for the feature or addition through ``git checkout -b [your branch name] [the branch you want to branch off of]``
 
You can now install the python package by running ``pip install -e client/``.


Opening & Prepping Project 
~~~~~~~~~~~~~~~~~~~~~~~~~~
Inside of your cloned repo in the engine directory, there is a holodeck.uproject file. Double click it, and choose "4.27" if an engine version dialog opens up, click "yes" to any dialog that says "Would you like to rebuild them now?", and then unreal should pop open!

There's many ways to develop in unreal, but we're going to focus on how I've found is the easiest way to development code.

In the Unreal Editor, go to File -> Cook Content for {Platform}. After a few minutes you should get a success popup in the lower right.

Setting up VSCode 
~~~~~~~~~~~~~~~~~~~~
I'm not a fan of the Visual Studio IDE, and instead prefer to use VSCode. If VSCode is installed and you want to do this as well, do the following:

* In Unreal Editor, Go to Edit -> Editor Preferences
* Then go to General -> Source Code -> Source Code Editor and select Visual Studio Code
* Once this is done you should now be able to generate a new Visual Studio Code project  using File -> Generate Visual Studio Code Project
* To open up Visual Studio Code go to File -> Open Visual Studio Code

Compiling 
~~~~~~~~~~
I generally compile by clicking the big "Compile" button in Unreal Editor. Do this anytime you make changes to your code. There's also a way to compile in Visual Studio if you wish.

The compile button is on the top toolbar next to 'cinematics' and 'build'. It might be hidden if your screen isn't wide enough. Click the double arrow to scroll to the right.

Launching Game Live 
~~~~~~~~~~~~~~~~~~~~
To avoid having to package the project anytime you want to see changes to your code, you can play the game live from Unreal Editor and then attached your python code to it. This is a multi-step process, as follows.

.. note::
   
   If developing a sonar module, in UE4 click the down arrow next to the "Play" button in the top toolbar, and click "Advanced Settings". Add the following line to "Additional Launch Parameters"

   .. code::

      -EnvMinX=-1000 -EnvMinY=-1000 -EnvMinZ=-1000 -EnvMaxX=1000 -EnvMaxY=1000 -EnvMinZ=1000 -OctreeMin=0.02 OctreeMax=5


   These are all in meters. Tweak them as you need, they're all pretty self-explanatory.

Open and prep a python script similar to the following

.. code:: python

   from holoocean.environments import HoloOceanEnvironment

   config = {
         "name": "test",
         "world": "ExampleLevel",
         "main_agent": "auv0",
         "agents": [
               {
                  "agent_name": "auv0",
                  "agent_type": "HoveringAUV",
                  "sensors": [
                     {
                           "sensor_type": "LocationSensor",
                     }
                  ],
                  "control_scheme": 1,
                  "location": [0, 0, 1]
               }
         ]
      }

   command = [0, 0, 0, 0, 0, 0, 0, 0]
   with HoloOceanEnvironment(scenario=config, start_world=False) as env:
      for _ in range(1000):
         state, reward, terminal, _ = env.step(command)

Tweak it to put the sensors/agents you need in as you see fit.

* Have some way to run this python file open and ready
* Back in Unreal Editor, click the arrow next to the "Play" button in the top toolbar, and select "Standalone Game". A seperate window should pop open with the unreal game.
* Once this window pops open, run your python script. It will attach to the new open unreal game window and proceed as a normal holoocean simulation. Note you may have to try to run your script a couple of times, the unreal game window takes a second to load.

That's it! There's a few weird quirks to keep an eye out for here as well. If you close the unreal game window before exiting the python script, your terminal will freeze and you'll have to open a new one. I have a small .bat script that runs the python file that I have pinned to my taskbar to get around this.
Alternatively, VSCode's play button works rather smoothly as well for quickly opening/closing terminals with the correct conda environment.

Logging 
~~~~~~~~~~ 
While definitely not the best way to do things, I generally use the unreal equivalent of print statements to debug my code. [https://unrealcommunity.wiki/logging-lgpidy6i Here's a good tutorial on sending things to the unreal log.]

This log will be saved in holoocean-engine/Saved/Logs if you want to see it later, or, I prefer this way. In Unreal Editor,

* Go to Window -> Developer Tools -> Session Frontend
* Under "My Sessions" your unreal game window will have an entry, and in it all it's log will be listed.

Easy Peasy!


See :ref:`develop-agents`, :ref:`develop-sensor`, and :ref:`develop-env` for information on developting custom sensors/agents/env and how to get started on those.

For developing a custom sonar, see the ``HolodeckSonarSensor.h`` and ``HolodeckSonarSensor.cpp`` files for the required superclass, and ``ImagingSonarSensor.h`` and ``ImagingSonarSensor.cpp`` for examples on how to use them.