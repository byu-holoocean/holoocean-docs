Getting Started & Examples
==========================
First, see :ref:`installation` to get the ``holoocean`` package and 
``Ocean`` installed.

A minimal HoloOcean usage example is below:

::

   import holoocean
   import numpy as np

   env = holoocean.make("PierHarbor-Hovering")

   # The hovering AUV takes a command for each thruster
   command = np.array([10,10,10,10,0,0,0,0])

   for _ in range(180):
      state = env.step(command)


Notice that:

1. You pass the name of a :ref:`scenario<scenarios>` into ``holoocean.make``
   
   See :ref:`all-packages` for all of the different worlds and scenarios that
   are available.
2. The interface of HoloOcean is designed to be familiar to `OpenAI Gym`_

.. _`OpenAI Gym`: https://gym.openai.com/

You can access data from a specific sensor with the state dictionary:

::

   dvl = state["DVLSensor"]

**That's it!** HoloOcean is meant to be fairly simple to use. 

Check out the different
:ref:`worlds<all-packages>` that are available, read the 
:ref:`API documentation<holoocean-api-index>`, or get started on making your own
custom :ref:`scenarios<scenarios>`.

Below are some snippets that show how to use different aspects of HoloOcean.

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :glob:

   examples/*


There is also an `examples.py`_ in the root of the `holoocean repo`_ with more 
example code.

.. _`examples.py`: https://bitbucket.org/frostlab/holoocean/src/master/example.py

.. _`holoocean repo`: https://bitbucket.org/frostlab/holoocean
