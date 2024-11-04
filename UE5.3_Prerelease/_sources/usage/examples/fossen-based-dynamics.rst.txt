.. _fossen-dynamics:

Fossen-Based Dynamics
=====================

Dynamics for underwater and surface vehicles can be modeled using equations of motion derived from Thor Fossen’s Python Dynamics Simulation: https://github.com/cybergalactic/PythonVehicleSimulator. These models are explained in the book by Thor Fossen, *Handbook of Marine Craft Hydrodynamics and Motion Control*.

We have implemented some of these models in HoloOcean to simulate the motion of the vehicle based on control surface commands. To use these Fossen dynamics implementations with a vehicle's "Custom Dynamics" control scheme in a simulation, we have implemented two objects that must be defined in the python script when creating a simulation:

- A vehicle controller of one of the classes described below. This implements the Fossen dynamics for that vehicle. 
- A dynamics manager of the class `FossenDynamics`. This handles the connection between the HoloOcean agent and the dynamics controller. It also handles coordinate frame change from NED to NWU, as HoloOcean does not currently have a defined North or West direction world coordinate frame (see :ref:`coordinate-system`).

These classes are implemented in `client/src/vehicle_dynamics`. The dynamics manager is located in `client/src/dynamics.py`. 

Currently, we have implemented the dynamics models for one vehicle class and several child classes:

- Generic Torpedo Vehicle Parent class (:class:`~holoocean.vehicle_dynamics.torpedo.TAUV`)
    - Three Independent Fins - Torpedo-shaped vehicle (:class:`~holoocean.vehicle_dynamics.torpedo.threeFinInd`)
    - Four Dependent Fins - Torpedo-shaped vehicle (:class:`~holoocean.vehicle_dynamics.torpedo.fourFinDep`)
    - Four Independent Fins - Torpedo-shaped vehicle (:class:`~holoocean.vehicle_dynamics.torpedo.fourFinInd`)

Note that the graphics for the vehicle model or fin configuration will not change in Unreal Engine when changing the dynamics class.

Default Fossen vehicle parameters are currently only tuned for the REMUS100 vehicle provided by Thor Fossen's simulations.

.. warning::
    Mass and other default vehicle parameters set in the engine are ignored when using the "Custom Dynamics" control scheme. The Fossen models account for these separately.

Below we give an example of using Fossen dynamics in HoloOcean. The full code file can be found in `client/example.py`.

Scenario Setup
~~~~~~~~~~~~~~

The setup for the simulation is similar to other HoloOcean examples. The total simulation time can be calculated by `(numSteps/ticks_per_sec)`.

.. warning::
    If you are running the simulation live with the Unreal Editor, make sure you change the additional launch parameters, as described in :ref:`start`. 
    Be sure to add the launch parameter `-TicksPerSec` to match what is in the Python script for consistent timing.

.. code-block:: python

    import holoocean
    import holoocean.vehicle_dynamics
    
    ticks_per_sec = 50
    numSteps = 600
    period = 1.0/ticks_per_sec

    initial_location = [0, 0, -10]  # Translation in NWU coordinate system
    initial_rotation = [0, 0, 0]    # Roll, pitch, yaw in Euler angle order ZYX and in degrees NWU coordinate system

For the scenario configuration, there are a few key differences to ensure dynamics work properly:

- You must include the Dynamics Sensor in the list of sensors with the configuration `UseRPY: False` (default is True) and `UseCOM: True` (default is True).
- The extra parameters "dynamics", "actuator", and "autopilot" are added to the agent. Default parameters are defined in the vehicle class.

See :func:`holoocean.vehicle_dynamics.torpedo.configure_from_scenario` for dynamics parameters definition as well as the book by Thor Fossen.

.. code-block:: python

    scenario = {
    "name": "torpedo_dynamics",
    "package_name": "TestWorlds",
    "world": "ExampleLevel",
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
            "location": initial_location,
            "rotation": initial_rotation,
            "dynamics": 
                {
                    "mass": 16,
                    "length": 1.6,
                    "rho": 1026,
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
                    "K_nomoto": 5.0 / 20.0
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

Simulation setup proceeds first by setting up an environment. We pass the vehicle parameters defined in the scenario configuration to a Fossen vehicle object, 
which specifies a target HoloOcean agent (e.g., `'auv0'`). Next we create a dynamics manager, passing the vehicle and simulation time period (1/ticks_per_sec), 
to attach the parameters to the agent. Finally we initialize a NumPy array with a length of 6 for accelerations in x, y, z (global frame) and angular 
accelerations around the x, y, and z axes (global frame).

In this example we select the `fourFinDep` vehicle, which has 3 control inputs (Rudder Fins, Stern Fins, Thruster).

.. code-block:: python

    env = holoocean.make(scenario_cfg=scenario)
    vehicle = fourFinDep(scenario, 'auv0','manualControl')    
    torpedo_dynamics = FossenDynamics(vehicle, period)  
    accel = np.array(np.zeros(6), float)  # HoloOcean parameter input 

Manual Control Example:
~~~~~~~~~~~~~~~~~~~~~~~

To use the manual control method, set the vehicle object to "manualControl" mode.

The fin angles can be passed directly to the vehicle dynamics, and an acceleration array will be returned to the HoloOcean agent given the state of the agent in the HoloOcean world.

The length of the `u_control` array is defined in the dynamic model class. It represents the number of command inputs.

- Fin angles should be given in radians. The example below shows how to convert fin angles from degrees to radians using NumPy.
- A positive fin deflection of a rudder fin will result in a yaw moment to the starboard side.
- A positive fin deflection of a stern/elevator fin will result in a pitch moment to pitch the vehicle up.

A custom controller can be used with this manual control method to input specific fin commands.

.. code-block:: python

    vehicle.set_control_mode('manualControl') 
    fins_degrees = np.array([5, -5])  # Rudder and Stern Fin Deflection (degrees)
    fin_radians = np.radians(fins_degrees)
    thruster_rpm = 800
    u_control = np.append(fin_radians, thruster_rpm)  # [RudderAngle, SternAngle, Thruster]

To tick the environment, call the `step` function and pass it a list of accelerations.

We send a command to the control surfaces with the `set_u_control_rad` function on the FossenDynamics object. 

It is not required to set the `u_control` every tick. If you want to change the control surfaces every tick, then you should set the control command before updating the dynamics.

The `FossenDynamics.update` function takes in the state returned from HoloOcean and parses the data from the Dynamics Sensor. Given the state of the vehicle and control surface inputs, it calculates an output of accelerations in the HoloOcean frame (NWU).

.. code-block:: python

    for i in range(numSteps):
        state = env.step(accel)
        torpedo_dynamics.set_u_control_rad(u_control)  # If desired, you can change the control command here
        accel = torpedo_dynamics.update(state)  # Calculate accelerations to be applied to HoloOcean agent

        # For Plotting the state of the vehicle
        pos = state['DynamicsSensor'][6:9]  # [x, y, z]
        pos_list.append(pos)
        time_list.append(state['t'])

Depth and Heading Control Example:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depth is defined as negative Z and increases the deeper the vehicle is underwater. Units are in meters.

Heading command ranges from

 -180 to 180 in degrees, with 0 deg being north (along the x-axis) and 90 deg East (along the negative y axis). This makes `heading = -yaw` for yaw values in NWU coordinate systems. 

The final value 1525 is the actual command value for the thruster in rpm. 

Surge control of the vehicle is also supported when specified. This is not enabled by default. 

.. warning::
    Every time the set_control_mode is called the controller integral values and Low Pass filter is reset. So
    this should only be called when switching control modes and should not be placed in the for loop. 

.. code-block:: python 

    depth = 15
    heading = 50    
    vehicle.set_goal(depth,heading,1525)     #Changes depth (positive depth), heading, thruster RPM goals for controller 
    vehicle.set_control_mode('depthHeadingAutopilot') #In this mode PID controller calculates control commands (u_control)
    for i in range(numSteps):
        state = env.step(accel)
        accel = torpedo_dynamics.update(state)

        # For plotting and arrows 
        pos = state['DynamicsSensor'][6:9]  # [x, y, z]
        x_end = pos[0] + 3 * np.cos(np.deg2rad(heading))
        y_end = pos[1] - 3 * np.sin(np.deg2rad(heading))
        pos_list.append(pos)
        time_list.append(state['t'])

        #change color if within 2 meters
        if abs(depth + pos[2]) <= 2.0:
            color = [0,255,0]
        else:
            color = [255,0,0]

        env.draw_arrow(pos.tolist(), end=[x_end, y_end, -depth], color=color, thickness=5, lifetime=0.03)
    

Plotting Vehicle State:
~~~~~~~~~~~~~~~~~~~~~~~

The following code block is optional to plot the vehicle state 

.. code-block:: python

    plot = True

    if plot:
        import matplotlib.pyplot as plt
        # Convert position list to a numpy array for easier slicing
        pos_array = np.array(pos_list)

        # Extract x, y, and z positions
        x_positions = pos_array[:, 0] #North Position
        y_positions = pos_array[:, 1]  #West Position
        east_positions = [-y for y in y_positions] #Convert from west to east
        z_positions = pos_array[:, 2]   #Z positions (Z up)

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

