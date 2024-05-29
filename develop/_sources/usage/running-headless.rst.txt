Using HoloOcean Headless
=========================

On Linux, HoloOcean can run headless without opening a viewport window. This
can happen automatically, or you can force it to not appear

Headless Mode vs Disabling Viewport Rendering
---------------------------------------------

These are two different features.

**Disabling Viewport Rendering** is calling the 
(:meth:`~holoocean.environments.HoloOceanEnvironment.should_render_viewport`) 
method on a :class:`~holoocean.environments.HoloOceanEnvironment`. This can be
done at runtime. It will appear as if the image being rendered in the viewport
has frozen, but :class:`~holoocean.sensors.RGBCamera` s and other sensors will 
still update correctly.

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
   This will not disable viewport rendering.
