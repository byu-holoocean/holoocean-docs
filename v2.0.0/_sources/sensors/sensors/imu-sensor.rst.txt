===============================
Inertial Measurement Unit (IMU)
===============================

Simulates an IMU sensor, potentially with noise added but defaults to no noise. Return is in a 2D 
numpy array of either 2x3 (default) or 4x3 (with biases).

See :py:class:`~holoocean.sensors.IMUSensor` for the python API and more details.

Example sensor definition::

    {
        "sensor_type": "IMUSensor",
        "socket": "IMUSocket",
        "Hz": 200,
        "configuration": {
            "AccelSigma": 0.00277,
            "AngVelSigma": 0.00123,
            "AccelBiasSigma": 0.00141,
            "AngVelBiasSigma": 0.00388,
            "ReturnBias": true
        }