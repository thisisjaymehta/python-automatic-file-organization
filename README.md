# python-automatic-file-organization
Automatically organize files to different folders based on its types

## Features
- Organise files based on its types to folders
- Works as 'always on process' so new files are organised as soon as they are moved / created inside folder

### Adding Soon
- Making script to run at windows startup / log in and no console window, so that it can run always in background without console coming in you way.
- Organising file two level deep to &lt;file_type&gt; --&gt; &lt;year&gt; --&gt; &lt;month&gt;
>Eg: Applications -&gt; 2020 -&gt; May -&gt; VSCode.exe

>or Photos -> 2020 -> June -> IMG0001.jpg

### How to use
1. As of now, dowload the automate.py from this github repo
2. Run it using console

> Eg: `python automate.py C:\Users\jay76\Downloads\` or just `python automate.py` to organise current working directory

>Compatibility: Definitely works on Windows, cause I made it in Windows

### How to modify folder names and file extensions
>You can edit the list of folders and what type of files gets sorted inside those folders in a `Directory` inside code called `DIR_TYPE`

For example you are a mac user and want to add deb files in a folder called Applications, add a new element in `DIR_TYPE` as `"Application":["deb","xip"]`

So that the new list looks like:
```python
DIR_TYPE={
    'Documents':['pdf','docx','doc','csv','txt','xls','xlsx','log'],
    'Archives':['zip','tar'],
    'Pictures':['jpg','jpeg','png','gif'],
    'Code':['py','css','js','html'],
    'Audio':['mp3'],
    "Video":['mp4','srt','mkv','3gp'],
    "Package":["exe",'ini'],
    "Torrent":["torrent"],
	
    #and the new one
    "Application":["deb", "xip"]
}

```
