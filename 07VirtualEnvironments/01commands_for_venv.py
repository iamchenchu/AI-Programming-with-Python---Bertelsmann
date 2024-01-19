"""Conda
Conda does two things: manages packages and manages environments.
As a package manager, conda makes it easy to install Python packages especially for data science. For instance, typing conda install
numpy will install the numpy package. As an environment manager, conda allows you to create silo-ed Python installations. With an environment 
manager, you can install packages on your computer without affecting your main Python installation.The command line code looks something like this:

conda create --name environmentname
source activate environmentname
conda install numpy


Pip and Venv
There are other environmental managers and package managers besides Conda. For example, venv is an environment manager that comes pre-installed with Python 3. Pip is a package manager.
Pip can only manage Python packages whereas conda is a language agnostic package manager. In fact, conda was invented because pip could not handle data science packages that depended on
libraries outside of Python. If you look at the history of conda, you'll find that the software engineers behind conda needed a way to manage data science packages (NumPy, Matplotlib, etc.)
that relied on libraries outside of Python. Conda manages environments AND packages. Pip only manages packages.
To use venv and pip, the commands look something like this:

python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy"""