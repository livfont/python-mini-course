# Python Mini Course
Welcome to Introduction to Python. This is the repository for Python mini-course.

<br/>

## Table of contents
* [Basic Information](#basic-information)
  - [Class Schedule](#class-schedule)
  - [Contact Information](#contact-information)
  - [Class Resources](#class-resources)
* [Environment Set Up](#environment-set-up)
  - [Installation Requirements](#installation-requirements)
* [Terminal Commands](#terminal-commands)
  - [Windows](#windows)
  - [Mac/Linux](#maclinux)
* [Git Setup](#git-setup)
  - [Extra Git/Github Tutorial](#extra-gitgithub-tutorial)
* [File Types](#file-types)
* [Run Python](#run-python)
  -[Run Python Code in Terminal](#run-python-code-in-terminal)
  -[Run Python Code in Visual Studio Code](#run-python-code-in-visual-studio-code)
* [Visual Studio Code Shortcuts](#visual-studio-code-shortcuts)
  - [Windows](#window)
  - [Mac](#mac)
* [Contributing](#contributing)
* [License](#license)

<br/>

## Basic Information

### Class Schedule
|  | |
| ------------- | ------------- |
|Date| 6 weeks (5/30 - 7/6)|
|Meeting Time| Tuesday & Thursday 3:15-5:15 PM|
|Classroom| S344 (Beginner) & S346 (Advanced)|

### Contact Information
|  |  |
| ------------- | ------------- |
|Jacob Jalinski| jjalinski134544@bergen.edu |
|Lisa Nam| lnam@me.bergen.edu |

### Class Resources
|  |  |
| ------------- | ------------- |
|Class Repository|https://github.com/python-mini-course/python-mini-course.git|
|Google Drive|https://drive.google.com/drive/folders/1Ar3fIPh9pUcBqGzvK1PriUtSu2PK8zgd?usp=sharing|
|Presentation|https://mebergen-my.sharepoint.com/:f:/g/personal/lnam_me_bergen_edu/Eq1HOiuQyElDooeQ3uhCQd8BJ4qi1eF3221sBxgLm_Y-rA?e=37CouU|
|Class Discord Channel| https://discord.gg/h6ggSdd2|

<br/>

## Environment Set Up

### Installation Requirements
|  |  |
| ------------- | ------------- |
|Visual Studio Code|https://code.visualstudio.com/|
|Python3| https://www.python.org/|
|Git| https://git-scm.com/downloads|

**For Mac, make sure to set PATH correctly**
- Open the Command Palette (Cmd+Shift+P) 
- Find & Run `Shell Command: Install 'code' command in PATH`

**For Mac, run the following command in the terminal before installing Git:**
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<br/>

## Terminal Commands
### Windows
|  |  |
| ------------- | ------------- |
|dir| which will list all the files in the current directory.|
|cd <directory>| moves you from the current directory to a specified |directory within the current directory.|
|cd ..| will bring you back one directory.|
|cd /| will bring you to your root directory (Not the same as your home directory which windows has 0 shortcuts for).|
|copy NUL <filename>| will create an empty file with that name in your current directory.|
|del <filename>| will delete that file.|
|mkdir <directoryname>| will create a new directory with that name in your current directory.|
|rmdir <directory>| will delete that directory from your current directory.|
|TAB| complete <directory> or <filename>|
| code . | open the current directory in Visual Studio Code |

### Mac/Linux
|  |  |
| ------------- | ------------- |
|ls |which will list all the files in the current directory.|
|cd <directory> |moves you from the current directory to a specified directory within the current directory.|
|cd .. |will bring you back one directory.|
|cd / |will bring you to your root directory.|
|cd ~ |will bring you back to your home directory.|
|touch <filename> |will create a file if it doesn't exist. |
|rm <filename> |will delete a file|
|mkdir <directoryname> |will create a new directory with that name in your current directory.|
|rmdir <directory> |will delete that directory from your current directory.|
|TAB| complete <directory> or <filename>|
| code . | open the current directory in Visual Studio Code |
| open . | open the current directory in finder |

<br/>

## Git Setup
1. Sign Up for [GitHub] (https://github.com/)

2. Set Up Your Github Account on Your Local Computer
  - Set your username in Git: `git config --global user.name "YOUR_NAME"`
  - Set an email address in Git: `git config --global user.email "YOUR_EMAIL"`<br />
  **If Mac gives errors try adding `sudo` in front of the commands**

3. Fork Repository
  Click Fork on the [Class Repository](https://github.com/python-mini-course/python-mini-course)

4. Clone Repository
  - Get a link to your repository by clicking `<> Code` button
  - Clone your repository: `git clone YOUR_REPO_LINK`

5. Repository Git Setup
  - cd into your project repository `cd python-mini-course`
  - add remote class directory `git remote add class https://github.com/python-mini-course/python-mini-course.git`

6. Commit
  - Save your work by committing
  - First stage all your changes: `git add .`
  - Commit with a message: `git commit -m "YOUR_MESSAGE"`

7. Push Changes
  - Push or Sync all your changes to your code with Github by pushing `git push origin main`
  **All of your code is saved in your Github account now**

8. Pull Changes from the Class Repository
  - Rebase: `git config pull.rebase true`
  - Pull from the class repository: `git pull class main`
  - Resolve any potential conflicts & commit if necessary
  - Push to my Github: `git push origin main`

### Extra Git/Github Tutorial
- [Introduction to Git](https://zarkom.notion.site/zarkom/Introduction-to-Git-ac396a0697704709a12b6a0e545db049)
- [Introduction to GitHub](https://zarkom.notion.site/zarkom/Introduction-to-GitHub-202af6f64bbd4299b15f238dcd09d2a7)

<br/>

## File Types
| Extension | Name | Description |
| ------------- | ------------- | ------------- |
|.py| Python file | Most common Python coding file |
|.ipynb| Jupyter notebook | Python file formated like a document |
|.txt| Text file |A file that contains text only|
|.md| README file | A formal format file for a programming repository|
|.gitignore| gitignore file | A list of folders & files ignored by Git |

<br/>

## Run Python
### Run Python Code in Terminal
`python3 /YOUR_PATH_TO_FILE/PYTHON_FILE.py`
### Run Python Code in Visual Studio Code
Click Run -> Run Without Debugging

<br/>

## Visual Studio Code Shortcuts
### Window 
[Window Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
### Mac
[Mac Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

<br/>

## Contributing

If you see an error or a place where content should be updated or improved, just fork this repository to your Github account, make the change you'd like and then submit a pull request. If you're not able to make the change, file an [issue](https://github.com/python-mini-course/python-mini-course/issues/new).

## License

`Python Mini-Course` is licensed under the [MIT License](http://opensource.org/licenses/MIT).
