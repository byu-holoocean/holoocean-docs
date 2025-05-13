.. _multi-agent-comms_example:

============================
Multi-Agent Communications
============================

Many times it's necessary to communicate between agents. This can be done using the 
``AcousticBeaconSensor`` or the ``OpticalModemSensor``. Below are some examples of these

Sending Acoustic Messages
=========================

The command :meth:`holoocean.environments.HoloOceanEnvironment.send_acoustic_message` is used to send messages between acoustic beacons.
There's a number of message types that can be sent, all with varying functionality, see :class:`holoocean.sensors.AcousticBeaconSensor`
for details.

Further, a few helper functions exist if needed, 

- :py:attr:`holoocean.environments.HoloOceanEnvironment.beacons` returns all beacons.
- :py:attr:`holoocean.environments.HoloOceanEnvironment.beacons_id` returns all beacons' ids.
- :py:attr:`holoocean.environments.HoloOceanEnvironment.beacons_status` returns all beacons' status (whether it's transmitting or not).

::

    import holoocean

    cfg = {
        "name": "test_acou_coms",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 200,
        "agents": [
            {
                "agent_name": "auv0",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "AcousticBeaconSensor",
                        "location": [0,0,0],
                        "configuration": {
                            "id": 0
                        }
                    },
                ],
                "control_scheme": 0,
                "location": [0, 0, -5]
            },
            {
                "agent_name": "auv1",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "AcousticBeaconSensor",
                        "location": [0,0,0],
                        "configuration": {
                            "id": 1
                        }
                    },
                ],
                "control_scheme": 0,
                "location": [0, 100, -5]
            }
        ]
    }

    env = holoocean.make(scenario_cfg=cfg)
    env.reset()

    # This is how you send a message from one acoustic com to another
    # This sends from id 0 to id 1 (ids configured above)
    # with message type "OWAY" and data "my_data_payload"
    env.send_acoustic_message(0, 1, "OWAY", "my_data_payload")

    for i in range(300):
        states = env.tick()
        if "AcousticBeaconSensor" in states['auv1']:
            # For this message, should receive back [message_type, from_sensor, data_payload]
            print(i, "Received:", states['auv1']["AcousticBeaconSensor"])
            break
        else:
            print(i, "No message received")


Sending Optical Messages
========================

The command :meth:`holoocean.environments.HoloOceanEnvironment.send_optical_message` is used to send messages between optical modems.
See :class:`holoocean.sensors.OpticalModemSensor` for configuration details. Note in order for a message to be transmitted,
the 2 sensors must be aligned.

Further, a few helper functions exist if needed, 

- :py:attr:`holoocean.environments.HoloOceanEnvironment.modems` returns all modems.
- :py:attr:`holoocean.environments.HoloOceanEnvironment.modems_id` returns all modems' ids.

::

    import holoocean

    cfg = {
        "name": "test_acou_coms",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 200,
        "agents": [
            {
                "agent_name": "auv0",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "OpticalModemSensor",
                        "location": [0,0,0],
                        "socket": "SonarSocket",
                        "configuration": {
                            "id": 0
                        }
                    },
                ],
                "control_scheme": 0,
                "location": [25, 0, -5],
                "rotation": [0, 0, 180]
            },
            {
                "agent_name": "auv1",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "OpticalModemSensor",
                        "location": [0,0,0],
                        "socket": "SonarSocket",
                        "configuration": {
                            "id": 1
                        }
                    },
                ],
                "control_scheme": 0,
                "location": [0, 0, -5]
            }
        ]
    }

    env = holoocean.make(scenario_cfg=cfg)
    env.reset()

    # This is how you send a message from one optical com to another
    # This sends from id 0 to id 1 (ids configured above)
    # with data "my_data_payload"
    env.send_optical_message(0, 1, "my_data_payload")

    for i in range(300):
        states = env.tick()
        if "OpticalModemSensor" in states['auv1']:
            print(i, "Received:", states['auv1']["OpticalModemSensor"])
            break
        else:
            print(i, "No message received")