# Supervised and unsupervised machine learning - Summer Term 2021
This repository contains all *public* material needed to reproduce our task in the course [Supervised and unsupervised machine learning in the science of behaviour][1] of the research group [Berlin BioRobotics Lab][2] at Freie Universität Berlin.

THIS IS A TUTORIAL FOR UNIX/macOS

## First things first
1. The repository (code section) contains everything related to the programming assignments we will do throughout the course.
1. All other information (data, assignment instructions, etc.) you find in the :arrow\_right: [wiki][3]:arrow\_left:.
1. Any private data will not be published and is running on our own computers as soon as we retrieve the data. 
1. You can clone the code repository in order to reproduce our solutions or to test/run this code.

## Getting started

To make sure everyone uses the same environment and make sure we don't run into any dependency hell :volcano: let's start with the prerequisites.

### Prerequisites

In order to run our code, please ensure that you have a Python version greater or equal to `3.6.1`, a working installation of and [git][5] installed.


### Setup

1. We start off by installing pip which is a package manager. Open your terminal and run

  `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
  
  `python3 get-pip.py`

1. Clone this repository (or use SSH) and move it into the repo root.

	git clone https://github.com/FUB-HCC/hcds-winter-2020.git
	cd hcds-winter-2020

1. Install the dependencies in the repo root.

	poetry install

1. Create a subshell within the virtual environment by running:

	poetry shell

1. Open the project with Jupyter in your browser.

	jupyter notebook

## Troubleshooting

* Problems when installing `poetry`? When installing `poetry` something goes wrong. It's not automatically in your path, so if you run `poetry --version` nothing happens. If you use `zsh` or `oh-my-zsh` then you need to add the following line to your `.zshrc` file `export PATH="$HOME/.poetry/bin:$PATH`.

* Trouble with previewing notebooks directly in GitHub? --\> https://nbviewer.jupyter.org/

---- 
`[1]` https://mungingdata.com/python/jupyter-workflow-poetry-pandas/, accessed: 2020-10-28

[1]:	https://www.mi.fu-berlin.de/en/inf/groups/hcc/teaching/winter_term_2020_21/course_human_centered_data_science.html
[2]:	https://www.mi.fu-berlin.de/en/inf/groups/hcc/index.html
[3]:	https://github.com/FUB-HCC/hcds-winter-2020/wiki
[4]:	https://python-poetry.org/docs/
[5]:	https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
