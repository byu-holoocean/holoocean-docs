Time of Day Controller
========================


HoloOcean worlds support a configurable time-of-day setting, which can be set either 
through scenarios or programmatically in real time. Additionally, a day cycle frequency
can be defined in the scenario.


.. image:: ../images/time_cycle.gif 
   :scale: 70%


Time
~~~~~~

The time of day can be set using a floating-point number between `0` and `24`, representing the desired hour. For example, `13.5` corresponds to 1:30 PM.
This system assumes a simplified day–night cycle: sunrise occurs at 6:00 AM and sunset at 6:00 PM.  


In a scenario
^^^^^^^^^^^^^

.. code-block:: python

   config = {
      "name": "time_test",
      ...
      "time_cycle": {
         "active": True,
         "hour": 12
      }
   }

Programmatically
^^^^^^^^^^^^^^^^

.. code-block:: python

   with holoocean.make("...") as env:
      while True:
         env.change_time_of_day(12) # set time to 12 PM
         ...
         env.tick()


Day cycle
~~~~~~~~~

The duration of the day cycle is defined in simulation ticks.  
For example, if `ticks_per_sec = 60` and the `time_cycle` frequency is set to 600, the full day cycle will last about 10 seconds (600 ticks ÷ 60 ticks per second).

In a scenario
^^^^^^^^^^^^^

.. code-block:: python

   config = {
      "name": "time_cycle_test",
      ...
      "time_cycle": {
         "active": True,
         "frequency": 600
      }
   }


.. note::
      For more information on how to use this command, please refer to the API Documentation: 
      :py:class:`~holoocean.command.ChangeTimeOfDayCommand`.   