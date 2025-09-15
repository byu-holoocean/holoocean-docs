.. _installation:

============
Installation
============


Base Requirements
=================

Depending on your installation method, other requirements may be necessary, but these are prerequisites that apply to all installation methods.

- GitHub account that is linked to an Epic Games account -- please `Follow the steps here <https://www.unrealengine.com/en-US/ue-on-github>`_ and remember to **accept the email invitation from Epic Games.**
- 64-bit Linux or Windows Operating System

While we don't have known minimal requirements, we recommend having:

- a dedicated GPU
- 8 GB of RAM or more
- Quad-core Intel or AMD CPU, 2.5 GHz or faster

Overview
========

Cloning HoloOcean
-----------------
For all installation methods the first step is to clone the repository.

To get the most recent stable release of the HoloOcean library, download or clone our repo at: 
https://github.com/byu-holoocean/HoloOcean. We suggest cloning it with lowercase naming, as our 
example code uses, like so:
::

   git clone git@github.com:byu-holoocean/HoloOcean.git holoocean

.. note::
   
   If you get a Page Not Found Error when trying to access the repository, it means you have not 
   linked your GitHub account to your Epic Games account. Please refer to the instructions above.


Installation Options
--------------------

Depending on your use case, different installation methods may apply. Please refer to the following list and determine 
the instructions that are most appropriate for your purposes.

- :ref:`Standard Packaged installation <install-packaged>` – Simplest method for using HoloOcean out of the box.
- :ref:`Development with Unreal Editor installation <install-dev>` – Method that should be used if you desire to customize the simulation such as developing custom worlds, agents, or sensors.
- :ref:`Docker-based installation <install-docker>` – Alternate setup using preconfigured Docker containers.

HoloOcean is installed in two parts:

1. The Python client library (``holoocean``), which is installed first.
2. The world packages (binaries), which are downloaded by the Python package after installation.

The Python portion is lightweight, but the world packages can be several gigabytes in size.


.. _install-packaged:

Standard Packaged Installation
==============================

Additional Requirements
-----------------------
- Python >= 3.7
- pip3
- For Linux: OpenGL 3+, gcc (minimum build-essential package) 
.. TODO i think you dont need open gl anymore?? vulkan? mention that pip will install numpy, scipy.. etc?

For the build-essential package for Linux, you can run the following console command:
::

   sudo apt install build-essential

Python Library
--------------
From the cloned repository, install the Python package by doing the following:
::

   cd holoocean/client
   pip install .

Worlds Packages
---------------
.. note::

   The Ocean package is the only package currently available. Users can create custom worlds and 
   packages if desired. 

To install the most recent version of the Ocean worlds package, open a Python shell by typing the 
following and hit enter:
::

   python

Install the package by running the following Python commands:
::

   import holoocean
   holoocean.install("Ocean")

To do these steps in a single console command, use:
::

   python -c "import holoocean; holoocean.install('Ocean')"


.. _install-dev:

Installation for Development with Unreal Editor
===============================================

If you desire to customize the simulation such as developing custom worlds, agents, or sensors,
you will need to be able to modify C++ engine code that implements the simulation using Unreal Engine.
This can be done in multiple ways:

- Standalone Live Editing using Unreal Editor Tools - Unreal provides tools that enable you to edit your own worlds and modify C++ engine code and then build and test your worlds in real-time. 
- Packaged Custom Worlds - After developing HoloOcean using these tools, you can then package your own worlds for later use.

For more detailed instructions on installation for development, see :ref:`develop`.


.. _install-docker:

Installation with Docker
========================

Holoocean Docker Containers
--------------------------

The `docker` directory contains resources to build and run Docker containers for 
the HoloOcean project, which integrates Unreal Engine 5 (UE5) and the HoloOcean client. 
The setup supports GPU-accelerated simulation and X11 display forwarding.

Requirements
------------

Before using the containers, ensure the following are installed and configured on your host system:

.. warning::

   Running these containers on a Windows host machine may cause problems with GPU access.
   The instructions provided below are intended for a Linux host machine.

- **CUDA and NVIDIA Drivers**

  - Install CUDA and a compatible NVIDIA driver. CUDA version and NVIDIA driver version are dependent on system requirements.
  - See the `official NVIDIA documentation <https://docs.nvidia.com/cuda/>`_ for installation instructions.

- **NVIDIA Container Toolkit** 

  - Required for GPU passthrough to Docker containers.
  - Follow the `official installation guide <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html>`_ to set up the toolkit and configure Docker.

- **Docker**

  - Ensure Docker Engine is installed and the daemon is running. Issues may occur when running Docker Desktop with the NVIDIA Container Toolkit.
  - See the `official Docker installation guide <https://docs.docker.com/engine/install/>`_.
  - Follow `Post-installation steps <https://docs.docker.com/engine/install/linux-postinstall/>`_ for Linux to run Docker without sudo.


Overview
--------

The provided Docker containers enable both development and runtime workflows for HoloOcean. 
The Python/client development container is designed for interactive development and compilation of HoloOcean, limited to changes of Python source code, 
whereas the runtime container is intended for executing pre-built HoloOcean applications
in a minimal environment.

For advanced Docker usage, consult the Docker and NVIDIA Container Toolkit documentation.

This repository provides two main container types:

Runtime Container
-----------------


- **Purpose:** For running pre-built HoloOcean applications and distributing HoloOcean internally.
- **Features:**

  - Minimal environment (no build tools).
  - HoloOcean code is pre-installed.
  - Intended for deployment and production.

- **Availability:**

  - Not distributed publicly online due to the Epic Games End User License Agreement (EULA).

- **Building:**

  - The Docker image must be built locally and cannot be pulled from Docker Hub. 
    Build the image using the Dockerfile located in the `docker/runtime` directory.

- **Usage**


   1. Allow display access by running on the host machine:

      .. code-block:: bash
         
         xhost +local:docker

   2. Navigate to the runtime directory inside the ``docker`` folder:

      .. code-block:: bash 

         cd docker/runtime

   3. To start a container, use ``docker compose up`` with the following options:

      - ``-d``: Run the container in detached mode.
      - ``--build``: Build the Docker image before starting the container.
      
      To build the image and start the container in detached mode, run:

      .. code-block:: bash

         docker compose up --build -d

   4. Test the example script:

      .. code-block:: bash

         docker cp ../../client/example.py holoocean:/home/ue4  # Copy the example script into the container
         docker exec -it holoocean bash   # Create bash terminal inside the container
         
      
      Inside the container run: 

      .. code-block:: bash
         
         python3 -c "from example import *; torpedo_example()"

   5. To stop and remove the container, run from the same directory:

      .. code-block:: bash

         docker compose down


Python/Client Development Container
-----------------------------------

- **Purpose:** For active development and compilation of the HoloOcean Python client (non-engine code).
- **Features:**

  - Source code is volume-mounted for live editing.
  - Includes all necessary build tools.
  - Suitable for iterative testing and debugging HoloOcean Python client code. 

- **Availability:**

  - Pre-built Docker images are available on Docker Hub.
  - Docker containers can be built and modified locally.


- **Usage**


   1. Allow display access by running on the host machine:

      .. code-block:: bash
         
         xhost +local:docker

   2. Navigate to the development directory inside the ``docker`` folder
      and change permissions of build cache for isolated pip installation:

      .. code-block:: bash 

         cd docker/dev
         sudo chmod -R a+w build_cache/ 
   
   3. To start a container, use ``docker compose up`` with the following options:

      - ``-d``: Run the container in detached mode.
      - ``--build``: Build the Docker image before starting the container.
      
      To start a container in detached mode run:

      .. code-block:: bash

         docker compose up -d

      If no local image is found, then the image will be attempted to be pulled from Docker Hub.

   4. Test the example script:

      .. code-block:: bash

         docker exec -it holoocean bash   # Create bash terminal inside the container
         
      
      Inside the container run: 

      .. code-block:: bash

         cd client
         python3 -c "from example import *; torpedo_example()"

   5. To stop and remove the container, run from the same directory:

      .. code-block:: bash

         docker compose down
   


Troubleshooting
---------------

- **Display Issues:**

  - Ensure ``xhost +local:docker`` has been run on the host.
  - Confirm the ``DISPLAY`` environment variable is set.
  - Make sure your X11 server is running and Docker has access.

- **CUDA Version:**

  - Ensure that the CUDA version used in the Docker container is:
   - Lower than or equal to your host CUDA installation
   - Compatible with your NVIDIA Driver
  - Change CUDA versions by modifying the Dockerfiles

- **Verify GPU Access:**

  - Inside the container, run:

    .. code-block:: bash

       nvidia-smi

- **Docker Not Found:**

  - Ensure Docker is properly installed and the daemon is running.



Develop Branch
==============

Both the Python library and the available worlds of HoloOcean are actively being developed. 
These instructions describe how to access the latest development updates. 
You can apply these steps to any of the installation methods described above.

Python Library
--------------
The "release" branch of the GitHub repository contains the latest stable release of the client 
library, while the "develop" branch contains the latest features and bug fixes but may not be 
stable. To install the develop branch, clone the repository as described above, then check out 
the develop branch and reinstall the holoocean package via pip using the commands below:
::

   git checkout develop
   cd holoocean/client
   pip install .

World Packages
--------------
It is advised that you use the development versions of the Ocean package when on the develop branch 
of the library. These will contain the latest updates to the worlds that may be necessary to use 
some features on the develop branch. Using the develop branch with the release version of the worlds 
may result in unexpected behavior. 

To install the development version of the Ocean package, open a Python shell and remove any previous 
versions of the binaries by running the following command:
::
   
   import holoocean
   holoocean.remove("Ocean")

Then install the development version:
::

   holoocean.install("Ocean", branch="develop")