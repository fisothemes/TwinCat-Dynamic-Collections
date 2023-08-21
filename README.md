# TwinCAT Dynamic Collections

A TwinCAT library for creating and manipulating dynamic collections of data in TwinCAT. It provides multiple data structures such as ArrayList (a dynamic array), List (a doubly linked list that is optimized for sequential access and mutation), Set, Map, Queue, Stack and more. Examples are in the project.

TwinCAT Dynamic Collections is written in Structured Text and is available under the MIT license. It is easy to use and can be integrated into any TwinCAT project.

Here are some of the features of Dynamic Collections:

* **Fast and efficient** 

  The collections in the library use data structures and algorithms along with optimisations that make them well-suited for PLCs allowing for fast and efficient access to data.

* **Easy to use** 

  The library provides a simple and intuitive interface for handling data.

* **Extendable** 

  The takes advantage of interfaces and the ANY type to support new algorithms and for handling any datatype.


## Function Blocks

* 👍 **FB_Collection** - Abstract class/Function Block that all collections inherit, contains many methods and base implementation for methods and properties for creating a collection. Implements `I_Collection`.

* 👍 **FB_Array** - An array that can store multiple datatypes whose size is fixed. Implements `I_Array`.

* 👍 **FB_Array_List** - A dynamic array that can grow and shrink as needed. Can store multiple types. Implements `I_List`.

* 👍 **FB_List** - A doubly linked list with iterator hint optimisation. Essentially the linked list keeps track of the node it last accessed. Iteration starts from the closest node (head, tail or last accessed) to the access/mutation index. This should result in sequential access times of O(1) and similar times for access/mutation on the same index. Can store multiple types. Implements `I_List`.

* 👍 **FB_Tree_Map** - A collection of key-value pair items implemented using an iterative AVL Tree. Keys and values can be retrieved as an immutable list (whose base is FB_ArrayList) via 4 traversal methods; Inorder, Preorder, Postorder and Level Order. Can store multiple types. Implements `I_Tree_Map` which inherits `I_Map`.

* 👍 **FB_Tree_Set** - A collection that contains no duplicate items implemented using an iterative AVL Tree. Keys and values can be retrieved as an immutable list (whose base is FB_ArrayList) via 4 traversal methods; Inorder, Preorder, Postorder and Level Order. Can store multiple types. Implements `I_Tree_Set` which inherits `I_Set`.

* 👍 **FB_Queue** - A collection whose access/mutation of items is first-in, first-out whose base is FB_List. Can store multiple types. Implements `I_Queue`.

* 👍 **FB_Stack** - A collection whose access/mutation of items is last-in, first-out whose base is FB_List. Can store multiple types. Implements `I_Stack`.

## Interface UML

![TwinCAT Collections Interface UML](./assets/images/TwinCAT%20Dynamic%20Collections%20Interface%20UML.jpg)

## Simple List Examples 

**Declarations:** 
```js
fbArray      : FB_Array(3);
fbArray_List : FB_Array_List(0);
fbList       : FB_List; 

sData   : STRING := 'Cats'; // variable that holds string data
nData   : DINT := 1234567; // variable that holds 32-bit int data
stData  : ST_DATA := (bMammals := TRUE, sDescription := 'Twin cats'); // variable that holds struct data

// variable to store returned data same as, "bVar := TRUE"
sRTNData    : STRING;
nRTNData    : DINT;
stRTNData   : ST_DATA; 

Arr_Count,
Arr_List_Count,
List_Count : T_Capacity; // variables will hold the number of items in the collection
```

**Implementation:**
```js
fbArray
    .Set(0, sData)
    .Set(1, nData)
    .Set(2, stData)
    .Reverse()
    .Get(2, sRTNData)
    .Get(1, nRTNData)
    .Get(0, stRTNData);
Arr_Count := fbArray._Count;

fbArray_List
    .Append(sData)
    .Append(nData)
    .Append(stData)
    .Swap(0,2)
    .Get(2, sRTNData)
    .Get(1, nRTNData)
    .Get(0, stRTNData);
Arr_List_Count := fbArray_List._Count;

fbList
    .Prepend(sData)
    .Prepend(nData)
    .Prepend(stData)
    .Get(2, sRTNData)
    .Get(1, nRTNData)
    .Get(0, stRTNData);

List_Count := fbList._Count;
```

## Simple Queue and Stack Examples 

```js
FOR i := 0 TO 2 DO
    fbQueue.Enqueue(i);
    END_FOR

fbQueue.Reverse();

WHILE NOT fbQueue._Empty DO
    fbQueue.Get(Values[j]).Dequeue();
    fbStack.Push(Values[j]);
    j := j + 1;
    END_WHILE

WHILE NOT fbStack._Empty DO
    fbStack.Get(Values[k]).Pop();
    k := k + 1;
    END_WHILE
```

## Simple Tree Set Example

**Declarations:** 
```js
fbSet : FB_Tree_Set; 

arnData,
arnItems : ARRAY[0..5] OF DINT := [3,1,2,1,3,2];
ipItems : I_Immutable_List;
Count : T_Capacity;
```
**Implementation:**
```js
FOR i := 0 TO 5 DO
    fbSet.Insert(i);
    END_FOR

Count := fbSet._Count; // Value is 3

fbSet._Traverse := T_BST_Traversal.In_Order; // will get the value in ascending order

ipItems := fbSet.Get_Values();
ipItems
    .Get(0, arnItems[0])
    .Get(1, arnItems[1])
    .Get(2, arnItems[2]);
```

## Simple Tree Map Example 

**Declarations:** 
```js

fbTree_Map : FB_Tree_Map;
ipKeys     : I_Immutable_List;
ipValues   : I_Immutable_List;

arKeys        : ARRAY[0..6] OF WSTRING := ["qwerty","play","thomas","jerry","perry","sarah"];
arValues      : ARRAY[0..6] OF WSTRING := ["Cats","Dogs","Ravens","Mollies","Anaconda","Cow"]
arUpdate      : ARRAY[0..1] OF WSTRING := ["Python", ""];
arRTNData     : ARRAY[0..6] OF WSTRING; // Array to store values retrieved using a key
arTravData    : ARRAY[0..1] OF ARRAY[0..9] OF STRING; // array containg all keys and values
rmvdVal       : WSTRING;
```
**Implementation:**
```js
// Insert data into map
fbTree_Map
       .Insert(arKeys[0], arValues[0])
       .Insert(arKeys[1], arValues[1])
       .Insert(arKeys[2], arValues[2])
       .Insert(arKeys[3], arValues[3])
       .Insert(arKeys[4], arValues[4])
       .Insert(arKeys[5], arValues[5]);

// Retrieve data using keys
fbTree_Map
       .Get(arKeys[0], arRTNData[0])
       .Get(arKeys[1], arRTNData[1])
       .Get(arKeys[2], arRTNData[2])
       .Get(arKeys[3], arRTNData[3])
       .Get(arKeys[4], arRTNData[4])
       .Get(arKeys[5], arRTNData[5]);

// Update a values of keys
fbTree_Map
       .Update(arKeys[1], arUpdate[0])
       .Update(arKeys[2], arUpdate[0]);

// Get and remove
fbTree_Map
       .Get(arKeys[3], rmvdVal)
       .Remove(arKeys[3]);

// Retrieve all keys and values
fbTree_Map._Traversal := T_BST_Traversal.Inorder // Sets traversal method in which keys/values are to be retrieved.
ipKeys := fbTree_Map.Get_Keys();
ipValues := fbTree_Map.Get_Values();
FOR i := 0 TO fbTree_Map._Count - 1 DO 
    ipKeys
        .Get_As_String(i, arTravData[0][i]);
    ipValues
        .Get_As_String(i, arTravData[1][i]); 
    END_FOR
```

# Developer Notes
Version 1 (v1.x.x.x) is still a work in progress. It is not backward compatible with version 0 (v0.x.x.x). If you were using version 0 a new branch has been created for it and updates will only be for bug fixes. 

Version 0 branch: [Click here!](https://github.com/fisothemes/TwinCat-Dynamic-Collections/tree/v0)

As always feel free to contribute or report issues.

# ⚠ Important ⚠ 

Be careful when storing `STRUCT`s or `FUNCTION BLOCK`s that contain `STRING`s or `WSTRING`s. You may not be able to retrieve them with any search operation method which includes keys to retrieve a value in a map. This is because strings are null delimited, so any junk characters after the null character are retained. Equality of `STRUCT`s and `FUNCTION BLOCK`s are checked using `MEMCMP`. For `FUNCTION BLOCK`s I recommend you store them using interfaces or pointers. For `STRUCT`s, clear any strings inside using `MEMSET` and set them to your chosen value before you store them. If you have questions I'm happy to answer them.
