.. _develop-sensor:

==================
Developing Sensors
==================

Similar to agents, sensors are built on both the C++ and Python sides. In this section we will give
an example of developing a sensor and explain how to set it up in both C++ and Python.

The example sensor we will be using is a simple sensor that returns the float ``2.0`` at each tick.
This is a very simple sensor, but it will give you the basic structure of how to set up a sensor.

C++
===
Each sensor will need a '.h' and '.cpp' file, as is standard practice for C++. 

These will both be placed in ``engine/Source/Holodeck/Sensors``, with the ``.h`` in Public and the 
``.cpp`` in Private.

.h file
-------
Start by including the following in your ``.h`` file:

.. code:: c++

    #pragma once
    #include "Holodeck.h"
    #include "HolodeckSensor.h"

Next, set up the class for the sensor:

.. code:: c++

    #include "ExampleSensor.generated.h"

    UCLASS(ClassGroup = (Custom), meta = (BlueprintSpawnableComponent))
    class HOLODECK_API UExampleSensor : public UHolodeckSensor {
        GENERATED_BODY()
        public:
            ...
        protected:
            ...
        private:
            ...
    };
.. note::

    * The name of the sensor needs to have the character "U" before it.
    * ``#include "ExampleSensor.generated.h"`` is necessary for Unreal Engine to generate the proper 
      code for the sensor. This is a requirement for all classes that are derived from UObjects.

Now let's go over a few of the main necessary functions to put into the .h file. First, make sure 
your sensor has a constructor and an InitializeSensor() override like this one (note that these 
should be under the ``public`` section of the class):

.. code:: c++

    UExampleSensor();
    virtual void InitializeSensor() override;

Next, in the ``protected`` section, you will need a tick function. This function defines the behavior 
of the sensor every time the simulation ticks.

.. code:: c++

    void TickSensorComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

Finally, the last item that is essential for a sensor is the pointer to the parent agent in the 
``private`` section. This simply stores a reference to whatever object the sensor is attached to:

.. code:: c++
    
    AActor* Parent;

You may also want to include some helper functions and some class variables. We suggest a function 
that defines your sensor model. 

.cpp file
---------

Now that you are working in the .cpp file, make sure to include the matching header file along with 
``holodeck.h`` and any other libraries you need. Next we will define our necessary functions.

Start with the constructor. It should look something like the following:

.. code:: c++

    UExampleSensor::UExampleSensor() {
        PrimaryComponentTick.bCanEverTick = true;
        SensorName = "ExampleSensor";
    }

Initialize the sensor with any variables that it needs to function. For example, make sure to attach 
the sensor to its parent:

.. code:: c++

    void UExampleSensor::InitializeSensor() {
        Super::InitializeSensor();
        //You need to get the pointer to the object the sensor is attached to. 
        Parent = this->GetAttachmentRootActor();
    }

Next, set up the ``.tick()`` function. This returns your sensor's output, which is sent to the client 
through the shared buffer. This is where you would call your sensor model that implements the sensor. 
For our example, we will have our sensor return the float ``2.0`` at each tick:

.. code:: c++

    void UExampleSensor::TickSensorComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) { 
        float* FloatBuffer = static_cast<float*>(Buffer);
        FloatBuffer[0] = 2.0;
    }

These are all of the necessary functions. Fill in your other functions from the .h file as needed.

Python
======
In ``client/src/holoocean/sensors.py``, add a class for your new sensor. Set the sensor type as 
follows:

.. code:: python

    class ExampleSensor(HolodeckSensor):
        sensor_type = "ExampleSensor"

Everything not specific to your sensor can be initialized by the super class. If you have sensor-
specific items that need to be initialized, do something like the following:

.. code:: python

    def __init__(self, client, agent_name, agent_type, name="OpticalModemSensor",  config=None):
            super(ExampleSensor, self).__init__(client, agent_name, agent_type, name=name, config=config)

Note that the above is not always necessary, but can be useful in some cases.

The only other requirements for your sensor class are the data type (dtype) and data shape 
(data_shape). These let the client know how what kind of data it should be expecting to receive from 
the buffer. 

Recall that in our example .cpp file we set the tick function to return the float ``2.0``. We also 
only returned a single float. With that in mind, we know that the dtype should be a float and the 
data_shape should be 1. It should look like this: 

.. code:: python
    
    @property
    def dtype(self):
        return np.float32 # Note that we are using numpy's data types to get the right size for the python data.

    @property
    def data_shape(self):
        return [1]

.. note::
    The data_shape can store a multi-dimensional array if necessary, so for a 2x2 array return [2, 2].

Allowing Your Sensor to Be Used In Holoocean
============================================

At this point the main structure of the sensor is implemented. The following steps make your sensor 
available to the HoloOcean client.

First, towards the bottom of the ``sensors.py`` file there should be a _sensor_keys_ dictionary in the 
``SensorDefinition`` class. Add a line to the dictionary for your sensor:

.. code:: python

    "ExampleSensor":ExampleSensor,

Next, in ``engine/Source/Holodeck/ClientCommands/Public/AddSensorCommand.h``, add an include statement 
for your sensor's .h file:

.. code:: c++

    #include "ExampleSensor.h"

Lastly, in the corresponding ``AddSensorCommand.cpp``, add an entry for your sensor in the SensorMap 
dictionary:

.. code:: c++
    
    { "ExampleSensor", UExampleSensor::StaticClass() },



Your sensor should now be available to use HoloOcean!