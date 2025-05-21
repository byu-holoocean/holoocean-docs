===============
Optical Modem
===============

An optical modem for communications for aerial or surface agents.

The command :meth:`holoocean.environments.HoloOceanEnvironment.send_optical_message` is used to send 
messages between optical modems.

..note::
    In order for a message to be transmitted, the 2 sensors must be aligned.

Further, a few helper functions exist if needed:

- :py:attr:`holoocean.environments.HoloOceanEnvironment.modems` returns all modems.
- :py:attr:`holoocean.environments.HoloOceanEnvironment.modems_id` returns all modem ID's.

See :ref:`multi-agent_example` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.OpticalModemSensor` for the python API.

Example sensor definition::

    {
        "sensor_type": "OpticalModemSensor",
        "location": [0,0,0],
        "configuration": {
            "id": 1
        }
    }