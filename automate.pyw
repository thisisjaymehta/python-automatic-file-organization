# -*- coding: utf-8 -*-
"""Auto File Organiser made in Python

    FileOrganiser
    =============
    
    Provides
        1. Rearranging files in folders based on their types
        2. Script run infinitly so that new files automatically get organised
    
    Use
        > Give path of folder as argument while excecuting the script or else
          Current Working Directory will be used
      
    Example
        python automate.pyw <path_to_dir>

"""

import os
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

DIR_TYPE={
    'Documents':['pdf','docx','doc','csv','txt','xls','xlsx','log'],
    'Archives':['zip','tar'],
    'Pictures':['jpg','jpeg','png','gif'],
    'Code':['py','css','js','html'],
    'Audio':['mp3'],
    "Video":['mp4','srt','mkv','3gp'],
    "Package":['exe','ini'],
    "Torrent":['torrent'],
    "SQL":['sql'],
    "SKIP":['crdownload', 'fdmdownload'],
    #All uncatogerised file extensions will go in 'Other' folder
}

PATH = sys.argv[1] if len(sys.argv) > 1 else '.'

def movefile(file_name,dir_type):
    """Function that actually move files

    Arguments:
        file_name {string} -- name of file to move
        dir_type {string} -- type of directory to move that file into
    """    
    
    try:
        dir_location=os.path.join(PATH,dir_type)
        if not os.path.exists(dir_location):
            os.mkdir(dir_location)
        original_filename = file_name
        file_name = os.path.basename(file_name)
        if os.path.exists(os.path.join(dir_location, file_name)):
            i = 1
            splited_text=os.path.basename(file_name).split('.')
            while os.path.exists(os.path.join(dir_location, splited_text[0]+str(i)+"."+splited_text[1])):
                i += 1
            file_name = splited_text[0] + str(i) + "."  + splited_text[1]
        shutil.move(original_filename,os.path.join(dir_location, file_name))
    except:
        time.sleep(5)
        organize()

def organize(event = None):
    """this function find all files inside dir and move it to specific folder

    Keyword Arguments:
        event {event} -- No used currently, but required as event_handler
                            send an event while calling this function
                            (default: {None})
    """    
    file_types= { file_type:dir_name
        for dir_name,file_types in DIR_TYPE.items() for file_type in file_types
    }

    onlyfiles = [f for f in os.listdir(PATH) 
                 if os.path.isfile(os.path.join(PATH, f))]

    for file_name in onlyfiles:
        splited_text=file_name.split('.')
        if len(splited_text)>1:
            ext=splited_text[-1].lower()
            if file_types[ext] == "SKIP":
                continue
            if ext in file_types:
                movefile(os.path.join(PATH,file_name),file_types[ext])
            else:
                movefile(os.path.join(PATH,file_name), "Other")
                

if __name__ == "__main__":    
    
    organize()
    
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns,
                        ignore_directories, case_sensitive)
    my_event_handler.on_created = organize
    my_event_handler.on_modified = organize
    
    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, PATH, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()
