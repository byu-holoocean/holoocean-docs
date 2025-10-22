.. _sampling_bst:

Sampling Biomass, Salinity, Temperature
============================

It can be useful to model more complex distributions of biomass, salinity, and temperature by utilizing clusters. 
Clusters allow us to place concentrations of biomass, salinity, or temperature at any point in the map that may not always 
follow the conventional trends. The following scenario uses the base function models for biomass and 
salinity, adds some biomass clusters that might represent phytoplankton blooms, and uses a custom 
temperature function that may model how temperature across simulation location is affected near 
glaciers. To upload a custom function instead of just tweaking the current parameters, use 
``env.set_biomass_function("auv0", new_biomass_function)``, ``env.set_salinity_function("auv0", new_salinity_function)``, 
or ``env.set_temperature_function("auv0", new_temperature_function)`` for biomass, salinity, or temperature 
respectively. "auv0" is the vehicle you want to modify the function for, and "new_temp_function" 
is your custom function that takes in at least a 1D, 3-element array and outputs the temperature.

::

    import holoocean
    import numpy as np
    from pynput import keyboard
    from multiprocessing import Process, Queue
    import time
    from holoocean.environments import HoloOceanEnvironment
    from queue import Empty

    def temp_fx(location):
        # NOTE: It's required that we name this parameter "location"
        x, y, z = location
        base_temp = 4
        alpha = -.2
        beta = .05
        return base_temp + alpha * z + beta * y

    scenario = {
        "name": "test_currents",
        "world": "PierHarbor",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 60,
        "frames_per_sec": 60,
        "agents": [
                {
                    "agent_name": "auv0",
                    "agent_type": "HoveringAUV",
                    "sensors": [
                        {
                            "sensor_type": "BSTSensor",
                            "socket": "COM",
                            "configuration": {
                                "biomass_clusters": [{"position":[10, 10, -10], "strength": 2, "falloff": 10}]
                            }
                        },
                        {
                            "sensor_type": "LocationSensor",
                            "socket": "COM"
                        }
                    ],
                "control_scheme": 0,
                "location": [-20, 10, -10]
                }
            ],
        }

    pressed_keys = list()
    force = 200

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

    def parse_keys(keys, val, visualizer=None, location=None):
        command = np.zeros(8)
        if 'i' in keys:
            command[0:4] += val
        if 'k' in keys:
            command[0:4] -= val
        if 'j' in keys:
            command[[4,7]] += .1 * val
            command[[5,6]] -= .1 * val
        if 'l' in keys:
            command[[4,7]] -= .1 * val
            command[[5,6]] += .1 * val

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

        if 'm' in keys:
            if visualizer is not None and location is not None:
                visualizer.update_position(location)
            

        return command

    def plot_process(location_queue, scenario, custom_temp):
        print("Process started")
        visualizer = HoloOceanEnvironment.initialize_bst_graphs(config=scenario, temperature_func=custom_temp)

        while True:
            latest_location = None
            while True:
                try:
                    latest_location = location_queue.get_nowait()
                except Empty:
                    break
            
            if latest_location is not None:
                visualizer.update_position(latest_location)

            time.sleep(.01)

    if __name__ == "__main__":
        time = 0
        with holoocean.make(scenario_cfg=scenario, start_world=False) as env:
            # Here we pass in the custom function into the live graph instance to get accurate figures
            queue = Queue()
            queue.put(scenario["agents"][0]["location"])
            p = Process(target=plot_process, args=(queue, scenario, temp_fx))
            p.start()
            env.set_temperature_function("auv0", temp_fx)
            while True:
                # We need to pass the same custom function into the BST sensor to get accurate readings in the terminal
                sensor_data = env.tick()
                location = sensor_data["LocationSensor"]
                queue.put(location)
                bst_data = sensor_data["BSTSensor"]
                # print(bst_data)
                time += 1

                if '-' in pressed_keys:
                    break
                
                # Your control logic
                command = parse_keys(pressed_keys, force)
                env.act("auv0", command)

            # Clean up
            p.join()