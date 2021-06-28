# For detailed documentation, see [WIKI][3]!


This repository contains all *public* material needed to reproduce our task in the course [Supervised and unsupervised machine learning in the science of behaviour](https://www.mi.fu-berlin.de/inf/groups/ag-ki/Teaching/SS19/SWP-Ueberwachtes-Lernen/index.html) of the research group [Dahlem Center for Machine Learning and Robotics][2] at Freie Universität Berlin.


## First things first
1. The code section of this repository contains everything related to the programming assignments we will do throughout the course.
1. All other information (documentation, data description, assignment instructions, constraints etc.) you find in the ❗[WIKI][3]❗.
1. Any private data will not be published and is running on our own computers as soon as we retrieve the data. 
1. You can clone the code repository in order to reproduce our solutions or to test/run this code.

## Getting started

To make sure everyone uses the same environment and make sure we don't run into any dependency hell :volcano: let's start with the prerequisites.

### Prerequisites

In order to run our code, please ensure that you have a [Python](https://www.python.org/downloads/) version greater or equal to `3.6.1`, a working installation of and [git][5] installed.


### Setup

:one: We start off by installing pip which is a package manager. Open your terminal and run the following command:

  	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  
  	python3 get-pip.py
  
:two: Install the dlib library (todo: explanation)
  
 	pip install dlib
  
3️⃣ Install opencv (todo: explanation)
  
  	pip install opencv-python
  
:four: Install the mathplotlib (todo: explanation)
  
	pip install matplotlib

:five: Clone this repository (or use SSH) and move it into the repo root.

	git clone https://github.com/mvrcx/SWP_Blitzer.git


## Troubleshooting

* coming
* soon


[1]:	https://www.mi.fu-berlin.de/inf/groups/ag-ki/Teaching/SS19/SWP-Ueberwachtes-Lernen/index.html
[2]:	https://www.mi.fu-berlin.de/inf/groups/ag-ki/index.html
[3]:	https://github.com/mvrcx/SWP_Blitzer/wiki/Wiki-of-this-software-project
[4]:	https://python-poetry.org/docs/
[5]:	https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
