#civil-engineering-toolbox
**civil-engineering-toolbox** is collection of small programs of
civil engineering that I built to help me to 
solve small to medium and common problems when designing something.
When I try to create programs for practical use, sometimes I will add programs
that is pure-theory (mathematics) when I'm interested on it.

It is web based application that can be opened in your own browser (offline)
or can be accessed from other computer if you are connected to LAN (Local Area
Network).
This software can be used as a problem-solver, reminder (through the shown
formula), or just to give quick estimation.

#Features
* Structure
    * Steel Profile Table (IWF)
* Geotechnic
    * Surcharge Point Load
    * Surcharge Strip Load
* Math
    * Unit Converter

#Contribute
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

#Request for an Application
If you want to request application, you can 
<a href="https://github.com/dukenmarga/civil-engineering-toolbox/issues/new?title=Application%20Request:%20_application_name_" target="_blank">
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
* Repoze.lru 0.6 (https://pypi.python.org/pypi/repoze.lru)

#Installation
I'm sorry that there are many steps to go through before you can use this
software. **civil-engineering-toolbox** depends on some software, especially
for interpreter, web server and templating. If you are using Windows 7, open all
of these files as Administrator (right click then choose `Run as Administrator`)
in case your computer doesn't allow installing program using non-privileged user.

## Windows 32-bit
* Download <a href="https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi">Python 2.7+</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/Mako-1.0.0.win32-py2.7.exe">Mako 1.0</a>
* Download <a href="http://download.cherrypy.org/cherrypy/3.2.2/CherryPy-3.2.2.win32.exe">CherryPy 3.2</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/numpy-MKL-1.9.1.win32-py2.7.exe">Numpy MKL</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/python-dateutil-2.2.win32-py2.7.exe">Dateutil</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/pytz-2014.7.win32-py2.7.exe">Pytz</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/pyparsing-2.0.3.win32-py2.7.exe">pyparsing</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/six-1.8.0.win32-py2.7.exe">six</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ekvtz8ci/setuptools-5.4.2.win32-py2.7.exe">Setuptools</a>
* Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/ensjsj6n/matplotlib-1.4.2.win32-py2.7.exe">Matplotlib</a>
* Install all 10 softwares above in sequence. When installing Python, on
customization option, ensure that you check item "Add python.exe to Path" to
"Will be installed on local hard drive" (see image below). If you do not enable this option, you
will not be able to complete the next step. 
<img src="http://duken.info/cet/img/customize_python.png" align="center" hspace="10" vspace="6">
* Download Routes 2.0 (http://duken.info/cet/routes/Routes-2.0.zip)
    * **Connected to internet**. Extract and unzip Routes, then double click `install.cmd`
      Please wait until installation has completed. If you are connected to internet,
      Routes will download a file from internet as its
      dependency. If you are offline when installing this, follow the next step.
    * **Offline**. You must download additional file named repoze.lru 
      (http://duken.info/cet/repoze.lru/repoze.lru-0.6.zip). After installing
      Routes above (and failed connected to internet), install repoze.lru
      after extracting it then double click `install.cmd`.
  You can safely delete these folders after completing the installation.
* Download civil-engineering-toolbox (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
* Extract and unzip it into one of your directory.
* Double click `Main.py`. A black window will be opened and hang there as an
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
* Install Python Routes 1.13+ or 2.0+ (https://pypi.python.org/pypi/Routes)
* Download **civil-engineering-toolbox** (https://github.com/dukenmarga/civil-engineering-toolbox/archive/master.zip)
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