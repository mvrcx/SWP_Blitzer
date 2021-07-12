# For detailed documentation, see [WIKI][3]!


This repository contains all *public* material needed to reproduce our task in the course [Supervised and unsupervised machine learning in the science of behaviour](https://www.mi.fu-berlin.de/inf/groups/ag-ki/Teaching/SS19/SWP-Ueberwachtes-Lernen/index.html) of the research group [Dahlem Center for Machine Learning and Robotics][2] at Freie Universität Berlin.


## First things first
1. The code section of this repository contains everything related to the programming assignments we will do throughout the course.
1. All other information (documentation, data description, assignment instructions, constraints etc.) you find in the ❗[WIKI][3]❗.
1. Any private data will not be published and is running on our own computers. 
1. You can clone the code repository in order to reproduce our solutions or to test/run this code.

## Getting started

To make sure everyone uses the same environment and make sure we don't run into any dependency hell :volcano: let's start with the prerequisites.

### Prerequisites

In order to run our code, please ensure that you have a [Python](https://www.python.org/downloads/) version greater or equal to `3.6.1`, a working installation of and [git][5] installed.

### Dependencies

Dependencies are all of our software components required by this project in order for it to work as intended and avoid runtime errors. Below is a list of the necessary dependencies and its working version. You will be guided through the installation by installing the necessary dependencies in Step 8 below.

> dlib==19.19.0   
> im utils==0.5.3   
> numpy==1.18.4   
> opencv-contrib-python==4.2.0.34   
> scipy==1.4.1


### Setup

:one: We start off by downloading pip which is a package manager. Open your terminal and run the following command:

  	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	
:two: To install pip, run the downloaded python script the following way 
  
  	python3 get-pip.py
  
:three: Install the dlib library (todo: explanation)
  
 	pip install dlib
  
:four: Install opencv (todo: explanation)
  
  	pip install opencv-python
  
:five: Install the mathplotlib (todo: explanation)
  
	pip install matplotlib

:six: Clone this repository (or use SSH) and move it into the repo root.

	git clone https://github.com/mvrcx/SWP_Blitzer.git
	
:seven: Change the current directory to repo root

	cd PATH/OF/THE/GITHUB/REPOSITORY/

:eight: Install remaining dependencies using [Poetry](https://python-poetry.org) which is used for Python packaging and dependency management.

	poetry install
	
:nine: Create a subshell within the virtual environment by running:

	poetry shell

:fireworks: You are ready to run the algorithm by the following command. Check out the [wiki][3] to see the outcome and explanations on that!

	python3 main.py

### Optional

We prepared our future improvements in so called [Jupyter Notebooks](https://jupyter.org/index.html). If you want to test these, you will need to do the following steps.

:one: Install Jupyter Notebook

	pip install notebook

:two: Run Jupyter Notebook

	jupyter notebook

This will open your jupyter notebook workspace in the respective directory. Navigate to the wanted `.ipynb` file and run it.


## Troubleshooting

* Problems when installing `poetry`? When installing `poetry` something goes wrong. It's not automatically in your path, so if you run `poetry --version` nothing happens. If you use `zsh` or `oh-my-zsh` then you need to add the following line to your `.zshrc` file `export PATH="$HOME/.poetry/bin:$PATH`.

* Trouble with previewing notebooks directly in GitHub? --\> https://nbviewer.jupyter.org/


[1]:	https://www.mi.fu-berlin.de/inf/groups/ag-ki/Teaching/SS19/SWP-Ueberwachtes-Lernen/index.html
[2]:	https://www.mi.fu-berlin.de/inf/groups/ag-ki/index.html
[3]:	https://github.com/mvrcx/SWP_Blitzer/wiki/Documentation
[4]:	https://python-poetry.org/docs/
[5]:	https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
