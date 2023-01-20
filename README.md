# TwinCAT Dynamic Collections

A library for handling collections of data dynamically.
Create python like maps and lists (a collections that can hold multiple-type data and can grow or shrink at runtime). True Queue and Stack data structures, in the form of list adaptors, are also contained here. Examples are in project.

# Function Blocks

* 👍 **FB_Collection** - Abstract class/Function Block that all collections inherit, handles contains many helper methods and properties for creating a collection. Implements `I_Collection`.

* 👍 **FB_List** - Python like List. Can store and operate on data of any size and type at runtime. The base is a singly-linked-list with a tail. Multi-type lists are supported. Implements `I_List`.

* 👍 **FB_Array_List** - Same as FB_List except it's implementation uses a Dynamic Array instead of a Linked List, similar to vectors in C++. Can store and operate on data of any size and type at runtime. Multi-type lists are supported. Implements `I_List`.

* 👍 **FB_Tree_Map** - Key-Value pair collection often referred to as a Dictionary or Map in other programming languages such as Python, C#, C++ etc. It's a called a Tree Map because its base is a binary search tree. Multi-type lists are supported. Implements `I_Tree_Map` which inherits from `I_Map`.

* ⚡ **FB_Hash_Map (W-I-P)** - Key-Value pair collection often referred to as a Dictionary or Map in other programming languages such as Python, C#, C++ etc. It's a called a Hash Map because it used a hash function to compute an index that is associated to the bucket the Key-Value pair is to be stored in a bucket list. Multi-types are supported. Implements `I_Map`.

* 👍 **FB_Binary_Search_Tree** - A regular Binary Search Tree. The tree can be traversed using the 4 main traversal methods; Inorder, Preorder, Postorder and Level Order. Strict and Multi-types are supported. Implements `I_Binary_Search_Tree`.

* 👍 **FB_Queue** - Standard Queue Data Struture. This is an adapter for Function Blocks/Classes that implement `I_List`. Implements `I_Queue`.

* 👍 **FB_Stack** - Standard Stack Data Struture. This is an adapter for Function Blocks/Classes that implement `I_List`. Implements `I_Stack`.

* 👍 **FB_Read_Only_List** - This is an adapter for Function Blocks/Classes that implement `I_List`. This will restrict operation to an implementor of `I_List` to read-only methods/properties. Implements `I_Read_Only_List`.

* 👍 **FB_Write_Only_List** - This is an adapter for Function Blocks/Classes that implement `I_List`. This will restrict operation to an implementor of I_List to write-only methods/properties. Implements `I_Write_Only_List`.

# Interface UML

![TwinCAT Collections Interface UML](./assets/images/TwinCAT%20Dynamic%20Collections%20Interface%20UML.bmp)

# Simple Example 

This example demostrates how a STRING, DINT and STRUCT can be stored in the queue data structure.

**Declarations:** 
```Pascal
(* implements I_List, used to store data. *)
fbList  : FB_List; 
(* implements I_Queue, will perform queue operations on any class that implements I_List *)
fbQueue : FB_Queue;

sData   : STRING;   // variable that holds string data
nData   : DINT;     // variable that holds 32-bit int data
stData  : ST_DATA := (bMammals := TRUE, sDescription := 'Twin cats');  // variable that holds data in the form of a struct

(* variable to store returned data same as, "bVar := TRUE"*)
sRTNData    : STRING;
nRTNData    : DINT;
stRTNData   : ST_DATA; 

nCount1, nCount2 : DINT; // variable will hold the number of items in the queue
```
**Implimentation:**
```Pascal
fbQueue(ipList := fbList); // tell FB_Queue which list implementation you want to operate on. Can swap lists at runtime.

sData := 'Cats'; 
fbQueue.Enqueue(sData); // Enqueues a copy of string data to fbList
nData := 1234567;
fbQueue.Enqueue(nData) // Enqueues a copy of 32-bit int data
       .Enqueue_At_Front(stData); // Enqueues stData at the front of the queue

nCount1 := fbQueue._Count; // should return 3

fbQueue.Dequeue(stRTNData) // removes data at the front of the queue and stores it's contents on stRTNData
       .Reverse() // reverse the queue
       .Peek(sRTNData, 1) // returns data at location at stores it on sRTNData without removing it.
       .Peek(nRTNData, 0);

nCount2 := fbQueue._Count; // should return 2

```
- - -
**TcXaeShell Screenshots:**

![Simple Example Implementation Online](./assets/images/Simple%20Example%20TcXaeShell%20Screencap.JPG)

![Simple Example Declarations Online](./assets/images/Simple%20Example%20TcXaeShell%20Screencap%202.JPG)


# Simple Tree Map Example 

Demostration on how to use the Tree Map data structure. The Tree Map balances itself whenever the collection count reaches a multiple of 4. You can also manually balance it by using the `<FB_Tree_Map instance>.balance()` method.

**Declarations:** 
```Pascal
(* implements I_Tree_Map which inherits I_Map, used to store data. *)
fbTree_Map    : FB_Tree_Map;
arKeys        : ARRAY[0..6] OF WSTRING := ["qwerty","play","thomas","jerry",   "perry",    "sarah"];
arValues      : ARRAY[0..6] OF WSTRING := ["Cats",  "Dogs","Ravens","Mollies", "Anaconda", "cow"]
arUpdate      : ARRAY[0..1] OF WSTRING := ["Python", ""];
arRTNData     : ARRAY[0..6] OF WSTRING; // Array to store values retrieved using a key
arTravData    : ARRAY[0..1] OF ARRAY[0..9] OF STRING; // array containg all keys and values
rmvdVal       : WSTRING;
```
**Implimentation:**
```Pascal
(* Insert data to map*)
fbTree_Map
       .Insert(arKeys[0], arValues[0])
       .Insert(arKeys[1], arValues[1])
       .Insert(arKeys[2], arValues[2])
       .Insert(arKeys[3], arValues[3])
       .Insert(arKeys[4], arValues[4])
       .Insert(arKeys[5], arValues[5]);

(* Retrieve data using keys *)
fbTree_Map
       .Get(arKeys[0], arRTNData[0])
       .Get(arKeys[1], arRTNData[1])
       .Get(arKeys[2], arRTNData[2])
       .Get(arKeys[3], arRTNData[3])
       .Get(arKeys[4], arRTNData[4])
       .Get(arKeys[5], arRTNData[5]);

(* Update a value of a key *)
fbTree_Map
       .Update(arKeys[1], arUpdate[0])
       .Update(arKeys[2], arUpdate[0]);

(* Get and remove *)
fbTree_Map
       .Get(arKeys[3],rmvdVal)
       .Remove(arKeys[3]);

(* Retrieve all keys and values *)
fbTree_Map._Traversal := T_BST_Traversal.Inorder // Sets traversal method in which keys/values are to be retrieved.
FOR i := 0 TO fbTree_Map._Keys._Count-1 DO 
       fbTree_Map
              ._Keys
              .Get_Value_As_String(i, sItem => arTravData[0][i]);
       fbTree_Map
              ._Values
              .Get_Value_As_String(i, sItem => arTravData[1][i]); 
END_FOR

(* Clear Map *)
fbTree_Map
       .Clear();
```

# Simple Binary Search Tree Example 

Demostration on how to use the Binary Search Tree (BST) data structure. The BST balances itself whenever the collection count reaches a multiple of 4. You can also manually balance it by using the `<FB_Binary_Search_Tree instance>.balance()` method.

**Declarations:** 
```Pascal
fbDINT_BST : FB_Binary_Search_Tree(T_Type.TYPE_DINT);    // Declare a DINT Only BST
fbWSTR_BST : FB_Binary_Search_Tree(T_Type.TYPE_WSTRING); // Declare WSTRING only BST
fbANY_BST  : FB_Binary_Search_Tree(T_Type.TYPE_ANY);     // Declare Multi-type BST
(* NOTE: Not all types of T_Type are supported yet *)
```

**Implimentation:**
```Pascal
(* Insert data to BST*)
fbBST
    .Insert(Value1)
    .Insert(Value2);

(* Find out is a value is stored in the BST *)
fbBST
    .Find(Value, bFound => bFound);

(* Traverse BST and store values in a list *)
fbBST
    .Traverse(T_BST_Traversal.Postorder, fbList); // fbList is where you want to store all values from the BST traversal. A collection must implement I_Generic_List

(* Remove value from BST *)
fbBST
    .Remove(Value, bSuccess => bRemoved);

(* Method chaining operations *)
fbBST
    .Insert(Value1)
    .Insert(Value2, bSuccess => bSuccess)
    .Find(Value, bFound => bFound)
    .Traverse(T_BST_Traversal.Postorder, fbList)
    .Remove(Value)
    .Balance();
```

# Developer Notes
As aways feel free to contribute or report issues.

# ⚠ Important ⚠ 
Be careful when storing `STRUCT`s or `FUNCTION BLOCK`s that contain `STRING`s or `WSTRING`s. You may not be able to retrieve them with a `find` method nor be able to use the as keys to retrieve a value in a map. This is because strings are null delimited so any junk characters after the null character are retained. Equality of `STRUCT`s and `FUNCTION BLOCK`s are checked using `MEMCMP`. For `FUNCTION BLOCK`s I recommend you store them using interfaces or pointers. For `STRUCT`s, clear any strings inside using `MEMSET` and set it to your chosen value before you store it. If you have questions I'm happy to answer them.
