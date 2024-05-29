Manually Defining Dynamics
===========================

Many times, it may be useful for research to easily be able to implement custom dynamics. For this purpose, we have created controllers for the :ref:`hovering-auv-agent` that take in linear and angular acceleration and integrate them for custom dynamics. Besides collisions, no other accelerations are applied to the vehicle in the simulator, allowing full custom dynamics to be implemented *in python*. The possibilities for this are endless and include complex hydrodynamics, water currents, and more.

In addition, the :class:`~holoocean.sensors.DynamicsSensor` was made to provide all necessary current state information for computing dynamics including, accelerations, velocities, and current pose information.

Here is an example of this in action, implementing gravity, buoyancy, and damping by hand.

::

    import numpy as np
    import holoocean
    from holoocean.agents import HoveringAUV
    from scipy.spatial.transform import Rotation

    scenario = {
        "name": "hovering_dynamics",
        "package_name": "Ocean",
        "world": "SimpleUnderwater",
        "main_agent": "auv0",
        "agents": [
            {
                "agent_name": "auv0",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "DynamicsSensor",
                        "configuration":{
                            "UseRPY": False # Use quaternion
                        }
                    },
                ],
                "control_scheme": 2, # this is the custom dynamics control scheme
                "location": [0,0,-10],
                "rotation": [20,20,90]
            }
        ]
    }

    g = 9.81 # gravity
    b = 3 # linear damping
    c = 2 # angular damping
    # HoveringAUV.mass += 1 # alternatively make it sink

    def f(x):
        # Extract all info from state
        a = x[:3]
        v = x[3:6]
        p = x[6:9]
        alpha = x[9:12]
        omega = x[12:15]
        quat = x[15:19]
        R = Rotation.from_quat(quat).as_matrix()

        # Sum all forces
        force = np.zeros(3)
        force[2] += -HoveringAUV.mass * g # gravity
        force[2] += HoveringAUV.water_density * g * HoveringAUV.volume # buoyancy
        force -= v*b # Damping

        # Sum all torques
        torque = np.zeros(3)
        buoy_force = HoveringAUV.water_density*g*HoveringAUV.volume*np.array([0,0,1]) # in global frame
        cob = R@HoveringAUV.cob # move center of buoyancy to global frame
        torque += np.cross(cob, buoy_force) # torque from buoyancy
        torque -= omega*c # damping

        # Convert force & torque to accelerations
        lin_accel = force / HoveringAUV.mass
        ang_accel = np.linalg.inv(HoveringAUV.I)@torque
        return np.append(lin_accel, ang_accel)

    u = np.zeros(6)
    # Make environment
    with holoocean.make(scenario_cfg=scenario) as env:
        for i in range(500):
            # Step simulation
            state = env.step(u)
            # Get accelerations to pass to HoloOcean
            u = f(state["DynamicsSensor"])
            