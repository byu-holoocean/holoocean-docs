.. _fossen-dynamics:

=====================
Fossen-Based Dynamics
=====================

Dynamics for underwater and surface vehicles can be modeled using equations of motion derived in 
Thor Fossen's *Handbook of Marine Craft Hydrodynamics and Motion Control*. Implementations of these 
dynamics are conveniently provided by Fossen at his 
`GitHub repository <https://github.com/cybergalactic/PythonVehicleSimulator>`_. We have ported some 
of Fossen's implementations into HoloOcean to enable accurate vehicle dynamics simulations.

Using Fossen-based dynamics in HoloOcean is an extension of the Custom Dynamics control scheme. To use the
built-in Fossen dynamics, there are just a few steps to configure these improved underwater vehicle dynamics. 
Here is a summary of the steps to set up Fossen dynamics in HoloOcean with
a more detailed explanation and examples in the next sections:

1. In the scenario configuration, in the agent dictionary, set the 'fossen_model' key to the matching 
   Fossen dynamics class. The available Fossen dynamics classes are listed in the `Fossen Vehicle Classes` section below.
2. In the agent dictionary, set the `control_scheme` key to the value for custom dynamics for the agent (see :ref:`control-schemes`)
3. Setup a Dynamics Sensor in the agent's sensors list. This sensor is required to read the vehicle state and 
   apply the dynamics model. 
4. Optionally, you can set the `dynamics`, `actuator`, and `autopilot` parameters in the agent 
   configuration. These parameters define the vehicle's dynamics, control surfaces, and autopilot 
   settings. This is only supported for Fossen dynamic models with a defined configure_from_scenario function defined.
5. Finally, create a FossenInterface manager object in your simulation script, passing the list of agent names and the scenario configuration.
   This class is implemented in `client/src/fossen_dynamics/fossen_interface.py`.


Fossen Vehicle Classes
======================
Currently, we have implemented the dynamics models for two vehicle classes:

There is a list of keys that are connected to the Fossen dynamics models. This is defined in the ``FossenInterface`` class.

- Torpedo (``Torpedo: "torpedo"``)
    This class implements the dynamics equations for a torpedo-like vehicle, including the necessary parameters and methods to 
    calculate accelerations based on control inputs to fins and a single propellor. 
    Default Fossen vehicle parameters are currently tuned to approximate the REMUS100 vehicle, as described by Thor Fossen.

    Control Modes:
        - manualControl: Manually set the commanded control surfaces (fins and propellor)
        - depthHeadingAutopilot: Set the depth, heading, and propellor RPM goals which will be handled by the controller

- Otter (``Otter: "otter"``)
    This class implements the dynamic equations for a surface vessel with two propellors at back of the ship. The vehicle does not
    support to configure the parameters yet from the scenario. 
    Default vehicle parameters match the Otter surface vessel.
    
    Control Modes:
        - manualControl: Manually set the commanded control surfaces (propellors)
        - headingAutopilot: Not verfied yet by HoloOcean developers. Likely works but with the NED reference frame instead of NWU.

.. note::
    The Unreal Engine graphics asset is not linked to the fossen model. 
    The number of fins shown on the vehicle will not change in Unreal Engine when changing between 
    child classes.

    Implementing Fossen dynamics does not change the asset, so the fins will not visibly move when 
    the simulation is running. 

.. note::
    Mass and other default vehicle parameters set in the HoloOcean engine are ignored when using 
    the "Custom Dynamics" control scheme. The Fossen models account for these separately.


.. Adding Custom Fossen Dynamics
.. -----------------------------
.. Users can add their own custom Fossen dynamics models for different types of vehicles by creating a 
.. new class. 

.. Dynamics model classes must have the following methods and attributes:

.. - `__init__`: This method should initialize the vehicle parameters and set up the dynamics model.

.. - `dynamics`: This method should implement the dynamics equations for the vehicle. It should take in 
..   the current state of the vehicle (eta, nu) and the control input, and return the accelerations in 
..   the NWU frame.

.. The model can also implement other functions as desired, such as controllers and plotting functions. 
.. We recommend using a `controlMode` attribute to define the control scheme for the vehicle. 

.. See the `TAUV` class for an example of how to implement a custom dynamics model.

Importing Models from PythonVehicleSimulator
============================================
If a user has developed a dynamics model class using Thor Fossen's PythonVehicleSimulator and would 
like to use it in HoloOcean, they must make the following changes: 

- Move the fossen model file into the `client/src/holoocean/fossen_dynamics` folder 

- In the fossen model file:

    - Change the following import statements:
        ``python_vehicle_simulator.lib`` to ``holoocean.fossen_dynamics``
        ``python_vehicle_simulator.lib.gnc`` to ``holoocean.fossen_dynamics.helper_functions``


    - The `dynamics` method must be changed to return nu_dot (body frame accelerations) instead of nu (body frame velocities). 

    - Add a class variable ``config_fnc`` that is either set to ``None`` or a function that takes a scenario configuration and modifies the class parameters based on the scenario configuration. See the `client/src/holoocean/fossen_dynamics/torpedo.py`  ``configure_torpedo_from_scenario`` function for an example of how to implement this function.

-  In the `client/src/holoocean/fossen_dynamics/fossen_interface.py` file:

    - Add an import statement to import the fossen model class

    - Add the class to the fossen model key pairs 

Be sure that all other methods and attributes are implemented as expected by the FossenInterface
manager.

Single Agent Fossen Dynamics Example
====================================
In this section we will step through the key elements of our Fossen dynamics implementation and give 
an example of using Fossen dynamics in HoloOcean. The full code can be found in `client/example.py`.

Configuration
-------------
Setting up a HoloOcean simulation that uses Fossen dynamics begins with the scenario configuration.
The scenario configuration follows the standard HoloOcean format, with a few key differences for Fossen dynamics:

- Dynamics Sensor: 
    When configuring the main agent, you must include the DynamicsSensor in the list of sensors. 
    The configuration block should include `UseRPY: False` (default is True; this forces the 
    dynamics to use quaternions instead of Euler angles) and `UseCOM: True` (default is True).

- Fossen Model:
    The `fossen_model` key must be set to the name of the Fossen dynamics class you want to use. 
    For example, for the Torpedo dynamics, set `fossen_model: "torpedo"`.

- Control Scheme:
    The `control_scheme` key must be set to value for Custom Dynamics to enable the Fossen dynamics model.

- Control Mode (optional):
    The `control_mode` key can be set to the desired control mode for the vehicle. 
    For example, you can set it to `depthHeadingAutopilot` for a depth and heading autopilot or 
    `manualControl` for manual control of the fins and propellor.

- Parameters (optional):
   The parameters `dynamics`, `actuator`, and `autopilot` can be added to the agent 
   configuration if the configuration function is implemented. 
   Each of these is a dictionary that overwrites the default vehicle parameters.
   The definitions of each dynamics parameters for supported vehicles is defined in the function. 

Below is an example torpedo vehicle scenario configuration that defines all the parameters (matching the default values for the torpedo) 
for the Torpedo class. A full description of each parameter can be found in the API documentation for the
Fossen dynamics classes.

.. code-block:: python

    scenario = {
        "name": "torpedo_dynamics",
        "package_name": "Ocean",
        "world": "OpenWater",
        "main_agent": 'auv0',
        "agents": [
            {
                "agent_name": 'auv0',
                "agent_type": "CougUV",
                "sensors": [
                    {
                        "sensor_type": "DynamicsSensor",
                        "configuration": {
                            "UseCOM": True,
                            "UseRPY": False  # Use quaternion for dynamics
                        }
                    },
                ],
                "control_scheme": 1,  # Control scheme 1 is how custom dynamics are applied to CougUV agents
                "location": [0, 20, -280],
                "rotation": [0, 0, 0],
                "fossen_model": "torpedo",  # Fossen dynamics model class to use
                "control_mode": "depthHeadingAutopilot",  # Initial control mode
                "dynamics": {
                    "rho":          1026,   # Density of water in kg/m^3
                    # Vehicle physical parameters:
                    "mass":         31.03,     # Mass of vehicle in kg
                    "length":       1.6,    # Length of vehicle in m
                    "diam":         0.19,   # Diameter of vehicle in m
                    "r_bg": [0, 0, 0.02],   # Center of gravity of the vehicle (x, y, z) in body frame x forward, y right, z down
                    "r_bb": [0, 0, 0],      # Center of boyancy of the vehicle (x, y, z) in body frame x forward, y right, z down
                    "area_fraction": 0.7,   # relates vehicle effective area to length and width. pi/4 for a spheroid
                    
                    # Low-speed linear damping matrix parameters:
                    "T_surge":      20,     # Surge time constant (s)
                    "T_sway":       20,     # Sway time constant (s)
                    "zeta_roll":    0.3,    # Roll damping ratio
                    "zeta_pitch":   0.8,    # Pitch damping ratio
                    "T_yaw":        1,      # Yaw time constant (s)
                    "K_nomoto":     0.25,   # Nomoto gain
                    
                    # Other damping parameters:
                    "r44":          0.3,    # Added moment of inertia in roll: A44 = r44 * Ix
                    "Cd":           0.42,   # Coefficient of drag
                    "e":            0.7,    # Oswald efficiency factor for vehicle drag
                },
                "actuator":{
                    # Fins: 
                    "fin_count": 4,         # Number of equally spaced fins on the vehicle
                    "fin_offset_deg": 0,    # Angle offset of first fin around x axis (deg) starting from positive y with z down
                                            # 0 deg: fin on port side 
                                            # 90 deg: fin on bottom
                    "fin_center":   0.1,    # radius (m) from COP on the fin to the COM in the YZ plane
                    "fin_area":     0.00697, # Surface area of one side of a fin
                    "x_fin":       -0.8,    # Body frame x distance (x forward) from center of mass to fin COP
                    "CL_delta":     0.5,    # Coefficient of lift for fin
                    "deltaMax_fin_deg": 15, # Max deflection of the fin (degrees)
                    "T_delta":      0.1,    # Time constant for fin actuation. (s)

                    # Propellor:
                    "nMax":         1525,   # Max rpm of the thruster
                    "T_n":          1.0,    # Time constant for thruster actuation. (s)
                    "D_prop":       0.14,   # Propeller diameter
                    "t_prop":       0.1,    # Propeller pitch
                    "KT_0":         0.4566, # Thrust coefficient at zero rpm
                    "KQ_0":         0.0700, # Torque coefficient at zero rpm
                    "KT_max":       0.1798, # Max thrust coefficient
                    "KQ_max":       0.0312, # Max torque coefficient
                    "w":            0.056,  # wake fraction number
                    "Ja_max":       0.6632, # Max advance ratio
                },
                "autopilot": {
                    'depth': {
                        'wn_d_z':   0.12,    # Damped natural frequency for low pass filter for depth commands
                        'Kp_z':     0.153,    # Proportional gain for depth controller
                        'T_z':      100,    # Time constant for depth controller
                        'Kp_theta': 39.78,    # Proportional gain for pitch angle for depth controller
                        'Kd_theta': 17.1,    # Derivative gain for pitch angle for depth controller
                        'Ki_theta': 0.5,    # Integral gain for pitch angle for depth controller
                        'wn_d_theta': 0.25,    # Damped natural frequency for low pass filter for depth commands
                        'K_w':      0.0,    # Optional heave velocity feedback gain
                        'theta_max_deg': 15, # Max output of pitch controller inner loop
                        'outer_loop_threshold': 2.91, # Threshold for outer loop to switch to surge control
                        'surge_threshold': 0.6, # Surge threshold for running depth controller. 
                    },
                    'heading': {
                        'wn_d':     0.4,    # Damped natural frequency of input commands for low pass filter
                        'zeta_d':   1.0,    # Damping coefficient
                        'r_max':    0.87,    
                        'lam':      0.1,    
                        'phi_b':    0.1,    
                        'K_d':      0.5,    
                        'K_sigma':  0.05,   
                    }
                }
            }
        ]
    }


Simulation Setup
----------------
The setup for the simulation is similar to other HoloOcean :ref:`examples`. 

Simulation setup proceeds first by setting up an environment. We create a list of the names of agents in our 
scenario that will be controlled by the Fossen dynamics. The list of 
fossen agent names and scenario configuration are passed to the Fossen Interface.
Finally, we initialize a NumPy array of length 6 for linear accelerations (x, y, z) 
and angular accelerations (about axis x, y, z), all in the global NWU frame.

.. code-block:: python

    import holoocean
    from holoocean.fossen_dynamics import *
    import numpy as np
    
    scenario = {...} # See above for scenario configuration

    env = holoocean.make(scenario_cfg=scenario)
    
    # Initialize Fossen dynamics model for the agent
    fossen_agents = ['auv0'] # List of names of the agents that will use Fossen dynamics
    fossen_interface = FossenInterface(fossen_agents, scenario)
    accel = np.array(np.zeros(6), float)  # Initialize HoloOcean acceleration input 


.. note::
    If you are running the simulation live with the Unreal Editor in Standalone mode, be sure to 
    change the additional launch parameters as described in :ref:`develop-start`. Add the launch 
    parameter `-TicksPerSec` to match what is in the Python script for consistent timing.


Manual Control Example
----------------------
To use the manual control method, configure the vehicle mode with the fossen interface to "manualControl" mode. 
The commanded fin angles can also be set using the Fossen interface.

The length of the `u_control` array is defined in the dynamic model class. It represents the number 
of command inputs.

- Fin angles should be given in radians. The example below shows how to convert fin angles from 
  degrees to radians using numpy.
- A positive fin deflection is represented by the right hand rule with a positive rotation about the Z axis. 
  The positive Z axis extends out of the vehicle from the center body frame x axis towards the COP of the fin.

A custom controller can be used with this manual control method to input specific fin commands.

.. code-block:: python

    fossen_interface.set_control_mode('auv0', 'manualControl')
    fins_degrees = np.array([10, 10, -10, -10])  # Fin deflections in degrees
    fin_radians = np.radians(fins_degrees)
    thruster_rpm = 800  # not a percent: check the vehicle dynamics for the max RPM
    u_control = np.append(fin_radians, thruster_rpm)  

To tick the environment, call the `step` function and pass it a list of accelerations. Next, 
send control commands to the surfaces using the set_u_control function on the FossenInterface object. 
It is not required to set the `u_control` every tick. If you want to change the control 
surfaces every tick, set the control command before calling update.

The `FossenInterface.update` function takes in the state returned from HoloOcean and parses the data 
from the Dynamics Sensor. Given the state of the vehicle and control surface inputs, it calculates 
an output of accelerations in the HoloOcean frame (NWU).

.. code-block:: python

    for i in range(1500):
        state = env.step(accel)
        fossen_interface.set_u_control('auv0', u_control)  # If desired, you can change the control command here
        accel = fossen_interface.update('auv0', state)  # Calculate accelerations to be applied to HoloOcean agent


Depth and Heading Control Example
---------------------------------

A common control strategy for underwater vehicles is to control depth and heading separately. This
can be done by setting the control mode to `depthHeadingAutopilot` and setting the goal depth, 
heading, and thruster RPM.

The depth goal is defined in meters. A positive depth corresponds to a negative z location, with 
depth increasing the further the vehicle descends.

The heading goal is given in the global frame. It ranges from -180 to 180 degrees, with 0 degrees 
being north (along the positive x-axis) and 90 degrees being West (along the positive y axis).

The thruster goal is given directly as RPM, not as a percentage of the maximum RPM. Be sure to 
check the max RPM in the Fossen vehicle configuration to ensure the command is below the maximum.

.. warning::
    When switching to the autopilot control mode more than once there is a possibility of irregular behavior
    from the autopilot not setting the LP initial position to the current position. This is a known issue
    and will be fixed in a future release.

.. code-block:: python 

    depth_goal = 279 # meters
    heading_goal = -10 # degrees
    thruster_goal = 1525 # RPM

    fossen_interface.set_control_mode('auv0', 'depthHeadingAutopilot')
    fossen_interface.set_goal('auv0', depth_goal, heading_goal, thruster_goal)

    # Run simulation
    for i in range(1500):
        state = env.step(accel)
        accel = fossen_interface.update('auv0', state)

        # Optional arrow visualization (for direction of heading and depth goal)
        pos = state['DynamicsSensor'][6:9]  # [x, y, z]
        x_end = pos[0] + 3 * np.cos(np.deg2rad(heading_goal))
        y_end = pos[1] + 3 * np.sin(np.deg2rad(heading_goal))

        color = [0, 255, 0] if abs(depth + pos[2]) <= 2.0 else [255, 0, 0]
        env.draw_arrow(pos.tolist(), end=[x_end, y_end, -depth], color=color, thickness=5, lifetime=0.03)
    

Multi Agent Fossen Dynamics Example
===================================
In this section we will step through using fossen dynamics with multiple 
agents in HoloOcean. The full code can be found in `client/example.py`.
This example is very similar to the above example but with two agents.

Configuration
-------------
See the above example for specific instructions for setting up the configuration for the following items:

- Dynamics Sensor

- Fossen Model

- Control Scheme
    Note that the surface vessel agent using the control scheme 2 for custom dynamics.

- Control Mode (optional)

- Parameters (optional)
    Note that the configuration from scenario of the otter class is not implemented yet so no parameters can be set. 



.. code-block:: python

    scenario = {
    "name": "multi_agent_fossen",
    "world": "OpenWater",
    "package_name": "Ocean",
    "main_agent": "auv0",
    "agents": [
        {
            "agent_name": "auv0",
            "agent_type": "TorpedoAUV",
            "sensors": [
                {
                    "sensor_type": "DynamicsSensor",
                    "configuration": {
                        "UseCOM": True,
                        "UseRPY": False  # Use quaternion for dynamics
                    }
                },
            ],
            "control_scheme": 1,  # Control scheme 1 is how custom dynamics are applied to TAUV
            "location": [10,0,0],
            "rotation": [0,0,0],
            "fossen_model": "torpedo",
            "control_mode": "manualControl",
            },
            {
            "agent_name": "sv1",
            "agent_type": "SurfaceVessel",
            "sensors": [
                {
                    "sensor_type": "DynamicsSensor",
                    "configuration": {
                        "UseCOM": True,
                        "UseRPY": False  # Use quaternion for dynamics
                    }
                },
            ],
            "control_scheme": 2,  # Control scheme 2 is how custom dynamics are applied to SV
            "location": [10, -10, 0],
            "rotation": [0,0,0],
            "fossen_model": "otter",
            "control_mode": "manualControl",
            },
        ]
    }

Simulation Setup
----------------
The setup is about the single agent example. 

The only difference is that you need to add the name of the surface vessel agent to the fossen_agents list

.. code-block:: python

    import holoocean
    from holoocean.fossen_dynamics import *
    import numpy as np
    
    scenario = {...} # See above for scenario configuration

    env = holoocean.make(scenario_cfg=scenario)
    main_agent = 'auv0'
    sv_agent = 'sv1'
    fossen_agents = [main_agent, sv_agent]
    fossen_interface = FossenInterface(fossen_agents, scenario)

    accel = np.array(np.zeros(6),float)


Manual Control Example
----------------------
To use the manual control method, configure the vehicle mode with the fossen interface to "manualControl" mode. 
The commanded fin angles can also be set using the Fossen interface.

The length of the `u_control` array is defined in the dynamic model class. It represents the number 
of command inputs. The defualt torpedo has 5 control surfaces and the otter model has two thruster control surfaces.

.. code-block:: python

    ins_degrees = np.array([10, -10, -10, 10]) #Rudder and Stern Fin Deflection (degrees)
    fin_radians = np.radians(fins_degrees)
    thruster_rpm = 1000
    u_control_torpedo = np.append(fin_radians,thruster_rpm)  #[RudderAngle, SternAngle,Thruster] IN RADIANS
    fossen_interface.set_control_mode(main_agent, 'manualControl')

    u_control_otter = np.array([105, 80])
    fossen_interface.set_control_mode(sv_agent, 'manualControl')


The biggest difference with the multi-agent case is that to send commands to both agents the ``act`` and ``tick`` functions
are used instead of the ``step`` function. This difference is explained more in :ref:`step`.

To set the control surface commands for the agent using the Fossen Interface the vehicle name is required. 

The ``FossenInterface.update`` function takes in the states for both agents returned from the ``tick`` function and calculates 
an output of accelerations. The update needs to be called for every agent in the list and then applied to the agent with the ``act`` function.

.. code-block:: python

    states = env.tick() # Get the inital states of the agent for the dynamics

    for i in range(1500):
        fossen_interface.set_u_control(main_agent, u_control_torpedo) #If desired you can change control command here
        fossen_interface.set_u_control(sv_agent, u_control_otter)
        
        for agent in fossen_agents:
            accel = fossen_interface.update(agent, states) #Calculate accelerations to be applied to HoloOcean agent
            env.act(agent, accel)
        
        states = env.tick()