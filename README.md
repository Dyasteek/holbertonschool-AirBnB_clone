# HBNB - The AirBNB clone - The console

  Console to control all classes and serializate and deserializates json files


## Repository contents

   File/Directory | Description
   -------------- | -----------
   console.py | Console of the AirBNB clone
   models | Folder containing all the models to be utilized
   tests | Unittest for all the classes used in the program
   AUTHORS | Creators of the program

## Clone the repository

   To be able to utilize the console you will need to download it using git
   If you don't have git installed in you Linux computer you can install it with the command:

   ```
   $ sudo apt-get install git
   ```

   Then you can use the command:

   ```
   $ git clone https://github.com/Dyasteek/holbertonschool-AirBnB_clone.git
   ```

   And with that you have you own copy of the program.

## Usage

   To execute the console use the command:

   ```
   $ ./console.py
   ```

   In the directory with the program in it.


## Commands

   The commands wich you can use are the following:

   **help** - Usage: `(hbnb) help` / `(hbnb) help command_name`
   	    If used `(hbnb) help` display the list of commands wich you can read the help. If it's used as `(hbnb) help command_name` it displays the help for the specified command

   **quit** - Usage: `(hbnb) quit`
   	    Exit the console, you can also use ctrl + D

   **create** - Usage: `(hbnb) create class_name`
   	      Creates an instance of the specified class and prints it's id

   **show** - Usage: `(hbnb) show class_name instance_id`
   	    Prints the string representation of an instance based in the class name and instance id

   **destroy** - Usage: `(hbnb) destroy class_name instance_id`
   	       Deletes an instance based in the class name and instance id

   **all** - Usage: `(hbnb) all` / `(hbnb) all class_name`
   	   Prints the string representation of all instances or instances of a single class if specified

   **update** - Usage `(hbnb) update class_name instance_id attribute "value"`
   	      Adds or updates an attribute based in the class name and the instance id

## String representation of an instance

   The format of presentation of an instance is the following:

   [class_name] (instance_id) instance_dict

   isntance_dict is a directory containing all the attributes and values in a key/value par

## Storage

   All instance created will be saved in a file called "file.json" in the root directory of the program

   It's possible to change it's path or name in the file /models/engine/file_storage.py in the private attribute __file_path

## Credits
This project was made by:

- Anit Rodriguez
- Andres del Rio