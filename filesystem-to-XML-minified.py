# import xml.etree.ElementTree as ET
# import os
# import sys

# # Adds the entries in the directory to the tree with the given parent and calls itself on any
# # directories it finds in the directory given
# def addFilesToTree(parent, dir_target):
    # # get list of files and dirs in dir_target
    # list_of_dir = os.listdir(dir_target)
    # for entry in list_of_dir:
        # # make entry = effectively the 'true' path of the file/dir because the way it's passed as an arg and
        # # other factors has an effect on this.
        # entry = os.path.join(os.path.abspath(dir_target), entry)
        # # if it is a file and we're not adding directories only
        # if os.path.isfile(entry):
            # # create a subelement with the basename as the entry (don't include path)
            # ET.SubElement(parent, "File").text = os.path.basename(entry)
        # if os.path.isdir(entry):
            # subdir_element = ET.SubElement(parent, "Dir")
            # # set the 'name' attrib to be the name of the directory.
            # subdir_element.set("name", os.path.basename(entry))
            # # only recurse into directories, passing the directory we just created for it, and the path
            # addFilesToTree(subdir_element, entry)
    # return parent

# # expand user in case '~' or $HOME is passed
# dir_to_scan = os.path.expanduser(str(sys.argv[1]))


# ################################ START PROGRAM ################################

# # root element
# root = ET.Element("Root")
# # recursion occurs here
# addFilesToTree(root, dir_to_scan)

# tree = ET.ElementTree(root)
# # includes the <?xml...?> declaration
# tree.write("out.xml", encoding='utf-8', xml_declaration=True)


import xml.etree.ElementTree as C,os as A,sys
def E(parent,dir_target):
	F=dir_target;D=parent;H=A.listdir(F)
	for B in H:
		B=A.path.join(A.path.abspath(F),B)
		if A.path.isfile(B):C.SubElement(D,'File').text=A.path.basename(B)
		if A.path.isdir(B):G=C.SubElement(D,'Dir');G.set('name',A.path.basename(B));E(G,B)
	return D
#D=A.path.expanduser(str(sys.argv[1])) 'teeecchhniicallly unneccesary'
B=C.Element('Root')
E(B,D)
F=C.ElementTree(B)
F.write('out.xml',encoding='utf-8',xml_declaration=True)
# 464 bytes
