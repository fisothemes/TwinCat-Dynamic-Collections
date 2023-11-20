# TwinCAT Dynamic Collections V2 Proposal

## Reason for Version 2

The purpose of the version 2 update is to improve error handling, optimise memory usage, enhance access control, and provide more robust iterability and queryability for existing data structures. These are the things a user of any collections library cares about. The design philosophy of version 2 differs from the previous version, iterability and queryability now lead the design decisions. This means new interfaces and features will have to be introduced and these break backward compatibility.

## Understanding the design notations

| Symbol      | Description                       |
| ----------- | --------------------------------- |
| I_          | Interface prefix                  |
| FB_         | Function Block prefix             |
| T_          | Alias type prefix                 |
| E_          | Enum prefix                       |
| ST_         | Struct prefix                     |
| ~>          | Inheritance                       |
| ->          | Returns                           |
| =>          | Output variable/parameter         |
| {set;}      | Setter accessor method            |
| {get;}      | Getter accessor method            |
| {get;set;}  | Getter and Setter accessor method |
| {FINAL;}    | Final access specifier            |
| {ABSTRACT;} | Abstact access specifier          |

### Notation Examples

```plaintext
FB_ChildClass ~> FB_ParentClass : I_ChildInterface ~> I_ParentInterface
	+ Method(arg : INT, e => : T_Error) -> STRING
	+ Property : BOOL {get; set;}
```
This means that `FB_ChildClass` inherits from `FB_ParentClass`, and it also implements `I_ChildInterface`, which itself inherits from `I_ParentInterface`. The class has a method named `Method` that takes an `INT` parameter (`arg`) and an output parameter (`e`) of type `T_Error`, returning a `STRING`. Additionally, the class has a property named `Property` of type `BOOL` with both get and set accessor methods.

## Aliases

| Identifier   | Asssignment               |
| ------------ | ------------------------- |
| T_Position   | LINT                      |
| T_Size       | UDINT                     |
| T_ErrorCode  | E_ErrorCode               |
| T_Queryable  | __SYSTEM.IQueryInterface  |
| T_Generic    | __SYSTEM.AnyType          |
| T_TypeClass  | __SYSTEM.TYPE_CLASS       |
| T_Error      | FB_Error                  |

## Error Handling

The new approach to error handling involves representing errors as instances of classes that inherit from FB_Error. This allows for a more modular and extensible error-handling system, where specific error types can be created by inheriting from FB_Error and overriding the Code and Message properties.

```plaintext
I_Error ~> T_Queryable
	+ Code -> T_ErrorCode {get;}
```
This interface defines the standard structure for error objects within the collections library. It includes a `Code` property, representing the error code, which is of type `T_ErrorCode`.

```plaintext
FB_Error : I_Error
	+ Code -> T_ErrorCode {get;}
    + Message -> T_MaxString {get;}
    + HasError -> BOOL {get;} {FINAL;}
    + HasNoError -> BOOL {get;} {FINAL;}
```
`FB_Error` is the base class for representing errors in the library. It implements the `I_Error` interface and introduces additional properties.

 + The `Message` property provides a human-readable description of the error. 
 + `HasError` and `HasNoError` are helper properties indicating the presence or absence of an error respectively. They're both marked as `FINAL` to prevent further modification in derived classes.

```plaintext
FB_MutableError ~> FB_Error
	+ Code -> T_ErrorCode {get;set;}
    + Message -> T_MaxString {get;set;}
```
`FB_MutableError` is a class that extends `FB_Error`, allowing modification of the error code and message after the error object is created. It introduces setter methods for both Code and Message, providing a mutable error representation for specific use cases. This class is useful when the error details need to be updated dynamically.


## Iterability

Iterability is a critical aspect of the collections library, enabling efficient traversal and manipulation of data structures. This section introduces interfaces related to iterability and provides examples to illustrate their usage.

### Iteration Interfaces

Overview
```plaintext
I_Iterable ~> T_Queryable
  + Begin -> T_Position {get;}
  + End -> T_Position {get;}
```
The `I_Iterable` interface defines the standard structure for indexable collections in the library. Collections implementing this interface provide methods to retrieve the starting index (`Begin`) and an ending index (`End`). This ensures a consistent and safe approach to iterating over elements in a for-loop, minimizing the risk of overflow or off-by-one errors.

Example usage
```js
FOR i := fbList.Begin TO fbList.End DO 
    // Do something with element at index 'i'
END_FOR
```

### Enumerable

Overview
```plaintext
I_Enumerable ~> T_Queryable
  + GetEnumerator(ipEnumerator : REFERENCE TO I_Enumerator,  e => : T_Error) -> I_Enumerable

I_Enumerator ~> T_Queryable
  + Next(e => : T_Error) -> BOOL
  + Reset(e => : T_Error) 
  + Dispose()
```
The `I_Enumerable` interface introduces a more generalized approach to iteration, suitable for collections that may not be indexable but can be iterated over. It defines a method `GetEnumerator` that takes a reference to an enumerator interface (`ipEnumerator`). The `I_Enumerator` interface, in turn, specifies methods for advancing to the next element (`Next`), resetting the enumerator (`Reset`), and releasing resources (`Dispose`).

Example usage
```plaintext
I_ListEnumerator ~> I_Enumerator
  + Current(Item : ANY, e => : T_Error)

I_KeyValueEnumerator ~> I_Enumerator
  + Current(Key : ANY, Value : ANY, e => : T_Error)
```

```js
VAR
    ipValues : I_ListEnumerator;
    ipEntries : I_KeyValueEnumerator;
    sKey : STRING; 
    nValue : INT;
END_VAR
```
```js
fbArrayList.GetEnumerator(ipValues);
WHILE ipValues.Next() DO 
    ipValues.Current(nValue);
    // Do something with value.
END_WHILE

fbHashMap.GetEnumerator(ipEntries);
WHILE ipEntries.Next() DO 
    ipEntries.Current(sKey, nValue);
    // Do something with key and value.
END_WHILE
```

The examples showcase the use of `I_Enumerable` and `I_Enumerator` interfaces in a while-loop scenario. `I_ListEnumerator` and `I_KeyValueEnumerator` inherit from I_Enumerator, providing specific methods to access the current item in the iteration (`Current`). This allows for a flexible and standardised approach to traversing elements in various types of collections, whether they are indexable or not.


## Functional Interfaces

Functional interfaces provide a mechanism for performing operations on elements within a collection, facilitating advanced queries and transformations.

Base Functional Interfaces
```plaintext
I_Predicate ~> T_Queryable
I_Consumer ~> T_Queryable
I_Function ~> T_Queryable
I_Supplier ~> T_Queryable
```
The base functional interfaces define the fundamental building blocks for querying and manipulating data within the collections library. Each interface serves a specific purpose: `I_Predicate` for filtering, `I_Consumer` for consuming elements, `I_Function` for transforming elements, and `I_Supplier` for providing new elements.

Extended Functional Interfaces
```
I_UnaryPredicate ~> I_Predicate
  + Evaluate(Item : T_Generic, bBusy => : BOOL, e => : T_Error) -> BOOL

I_BiPredicate ~> I_Predicate
  + Evaluate(Item1 : T_Generic, Item2 : T_Generic, bBusy => : BOOL, e => : T_Error) -> BOOL

I_UnaryConsumer ~> I_Consumer
  + Consume(Item : T_Generic, bBusy => : BOOL, e => : T_Error)

I_BiConsumer ~> I_Consumer
  + Consume(Item1 : T_Generic, Item2 : T_Generic, bBusy => : BOOL, e => : T_Error)

I_UnaryFunction ~> I_Function
  + Invoke(Input : T_Generic,  bBusy => : BOOL, e => : T_Error) -> T_Generic

I_UnarySupplier ~> I_Supplier
  + Supply(bBusy => : BOOL, e => : T_Error) -> T_Generic
```
The extended functional interfaces refine the basic operations, introducing unary and binary versions to handle one or two elements, respectively. These interfaces provide more flexibility for creating sophisticated queries and transformations.

### I_Predicate

Example Usage of `I_UnaryPredicate`:
```plaintext
FB_EvenNumberPredicate : I_UnaryPredicate ~> I_Predicate
  + Evaluate(Item : T_Generic, bBusy => : BOOL, e => : T_Error) -> BOOL
```

```js
VAR
    fbEvensList : FB_List;
    fbIsEven : FB_EvenNumberPredicate;
END_VAR
```

```js
fbList.Filter(fbIsEven, fbEvenList);
```
Here, a unary predicate (`FB_EvenNumberPredicate`) is used to filter elements/items from `fbList` that satisfy the condition defined in the `Evaluate` method. The filtered elements are stored in `fbEvensList`.

Example Usage of `I_BiPredicate`:
```plaintext
FB_DogLoverPredicate : I_BiPredicate ~> I_Predicate
  + Evaluate(Item1 : T_Generic, Item2 : T_Generic, bBusy => : BOOL, e => : T_Error) -> BOOL
```

```js
VAR
    fbDogLovers : FB_TreeMap;
    fbIsDogLover : FB_DogLoverPredicate ;
END_VAR
```

```js
fbAnimalLoversMap.Filter(fbIsDogLover, fbDogLovers);
```
In this example, a binary predicate (`FB_DogLoverPredicate`) is used to filter elements from `fbAnimalLoversMap`. The Evaluate method defines a condition based on two items (`Item1` and `Item2`). The filtered elements are stored in `fbDogLovers`.

### I_UnaryConsumer

Example Usage of `I_UnaryConsumer`:
```plaintext
FB_PrintConsumer : I_UnaryConsumer ~> I_Consumer
  + Consume(Item : T_Generic, bBusy => : BOOL, e => : T_Error)
```

```js
VAR
    bPrintAll : BOOL;
    fbPrintItem : FB_PrintConsumer;
END_VAR
```

```js
IF bPrintAll THEN 
    fbList.ForEach(fbPrintItem, bBusy => bPrintAll);
END_IF
```
Here, a unary consumer (`FB_PrintConsumer`) is used to consume elements from `fbList` using the `Consume` method. The `ForEach` method iterates over each element in the list, applying the consumer to each element.

### I_BiConsumer

Example Usage of `I_BiConsumer`:
```plaintext
FB_PrintKeyValueConsumer : I_BiConsumer ~> I_Consumer
  + Consume(Item1 : T_Generic, Item2 : T_Generic, bBusy => : BOOL, e => : T_Error)
```

```js
VAR
    bPrintAll : BOOL;
    fbPrintKeyValuePair : FB_PrintKeyValueConsumer;
END_VAR
```

```js
IF bPrintAll THEN 
    fbMap.ForEach(fbPrintKeyValuePair, bBusy => bPrintAll);
END_IF
```
In this example, a binary consumer (`FB_PrintKeyValueConsumer`) is used to consume key-value pairs from `fbMap` using the `Consume` method. The `ForEach` method iterates over each key-value pair in the map, applying the consumer to each pair.

### I_UnaryFunction

Example Usage of `I_UnaryFunction`
```plaintext
FB_SquareFunction : I_UnaryFunction ~> I_Function
  + Invoke(Input : T_Generic, bBusy => : BOOL, e => : T_Error) -> T_Generic
```
```js
VAR
    fbSquare : FB_SquareFunction;
    fbSquaredList : FB_List; // Assume a list of numbers
END_VAR
```
```js
fbList.Map(fbSquare, fbSquaredList);
```
Here, a unary function (`FB_SquareFunction`) is used to square elements from fbList using the `Invoke` method. The `Map` method applies the function to each element in the list, creating a new list with the squared values.

### I_UnarySupplier
Example Usage of `I_UnarySupplier`
```plaintext
FB_RandomNumberSupplier : I_UnarySupplier ~> I_Supplier
  + Supply(bBusy => : BOOL, e => : T_Error) -> T_Generic
```
```js
VAR
    fbRandomNumber : FB_RandomNumberSupplier;
    fbNewList : FB_List;
END_VAR
```
```js
fbNewList.Generate(fbRandomNumber, 5);
```
Here, a unary supplier (`FB_RandomNumberSupplier`) is used to supply random numbers using the `Supply` method. The `Generate` method of `fbNewList` utilizes the supplier to populate the list with 5 randomly generated numbers.