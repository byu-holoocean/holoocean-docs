.. _`viewport`:

========
Viewport
========

HoloOcean simulations are run in a pop-up window known as the "viewport". 


.. _`hotkeys`:

Hotkeys
=======
There are a few hotkeys you can use to control the viewport when the window is open and the 
environment is being ticked (with calls to :meth:`~holoocean.environment.HoloOceanEnvironment.tick` 
or :meth:`~holoocean.environment.HoloOceanEnvironment.step`). 

The "AgentFollower", or the camera that the viewport displays, can be 
manipulated as follows:

+----------+-----------------------+-----------------------------------------+
| Key      | Action                | Description                             |
+==========+=======================+=========================================+
| ``c``    | Toggle camera mode    | Toggles the camera from a chase camera  |
|          |                       | and perspective camera, which shows what|
|          |                       | the agent's camera sensor sees.         |
+----------+-----------------------+-----------------------------------------+
| ``v``    | Toggle spectator mode | Toggles spectator mode, which allows you|
|          |                       | to free-cam around the world with the   |
|          |                       | mouse or WASD commands.                 |
+----------+-----------------------+-----------------------------------------+
| ``w``    | Move camera           | Move the viewport camera around when in |
| ``a``    |                       | spectator/free-cam mode.                |
| ``s``    |                       |                                         |
| ``d``    |                       |                                         |
+----------+-----------------------+-----------------------------------------+
| ``q``    | Descend               | For spectator/free-cam mode             |
| ``ctrl`` |                       |                                         |
+----------+-----------------------+-----------------------------------------+
| ``e``    | Ascend                | For spectator/free-cam mode             |
| ``space``|                       |                                         |
+----------+-----------------------+-----------------------------------------+
| ``shift``| Turbo                 | Move faster when in spectator/free-cam  |
+----------+-----------------------+-----------------------------------------+
| ``tab``  | Cycle through agents  | When not in spectator/free-cam mode,    |
|          |                       | cycles through the agents in the world  |
+----------+-----------------------+-----------------------------------------+
| ``h``    | Toggle HUD            | The HUD displays the name and location  |
|          |                       | of the agent the viewport is following, |
|          |                       | or the location of the camera if the    |
|          |                       | viewport is detached (spectator mode)   |
|          |                       |                                         |
|          |                       | Note that this will interfere with the  |
|          |                       | ViewportCapture sensor                  |
+----------+-----------------------+-----------------------------------------+

Opening Console
===============

Pressing ``~`` will open Unreal Engine 5's developer console, which has a few useful 
commands. See `the Unreal Docs <https://api.unrealengine.com/udk/Three/ConsoleCommands.html>`_
for a complete list of commands.

**Useful Commands**

- ``stat fps``
  Prints the frames per second on the screen.


.. _`headless`:

Using HoloOcean Headless
=========================

On Linux, HoloOcean can run headless without opening a viewport window. This
can happen automatically, or you can force it to not appear.

Headless Mode vs Disabling Viewport Rendering
---------------------------------------------

These are two different features.

**Disabling Viewport Rendering** is calling the 
(:meth:`~holoocean.environments.HoloOceanEnvironment.should_render_viewport`) 
method on a :class:`~holoocean.environments.HoloOceanEnvironment`. This can be
done at runtime. It will appear as if the image being rendered in the viewport
has frozen, but cameras other sensors will still update correctly.

**Headless Mode** is when the viewport window does not appear. If Headless
Mode is manually enabled, it will also disable viewport rendering
automatically.

Forcing Headless Mode
---------------------

In :func:`holoocean.make`, set ``show_viewport`` to ``False``. 

.. note::
   This will also
   disable viewport rendering 
   (:meth:`~holoocean.environments.HoloOceanEnvironment.should_render_viewport`)

   If you still want to render the viewport (ie for the 
   :class:`~holoocean.sensors.ViewportCapture`) when running headless,
   simply set 
   (:meth:`~holoocean.environments.HoloOceanEnvironment.should_render_viewport`)
   to ``True``

Automatic Headless Mode
-----------------------

If the engine does not detect the ``DISPLAY`` environment variable, it will
not open a window. This will happen automatically if HoloOcean is run from a
SSH session.

.. note::
   This will not disable viewport rendering, meaning the simulaito nwill still be generating the 
   displayed images, but they will not be displayed. When running over an SSH session, 
   be sure to manually disable viewport rendering to avoid wasting resources.
