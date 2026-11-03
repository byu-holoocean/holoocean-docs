.. _visualizing_raycast_lidar:

==========================
Visualizing Raycast LIDAR
==========================

It can be useful to visualize the output of the LIDAR sensor during a simulation. This script will do 
that, plotting each scan within the HoloOcean environment. The script also allows you to control the agent.


::

    import holoocean
    import numpy as np
    from pynput import keyboard

    pressed_keys = list()
    name = "sv"

    config = {
        "name": "SurfaceNavigator",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": name,
        "ticks_per_sec": 30,
        'frames_per_sec': 150,
        "agents": [
            {
                "agent_name": name,
                "agent_type": "SurfaceVessel",
                "sensors": [
                    {
                        "sensor_type": "GPSSensor",
                    },
                    {
                        "sensor_type": "RaycastLidar",
                        "configuration": {
                            "socket": "Platform",
                            "Channels": 128,                     # Number of lasers
                            "Range": 200,                         # Max distance each laser can measure
                            "PointsPerSecond": 200000,            # Number of points per second
                            "RotationFrequency": 10,               # Lidar rotation frequency in Hz
                            "UpperFovLimit": 30,                  # Upper field of view limit (degrees above horizontal)
                            "LowerFovLimit": -30,                 # Lower field of view limit (degrees below horizontal)
                            "HorizontalFov": 360.0,               # Horizontal field of view (degrees)
                            "AtmospAttenRate": 0.4,               # Atmospheric attenuation rate
                            "RandomSeed": 0,                      # Seed for random number generation
                            "DropOffGenRate": 0.2,                # General drop-off rate
                            "DropOffIntensityLimit": 0.8,         # Intensity value below which drop-off starts
                            "DropOffAtZeroIntensity": 0.4,        # Drop-off rate at zero intensity
                            "ShowDebugPoints": True,              # Show laser hit points in simulator for debugging
                            "NoiseStdDev": 0.0                    # Standard deviation of measurement noise in centimeters
                        },
                        "Hz": 10
                    }
                ],
                "control_scheme": 0, # Manual control scheme
                "location": [-20,0,10],
                "rotation": [0, 0, 0]
            }
        ],
    }

    # Allow keyboard input to control the agent
    def on_press(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.append(key.char)
            pressed_keys = list(set(pressed_keys))

    def on_release(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.remove(key.char)

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    force = 300
    def parse_keys(keys, val):
        command = np.zeros(2)
        if 'i' in keys: # forward thrust
            command[:] += val
        if 'k' in keys: # backward thrust
            command[:] -= val
        if 'j' in keys: # roll CCW
            command[0] -= val
            command[1] += val
        if 'l' in keys: # roll CW
            command[0] += val
            command[1] -= val

        return command

    with holoocean.make(scenario_cfg=config, start_world=False) as env: #
        while True:
            if 'q' in pressed_keys:
                break
            command = parse_keys(pressed_keys, force)

            #send to holoocean
            env.act(name, command)
            state = env.tick()