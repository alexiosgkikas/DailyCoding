"""
Daily Coding Problem: Problem #658 [Hard] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

def subdirectories(folder):
    if len(folder) == 1 and '.' in folder[0]:
        return [folder[0]]
    if folder is None or len(folder)<=1:
        return []
    
    parent_name = folder[0]
    folder = [f.replace("\t","",1) for f in folder[1:]] 
    list_files = [idx for idx,sub in enumerate(folder) if sub[0] != '\t']
    list_path = []
    right = len(folder)
    for idx in list_files[::-1]:
        list_path +=subdirectories(folder[idx:right])
        right = idx
    
    if list_path:
        list_path = [(parent_name+'/'+file) for file in list_path]
        return [max(list_path,key=len)]
    else:
        return []


def find_max_path(directory):
    file_path = subdirectories(directory.split('\n'))
    if len(file_path)  == 0:
        return 0
    return file_path[0]


if __name__ == "__main__":
   #without files
   directory = "dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2"
   print(find_max_path(directory))
   directory = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
   print(find_max_path(directory))
