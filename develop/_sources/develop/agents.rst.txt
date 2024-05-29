.. _develop-agents:

Developing Agents
==================
Unfortunately, due to agents needing to exist on the python, C++, and UE4 portions this is a rather involved process. It's not difficult, mostly just tedious, but I'll walk you through it here. 

General Agents
---------------

Python Portion
~~~~~~~~~~~~~~~~~
First, open up ``holodeck/client/src/agents.py``. To create my agent, I usually just copy ``TurtleAgent`` and edit it to my liking. You'll need to edit the following:

* Class name
* agent_type
* Anything related to the controls. This includes all the constants, and ``control_schemes()``. Make sure you put the number of inputs your agent will have in ``ContinuousActionSpace`` in the return

That should be about it for the python portion, you should end up with something like this

.. code:: python

    class CustomAgent(HoloOceanAgent):
        """A simple custom bot.

        Inherits from :class:`HoloOceanAgent`."""
        # constants in CustomAgent.h in holodeck-engine
        __MAX = 160.0
        __MIN = -__MAX

        agent_type = "CustomAgent"

        @property
        def control_schemes(self):
            low = [self.__MIN]*4
            high = [self.__MAX]*4
            return [("[first, second, third, fourth]", ContinuousActionSpace([4], low=low, high=high))]

        def get_joint_constraints(self, joint_name):
            return None

        def __repr__(self):
            return "CustomAgent " + self.name

        def __act__(self, action):
            np.copyto(self._action_buffer, np.array(action))
            np.copyto(self._action_buffer, action)


Lower in the same file, in the ``AgentDefinition`` class, there is a dictionary mapping names to python classes. Add an entry for our new class, something like ``"CustomAgent": CustomAgent,``. The name should match ``agent_type`` set in your class.

C++ Portion
~~~~~~~~~~~~~~~~~

Next, open up ``holodeck/engine`` in UE4. Then go to File->Open Visual Studio (or open your project files in your C++ editor of choice). You'll need to duplicate 4 TurtleAgent files, and rename them accordingly: TurtleAgent.cpp, TurtleAgent.h, TurtleAgentController.cpp, and TurtleAgentController.h should be duplicated to CustomAgent.cpp, CustomAgent.h, CustomAgentController.cpp, and CustomAgentController.h. Make sure they stay in the same folder as the files they're duplicates of (should be in some combination of public/private folders). 

Next, we'll make edits to CustomAgent.h. Do the following:

* ``#include "TurtleAgent.generated.h"`` to ``#include "CustomAgent.generated.h"``
* ``class HOLODECK_API ATurtleAgent : public AHolodeckAgent`` to ``class HOLODECK_API ACustomAgent : public AHolodeckAgent``
* ``ATurtleAgent();`` to ``ACustomAgent();``
* The line ``unsigned int GetRawActionSizeInBytes() const override { return 2 * sizeof(float); };`` change the 2 to however many inputs your agent has
* The line ``float CommandArray[2];`` change the 2 to however many inputs your agent has

CustomAgent.cpp is where most of the magic happens: your dynamics, reactions to inputs, etc should all be here. In it, change all of the following 

* ``#include "TurtleAgent.h"`` to ``#include "CustomAgent.h"``
* All ``ATurtleAgent`` to ``ACustomAgent``
* Anything you want your agent to do, or how it responds to the inputs all need to be put into ``Tick(float DeltaSeconds)``.

In CustomAgentController.h, change all of the following

* ``#include "TurtleAgent.h"`` to ``#include "CustomAgent.h"``
* ``#include "TurtleAgentController.generated.h"`` to ``#include "CustomAgentController.generated.h"``
* All instances of ``ATurtleAgentController`` to ``ACustomAgentController``

In CustomAgentController.cpp, change all of the following

* ``#include "TurtleAgentController.h"`` to ``#include "CustomAgentController.h"``
* All instances of ``ATurtleAgentController`` to ``ACustomAgentController``

That covers the C++ portion.

Unreal Engine 4
~~~~~~~~~~~~~~~~~

This is the one where things can be a little hidden. In UE4, click the compile button on the top toolbar. This will load our new C++ code into UE4. If you get errors, you likely did something wrong in the previous step and will have to go back to debug. Once compiling happens successfully, navigate to ``Content/HolodeckContent/Agents`` in the content browser. Create a new folder for your agent, and go into it. Right click and select to create a blueprint class. You'll now get a dialog asking you to choose your parent class. Choose your C++ class (``CustomAgent``) from the previous step, and name your new blueprint something like CustomAgentBp. Here is where you'll want to insert any meshes, weight, etc to make your agent look/weigh what you want. This is a little tricky sometimes, but there's a bunch of UE4 tutorials online on making custom pawns.

Finally, we'll need to connect our python class with our UE4/C++ code. Navigate to ``Content/`` in the content browser and open up HolodeckGameModeBP. You'll see an entry called Agent Bp Map on the right under the Default section. Expand it, and insert a new entry. On the left choose whatever you put as agent_type in your code before, and on the right, choose the blueprint (CustomAgentBp) that we just created.

That's it! If you find anything unclear/wrong here, feel free to edit it and clarify things for a future reader. You'll need to repackage your environment (see above) and then should be able to use your new agent!



Buoyant Agents
---------------
The ``AHolodeckBuoyantAgent`` class was made to remove the need to re-implement buoyancy dynamics for all future AUVs put into HoloOcean. By setting a few necessary variables everything should basically work out of the box. All of the physics information is set in C++ and not in the blueprint. Anything set in the blueprint (like mass or COM offset) will be overriden in C++.

We're not going to go into details on how to create a custom agent here, see the above section for that. The only difference is you'll need to inherit from ``AHolodeckBuoyantAgent`` instead of ``AHolodeckAgent`` and should probably copy the files of ``AHoveringAUV`` instead of ``ATurtleAgent``. 

Necessary Variables
~~~~~~~~~~~~~~~~~~~
.. note::
    All these variables are stored with respect to to correct origin (without the OffsetToOrigin added into it)

The following MUST be set, either in your class constructor or in the ``InitializeAgent`` function before ``Super::InitializeAgent()`` is called.

.. code:: c++

    float Volume;
    FVector CenterBuoyancy;
    FVector CenterMass;
    float MassInKG;
    FVector OffsetToOrigin = FVector(0,0,0);

These are all basically what you'd expect them to be. You may get away with not setting ``OffsetToOrigin`` if your mesh was imported with the correct pivot point.

Extra Variables
~~~~~~~~~~~~~~~~~~~
.. note:: 
    All these variables are stored with respect to to correct origin (without the OffsetToOrigin and CenterVehicle added into them) EXCEPT ``SurfacePoints``.

These variables can be set to customize various aspects of how surface buoyancy is used, although all of them will be calculated if you don't. Surface Buoyancy is calculated by random sampling points inside of the "Bounding Box" of your vehicle, then checking how many of them are above the surface in real time. You can see this bounding box by opening your static mesh in UE4 and clicking "Bounding Box". This will obviously be a poor approximation if your robot isn't a box, but works for our more boxy vehicles. Alternatively, if you want to sample offline and store the points, you can set them explicitly by hand.

.. code:: c++

    FVector CenterVehicle = FVector(0,0,0); // Center of vehicle from true origin. NEED to set if origin isn't center of vehicle
    int NumSurfacePoints = 1000;
    FBox BoundingBox = FBox();
    TArray<FVector> SurfacePoints;
    float SurfaceLevel = 0;

``CenterVehicle`` is the distance from the true origin to the physical center of your vehicle. It's used to make sure your bounding box is actually where it should be. It MUST be set if you don't use the center of your vehicle as the surface point.

``NumSurfacePoints`` will be the next most likely one you'll set. It's what is sounds like. May need to be larger/smaller based on robot size.

``BoundingBox`` is the bounding box around your vehicle. It's calculated automatically by the mesh if it's not set. You can set this by hand if the auto-calculated one is too large.

``SurfacePoints`` are the sampled points. Set explicitly if you don't want to use the bounding box method. NOTE: These are stored with ``OffsetToOrigin`` and ``CenterVehicle`` pre-added to reduce complexity. (IE we don't want to do the same 2*NumSurfacePoints additions every tick)

``SurfaceLevel`` is the water level. For all of our environments, this has been set to 0.

Debugging Tools
~~~~~~~~~~~~~~~~~~~
To be able to visualize the bounding box and surface points to make sure they're placed currently, you can use the inherited functions ``ShowBoundingBox()`` and ``ShowSurfacePoints()`` functions in your agents tick method.