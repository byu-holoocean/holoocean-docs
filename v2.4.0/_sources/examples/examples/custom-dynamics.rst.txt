.. _custom-dynamics-example:

==========================
Manually Defining Dynamics
==========================

In some situations it may be useful to implement custom dynamics for a vehicle. For this purpose, 
most vehicles have a Custom Dynamics control scheme that take in linear and angular acceleration 
and integrate them to generate motion. 

Here is an example of manually defining a vehicle's dynamics where we implementing gravity, 
buoyancy, and damping by hand for a Hovering AUV.

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

    accels = np.zeros(6)
    # Make environment
    with holoocean.make(scenario_cfg=scenario) as env:
        for i in range(500):
            # Step simulation
            state = env.step(accels)
            # Get accelerations to pass to HoloOcean
            accels = f(state["DynamicsSensor"])
            