.. _`agents`:

================
HoloOcean Agents
================

Agents are the entities that interact with the environment in HoloOcean. They are defined in the 
scenario configuration file. Agents are equipped with sensors that collect data from the environment. 
Agents are controlled by passing commands using ``env.act()`` or ``env.step()``, which are 
interpreted by the agent's control scheme. 

.. code-block:: python

   import holoocean

   scenario = {
      "name": "{Scenario Name}",
      "world": "{world it is associated with}",
      "package_name": "{package it is associated with}",
      "agents":[
         {
            "agent_name": "uav0",
            "agent_type": "{agent types}",
            "location": [1.0, 2.0, 3.0],
            "control_scheme": 0,
            "sensors": [
               { ... }
            ]
      ],
   }
   
   env = holoocean.make(scenario_cfg=scenario)

   command = [0, 0, 0, 0, ...]

   for range(100):
      env.step(command)


HoloOcean provides a variety of agents, each with different capabilities. The three primary 
agents in HoloOcean representing the three most common water vehicles are the 
:ref:`HoveringAUV<hovering-auv-agent>`, :ref:`SurfaceVessel<surface-vessel-agent>`, and 
:ref:`TorpedoAUV<torpedo-auv-agent>`. These three agents can perform the majority of navigation and 
sensing tasks. Other agents representing aerial vehicles and specific real-world vehicles are also 
available.

For information on developing custom agents in HoloOcean, see :ref:`Developing Agents<develop-agents>`.


Using Agents
============

Documentation on how to use agents in HoloOcean:

.. toctree::
   :maxdepth: 1

   docs/agent-config
   docs/control-schemes
   docs/fossen-based-dynamics


.. _`agent-pages`:

HoloOcean Agents
================

Documentation on specific agents available in HoloOcean. Note that the Test agents don't apply gravity.

Underwater Agents
-----------------
.. toctree::
   :maxdepth: 1
   :glob:

   agents/hovering-auv-agent
   agents/torpedo-auv-agent
   agents/blue-rov-agent
   agents/coug-uv-agent

Water Surface Agents
--------------------
.. toctree::
   :maxdepth: 1
   :glob:

   agents/surface-vessel-agent

Test Agents
-----------
.. toctree::
   :maxdepth: 1
   :glob:

   agents/turtle-agent
   agents/sphere-agent

Aerial Agents
-------------
.. toctree::
   :maxdepth: 1
   :glob:

   agents/uav-agent
   .. agents/fixed-wing-agent commenting out fixed wing for now

