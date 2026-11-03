.. _control-schemes:

===============
Control Schemes
===============

Agents in HoloOcean can be controlled using a variety of control schemes. Control schemes determine 
how commands given to the agent are interpreted. Control schemes are specified using an integer 
value in the agent configuration file:

.. code-block:: json

   "agents":[
        {
         "agent_name": "uav0",
         "agent_type": "HoveringAUV",
         "control_scheme": 0,
        } 
    ]

Each agent has a different selection of control schemes. Some control schemes are only available on 
certain agents, due mostly to historical use, as control schemes were developed as needed for 
specific agents. 

Command are specified as either a list or numpy array of floats. The documentation for each agent 
specifies the format for the command list for each specific control scheme. 

The following is a list of control schemes commonly available for HoloOcean agents. 

.. note::
    The control scheme numbering below is used for most agents, but some agents may have fewer or 
    more control schemes available, and their numbering may be different. Be sure to check the
    :ref:`documentation page<agents>` for the agent you are using to see which control schemes
    are available and how they are numbered.


Thusters & Fins (Control Scheme 0)
==================================
Control scheme 0 is the default control scheme for most agents in HoloOcean. Most underwater and 
surface agents in HoloOcean are equipped with thrusters for propulsion, and the torpedo-style agents
use fins to steer. Aerial agents use propellors and control surfaces. This control scheme provides 
commands directly to an agent's propulsion and control actuators. Each agent's 
:ref:`documentation page<agents>` provides details on the format of the command list for this 
control scheme.

Controlling an agent using the Thrusters & Fins control scheme involves generating commands for each 
agent at each time step. :ref:`This example<manual-control>` demonstrates how to manually control 
an agent by converting keyboard inputs into commands. 


PID Controller (Control Scheme 1)
==================================
The PID control scheme enables easy waypoint navigation by implementing position control. It uses a 
simple proportional-integral-derivative controller to move the agent to a specified position in the global 
frame.

The command list for this control scheme specifies the desired position, in either [x, y] or  
[x, y, z, roll, pitch, yaw] format, depending on the agent. 

.. note::
    The PID controller is a simple implementation that directly applies accelerations to an agent, 
    instead of achieving control through its thrusters or fins. As such, the agent's movement may 
    not be realistic. 
    
    For more realistic movement, consider implementing a controller using the Thruster/Fin control 
    scheme, or implement a controller using custom dynamics.

For an example demonstrating how to use the PID controller, see :ref:`here<pd-controller_example>`.


Custom Dynamics (Control Scheme 2)
==================================
Because HoloOcean uses the Unreal physics engine, most agents move and respond to forces and torques
in a realistic manner. However, if more specific control over an agent's movement is needed, the 
Custom Dynamics control scheme allows for the implementation of custom dynamics and motion models. 
Custom dynamics can be used to model specific real-world vehicles, implement complex hydrodynamics, 
simulate water currents, and more.

The command list for this control scheme is a 6-length vector specifying the linear and angular 
accelerations to apply to the agent in the **global frame** at each step of the simulation. The user
is responsible for implementing the dynamics of the agent that generate those accelerations. These 
accelerations are integrated by the physics engine at each time step to determine the agent's
position and velocity. 

To enable total user control, all external forces and torques (including gravity, buoyancy, and 
damping) are disabled in the simulator when using the Custom Dynamics control scheme. This allows 
the user to start with a clean slate and implement their own forces and torques. Collisions are 
still enabled to ensure that the agent interacts with the environment in a realistic manner.

Dynamics should be implemented in Python, or in a package that can interface correctly with the 
HoloOcean Python package. For an example demonstrating how to use the Custom Dynamics control scheme, 
see :ref:`here<custom-dynamics-example>`.

To aid in implementing dynamics, HoloOcean comes with several "sensors" designed to provide ground-truth 
state information from the simulation. In particular, the :ref:`dynamics-sensor` was made to 
return pose, velocity, and acceleration information for the agent. Other sensors such as the 
:ref:`pose-sensor` and :ref:`velocity-sensor` can be used to return specific information. For more 
detail, visit the :ref:`sensors`.

Fossen Dynamics
---------------
In "Marine Craft Hydrodynamics and Control" by Thor Fossen, several dynamics models are presented for
different types of marine vehicles. HoloOcean has implemented the dynamics models for torpedo vehicles
from Fossen's book. These models can be used in conjunction with the Custom Dynamics control scheme 
to accurately simulate the dynamics of torpedo vehicles. For more information on how to use our 
implementation of the Fossen dynamics models, see :ref:`fossen-dynamics`.