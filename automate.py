import os,shutil

DIR_TYPE={
    'Documents':['pdf','docx','doc','csv','txt','xls','xlsx','log'],
    'Archives':['zip','tar'],
    'Pictures':['jpg','jpeg','png','gif'],
    'Code':['py','css','js','html'],
    'Audio':['mp3'],
    "Video":['mp4','srt','mkv','3gp'],
    "Package":["exe",'ini'],
    "Torrent":["torrent"]
}

PATH='C:\\Users\\jay76\\Downloads\\'  #replace this path with the folder you want to organise

def movefile(file_name,dir_type):
    dir_location=os.path.join(PATH,dir_type)
    if not os.path.exists(dir_location):
        os.mkdir(dir_location)
    shutil.move(file_name,dir_location)

def organize():
    file_types={ file_type:dir_name
        for dir_name,file_types in DIR_TYPE.items() for file_type in file_types
    }

    onlyfiles = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]

    for file_name in onlyfiles:
        splited_text=file_name.split('.')
        if len(splited_text)>1:
            ext=splited_text[-1].lower()
            if ext in file_types:
                movefile(os.path.join(PATH,file_name),file_types[ext])
            else:
                print("Unknown File format found -",splited_text[-1])
organize()
