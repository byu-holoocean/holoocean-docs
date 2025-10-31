.. _`manual-control`:

=============================
Manually Controlling an Agent
=============================

We've found that `pynput` is a good library for sending keyboard commands to the agents for manual control.
Below are three examples that allows for controlling three different kinds of agents using keyboard inputs. 

Example 1: Hovering AUV
-----------------------

The :ref:`hovering-auv-agent` uses the following keyboard shortcuts to control the vehicle:

.. list-table::
   :widths: 35 25 25
   :header-rows: 1

   * - Key
     - Forward Key
     - Backward Key
   * - Ascend/Descend
     - i
     - k
   * - Yaw Left/Right
     - j
     - l
   * - Forward/Backward
     - w
     - s
   * - Strafe Left/Right
     - a
     - d

::

    import holoocean
    import numpy as np
    from pynput import keyboard

    name = "agent"
    config = {
            "name": "test",
            "world": "Dam",
            "package_name": "Ocean",
            "main_agent": name,
            "agents": [
                {
                    "agent_name": name,
                    "agent_type": "HoveringAUV",
                    "sensors": [
                    ],
                    "control_scheme": 0,
                    "location": [0, 0, -10],
                    "rotation": [0, 0, 180]
                }
            ]
        }

    def parse_keys(keys, val):
        command = np.zeros(8)

        if 'i' in keys: # ascend
            command[0:4] += val
        if 'k' in keys: # descend
            command[0:4] -= val
        if 'j' in keys: # yaw left
            command[[4,7]] += val
            command[[5,6]] -= val
        if 'l' in keys: # yaw right
            command[[4,7]] -= val
            command[[5,6]] += val
        if 'w' in keys: # forward
            command[4:8] += val
        if 's' in keys: # backward
            command[4:8] -= val
        if 'a' in keys: # strafe left
            command[[4,6]] += val
            command[[5,7]] -= val
        if 'd' in keys: # strafe right
            command[[4,6]] -= val
            command[[5,7]] += val
        return command

    def on_press(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.append(key.char)
            pressed_keys = list(set(pressed_keys))

    def on_release(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.remove(key.char)

    pressed_keys = list()
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    with holoocean.make(scenario_cfg=config) as env:
        force = 25
        while True:
            if 'q' in pressed_keys:
                break
            command = parse_keys(pressed_keys, force)
            env.act(name, command)
            state = env.tick()


Example 2: Torpedo AUV
----------------------

The :ref:`torpedo-auv-agent` uses the following keyboard shortcuts:

.. list-table::
   :widths: 35 25 25
   :header-rows: 1

   * - Key
     - Forward Key
     - Backward Key
   * - Thrust Forward/Backward
     - w
     - s
   * - Pitch Up/Down
     - i
     - k
   * - Yaw Left/Right
     - j
     - l

::

    import holoocean
    import numpy as np
    from pynput import keyboard

    name = "agent"
    config = {
            "name": "test",
            "world": "Dam",
            "package_name": "Ocean",
            "main_agent": name,
            "agents": [
                {
                    "agent_name": name,
                    "agent_type": "TorpedoAUV",
                    "sensors": [
                    ],
                    "control_scheme": 0,
                    "location": [0, 0, -10],
                    "rotation": [0, 0, 180]
                }
            ]
        }
        
    def parse_keys(keys, val):
        command = np.zeros(5)
        if 'w' in keys: # forward thrust
            command[4] += val
        if 's' in keys: # backward thrust
            command[4] -= val
        if 'i' in keys: # pitch up
            command[0] -= val
            command[2] += val
        if 'k' in keys: # pitch down
            command[0] += val
            command[2] -= val
        if 'j' in keys: # yaw left
            command[1] -= val
            command[3] += val
        if 'l' in keys: # yaw right
            command[1] += val
            command[3] -= val
        return command

    def on_press(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.append(key.char)
            pressed_keys = list(set(pressed_keys))

    def on_release(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.remove(key.char)

    pressed_keys = list()
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    with holoocean.make(scenario_cfg=config) as env:
        force = 20
        while True:
            if 'q' in pressed_keys:
                break
            command = parse_keys(pressed_keys, force)
            env.act(name, command)
            state = env.tick()

Example 3: Surface Vessel
-------------------------

The :ref:`surface-vessel-agent` uses the following keyboard shortcuts:

.. list-table::
   :widths: 35 25 25
   :header-rows: 1

   * - Key
     - Forward Key
     - Backward Key
   * - Thrust Forward/Backward
     - w
     - s
   * - Yaw Left/Right
     - a
     - d

::

    import holoocean
    import numpy as np
    from pynput import keyboard

    name = "agent"
    config = {
            "name": "test",
            "world": "Dam",
            "package_name": "Ocean",
            "main_agent": name,
            "agents": [
                {
                    "agent_name": name,
                    "agent_type": "SurfaceVessel",
                    "sensors": [
                    ],
                    "control_scheme": 0,
                    "location": [0, 0, 0],
                    "rotation": [0, 0, 0]
                }
            ]
        }
        
    def parse_keys(keys, val):
        command = np.zeros(2)
        if 'w' in keys: # forward thrust
            command[:] += val
        if 's' in keys: # backward thrust
            command[:] -= val
        if 'a' in keys: # yaw left
            command[0] -= val
            command[1] += val
        if 'd' in keys: # yaw right
            command[0] += val
            command[1] -= val
        return command

    def on_press(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.append(key.char)
            pressed_keys = list(set(pressed_keys))

    def on_release(key):
        global pressed_keys
        if hasattr(key, 'char'):
            pressed_keys.remove(key.char)

    pressed_keys = list()
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    with holoocean.make(scenario_cfg=config) as env:
        force = 1000
        while True:
            if 'q' in pressed_keys:
                break
            command = parse_keys(pressed_keys, force)
            env.act(name, command)
            state = env.tick()
