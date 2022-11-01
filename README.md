# civil-engineering-toolbox

### Note 1 Nov 2022:
This repository will be updated using Flask for a better project framework.
Heavy changes of migration will be seen in the future commits.

**civil-engineering-toolbox** is collection of small programs of
civil engineering that I built to help me to 
solve small to medium and common problems when designing something.

It is web based application that can be opened in your own browser (offline)
or can be accessed from other computer if you are connected to LAN (Local Area
Network).

# Features

* Structure
    * Steel Section Table (IWF, Angle)
    * Concrete Two Way Slab
    * Concrete Flexural Analysis
    * Response Spectrum
* Geotechnic
    * Surcharge Point Load
    * Surcharge Strip Load
* Math
    * Unit Converter (Pressure, Force, Distance)

# Documentation

You can see the documentation (theories) in <a href="https://github.com/dukenmarga/civil-engineering-toolbox/releases">
releases</a> page. Although the documentation has not completed yet, at least
you know what calculation is being performed behind the scene.

# Contribute

You can contribute to make this software better, even if you know nothing about
programming. Your contribution include:

* Create documentation
* <a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Fix%20typo%20/%20Ambiguous%20Sentences:%20_your_subject_"
target="_blank">
Fix typo, misspelled words, wrong grammar, ambiguous sentences, or propose
better vocabulary/definition</a>
* <a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Improve%20Layout:%20_your_subject_"
target="_blank">
Improve layout of application</a>. Please send your better proposed layout.
* <a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Feature%20request:%20_your_subject_"
target="_blank">
Request for a feature to create flexible application</a> (for example: fixed table
header on top of browser if scrolled down)
* <a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Numeric%20algorithm:%20_your_subject_"
target="_blank">
Better numeric algorithm</a>. Please send a detailed explanation.
* Request for an application (see below for more detailed explanation)

# Request for an Application

If you want to request application, you can 
<a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Application%20Request:%20_application_name_" target="_blank">
create a new issue </a> and describe your application.
You can send link or reference to the description, algorithm, picture, code, and 
sample calculation of requested application so I can 
review it first before creating it.
Application must be as general as possible and be used by most of civil
engineers.

# Installation

I'm sorry that there are many steps to go through before you can use this
software. **civil-engineering-toolbox** depends on some software, especially
for interpreter, web server and templating. If you are using Windows 7, open all
of these files as Administrator (right click then choose `Run as Administrator`)
in case your computer doesn't allow installing program using non-privileged user.

## Windows 32-bit
* Download <a href="https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe">
Python 3.8.2</a> or above.
* Install Python language above. When installing the software, on
customization option, ensure that you check item "Add python.exe to Path" to
"Will be installed on local hard drive" (see image below). If you do not enable this option, you
will not be able to complete the next step. 
<img src="http://dukenmarga.id/cet/img/customize_python.png" align="center" hspace="10" vspace="6">

* Download **civil-engineering-toolbox** (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it into one of your directory.
* Double click `install_windows.cmd`. This script will install required software
to run civil-engineering-toolbox. Right click and `Run as administrator` if possible.
This process will require internet connection.
* Ensure that there are no errors during installation.
* Double click `Main.py`. A black window will be opened and hang in there as an
indication that your program is started correctly.
* Open your browser to access http://127.0.0.1:1234
* Happy designing :)

## Windows 64-bit
I'm sorry but it seems that CherryPy installer can not detect Python 64 bit
on Windows. So, for you who use Windows 64 bit, you can still install using 
installation guide for 32 bit above.

## Linux

Due to many variant of Linux distribution, here I will summarize steps to install
**civil-engineering-toolbox**. I believe that you had already able to use your
software manager, either by GUI (graphical user interface) or command line from
terminal. If your repository doesn't have package below, you can download them
manually, extract them, and then install it by invoking `python setup.py install`
from command line in that extracted directory.
Ensure you have installed Python setuptools before using the command.
* Install Python 2.7+
* Install Mako 0.9 or later (http://www.makotemplates.org/)
* Install CherryPy 3.2 (http://www.cherrypy.org/)
* Install Matplotlib 1.3+ (http://matplotlib.org/)
* Install SymPy 0.7+ (http://sympy.org/)
* Install Python Routes 1.13+ or 2.0+ (https://pypi.python.org/pypi/Routes)
* Download **civil-engineering-toolbox** (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it. Then open terminal and change your directory into it.
* From terminal invoke `python Main.py`
* Open your browser to access http://127.0.0.1:1234
* Happy designing :)

# Access From Network (LAN or Internet)

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

# License

This software is using BSD 3-clause license. In other words, you
can use, distribute, even sell it without any restriction. But, you
must include the copyright notice, the license, and the following
disclaimer.
