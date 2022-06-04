# filesystem-to-xml
Converts a filesystem to an XML structure, optionally including only the directories (no files). No external dependencies.


### Implementation
Uses the ElementTree from XML, os, sys and getopt modules. No external dependencies. A main XML element called RootDir is the container for everything else. Recursion is used to go over all directories in the path given. Files are given the `<File>` tag and directories are given the `<Dir>` tag. 
Directories are named with a `name` attribute and files are given their name within their tag.

### Future
<!-- I want to make this very memory-efficient and fast (currently average of 22.5 MiB (measured with memory_profiler module) and runtime of 380 ms average (measured with time) on a directory with 1,921 files and 529 folders).--> I realised that it is very memory efficient (barely uses anything above what the python interpreter requires I may implement it in C now that I have a python prototype for inspiration. Any issues or tips are welcome 

### License
[GPL V3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html) is used.
