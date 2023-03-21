from PIL import Image
import os, sys

#===CONFIGURATION


#Image file extensions to be included
ext_list = ['.png', '.jpg']

#This is what the images gets resizes to
width_to_resize_to = 0
height_to_resize_to = 0

#The ABSOLUTE path of the folder you want to recursively convert assets in
input_path = r'C:\Users\X\input'
output_path = r'C:\Users\X\output'

#Usage error text
usage_text = "-USAGE- (desiredWidth) (desiredHeight) [inputFolderPath] [outputFolderPath]"


#===METHODS


def printError(error_msg):
    print("\n-ERROR- " + error_msg + "\n" + usage_text)


def main():
    for folder, sub, files in os.walk(input_path):
        for f in files:
            file_name_parts = os.path.splitext(f)
            
            #Check if file extension is in list specified above...
            if file_name_parts[1].lower() in ext_list:
                full_input_path = os.path.join(folder, f)
                image = Image.open(full_input_path)

                full_output_path = os.path.join(output_path, f)
                new_img = image.resize((width_to_resize_to, height_to_resize_to))
                new_img.save(full_output_path)
                
                print("Resized [to (" + str(width_to_resize_to) + ", " + str(height_to_resize_to) + ")]: " + output_path)


def assignImageDimensions():
    global width_to_resize_to
    global height_to_resize_to
    
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        printError("The first two arguments must be valid integers")
        sys.exit()
    
    width_to_resize_to = int(sys.argv[1])
    height_to_resize_to = int(sys.argv[2])
    
    
def isValidInputPath():
    return os.path.isdir(input_path)
    
   
def isValidOutputPath():
    return os.path.isdir(output_path)


def assignFolderPaths():
    global input_path
    global output_path

    input_path = sys.argv[3]
    output_path = sys.argv[4]
    
    if not isValidInputPath():
        printError("The input path is incorrect")
        sys.exit()
    elif not isValidOutputPath():
        printError("The output path is incorrect")
        sys.exit()


#===MAIN


if __name__ == '__main__':
    args = len(sys.argv)

    if args == 3:
        assignImageDimensions()
        
        if not isValidInputPath() or not isValidOutputPath():
            printError("When not supplying your own folder paths, you must put valid paths inside the .py file")
            sys.exit()
    elif args == 5:
        assignImageDimensions()
        assignFolderPaths()
    else:
        printError("You must supply either 2 or 4 arguments")
        sys.exit()

    #Here only to give a space before the resize messages
    print()

    main()
