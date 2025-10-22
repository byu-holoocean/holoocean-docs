.. _flashlight:

===========
Flashlight
===========

HoloOcean vehicles have one or more built-in flashlights that are **off by default**.

Location
~~~~~~~~~

The location and number of flashlights vary by vehicle:

    * :ref:`BlueROV2 Flashlights <bluerov2-flashlights>`
    * :ref:`HoveringAUV Flashlights <hoveringauv-flashlights>`
    * :ref:`CougUV Flashlights <couguv-flashlights>`
    * :ref:`TorpedoAUV Flashlights <torpedoauv-flashlights>`
    * :ref:`SurfaceVessel Flashlights <surfacevessel-flashlights>`

Commands
~~~~~~~~

.. image:: ../images/flashlights_hov.gif
   :scale: 40%
   
There are two commands available to control the flashlights, `TurnOnFlashlightCommand` and `TurnOffFlashlightCommand`. The `TurnOnFlashlightCommand` allows you to optionally customize several parameters, such as: intensity, beam width, location, rotation, and color.

.. note::  
    Flashlight color values use normalized RGB in the range **0.0 – 1.0**, not the standard 0 – 255 scale.

Refer to the Python API documentation for full usage details:
   
- :py:class:`~holoocean.command.TurnOnFlashlightCommand`
- :py:class:`~holoocean.command.TurnOffFlashlightCommand`

Usage Example (for a HoveringAUV/BlueROV2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a scenario
++++++++++++++

.. code-block:: python

    config = {
        "name": "test_flashlight",
        "main_agent": "auv0",
        ...
        "flashlight":[
            {
                "flashlight_name": "flashlight1",
                "intensity": 10000,
                "beam_width": 60,
            },
            {
                "flashlight_name": "flashlight4",
                "intensity": 10000,
                "color_G": 0,
                "angle_pitch": -30,
            },
        ]
    }


Programmatically
++++++++++++++++

.. code-block:: python

    with holoocean.make("...") as env:
        while True:
            if 'o' in pressed_keys:
                env.turn_on_flashlight("flashlight1") 
                env.turn_on_flashlight("flashlight4", beam_width=80, color_B=0) #Turning on flashlight 4 with a beam width of 80 degrees and turning the blue color component to zero

            if 'p' in pressed_keys:
                env.turn_off_flashlight("flashlight1")
                env.turn_off_flashlight("flashlight4")

            env.tick()

.. note::  
    When calling ``turn_on_flashlight("flashlight_number")`` without specifying additional parameters, the system will first look for values defined in the scenario config. If the flashlight was configured there, those values become its defaults. Only if no config values are found will the command fall back to its built-in default parameters.  
