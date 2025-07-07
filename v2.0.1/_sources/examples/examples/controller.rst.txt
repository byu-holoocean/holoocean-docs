.. _`manual-control`:

=============================
Manually Controlling an Agent
=============================

We've found that `pynput` is a good library for sending keyboard commands to the agents for manual control.

Here's an example of controlling the :ref:`hovering-auv-agent` using the following keyboard shortcuts.

.. list-table::
   :widths: 35 25 25
   :header-rows: 1

   * - Key
     - Forward Key
     - Backward Key
   * - Up/Down
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

    pressed_keys = list()
    force = 25

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

    def parse_keys(keys, val):
        command = np.zeros(8)
        if 'i' in keys:
            command[0:4] += val
        if 'k' in keys:
            command[0:4] -= val
        if 'j' in keys:
            command[[4,7]] += val
            command[[5,6]] -= val
        if 'l' in keys:
            command[[4,7]] -= val
            command[[5,6]] += val

        if 'w' in keys:
            command[4:8] += val
        if 's' in keys:
            command[4:8] -= val
        if 'a' in keys:
            command[[4,6]] += val
            command[[5,7]] -= val
        if 'd' in keys:
            command[[4,6]] -= val
            command[[5,7]] += val

        return command

    with holoocean.make("Dam-Hovering") as env:
        while True:
            if 'q' in pressed_keys:
                break
            command = parse_keys(pressed_keys, force)

            #send to holoocean
            env.act("auv0", command)
            state = env.tick()