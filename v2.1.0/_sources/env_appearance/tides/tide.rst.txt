Tide Controller
==================


HoloOcean worlds have tide settings that can be configured, either with the scenario or real time with commands during simulation.

.. image:: ../images/tidesinaction.gif


Tide Options
~~~~~~~~~~~~~~~

Holoocean worlds have a tide configuration and command. This allows you to set either a consistent tide cycle 
in your world or use env.tide() commands to set or adjust the tide to whatever you want at any point. With the command,
you can either set the tide water level by setting the absolute parameter to be True, or you can offset the current tide level
by setting absolute to be False.

In a scenario 
^^^^^^^^^^^^^
Amplitude is in cm and frequency is in ticks.

.. code-block:: python

   config = {  
      "tide_cycle":{
            "active": True,
            "amplitude": ###,
            "frequency": ###,
         },
      }

Programmatically
^^^^^^^^^^^^^^^^
Usage of commands.

.. code-block:: python

   env = holoocean.make("...")
   #This would set the tide to 1 meter
   env.tide(1, True)
   #This would adjust the tide by -2 meters relative to its current position - setting the tide to -1 meter 
   env.tide(-2, False)

Example of pushing a button to raise tide by 10cm.

.. code-block:: python

   with holoocean.make("...") as env:
      while True:
         if 't' in pressed_keys:
            #Raise tide by 10cm
            env.tide(0.1, False)

.. note::
      For more information on how to use this command, please refer to the API Documentation: 
      :py:class:`~holoocean.command.TideCommand`.