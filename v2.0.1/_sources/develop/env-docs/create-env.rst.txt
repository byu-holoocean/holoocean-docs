.. _`create-env`:

=======================
Creating a Custom Level
=======================

For a custom level in HoloOcean, you must make a level using Unreal Engine. See the `Unreal Engine documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine?application_version=5.3>`_ for
more information on saving and creating a new level.

There are 2 main aspects to our HoloOcean levels: the landscape, and the water. 

Landscape
=========

For help creating your own landscape, please reference `Unreal Engine's landscape documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine>`_.
The documentation explains how to use the Landscape Mode within the editor, as well as how to apply and create materials for your landscape. 

.. note::
    As you create a landscape, please note that the water level is at z=0. The landscape must be below z=0 in order for our underwater agents to work as expected. 

To aquire materials or assets for your landscape, you can purchase materials or find some free ones at `Fab <https://www.fab.com/>`_. `Quixel <https://www.fab.com/sellers/Quixel>`_ offers many free assets and materials.

If you wish to enclose the sides of your environment, you can either place assets like walls or sculpt the edges of the landscape to be taller. Both examples can be seen in the SimpleUnderwater environment.

.. image:: images/landscape-example.png

Water
=====

**The Unreal Engine Water plugin is not compatible with HoloOcean and will not work.** Instead, to achieve an underwater appearance, 
you will need to place a water plane, ExponentialHeightFog, and a PostProcessVolume within your environment. Please note the following are suggested settings, and there may be others you would want to consider adjusting for your level.

Water Plane
-----------

For the water plane, place a plane actor at z=0. Change the material to be any water-like material. You will also need to change the collision settings so that vehicles can pass through the plane. In the Details panel, search for "collision" and set custom collision presets to ignore all options.

.. image:: images/plane_settings.png

Fog
---

If you created a basic level, it should already come with an ExponentialHeightFog located in the Lighting folder in the level outliner. Otherwise, go to Window ➡ Env. Light Mixer ➡ Create Height Fog. 
As a note, the other lighting options through the Env. Light Mixer should also be added to the level, although no changes to them need to be made.

Adjust the ExponentialHeightFog "Fog Distance", "Fog Height Fallout", and "Fog Inscattering Color" in the details panel until it fits your needs. For example, the Dam environment has a "Fog Density" of 0.4, "Fog Height Falloff" of 0.2, and "Fog Inscattering Color" of Hex sRGB B2D1FFFF. 

PostProcessVolume
-----------------

For the PostProcessVolume, go to Place Actors ➡ Volumes ➡ Post Process Volume and drag it into your level. Adjust the scale of the volume to fit your entire underwater area. To adjust the color of the volume, go to the Details pannel ➡ Color Grading ➡ Misc ➡ "Scene Color Tint". 
Blue to green colors are best, and the Dam environment has the "Scene Color Tint" set to Hex sRGB AAD9C8FF. 

As seen in the Dam environment, the water plane is a separate landscape located at z=0. The red outline box that surrounds the environment is the PostProcessVolume. 

.. image:: images/water_w_postprocess.png

Adding Objects
==============

Obtaining Assets
----------------

To populate your level with assets, you will either need to import your own assets or find assets on `Fab <https://www.fab.com/>`_. 

To replicate similar levels as HoloOcean, we use the following asset packs:

* :ref:`dam`: 
    * `Ocean Floor Environment <https://www.fab.com/listings/0c40a773-c71b-4c51-9286-721126fd9b0f>`_ 
* :ref:`openwater`: 
    * `Modular Dam Environment <https://www.fab.com/listings/f6ff3c58-7fcd-43b8-bc0a-55ab6c405e1b>`_
* :ref:`pierharbor`: 
    * `Container Ships <https://www.fab.com/listings/d15bb4d9-e292-4bc0-a058-14aee645f69e>`_ 
    * `Boat Pack Vol_1 <https://www.fab.com/listings/7e671469-af0a-4516-88a4-dfffefdbc640>`_
    * `Pier Set <https://www.fab.com/listings/4a89aaec-7b13-46b6-957e-667262149c12>`_
    * `Modular Harbor Building Kit <https://www.fab.com/listings/aeed2616-24b1-4bb9-8fde-cd268602dfcc>`_

Importing Assets
----------------
If you have purchased or obtained free assets from Fab, you can view them in the Epic Games Launcher under the Unreal Engine Library tab. 
Under the "Fab Library" section, you can click on "Add To Project" and select your project to add the assets. 

If you are importing your own models, it is best to save them as FBX files. From there, you can click on the "Import" button from within the Unreal Engine editor and select your FBX file.
Please reference `Unreal Engine's Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine?application_version=5.3>`_
for further help with importing assets. 

Placing Assets
--------------
From the Content Drawer, you can drag and drop your assets into your custom level. Or, you can select the icon of the cube with the green plus symbol to quickly add actors such as basic shapes to your level.

.. image:: images/place-actor.png

It is simple to move, rotate, and scale objects within your level. You can either directly edit these values within the Details panel or use keyboard shortcuts.

.. list-table::
   :widths: 25 35
   :header-rows: 1

   * - Key
     - Action
   * - W
     - Selects the Move tool
   * - E
     - Selects the Rotate tool
   * - R
     - Selects the Scale tool

::

For more information please reference `Unreal Engine's Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/transforming-actors-in-unreal-engine>`_.

.. _object-collision:

Note on Collision Settings for Objects and Sonar
================================================

Sonar simulation relies upon the collision mesh for objects when generating the octree. 

First, make sure to set the environment boundaries to have the environment min and max. 
In standalone through Unreal Engine, this would be done by setting the Additional Launch Parameters as seen here: :ref:`live-game`.
If you have packaged your worlds, this would be set in the config file. 

.. warning::
   Octrees must be regenerated for a level whenever an object is changed or moved. To regenerate the octrees, delete the octree folder and rerun your simulation. Please see :ref:`octree` for the octree location.
 
If the collision mesh of an object is coarser than the visual mesh then the representation of
that object in a sonar image will be inaccurate. This issue can be addressed for the objects
by using the Unreal Engine editor and setting the “Collision Complexity” option in the 
details section of the static mesh editor to “use complex collision as simple”.

.. image:: images/collision_setting.png

If you still have issues with your collision mesh, it is often helpful to enable "Double Sided Geometry" in the details panel of the static mesh editor.

.. image:: images/static_mesh_double_sided.png

Finally, within the level, click on the object and go to the details panel. Go to the collision section and enable "Simulation Generates Hit Events".

.. image:: images/level_collision_settings.png

You can verify the shape of the collision mesh by changing the view mode to "Player Collision" in the level or in the static mesh editor.

.. image:: images/check_collisions.png

Testing Your Custom Level
=========================

For quick testing of your level, it is often easiest to run in standalone mode. This will allow you to 
quickly verify collision settings or visuals without having to package the level. 
Please reference :ref:`live-game` to run your level from within the Unreal Engine Editor. 

Otherwise, you will have to package your level after each change. Please reference :ref:`packaging-environments` for information.
