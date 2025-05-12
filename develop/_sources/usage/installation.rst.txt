.. _installation:

============
Installation
============

.. note::

   In accordance with the Unreal Engine EULA, we cannot offer HoloOcean through pypi. Before 
   installing HoloOcean, you must make an Epic Games account, link it to your GitHub account, and 
   accept the Unreal Engine EULA. `Follow the steps here. 
   <https://www.unrealengine.com/en-US/ue-on-github>`_ After linking the accounts, you can proceed 
   to install HoloOcean. **Please remember to accept the email invitation from Unreal Engine.**

.. note::
   
   HoloOcean has updated from using Unreal Engine 4.27 to 5.3. If you are developing worlds, agents, 
   sensors, etc. using Unreal, you will need to download Unreal Engine 5.3 to develop from the 
   current release and develop branches. Unreal Engine 4.27 usage is still available using previous 
   releases of HoloOcean. 

HoloOcean is installed in two portions: a client python library (``holoocean``) is installed first, 
which then downloads world packages. The python portion is very small, while the world packages 
("binaries") can be several gigabytes.


Requirements
============
- Python >= 3.7
- Several gigabytes of storage
- pip3
- Linux or Windows 64bit
- Preferably a competent GPU
- For Linux: OpenGL 3+, gcc (minimum build-essential package) 

For the build-essential package for Linux, you can run the following console command:
::

   sudo apt install build-essential

Installation
=============

Python Library
--------------
To install the most recent stable release of the HoloOcean library, download or clone our repo at: 
https://github.com/byu-holoocean/HoloOcean. We suggest cloning it with lowercase naming, as our 
example code uses, like so:
::

   git clone git@github.com:byu-holoocean/HoloOcean.git holoocean

.. note::
   
   If you get a Page Not Found Error when trying to access the repository, it means you have not 
   linked your GitHub account to your Epic Games account. Please refer to the instructions above.

From the cloned repo, install the package by doing to following:
::

   cd holoocean/client
   pip install .

Worlds Packages
---------------
.. note::

   The Ocean package is the only package currently available. Users can create custom worlds and 
   packages if desired. 

To install the most recent version of the Ocean worlds package, open a python shell by typing the 
following and hit enter:
::

   python

Install the package by running the following python commands:
::

   import holoocean
   holoocean.install("Ocean")

To do these steps in a single console command, use:
::

   python -c `import holoocean; holoocean.install("Ocean")`


Installation for Development
============================

Both the python library and the available worlds of HoloOcean are actively being developed. 
These instructions describe how to access the most recent development updates. 

For more detailed instructions on installation for development, see :ref:`develop`.

Python Library
--------------
The "release" branch of the GitHub repository contains the latest stable release of the client 
library, while the "develop" branch contains the latest features and bug fixes but may not be 
stable. To install the develop branch, clone the repository as described above, then check out 
the develop branch and rebuild the package:
::

   git checkout develop
   cd holoocean/client
   pip install .

World Packages
--------------
.. note::

   Development versions of the HoloOcean worlds are auto-generated for Linux machines, but not for
   Windows. Windows binaries are currently compiled manually and may not be up-to-date with the
   latest changes. To get development versions of the Windows worlds, please reach out to the 
   HoloOcean team.

It is advised that you use the development versions of the Ocean package when on the develop branch 
of the library. These will contain the latest updates to the worlds that may be necessary to use 
some features on the develop branch. Using the develop branch with the release version of the worlds 
may result in unexpected behavior. 

To install the development version of the Ocean package, open a python shell and remove any previous 
versions of the binaries by running the following command:
::
   
   import holoocean
   holoocean.remove("Ocean")

Then install the development version:
::

   holoocean.install("Ocean", branch="develop")
