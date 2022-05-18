# TwinCAT Dynamic Collections

A library for handling collections of data dynamically.
Create python like lists (a list containing multiple data type that can grow or shrink at runtime), true Queue and Stack data structures. Examples are in project.

# Function Blocks

* 👍 **FB_Collections** - Abstract class/Function Block that all collections inherit, handles the passing internal errors to the outside world. Implements I_Collections.
* 👍 **FB_List** - Python like List. Can store and operate lists of any size and type at runtime. Multi-type lists are supported. Implements I_List.
* 👍 **FB_Queue** - Standard Queue Data Struture. Can perform queue operations on any class/Function Block that implements I_List. Implements I_Queue.
* 👍 **FB_Stack** - Standard Stack Data Struture. Can perform stack operations on any class/Function Block that implements I_List. Implements I_Stack.

# Simple Example 

This example demostrates how a STRING, DINT and STRUCT can be stored in the queue data structure.

**Declarations:** 
```Pascal
(* implements I_List, used to store data. *)
fbList  : FB_LIST; 
(* implements I_Queue, will perform queue operations on any class that implements I_List *)
fbQueue : FB_QUEUE;

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
**TcXaeShell Screencap:**

![Front Panel](./assets/images/Simple%20Example%20TcXaeShell%20Screencap.JPG)

![Front Panel](./assets/images/Simple%20Example%20TcXaeShell%20Screencap%202.JPG)
- - -




