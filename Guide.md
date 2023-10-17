# Guide to running and testing the API
This guide is here to help you start up the webserver, connect to the swagger docs page and test the API endpoints

## Step 1: Running python
The API is wrtten in python and so to start it up, you need to install python on to your system.
<br>
For brevity sake, I have included a few videos the show the installation process indepth for both Windows and MacOS systems
<br>
Windows: https://www.youtube.com/watch?v=yivyNCtVVDk
<br>
MacOS: https://www.youtube.com/watch?v=3-sPfR4JEQ8

On Windows, make sure you check the box that says `add python.exe to PATH`. very important. If there is an option confirming the installation of `pip`, make sure its checked.

Now for running python:
<br>
If python has been properly installed, you can probably run a python from the desktop.
<br>
On Windows just by double clicking it and on macOS by right click and select Open With -> Python Launcher.

The problem with this method of running python is that depending on the script being run, its hard to capture output and thus harder to debug.
<br>
I suggest using the Command Prompt/terminal for running python programs.
<br>
Here is some help on command lines:
<br>
Windows/Command prompt: https://www.youtube.com/watch?v=A3nwRCV-bTU
<br>
MacOS/terminal: https://www.youtube.com/watch?v=FfT8OfMpARM

## Step 2: Running and interfacing with the app
If you decided to opt out of using a command line, all you would need to do is first click on `install.py` in the directory to install the required dependencies and the click on `run.py` to run the web server.
<br>
(NOTE: Doing this will probably spawn command lines, but they will probably dissapear once the program has been terminated)

If you decide to use a command line. First navigate to the project's folder.
<br>
Then run either `python install.py` or `pip install -r requirements.txt` to install the dependencies
After that terminates, run `python run.py`. This will start up the webserver which will stay on until to terminate the program.'










