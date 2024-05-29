.. _develop-sensor:

Developing Sensors
===================

Similar to agents, the sensors are built on both the C++ and Python sides.

C++
~~~~~~~~~
Each sensor will need a '.h' and '.cpp' file, as is standard practice for C++. 

These will both be placed in the holoocean-engine repository. Most likely your .h file should be placed in ``holoocean/engine/Source/Holodeck/Sensors/Public``, while your .cpp file should then go in ``holoocean/engine/Source/Holodeck/Sensors/Private``

.h file
---------

You will want to start by including the following in your '.h' file:

.. code:: c++

    #pragma once
    #include "Holodeck.h"
    #include "HolodeckSensor.h"

Next you will want to set up the class for the sensor which will look something like this:

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

A few things to take note of:

* The name of the sensor needs to have the character "U" before it.
* The GENERATED_BODY() function automatically generates some things for you, but in order for it to work you need to also add the following line to your includes using the name of your sensor.  In this case we are using ExampleSensor:

.. code:: c++

    #include "ExampleSensor.generated.h"

Now let's go over a few of the main necessary functions to put into the .h file.  First, make sure your sensor has a constructor and an InitializeSensor() override like this one (Note that these should be under '''public'''):

.. code:: c++

    UExampleSensor();
    virtual void InitializeSensor() override;

Next, in the '''protected''' section, you will need a tick function.  What this function does is defines the behavior of the sensor every time the simulation ticks.  The details of it can be covered later when we get to the '.cpp' file, but for now, just declare it like so:

.. code:: c++

    void TickSensorComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

Finally, the last item that is essential for a sensor is the pointer to the parent agent in the '''private''' section.  This simply stores a reference to whatever object the sensor is attached to.  All you need is the following line of code:

.. code:: c++
    
    AActor* Parent;

You may also want to include some helper functions and some class variables, however, the above should be the bare essentials you need for your custom sensor.

.cpp file
-----------

Now that you are working in the .cpp file, you will want to make sure to include the matching header file along with ``holodeck.h`` and any other libraries you need.  At this point we can start defining the functions.
Let's start with the constructor first. It should look something like the following:

.. code:: c++

    UExampleSensor::UExampleSensor() {
        PrimaryComponentTick.bCanEverTick = true;
        SensorName = "ExampleSensor";
    }

We now also need to initialize the sensor with any variables that it needs to function.  For example, we need to make sure to attach the sensor to it's parent like so:

.. code:: c++

    void UExampleSensor::InitializeSensor() {
        Super::InitializeSensor();
        //You need to get the pointer to the object the sensor is attached to. 
        Parent = this->GetAttachmentRootActor();
    }

Next we can take a look at the tick function.  How this typically works is that you want the engine to return sensor information to the client through the shared buffer.  So let's have our sensor simply return the float 2.0 every time it ticks:

.. code:: c++

    void UExampleSensor::TickSensorComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) { 
        float* FloatBuffer = static_cast<float*>(Buffer);
        FloatBuffer[0] = 2.0;
    }

These should be all of the necessary functions, but you will need to also fill in your other functions from the .h file as well.

Python
~~~~~~~~~
Now that we have our C++ files, we don't actually need to create a new python file for the sensor.  Instead, you will want to open up sensors.py (Found in the holoocean repository at holoocean/src/holoocean/sensors.py) and add a class for your new sensor.  Make sure you set the sensor type as follows as that will be important later.

.. code:: python

    class ExampleSensor(HolodeckSensor):
        sensor_type = "ExampleSensor"

At this point you will also want to initialize anything you need to, but everything not specific to you sensor can be initialized by the super class.  If you have items that need to be initialized, at the very least, you will probably want something that looks like the following:

.. code:: python

    def __init__(self, client, agent_name, agent_type, name="OpticalModemSensor",  config=None):
            super(ExampleSensor, self).__init__(client, agent_name, agent_type, name=name, config=config)

Note that the above is not always necessary, but can be useful in some cases.

The only other things that are required are the data type (dtype) and data shape (data_shape).  These let the client know how what kind of data it should be expecting to receive from the buffer.  Recall that in the .cpp file we set the tick function to return the float 2.0.  We also only returned the single float, not several.  With that in mind we know that the dtype should be a float and the data_shape should be 1.  It should look like this: 

.. code:: python
    
    @property
    def dtype(self):
        return np.float32 #Note that we are using numpy's data types to get the right size for the python data.

    @property
    def data_shape(self):
        return [1]

(Note that the data_shape can store a multi-dimensional array if necessary, so for a 2x2 array return [2, 2].)

Allowing Your Sensor to Be Used In Holoocean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point you have the main body of the sensor mostly figured out.  But there are a couple things we need to modify as well.
First of all, towards the bottom of the sensors.py file there should be a _sensor_keys_ dictionary in the SensorDefinition class.  You will need to add a line to the dictionary so that certain functions can pull the sensor type if given the proper string.  In our case we simply add the following line to the end of the dictionary:

.. code:: python

    "ExampleSensor":ExampleSensor,

Similarly, you will need to find the file AddSensorCommand.h and add a #include for your sensor's .h file before adding the sensor to the AddSensorCommand.cpp SensorMap like this:

.. code:: python
    
    { "ExampleSensor", UExampleSensor::StaticClass() },