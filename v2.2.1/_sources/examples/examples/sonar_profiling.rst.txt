.. _visualizing_profiling_sonar:

Visualizing Profiling Sonar
============================

It can be useful to visualize the output of the sonar sensor during a simulation. This script will do 
that, plotting each time sonar data is received.

Note, running this script will create octrees while running and may cause some pauses. See 
:ref:`octree` for workarounds and more info.
::

    import holoocean
    import matplotlib.pyplot as plt
    import numpy as np

    #### GET SONAR CONFIG
    scenario = "OpenWater-TorpedoProfilingSonar"
    config = holoocean.packagemanager.get_scenario(scenario)
    config = config['agents'][0]['sensors'][-1]["configuration"]
    azi = config['Azimuth']
    minR = config['RangeMin']
    maxR = config['RangeMax']
    binsR = config['RangeBins']
    binsA = config['AzimuthBins']

    #### GET PLOT READY
    plt.ion()
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(8,5))
    ax.set_theta_zero_location("N")
    ax.set_thetamin(-azi/2)
    ax.set_thetamax(azi/2)

    theta = np.linspace(-azi/2, azi/2, binsA)*np.pi/180
    r = np.linspace(minR, maxR, binsR)
    T, R = np.meshgrid(theta, r)
    z = np.zeros_like(T)

    plt.grid(False)
    plot = ax.pcolormesh(T, R, z, cmap='gray', shading='auto', vmin=0, vmax=1)
    plt.tight_layout()
    fig.canvas.flush_events()

    #### RUN SIMULATION
    command = np.array([0,0,0,0,20])
    with holoocean.make(scenario) as env:
        for i in range(1000):
            env.act("auv0", command)
            state = env.tick()

            if 'ProfilingSonar' in state:
                s = state['ProfilingSonar']
                plot.set_array(s.ravel())

                fig.canvas.draw()
                fig.canvas.flush_events()

    print("Finished Simulation!")
    plt.ioff()
    plt.show()