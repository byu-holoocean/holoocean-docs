.. _`agent-configuration`:

===================
Agent Configuration
===================

HoloOcean agents are declared in a list in the scenario dictionary. Each agent is defined using a
new dictionary in the list.

.. note::
   The first agent in the ``agents`` array is the "main agent".

.. code-block:: json

   "agents":[
      {
         "agent_name": "uav0",
         "agent_type": "{agent types}",
         "sensors": [
            "array of sensor objects"
         ],
         "location": [1.0, 2.0, 3.0],
         "rotation": [1.0, 2.0, 3.0],
         "location_randomization": [1, 2, 3],
         "rotation_randomization": [10, 10, 10],
         "control_scheme": "{control scheme type}",
      },
      { 
         "agent_name": "uav1",
         ...
      }
   ]

Below is a description of the keys in the agent dictionary:


Agent Name
==========
``agent_name`` is a string that specifies the name of the agent. This name is used to identify the 
agent when interacting with the environment.


Agent Type
==========
``agent_type`` is a string that specifies the type of agent. This table gives the current valid 
arguments for ``agent_type``:

=========================== ========================
Agent Type                  String in agent_type
=========================== ========================
:ref:`hovering-auv-agent`   ``HoveringAUV``
:ref:`surface-vessel-agent` ``SurfaceVessel``
:ref:`torpedo-auv-agent`    ``TorpedoAUV``
:ref:`coug-uv-agent`        ``CougUV``
:ref:`blue-rov-agent`       ``BlueROV2``
:ref:`sphere-agent`         ``Sphere``
:ref:`turtle-agent`         ``TurtleAgent``
:ref:`fixed-wing-agent`     ``FixedWing``
:ref:`uav-agent`            ``UAV``
=========================== ========================

Details on each agent can be found at the individual agent pages in :ref:`agents`. This list will 
be updated as more agents are added to HoloOcean.


Sensors
=======
``sensors`` is an array of sensor objects that are attached to the agent. Each sensor is defined 
using a new dictionary in the list. For details on configuring and using sensors, see 
:ref:`sensor-configuration`.


Location and Rotation
=====================
These keys define the location and orientation of the agent in the world, measured in meters and 
degrees respectively. The location is in the format ``[dx, dy, dz]`` and the rotation is 
``[roll, pitch, yaw]``, rotated about XYZ fixed axes, ie R_z R_y R_x.

.. note::
   - Location uses HoloOcean world coordinates, not Unreal Engine level coordinates! 
   - HoloOcean coordinates are **right handed** in meters. 
   - See :ref:`units-and-coordinates` for details. 


.. _`location-randomization`:

Location Randomization
======================
``location_randomization`` and ``rotation_randomization`` are optional. If provided, the agent's 
start location and/or rotation will vary by a random amount sampled uniformly from the specified 
range. Randomization in each direction is sampled independently. 

The location randomization value is measured in meters, in the format ``[dx, dy, dz]``. The rotation 
randomization is in the format ``[roll, pitch, yaw]``, rotated about the XYZ fixed axes (i.e. 
R_z*R_y*R_x).


Control Scheme
==============
``control_scheme`` is a string that specifies the control scheme (represented as an integer) used 
by the agent.

Control schemes determine how commands sent to the agent are interpreted. Most agents have a control 
scheme that exposes their thrusters, fins, and so forth to direct commands. Other control schemes 
implement convenient features, such as position PID controllers. A Custom Dynamics control scheme 
is available for users to fine-tune the motion of the vehicle. 

For more details on control schemes, see :ref:`control-schemes`.
