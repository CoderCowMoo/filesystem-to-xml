import xml.etree.ElementTree as ET
import os
import getopt
import sys

# dirsonly flag is global
dirsonly = False

# Adds the entries in the directory to the tree with the given parent and calls itself on any
# directories it finds in the directory given
def addFilesToTree(parent: ET.Element, dir_target: str) -> ET.Element:
    # get list of files and dirs in dir_target
    list_of_dir = os.listdir(dir_target)
    for entry in list_of_dir:
        # make entry = effectively the 'true' path of the file/dir because the way it's passed as an arg and
        # other factors has an effect on this.
        entry = os.path.join(os.path.abspath(dir_target), entry)
        # if it is a file and we're not adding directories only
        if os.path.isfile(entry) and dirsonly == False:
            # create a subelement with the basename as the entry (don't include path)
            ET.SubElement(parent, "File").text = os.path.basename(entry)
        if os.path.isdir(entry):
            subdir_element = ET.SubElement(parent, "Dir")
            # set the 'name' attrib to be the name of the directory.
            subdir_element.set("name", os.path.basename(entry))
            # only recurse into directories, passing the directory we just created for it, and the path
            addFilesToTree(subdir_element, entry)
    return parent

def main():
    # help text written according to this guide:
    # https://stackoverflow.com/a/9727046/16495502
    help_text = """This program creates an XML file containing the directory structure of the\
directory passed. If no directory is passed, the current directory is assumed to be\
the target. Files are given the 'file' tag, while directories are given the\
'directory' tag.

Usage: """ + os.path.basename(sys.argv[0]) + """ [options] directory_to_target
    Options:
        [-o | --output] outputfile: sets the name of the XML file to be outputted. By default, the name of directory to scan.
        [-d | --dirs-only]: makes it scan directories only. False by default """
    # getopt returns the opts and args as lists.
    # "dho:" means short options are -d, -h and -o where -o takes an argument (':')
    # longopts are obvious.

    # if no arguments are passed, print help and exit
    if len(sys.argv) < 2:
        print(help_text)
        exit(0)
    
    opts, args = getopt.getopt(sys.argv[1:], "dho:", ["help", "output=", "dirs-only"])
    for option, argument in opts:
        if option in ("-h", "--help"):
            print(help_text)
            exit(0)
        elif option in ("-o", "--output"):
            filename = argument
        # in case someone wants just the directories and no files
        elif option in ("-d", "--dirs-only"):
            # flag is checked elsewhere so global required for editing
            global dirsonly
            dirsonly = True

    # > 1 because here args is omitting the first sys.argv of the filename.
    if len(args) > 1:
        print("Error: more than 1 directory/argument passed")
        print(args)
        exit(-1)

    # expand user in case '~' or $HOME is passed
    dir_to_scan = os.path.expanduser(str(args[0]))

    # if filename wasn't given as an option
    try:
        #check that it isn't defined
        # Source: stackoverflow.com/q/843277/16495502
        filename
    except UnboundLocalError:
        # normalise path then split it and grab last element to make filename the dir passed.
        filename = os.path.normpath(dir_to_scan).split(os.path.sep)[-1] + ".xml"


    ################################ START PROGRAM ################################

    # root element
    root = ET.Element("RootDir")
    # set the root name to be the basename of the directory given
    root.set("name", os.path.normpath(dir_to_scan).split('\\')[-1])

    # recursion occurs here
    addFilesToTree(root, dir_to_scan)

    tree = ET.ElementTree(root)
    # pretty print XML output
    ET.indent(tree)
    # includes the <?xml...?> declaration
    tree.write(filename, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    main()
