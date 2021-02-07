# Quiz Engine

The quiz engine exists to facilitate the transactions between a frontend interface and a database made up of quizzes and users, providing the necessary data and access, as needed.

## Installation

To run the application, you will need an installed version of Python 3.9.1 (earlier may work, but it's not guaranteed), and Git in order to download the repositoty from GitHub.

These can both be found, respectively, at:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

[https://git-scm.com/downloads](https://git-scm.com/downloads)

Once those have been installed for your Operating System, you can pick a folder where you'd like the repository to be, open up Git Bash, and clone the repository by typing something like:

```bash
git clone [GitHub link].git
```

Now that the repository is on your local machine, you can install all of the relevant Python packages. This can be done either on your standard Python installation, or in a virtual environment that will only contain the packages needed for this app to work. To create and activate a virtual environment in Python 3, please follow the instructions at:

[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

To install everything on your standard Python, open a CLI, change directory to the root directory of the repository and type:
```bash
py -3 -m pip install -r requirements.txt
```
To install it on a virtual environment, go to the root repository directory, open a CLI, activate the virtual environment, and type:
```bash
pip install -r requirements.txt
```
You should now be able to run the quiz API.

## Usage

In order to actually launch the app, first open up a CLI, then change the directory to the root directory of the repository.

If you are running with your standard Python installation, then type:
```bash
py -3 -m flask run
```

If you've activated your virtual environment, type:
```bash
flask run
```

This should launch a testing server that can be used to check out the app's features locally. A browser of choice can now be opened, and the app homepage should be able to be accessed through the default link:

[http://localhost:5000](http://localhost:5000)

If not, then check out the CLI, where is says "Running on", which should point to the right port.

Afterward, you may use [Postman](https://www.postman.com/downloads/), or a language of your choice, to make calls to the API.

A tool that may help interact with the SQLite database more freely is also available [here](https://sqlitebrowser.org/dl/).

To close the testing server, you can press <kbd>CTRL</kbd>+<kbd>C</kbd> in the CLI, or whichever instructions are displayed next to the "Running on" part of the CLI.