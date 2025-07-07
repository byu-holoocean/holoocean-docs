.. _`octree`:


Octree Generation
=========================

When running an environment with a sonar sensor, octrees must be generated. These can often take up 
several gigabytes of storage, thus aren't feasible as part of the downloaded package.

Upon startup, all octrees within the ``InitOctreeRange`` parameter are created, then more are made as 
the agent moves throughout the environment. This can cause pauses in the simulation the first time it 
is ran. A warning will appear onscreen about this and can be disabled with the ``ShowWarning`` 
parameter. All subsequent simulation runs will use the cached octrees and run much faster. 

One option to avoid waiting times, is to run the simulation without the viewport, and let it generate 
octrees in the background. Here's an example script that does exactly that; just change the scenario 
to the one that you would like to create octrees for.

::

    import holoocean
    import numpy as np
    from tqdm import tqdm

    command = np.array([0,0,0,0,-20,-20,-20,-20])
    print("Building octrees...")
    with holoocean.make("PierHarbor-HoveringImagingSonar", show_viewport=False) as env:
        for i in tqdm(range(1000)):
            env.act("auv0", command)
            state = env.tick()

    print("Finished Simulation")


When octrees are made, they are saved in the :ref:`package-locations` in an octree folder. This will 
be as follows:

========== ==================================================================================================================
 Platform   Octree Save Location
========== ==================================================================================================================
Linux      ``~/.local/share/holoocean/{holoocean_version}/worlds/{world_name}/LinuxNoEditor/Holodeck/Octrees``
Windows    ``%USERPROFILE%\AppData\Local\holoocean\{holoocean_version}\worlds\{world_name}\WindowsNoEditor\Holodeck\Octrees``
========== ==================================================================================================================

In this octree folder, there will be additional folders for each level name, and in those a folder 
for each octree size used. If files are being actively saved here it means that the simulation is 
still running and isn't frozen.