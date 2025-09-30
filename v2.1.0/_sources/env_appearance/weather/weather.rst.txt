Weather Controller
==================


HoloOcean worlds have weather settings that can be configured, either with scenarios or programmatically in real time.
Weather is purely a visual effect; it does not impact vehicle movement or sensor data input.


Weather Options
~~~~~~~~~~~~~~~

Type
----

.. image:: ../images/weather.gif
   :scale: 40%

HoloOcean worlds have three possible types of weather: ``0 - sunny``,
``1 - cloudy``, and ``2 - rainy``.

In a scenario
^^^^^^^^^^^^^

.. code-block:: python

   config = {
      "name": "weather_test",
      ...
      "weather": {
         "type": 0
      }
   }

Programmatically
^^^^^^^^^^^^^^^^

.. code-block:: python

   with holoocean.make("...") as env:
      while True:
         env.change_weather(0)
         ...
         env.tick()


Rain parameters
~~~~~~~~~~~~~~~

In rainy weather, you can programmatically customize the rain's velocity and spawn rate (the number of rain particles). This feature is only available during simulation and **not** through scenario configuration.

.. image:: ../images/rain_spawn_rate.gif 
   :scale: 40%

Velocity
--------

Rain velocity is defined by three components: ``x``, ``y``, and ``z``, corresponding to movement along each axis. These can be used to simulate wind:

- **x** component: Controls horizontal tilt (left/right) relative to the world frame.
- **y** component: Controls horizontal tilt (forward/backward) relative to the world frame.
- **z** component: Controls vertical speed. This value **must be negative** for the rain to fall downward. A positive ``z`` will make the rain rise, effectively making it invisible around the vehicle.

A good starting point for mildly tilted rain is::

    velocity = (0, 400, -1000)


Spawn Rate
----------

This parameter defines how many rain particles are generated. Typical values for realistic rain effects range from **1000 to 4000**. You can adjust this to simulate light or heavy rain as needed.

.. warning::

    Setting the spawn rate too high (e.g., in the millions) can severely affect performance or crash the simulation.

Usage
^^^^^

To set rain parameters, use the following command::

    set_rain_parameters(vel_x, vel_y, vel_z, spawn_rate)

If not explicitly set, the default rain settings are::

    velocity = (0, 300, -1000)
    spawn_rate = 3000


Programmatically
^^^^^^^^^^^^^^^^

.. code-block:: python

   with holoocean.make("...") as env:
      while True:
         env.change_weather(2)  # Set weather to rain here or in the config
         env.set_rain_parameters(0,400,-1000, 2000)  # Custom rain behavior
         ...
         env.tick()



.. note::
         For more information on how to use these commands, please refer to the API Documentation: 
         :py:class:`~holoocean.command.ChangeWeatherCommand` and :py:class:`~holoocean.command.SetRainParametersCommand`.