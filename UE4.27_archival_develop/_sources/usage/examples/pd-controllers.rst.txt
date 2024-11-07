PD Controller
===========================

A number of built in agents have simple PD controllers built in to allow for easy navigating when data is being generated, namely the :class:`~holoocean.agents.HoveringAUV` and :class:`~holoocean.agents.SurfaceVessel`. When the the PD control scheme is selected, the control passed to holoocean will be the desired
state to navigate to. Below is an example of this for the Surface Vessel where it navigates to a number of predefined waypoint on the surface.

::

    import holoocean
    import numpy as np

    config = {
        "name": "SurfaceNavigator",
        "world": "SimpleUnderwater", 
        "package_name": "Ocean",
        "main_agent": "sv",
        "agents":[
            {
                "agent_name": "sv",
                "agent_type": "SurfaceVessel",
                "sensors": [
                {
                    "sensor_type": "GPSSensor",
                }
                ],
                "control_scheme": 1, # PD Control Scheme
                "location": [0,0,2],
                "rotation": [0, 0, 0]
            }
        ],
    }

    # Define waypoints
    idx = 0
    locations = np.array([[25,25],
                        [-25,25],
                        [-25,-25],
                        [25,-25]])

    # Start simulation
    with holoocean.make(scenario_cfg=config) as env:
        # Draw waypoints
        for l in locations:
            env.draw_point([l[0], l[1], 0], lifetime=0)

        print("Going to waypoint ", idx)

        while True:
            #send waypoint to holoocean
            state = env.step(locations[idx])

            # Check if we're close to the waypoint
            p = state["GPSSensor"][0:2]
            if np.linalg.norm(p-locations[idx]) < 1e-1:
                idx = (idx+1) % 4
                print("Going to waypoint ", idx)
            