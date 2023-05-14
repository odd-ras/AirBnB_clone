# AirBnB

# Project Description

This project is broken down into several steps with each step linking to an important concept.

The first step is console development.
The console

1. creates your data model
2. manages the command interpreter
3. Stores and persists data

The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and
“How they are stored and persisted”. This means: from your console code
(the command interpreter itself) and from the front-end and RestAPI you will build later,
you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily
without updating all of your codebase.

The console will be a tool to validate this storage engine
