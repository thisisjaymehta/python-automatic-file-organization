# python-automatic-file-organization
Automatically organize files to different folders based on its types

## Features
- Organise files based on its types to folders

### Adding Soon
- Making script to work in background as always on process, so that as soon as new file is added to folder, it will be moved to organised folder and you dont have to run py script maually (thinking of using watchdog to detect system change)
- Organising file two level deep to &lt;file_type&gt; --&gt; &lt;year&gt; --&gt; &lt;month&gt;
>Eg: Applications -&gt; 2020 -&gt; May -&gt; VSCode.exe

>or Photos -> 2020 -> June -> IMG0001.jpg

### How to use
1. As of now, dowload the automate.py from this github repo
2. And Run it (as simple as that)
>Dont forget to change the folder path to your own folder
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
