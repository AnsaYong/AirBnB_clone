# AirBnB clone

### Overview

This project is the initial phase of building our first full-fledged web application – the Airbnb clone.
This foundational step is pivotal as the components developed here will serve as the building blocks for
subsequent projects, encompassing HTML/CSS templating, database storage, API integration, and front-end
development.

Throughout this phase, we aim to:

- Establish a fundamental class named BaseModel that takes charge of initializing, serializing, and
deserializing instances in our system.
- Develop a streamlined process for serialization and deserialization:
Instance <-> Dictionary <-> JSON string <-> File.
- Create all essential classes for Airbnb functionalities, such as User, State, City, and Place, each
inheriting from our BaseModel.
- Introduce the project's first abstracted storage engine: File storage.
- Formulate a comprehensive suite of unit tests to validate the functionality of all classes and the
storage engine.
- Build a command line interpreter which we intend to use to manage the objects of our project


### The Console - command-line interpreter

The command-line interpreter allows users to interact with and manage instances of various classes
representing elements like users, states, cities, places, and more. The script employs the `cmd` module
to provide a command prompt with functionalities for creating, displaying, updating, and deleting instances.

##### How to Start:

To start the interpreter, run the script as follows
- `$ ./console.py`

If executed directly, it enters the command loop, displaying the prompt `(hbnb) `.

##### How to Use:

The interpreter supports various commands:

- `quit`: Exits the program.
- `EOF` (Ctrl + D): Forces the program to exit.
- `create [class]`: Creates a new instance of the specified class.
- `show [class] [id]`: Prints the string representation of an instance based on the class name and id.
- `destroy [class] [id]`: Deletes an instance based on the class name and id.
- `all [class] or all`: Prints the string representation of all instances based on the class name or all instances, respectively.
- `update [class] [id] [attribute] [value]`: Updates the specified attribute of an instance based on the class name and id.

##### Examples:

1. Create an Instance:
- `(hbnb) create BaseModel`

2. Show an Instance:
- `(hbnb) show BaseModel 1234-1234-1234`

3. Destroy an Instance:
- `(hbnb) destroy BaseModel 1234-1234-1234`

4. Show All Instances:
- `(hbnb) all`
- `(hbnb) all User`
- `(hbnb) all Amenity`

5. Update an Instance:
- `(hbnb) update BaseModel 1234-1234-1234 name "New Name"`


We look forward to laying the groundwork for an efficient and robust Airbnb clone.
