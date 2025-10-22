===============
Getting Started
===============

First, see :ref:`installation` to get the ``holoocean`` package and 
``Ocean`` installed.

A minimal HoloOcean usage example is below:

::

   import holoocean
   import numpy as np

   env = holoocean.make("PierHarbor-Hovering")

   # The hovering AUV takes a command for each thruster
   command = np.array([10,10,10,10,0,0,0,0])

   for _ in range(2000):
      state = env.step(command)
   print("Finished!")


Notice that:

1. You pass the name of a :ref:`scenario<scenarios>` into ``holoocean.make``. The scenario 
defines a world, the agents in it, the sensors on the agents, and so on. ``holoocean.make``
returns an environment object that you can interact with.
   
   See :ref:`all-packages` for all of the different worlds and pre-built scenarios that
   are available, or make your own custom scenario.

2. You pass a command to the environment object with ``env.step``. The command is passed to the 
agent in the world, and the environment is updated. The environment returns a dictionary of the 
state of the world after the update, including sensor data. 

   You can access data from a specific sensor with the state dictionary:
   ::

      dvl = state["DVLSensor"]

**That's it!** HoloOcean is meant to be fairly simple to use. 

Check out the different :ref:`worlds<all-packages>` that are available, read the 
:ref:`API documentation<holoocean-api-index>`, or get started on making your own
custom :ref:`scenarios<scenarios>`.
