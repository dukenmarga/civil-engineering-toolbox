#civil-engineering-toolbox
civil-engineering-toolbox is collection of small programs to help 
civil engineer to solve small to medium size and common problems found in 
engineering world in order to solve the main problems.
It is web based application that can be opened in your own browser (offline)
or can be accessed from other computer if you are connected to LAN (Local Area
Network).
This software can be used as a problem-solver, reminder (through the shown
formula), or to give quick estimation.


#Features
Structure
 * Steel Profile Table (IWF)

#Request for a Feature
If you want to request application, you can 
<a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/
new?title=Application%20Request:%20_application_name_" target="_blank">
create a new issue </a> and describe your application.
You can send link or reference to the description, algorithm, picture, code, and 
sample calculation of requested application so I can 
review it first before creating it.
Application must be as general as possible and be used by most of civil
engineers.

#Requirement
* Python 2.7+ (https://www.python.org/)
* CherryPy 3.2.2 (http://www.cherrypy.org/)
* Mako 0.9 or later (http://www.makotemplates.org/)
* Python Routes 1.13+ or 2.0+ (https://pypi.python.org/pypi/Routes)

#Installation
I'm sorry that there are many steps to go through before you can use this
software. civil-engineering-toolbox depends on some software, especially
to for web server and templating.
## Windows 32-bit
* Download Python 2.7+ (https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi)
* Download Mako 1.0 (http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/Mako-1.0.0.win32-py2.7.exe)
* Download CherryPy 3.2 (http://download.cherrypy.org/cherrypy/3.2.2/CherryPy-3.2.2.win32.exe)
* Download Setuptools (http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/setuptools-5.4.2.win32-py2.7.exe)
* Install all 4 softwares above in sequence
* Download Routes 2.0 (http://duken.info/cet/routes/Routes-2.0.zip)
* Extract and unzip Routes, then double click `install.cmd`
  Please wait until installation has completed. You can safely delete this folder
  after completing the installation.
* Download civil-engineering-toolbox (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it into one of your directory.
* Double click `Main.py`
* Open your browser to access http://127.0.0.1:1234
* Happy designing :)

## Windows 64-bit
* Download Python 2.7+ (https://www.python.org/ftp/python/2.7.8/python-2.7.8.amd64.msi)
* Download Mako 1.0 (http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/Mako-1.0.0.win-amd64-py2.7.exe)
* Download CherryPy 3.2 (http://download.cherrypy.org/cherrypy/3.2.2/CherryPy-3.2.2.win32.exe)
* Download Setuptools (http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/setuptools-5.4.2.win-amd64-py2.7.exe)
* Install all 4 softwares above in sequence
* Download Routes 2.0 (http://duken.info/cet/routes/Routes-2.0.zip)
* Extract and unzip Routes, then double click `install.cmd`
  Please wait until installation has completed. You can safely delete this folder
  after completing the installation.
* Download civil-engineering-toolbox (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it into one of your directory.
* Double click `Main.py`
* Open your browser to access http://127.0.0.1:1234
* Happy designing :)

## Linux
Due to many variant of Linux distribution, here I will summarize steps to install
civil-engineering-toolbox. I believe that you had already able to use your
software manager, either by GUI (graphical user interface) or command line from
terminal. If your repository doesn't have package below, you can download them
manually, extract them, and then install it by invoking `python setup.py install`
from command line in that extracted directory.
Ensure you have installed Python setuptools before using the command.
* Install Python 2.7+
* Install Mako 0.9 or later (http://www.makotemplates.org/)
* Install CherryPy 3.2 (http://www.cherrypy.org/)
* Install Python Routes 1.13+ or 2.0+ (https://pypi.python.org/pypi/Routes)
* Download civil-engineering-toolbox (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it. Then open terminal and change your directory into it.
* From terminal invoke `python Main.py`
* Open your browser to access http://127.0.0.1:1234
* Happy designing :)

#Access From Network (LAN or Internet)
This software can be run in a computer and act as a server to give services
to client that are connected to the same network with the server.
In other words, many computer can use the same software that are run only in
one computer.
Here are some rough steps to do that:
* Ensure you have installed civil-engineering-toolbox and can be accessed 
via browser in that computer.
* Write down your IP_ADDRESS in that computer (that will act as server). Ask
your network administrator how to get the IP_ADDRESS. Please note that in order
to use the same URL over and over, you must use static IP_ADDRESS, instead of
dynamic using DHCP. Ask your network administrator if you don't know how to do
that.
* civil-engineering-toolbox can be accessed via browser in another computer 
using that IP_ADDRESS, for example http://IP_ADDRESS:1234

#License
This software is using BSD 3-clause license. In other words, you
can use, distribute, even sell it without any restriction. But, you
must include the copyright notice, the license, and the following
disclaimer.