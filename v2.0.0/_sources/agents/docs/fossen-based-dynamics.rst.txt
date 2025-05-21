.. _fossen-dynamics:

=====================
Fossen-Based Dynamics
=====================

Dynamics for underwater and surface vehicles can be modeled using equations of motion derived in 
Thor Fossen's *Handbook of Marine Craft Hydrodynamics and Motion Control*. Implementations of these 
dynamics are conveniently provided by Fossen at his 
`GitHub repository <https://github.com/cybergalactic/PythonVehicleSimulator>`_. We have ported some 
of Fossen's implementations into HoloOcean to enable accurate vehicle dynamics simulations.

Using Fossen-based dynamics in HoloOcean is an extension of the Custom Dynamics control scheme. It 
requires defining two objects in python when creating a simulation:

1.  A vehicle controller of one of the classes described below. This implements the Fossen dynamics 
    for that vehicle. 
2.  A dynamics manager of the class `FossenDynamics`. This handles the connection between the 
    HoloOcean agent and the dynamics controller by associating the dynamics with a specific agent. 
    It also handles coordinate frame changes from NED to NWU, as HoloOcean does not currently have 
    a defined North or West direction world coordinate frame (see :ref:`coordinate-system`).

These classes are implemented in `client/src/vehicle_dynamics`. The dynamics manager is located in 
`client/src/dynamics.py`. 

.. note::
    Fossen dynamics does not currently support multiple agents. A multi-agent implementation is 
    planned for a future release.

Fossen Vehicle Classes
======================
Currently, we have implemented the dynamics models for one vehicle class and several child classes:

- Torpedo Vehicle Parent class (:class:`~holoocean.fossen_dynamics.torpedo.TAUV`)
    - Three Independent Fins - Torpedo-shaped vehicle (:class:`~holoocean.fossen_dynamics.torpedo.threeFinInd`)
    - Four Dependent Fins - Torpedo-shaped vehicle (:class:`~holoocean.fossen_dynamics.torpedo.fourFinDep`)
    - Four Independent Fins - Torpedo-shaped vehicle (:class:`~holoocean.fossen_dynamics.torpedo.fourFinInd`)

Default Fossen vehicle parameters are currently tuned for the REMUS100 vehicle provided by 
Thor Fossen. 

.. note::
    The Unreal Engine graphics asset is the same across all three classes of torpedo dynamics. 
    The number of fins shown on the vehicle will not change in Unreal Engine when changing between 
    child classes.

    Implementing Fossen dynamics does not change the asset, so the fins will not visibly move when 
    the simulation is running. 

.. note::
    Mass and other default vehicle parameters set in the HoloOcean engine are ignored when using 
    the "Custom Dynamics" control scheme. The Fossen models account for these separately.

Adding Custom Fossen Dynamics
-----------------------------
Users can add their own custom Fossen dynamics models for different types of vehicles by creating a 
new class. 

Dynamics model classes must have the following methods and attributes:

- `__init__`: This method should initialize the vehicle parameters and set up the dynamics model.

- `dynamics`: This method should implement the dynamics equations for the vehicle. It should take in 
  the current state of the vehicle (eta, nu) and the control input, and return the accelerations in 
  the NWU frame.

The model can also implement other functions as desired, such as controllers and plotting functions. 
We recommend using a `controlMode` attribute to define the control scheme for the vehicle. 

See the `TAUV` class for an example of how to implement a custom dynamics model.

Importing Models from PythonVehicleSimulator
--------------------------------------------
If a user has developed a dynamics model class using Thor Fossen's PythonVehicleSimulator and would 
like to use it in HoloOcean, they must make the following changes: 

- The `dynamics` method must be changed to only take in the state of the vehicle (eta, nu) and control input vector as inputs and return only NWU accelerations. 

- `sampleTime` must be made a class attribute instead of a passed-in parameter. 

- `u_actual` must be made a class attribute tracked by the vehicle class instead of a passed-in parameter. The FossenDynamics manager relies on the vehicle class to track its own current actuator positions. 

Be sure that all other methods and attributes are implemented as expected by the FossenDynamics
manager.

Fossen Dynamics Example
=======================
In this section we will step through the key elements of our Fossen dynamics implementation and give 
an example of using Fossen dynamics in HoloOcean. The full code can be found in `client/example.py`.

Configuration
-------------
Setting up a HoloOcean simulation that uses Fossen dynamics begins with the scenario configuration.
The scenario configuration is similar to other HoloOcean examples, but with some key differences:

1. When configuring the main agent, you must include the Dynamics Sensor in the list of sensors. 
   The configuration block should include `UseRPY: False` (default is True; this forces the 
   dynamics to use quaternions instead of Euler angles) and `UseCOM: True` (default is True).

2. The extra parameters `dynamics`, `actuator`, and `autopilot`` must be added to the agent 
   configuration. Each of these is a dictionary that defines further vehicle parameters.
   See :func:`holoocean.fossen_dynamics.torpedo.configure_from_scenario` for definitions of each 
   dynamics parameter. 

Below is an example scenario configuration that fully defines all the parameters for the Fossen
dynamics. A full description of each parameter can be found in the API documentation for the
Fossen dynamics classes.

.. code-block:: python

    scenario = {
    "name": "torpedo_dynamics",
    "package_name": "Oceans",
    "world": "SimpleUnderwater",
    "main_agent": "auv0",
    "ticks_per_sec": ticks_per_sec,
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
            "location": [0, 0, -10],  # Represented in NWU coordinate system
            "rotation": [0, 0, 0], # Roll, pitch, yaw in Euler angle order ZYX and in degrees NWU coordinate system
            "dynamics": 
                {
                    "sampleTime": 1/60,
                    "rho": 1026,
                    "mass": 16,
                    "length": 1.6,
                    "diam": 0.19,
                    "r_bg": [0, 0, 0.02],
                    "r_bb": [0, 0, 0],
                    "r44": 0.3,
                    "Cd": 0.42,
                    "T_surge": 20,
                    "T_sway": 20,
                    "zeta_roll": 0.3,
                    "zeta_pitch": 0.8,
                    "T_yaw": 1,
                    "K_nomoto": 0.25
                },
            "actuator": 
                {
                    "fin_area": 0.00665,
                    "deltaMax_fin_deg": 15,
                    "nMax": 1525,
                    "T_delta": 0.1,
                    "T_n": 0.1,
                    "CL_delta_r": 0.5,
                    "CL_delta_s": 0.7
                },
            "autopilot": 
                {
                    'depth': {
                        'wn_d_z': 0.2,
                        'Kp_z': 0.08,
                        'T_z': 100,
                        'Kp_theta': 4.0,
                        'Kd_theta': 2.3,
                        'Ki_theta': 0.3,
                        'K_w': 5.0,
                    },
                    'heading': {
                        'wn_d': 1.2,
                        'zeta_d': 0.8,
                        'r_max': 0.9,
                        'lam': 0.1,
                        'phi_b': 0.1,
                        'K_d': 0.5,
                        'K_sigma': 0.05,
                    }
                },
            }
        ]
    }


Simulation Setup
----------------
The setup for the simulation is similar to other HoloOcean :ref:`examples`. 

Simulation setup proceeds first by setting up an environment. We pass the vehicle parameters defined 
in the scenario configuration to a Fossen vehicle object, which specifies a target HoloOcean agent 
(e.g., `'auv0'`). Next we create a dynamics manager, passing the vehicle and simulation time period 
(1/ticks_per_sec), to attach the parameters to the agent. Finally we initialize a numpy array with a 
length of 6 for accelerations in x, y, z (global frame) and angular accelerations around the x, y, 
and z axes (global frame).

In this example we select the `fourFinDep` vehicle, which has 3 control inputs (Rudder Fins, Stern 
Fins, Thruster).

.. code-block:: python

    import holoocean
    import holoocean.fossen_dynamics as fd
    
    numSteps = 600   # The total simulation time can be calculated by (numSteps/ticks_per_sec).
    period = 1.0/ticks_per_sec

    scenario = {...} # See above for scenario configuration

    env = holoocean.make(scenario_cfg=scenario)
    
    fossen_vehicle = fd.torpedo.fourFinDep(env, 'auv0')
    fossen_manager = fd.dynamics.FossenDynamics(fossen_vehicle)
    accel = np.array(np.zeros(6), float)  # Initialize HoloOcean parameter input 


.. note::
    If you are running the simulation live with the Unreal Editor in Standalone mode, be sure to 
    change the additional launch parameters as described in :ref:`develop-start`. Add the launch 
    parameter `-TicksPerSec` to match what is in the Python script for consistent timing.


Manual Control Example
----------------------
To use the manual control method, set the vehicle object to "manualControl" mode. The fin angles can 
be passed directly to the vehicle dynamics, and an acceleration array will be returned to the 
HoloOcean agent given the state of the agent in the HoloOcean world.

The length of the `u_control` array is defined in the dynamic model class. It represents the number 
of command inputs.

- Fin angles should be given in radians. The example below shows how to convert fin angles from 
  degrees to radians using numpy.
- A positive fin deflection of a rudder fin will result in a yaw moment to the starboard side.
- A positive fin deflection of a stern/elevator fin will result in a pitch moment to pitch the 
  vehicle up.

A custom controller can be used with this manual control method to input specific fin commands.

.. code-block:: python

    fossen_vehicle.set_control_mode('manualControl') 
    fins_degrees = np.array([5, -5])  # Rudder and Stern Fin Deflection (degrees)
    fin_radians = np.radians(fins_degrees)
    thruster_rpm = 800 # not a percent: check the vehicle dynamics for the max RPM
    u_control = np.append(fin_radians, thruster_rpm)  # [RudderAngle, SternAngle, Thruster]

To tick the environment, call the `step` function and pass it a list of accelerations. Next, send a 
command to the control surfaces with the `set_u_control_rad` function on the FossenDynamics 
object. It is not required to set the `u_control` every tick. If you want to change the control 
surfaces every tick, set the control command before updating the dynamics.

The `FossenDynamics.update` function takes in the state returned from HoloOcean and parses the data 
from the Dynamics Sensor. Given the state of the vehicle and control surface inputs, it calculates 
an output of accelerations in the HoloOcean frame (NWU).

.. code-block:: python

    for i in range(numSteps):
        state = env.step(accel)
        torpedo_dynamics.set_u_control_rad(u_control)  # If desired, you can change the control command here
        accel = torpedo_dynamics.update(state)  # Calculate accelerations to be applied to HoloOcean agent

        # For Plotting the state of the vehicle
        pos = state['DynamicsSensor'][6:9]  # [x, y, z]
        pos_list.append(pos)
        time_list.append(state['t'])


Depth and Heading Control Example
---------------------------------

A common control strategy for underwater vehicles is to control depth and heading separately. This
can be done by setting the control mode to `depthHeadingAutopilot` and setting the goal depth, 
heading, and thruster RPM.

The depth goal is defined in meters. A positive depth corresponds to a negative z location, with 
depth increasing the further the vehicle descends.

The heading goal is given in the global frame. It ranges from -180 to 180 degrees, with 0 degrees 
being north (along the positive x-axis) and 90 degress being East (along the negative y axis). This 
makes `heading = -yaw` for yaw values in NWU coordinate systems. 

The thruster goal is given directly as RPM, not as a percentage of the maximum RPM. Be sure to 
check the max RPM in the Fossen vehicle configuration to ensur ethe command is below the maximum.

Surge control of the vehicle is also supported when specified. This is not enabled by default. 

.. warning::
    Every time `set_control_mode` is called, the controller integral values and Low Pass filter 
    is reset. Calling `set_control_mode` should only be done when switching control modes and should 
    not be placed in the for loop. 

.. code-block:: python 

    depth_goal = 15 # meters
    heading_goal = 50 # degrees
    thruster_goal = 1525 # RPM

    vehicle.set_control_mode('depthHeadingAutopilot') # In this mode, PID controller calculates control commands (u_control)
    vehicle.set_goal(depth_goal, heading_goal, thruster_goal) # Changes depth (positive), heading, thruster RPM goals for controller 
    
    # Run simulation
    for i in range(numSteps):
        state = env.step(accel)
        accel = torpedo_dynamics.update(state)

        # For plotting and arrows 
        pos = state['DynamicsSensor'][6:9]  # [x, y, z]
        x_end = pos[0] + 3 * np.cos(np.deg2rad(heading))
        y_end = pos[1] - 3 * np.sin(np.deg2rad(heading))
        pos_list.append(pos)
        time_list.append(state['t'])

        # Change color if within 2 meters
        if abs(depth + pos[2]) <= 2.0:
            color = [0,255,0]
        else:
            color = [255,0,0]

        env.draw_arrow(pos.tolist(), end=[x_end, y_end, -depth], color=color, thickness=5, lifetime=0.03)
    

Plotting Vehicle State
----------------------

The following code can be used to plot the vehicle's state over time. This code is placed after the
simulation loop.


.. code-block:: python

    plot = True

    if plot:
        import matplotlib.pyplot as plt

        # Convert position list to a numpy array for easier slicing
        pos_array = np.array(pos_list)

        # Extract x, y, and z positions
        x_positions = pos_array[:, 0] # North Position
        y_positions = pos_array[:, 1] # West Position
        east_positions = [-y for y in y_positions] # Convert from west to east
        z_positions = pos_array[:, 2] # Z positions (Z up)

        # Plot x and y positions
        plt.figure()
        plt.plot( east_positions,x_positions, marker='o')
        plt.title('X and Y Positions')
        plt.xlabel('East (meters)')
        plt.ylabel('North (meters)')
        plt.grid(True)

        # Plot z positions over time
        plt.figure()
        plt.plot(time_list, z_positions, marker='o')
        plt.title('Z Position over Time')
        plt.xlabel('Time Step')
        plt.ylabel('Z Position')
        plt.grid(True)

        # Show the plots
        plt.show()


