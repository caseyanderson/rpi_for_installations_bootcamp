## workflow

### parallel development environments

1. a laptop: your primary work space, you should always start exploring/testing your idea by writing code on your laptop to confirm general functionality
2. a Raspberry Pi: move your generally-functional code to your Raspberry Pi for platform-specific tests and, eventually, deployment.

In other words, I recommend doing most of your programming on your laptop and moving to the pi only after you have confirmed basic functionality.


## tools

### Xcode / The Command Line Tools

Do you have Xcode? To check go to the terminal and execute `xcode-select -p`.

* If `/Applications/Xcode.app/Contents/Developer` (or something similar) appears as a response proceed to the next step.
* If anything else happens download and install `Xcode` from [here](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) before moving on.

Enter `xcode-select --install` into the terminal, which should result in something like this:

<img src="/media/xcode-select_install_cmnd_line_tools.png" width="630" height="375">

Click `Install` to download and install the `Xcode Command Line Tools` (it takes a while so maybe go make some food or get a cup of coffee or something).


### Text Editor

You will test and confirm functionality in an interactive developer environment (IDE, more below) and use a Text Editor to write and save files filled with working/tested code (in fact you will often have them both up side-by-side). I recommend [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/) (and actually use Atom). Download and install one of them.


### Homebrew

Copy and paste this code into the terminal and press `enter` to install [homebrew](http://brew.sh/):  `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

If prompted, agree to the Xcode license

<img src="/media/agree_to_xcode_license.png" width="630" height="375">

by executing `sudo xcodebuild -license` in the terminal.

Search to see if something is available on `homebrew` with `search`. For example:  `brew search python3`


### Python3

To install Python 3 (**not Python 2**) execute `brew install python3` in the terminal.


### PyPI

PyPi is frequently referred to as `pip`. It is used to manage Python library installations and ships with `Python3` when installed via `Homebrew`. The command to use it is `pip3`, **not** pip.

Search for something on `pip` with the `search` command. For example: `pip3 search ipython`


### iPython

Install `iPython` via `pip`: `pip3 install ipython`

executing `ipython3` in the terminal starts the [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment).
