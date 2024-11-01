# pineDOS #

Hello! 

This library is created to write mini-programms for Pineapple-IV (Imitation of DOS systems)

BUT this library can be used anywhere u want! (It supports any python project)

It can create directories, clear output, customize console output, etc.

Have fun :D 

### Updated (Version: 0.0.5) ###

1. Made the lib usable
2. Made documentaion
3. Tags to the lib


## Usage (Main commands) ##

```

from pineDOS import *

cout("hello world!", Color.yellow, BGColor.bg_red) #alternative of print()

cin(placeholder = ">>>  ", type = str, ascii_check = False, color = Color.yellow, bg = BGColor.bg_red) #alternative of input()

delay(time in seconds) #no comments

clear_output() #no comments

```

## Usage (File editor) ##

```

from pineDOS import *

FileController().create_file("cute.txt", "some path") #creates a file

FileController().delete_file("some path") #deletes a file

FileController().rename_file("cute", "not_cute", "some path") #renames a file

```

## Usage (Directory editor) ##

```

from pineDOS import *

DirectoryControllerClass().create_directory("cute", "some path") #creates a directory (folder)

DirectoryControllerClass().delete_directory("some path") #deletes a directory (folder)

DirectoryControllerClass().rename_directory("cute", "not cute", "some path") #renames a directory (folder)

directory = current_directory("some path") #checks if directory exists and saves it in variable

directory_content = directory_content("some path") #returns a list of directory content

```

## Usage (Extra commands) ##

```

from pineDOS import *

file_info().file_date("some path", "modification date") #Returns the date of the file
    Types: 
        modification_date,
        creation_date

file_info().file_size("some path", "bytes") #Returns the size of the file
    Units:
        bytes,
        kilobytes,
        megabytes,
        gigabytes,
        terabytes

Errors.enable_logging = True #enables logging (.log file will be created anyways even the value of variable set on False)

```


## Developer ##
MKMysteryKey
