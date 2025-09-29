.. image:: images/holoocean-logo.png


.. figure:: images/inspect_plane.jpg


Welcome to HoloOcean's documentation!
==============================================

HoloOcean is a high-fidelity simulator develped by the `Field Robotic Systems Lab (FRoStLab) <https://frostlab.byu.edu>`_
at `Brigham Young University <https://www.byu.edu>`_.
Built upon Unreal Engine (by Epic Games) and Holodeck (developed by the BYU PCCL Lab), HoloOcean enables easy simulation of marine robotics and autonomy with a wide variety of sensors, agents, and features.

Features
""""""""
#. 3+ rich worlds with various infrastructure for generating data or testing underwater algorithms
#. Complete with common underwater sensors including DVL, IMU, optical camera, various sonar, depth sensor, and more
#. Highly and easily configurable sensors and missions
#. Multi-agent missions, including optical and acoustic communications
#. Novel sonar simulation framework for simulating imaging, profiling, sidescan, and echosounder sonars
#. Imaging sonar implementation includes realistic noise modeling for small sim-2-real gap
#. Easy installation and simple, OpenAI Gym-like Python interface
#. High performance - simulation speeds of up to 2x real time are possible. Performance penalty only for what you need
#. Run headless or watch your agents learn
#. Linux and Windows support

Attribution and Relevent Publications
"""""""""""""""""""""""""""""""""""""
If you use HoloOcean in your research, please cite the following publications depending on the features you use as outlined below:

General HoloOcean use:
::
      
   @inproceedings{Potokar22icra,
      author = {E. Potokar and S. Ashford and M. Kaess and J. Mangelson},
      title = {Holo{O}cean: An Underwater Robotics Simulator},
      booktitle = {Proc. IEEE Intl. Conf. on Robotics and Automation, ICRA},
      address = {Philadelphia, PA, USA},
      month = may,
      year = {2022}
   }

Simulation of Sonar (Imaging, Profiling, Sidescan) sensors:
::
   
   @inproceedings{Potokar22iros,
      author = {E. Potokar and K. Lay and K. Norman and D. Benham and T. Neilsen and M. Kaess and J. Mangelson},
      title = {Holo{O}cean: Realistic Sonar Simulation},
      booktitle = {Proc. IEEE/RSJ Intl. Conf. Intelligent Robots and Systems, IROS},
      address = {Kyoto, Japan},
      month = {Oct},
      year = {2022}
   }

.. toctree::
   :maxdepth: 2
   :caption: HoloOcean Documentation

   usage/installation
   usage/getting-started
   usage/usage
   packages/packages
   agents/agents
   sensors/sensors
   env_appearance/env_appearance
   examples/examples
   sensors/sensors
   examples/examples
   develop/develop
   changelog/changelog

.. toctree::
   :maxdepth: 3
   :caption: API Documentation

   holoocean/index
   holoocean/agents
   holoocean/environments
   holoocean/spaces
   holoocean/commands
   holoocean/holooceanclient
   holoocean/packagemanager
   holoocean/sensors
   holoocean/lcm
   holoocean/dynamics
   holoocean/shmem
   holoocean/util
   holoocean/exceptions

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
