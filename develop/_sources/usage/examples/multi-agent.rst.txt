Multi Agent Example
===================

With HoloOcean, you can control more than one agent at once. Instead of calling 
``.step()``, which both

1. passes a single command to the main agent, and
2. ticks the simulation

you should call ``.act()``. Act supplies a command to a specific 
agent, but doesn't tick the game. 

Once all agents have received their actions, you can call ``.tick()`` to tick
the game.

After calling ``.act()``, every time you call ``.tick()`` the same command 
will be supplied to the agent. To change the command, just call ``.act()`` again.

The state returned from tick is also somewhat different. 

The state is now a dictionary from agent name to sensor dictionary.

Press tab to switch the viewport between agents. See :ref:`hotkeys` for more.

::

    import holoocean
    import numpy as np

    cfg = {
        "name": "test_rgb_camera",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 60,
        "agents": [
            {
                "agent_name": "auv0",
                "agent_type": "TorpedoAUV",
                "sensors": [
                    {
                        "sensor_type": "IMUSensor"
                    }
                ],
                "control_scheme": 0,
                "location": [0, 0, -5]
            },
            {
                "agent_name": "auv1",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "DVLSensor"
                    }
                ],
                "control_scheme": 0,
                "location": [0, 2, -5]
            }
        ]
    }

    env = holoocean.make(scenario_cfg=cfg)
    env.reset()

    env.act('auv0', np.array([0,0,0,0,75]))
    env.act('auv1', np.array([0,0,0,0,20,20,20,20]))
    for i in range(300):
        states = env.tick()

        # states is a dictionary
        imu = states["auv0"]["IMUSensor"]

        vel = states["auv1"]["DVLSensor"]
