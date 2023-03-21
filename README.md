# simple-file-resizer
A one-file Python script using Pillow that resizes all images in a given folder, to an output folder

# NOTE: Preqrequisites

You need to have the following:

1. PIL / Pillow
2. Python 3+

# How to use the tools

## Command Line:

**Usages**: 

- python file_resizer.py (desiredWidth) (desiredHeight)
- python file_resizer.py (desiredWidth) (desiredHeight) [inputFolderPath] [outputFolderPath]

**Where**:

- (desiredWidth) = a valid integer above 0
- (desiredHeight) = a valid integer above 0
- [inputFolderPath] = a valid absolute folder path that exists 
- [outputFolderPath] = a valid absolute folder path that exists

**Examples**:

To resize all images in the path in the input_path variable to the path in the output_path variable in the file to 250px width and 250px height
- python file_resizer.py 250 250

To resize all images in the supplied input_path to the supplied output_path to 250px width and 250px height
- python file_resizer.py 250 250 C:\Users\X\input C:\Users\X\output
