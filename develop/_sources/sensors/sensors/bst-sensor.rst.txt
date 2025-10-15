===============
Biomass, Salinity, and Temperature (BST) Sensor
===============

Simulates the distribution and sampling of biomass, salinity, and temperature throughout a world based on real data.

See :ref:`sampling_bst` for an example of how to use this sensor.

See :py:class:`~holoocean.sensors.BSTSensor` for the Python API.

In order to pass a custom function into the BST sensor for biomass, salinity, or temperature, call the following command at 
the beginning of your script. More info on customizing the BST sensor found in the example configuration below, the example script linked above, 
and the API docs:
``set_temperature_function(new_function)`` where "new_function" is a pointer to your custom function that takes in only the parameter "location" (3 element array)

---------------
Graphing
---------------
There is an implementation for graphing BST data live by calling the following commands:
``visualizer = env.initialize_bst_graphs()``, with different graphing parameters found in the API docs and in the example
``visualizer.update(location)``, where location is the live location taken from the location sensor

Note: In order to simplify the coordinate system BST sampling and graphing is based upon world coordinates. As such, changing the surface level of the 
world will not transform the sampling from the sensor or the graphs. If you wish to incorporate a dynamic surface level, simply upload your custom 
BST functions incorporating those dynamics.

Below is an example of what the live graphing looks like when ran. Note that the distributions of the graphs themselves differ from the example config 
below in that each is the standard, default distribution models. The only additionaly parameters that went into the distribution models were a couple 
biomass clusters to display how they appear on the heat maps.

.. image:: ../BSTGraph.PNG

Example sensor definition::
    
    {
        "sensor_type": "BSTSensor",
        "socket": "COM",
        "Hz": 1,
        "configuration": {
            "max_biomass": 2.0,
            "max_concentration_depth": 150.0,
            "attenuation_exponent": 1.2,
            "biomass_clusters": [
                {
                    "position": [10, 20, -50],
                    "strength": 0.5,
                    "falloff": 15
                },
                {
                    "position": [5, -10, -75],
                    "strength": 0.8,
                    "falloff": 20
                }
            ],
            "surface_psu": 31.0,
            "deep_psu": 35.5,
            "halocline_depth": 120,
            "halocline_thickness": 25,
            "salinity_clusters": [
                {
                    "position": [15, 5, -100],
                    "strength": 0.3,
                    "falloff": 10
                }
            ],
            "surface_temp": 26.0,
            "deep_temp": 2.0,
            "thermocline_depth": 110,
            "thermocline_thickness": 30,
            "thermo_clusters": [
                {
                    "position": [-10, 0, -60],
                    "strength": 1.0,
                    "falloff": 12
                },
                {
                    "position": [20, 10, -90],
                    "strength": 0.4,
                    "falloff": 25
                }
            ]
        }
    }