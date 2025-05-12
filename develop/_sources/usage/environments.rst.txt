.. _`environments`:

============
Environments
============

HoloOcean simulations defined by a scenario are run in an environment object. The environment 
object provides methods to interact with agents and progress the simulation, and returns the 
state of the simulation after each progression.


HoloOcean Make
==============

HoloOcean environments are created by calling ``holoocean.make()``. The function takes as input 
the name of a scenario, which defines the world, agents, sensors, and so on. If using pre-built 
scenarios, the name of the scenario is passed as a string:

.. code-block:: python

    env = holoocean.make("PierHarbor-Hovering")

If using a custom scenario without a ``.json`` file, the scenario object is passed directly:

.. code-block:: python

    scenario = {
      "name": "{Scenario Name}",
      "world": "{world it is associated with}",
      "package_name": "{package it is associated with}",
      "agents":["array of agent objects"]
    }
    env = holoocean.make(scenario_cfg=scenario)

``holoocean.make()`` returns an environment object that you can interact with.

.. note::

    ``holoocean.make()`` is the easiest way to create an environment object and enables the use of
    pre-built scenarios. It builds the binary paths from the provided string and creates a 
    ``HoloOceanEnvironment`` object. If you want to create an environment object without using
    pre-built scenarios, you can create a ``HoloOceanEnvironment`` object directly, though this is 
    not recommended for most users.

For a full list of inputs to ``holoocean.make()``, see the :ref:`API documentation<holoocean-api-index>`.

.. _`step`:

Act, Tick, and Step
===================

The simulation defined in an Environment object is progressed in two steps:

1. ``.act(command, agent)`` takes as input a command and the name of a target agent, and provides that 
command to the agent. ``act`` does not progress the simulation, but rather queues the
command to be executed on the next tick. For details on the formats of the commands and agent inputs, 
see :ref:`agents`. 

.. note::

    After calling ``.act()``, the same command will continue to be supplied to the designated agent 
    at each tick of the simulation. To change the command, just call ``.act()`` again.

2. ``.tick()`` progresses the simulation by one step. Any queued commands from ``act()``
are executed, and the simulation is updated. ``tick()`` returns the state of the simulation. 

We provide a convenience function, ``.step(command, agent)``, that combines ``.act()`` and 
``.tick()``. It does the following: 

- takes a command as input,
- provides that command to the **main agent only**,
- ticks the simulation, and
- returns the state of the simulation. 

``.step()`` is the primary mode of interaction for single-agent scenarios. For multi-agent 
scenarios, use ``.act()`` multiple times to provide commands to each agent, then call ``.tick()`` 
to progress the simulation. 

.. This could potentially be expanded into its own section with examples/detail

The state returned from ``.tick()`` and ``.step()`` is a dictionary from agent name to sensor 
dictionary. The sensor dictionary contains the sensor data for that agent.



