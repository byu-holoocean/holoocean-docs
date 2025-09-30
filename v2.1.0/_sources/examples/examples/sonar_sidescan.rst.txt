.. _visualizing_sidescan_sonar:

Visualizing Sidescan Sonar
===========================

It can be useful to visualize the output of the sonar sensor during a simulation. This script will do 
that, plotting each time sonar data is received.

Note, running this script will create octrees while running and may cause some pauses. See 
:ref:`octree` for workarounds and more info.
::

    import holoocean
    import matplotlib.pyplot as plt
    import numpy as np

    #### GET SONAR CONFIG
    scenario = "OpenWater-TorpedoSidescanSonar"
    config = holoocean.packagemanager.get_scenario(scenario)
    config = config['agents'][0]['sensors'][-1]["configuration"]
    maxR = config['RangeMax']
    binsR = config['RangeBins']

    #### GET PLOT READY
    plt.ion()

    t = np.arange(0,50)
    r = np.linspace(-maxR, maxR, binsR)
    R, T = np.meshgrid(r, t)
    data = np.zeros_like(R)

    plt.grid(False)
    plot = plt.pcolormesh(R, T, data, cmap='copper', shading='auto', vmin=0, vmax=1)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.gcf().canvas.flush_events()

    #### RUN SIMULATION
    command = np.array([0,0,0,0,20])
    with holoocean.make(scenario) as env:
        for i in range(1000):
            env.act("auv0", command)
            state = env.tick()

            if 'SidescanSonar' in state:
                data = np.roll(data, 1, axis=0)
                data[0] = state['SidescanSonar']

                plot.set_array(data.ravel())

                plt.draw()
                plt.gcf().canvas.flush_events()

    print("Finished Simulation!")
    plt.ioff()
    plt.show()