.. _fb_collection:

FB_Collection (Function Block)
==============================

Abstract class/Function Block that all collections inherit.
Contains inheritable helper methods and base implementation
for methods and properties for creating a collection.

**Implements:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _fb_collection._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_collection._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_collection._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

Methods
-------

.. _fb_collection.clear_error:

Clear_Error
~~~~~~~~~~~

.. _fb_collection.decrement_count:

Decrement_Count
~~~~~~~~~~~~~~~

Decrement collection count by 1.

.. _fb_collection.increment_count:

Increment_Count
~~~~~~~~~~~~~~~

Increments collection count by 1
