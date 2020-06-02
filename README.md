# python-automatic-file-organization
Automatically organize files to different folders based on its types

## Features
- Organise files based on its types to folders
- Works as 'always on process' so new files are organised as soon as they are moved / created inside folder
- Option for auto run at startup

### Adding Soon
- Organising file two level deep to &lt;file_type&gt; --&gt; &lt;year&gt; --&gt; &lt;month&gt;

>Eg: Applications -&gt; 2020 -&gt; May -&gt; VSCode.exe

>or Photos -> 2020 -> June -> IMG0001.jpg

# How to use
There are two ways you can use this code:
### 1. Run one time only to organise a folder just once (manually)
- Here you need to download `automate.pyw` and run it using `python automate.pyw <path to dir>` command, where `<path to dir>` is path to directory which you want to organise
- Once all files are organised and you want to stop excecuting the script press `CTRL + C` to stop the script and you are done.
- Then you can repeat same procedure for some other folder if you want

### 2. Run as always on service and auto run at startup
- In this mode, script will keep running in background and automatically organise current files and new files that will come in future
- To achieve this there are different steps for different OS (because it include making a shell script for Unix environment or Batch File for Windows)
	- First store the `automate.pyw` somewhere nice and cozy on your computer (for ex in Documents)
	- Then make a script file which calls this pyw (File for windows is already included, follow instructions in file)
	- Then move the file to startup folder so that it is executed as soon as computer starts
	>For windows open run and enter `shell:startup`, which will open startup folder. Move your bat file there and then it will automatically run at startup

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
