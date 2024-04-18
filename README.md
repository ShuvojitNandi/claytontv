# The official website for Clayton TV

<img width="1672" alt="image" src="https://github.com/Clayton-TV/claytontv/assets/14878653/c2c09122-1118-4b3c-bfbb-3d3b9516915d">

\*This is a demo site, soon to undergo substantial changes! Join our hackathon!

## Getting Started

To get started, you'll need to install a few things. All the tech used is cross-platform, but there will still be a few differences for macOS, Windows and Linux users.

Please follow the instructions carefully, and raise an issue for anything that doesn't work!

### Prerequisites

One of the following code editors (aka an Integrated Development Environment, or IDE)
- [VS Code](https://code.visualstudio.com/) (Free! You'll likely want the [Django extension](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) too)
- [PyCharm](https://www.jetbrains.com/toolbox-app/) (Pycharm Community is free, Pycharm Pro is Paid/Trial. Or, download the toolbox and install the Release Candidate, which is free but not always stable.)
- If you dare, you can use Atom, Sublime, or (please don't) Notepad++.

GitHub Desktop (A nice UI for git, the version management software. It will install git for you if you don't already have it.)
- https://desktop.github.com/ (Mac and Windows only. Linux users, you're likely familiar with terminal commands anyway, but check out [Oh-My-Zsh](https://github.com/ohmyzsh/ohmyzsh?tab=readme-ov-file#basic-installation) and their [git plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git))

Python (the programming language that our Django app uses)
- [Python 3.12](https://www.python.org/downloads/release/python-3123/) (Select the `Windows installer (64-bit)` or `macOS 64-bit universal2 installer`, depending on your OS. Linux users you can follow [this guide](https://ubuntuhandbook.org/index.php/2023/05/install-python-3-12-ubuntu/))
- Note: for users that use an existing Python version, don't worry, you can have multiple versions installed at a time. We'll use `pipenv` to auto-configure the app to use 3.12.

Node.js (for the front-end design of our app)
- [Node 20.1.2 LTS](https://nodejs.org/en/download) (Long-Term Support, or LTS, means that it will get features and security updates for longer)
- Alternatively, for Mac or Linux users, check out [Node Version Manager](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating). This requires technical skill to set up.

### Install instructions

Clone the repo in Github Desktop, or with the following command
```sh
git clone git@github.com:Clayton-TV/claytontv
```

Open the project in your editor, or change directory into the project
```sh
cd claytontv
```

Set up python environment
```sh
# Install pipenv
python3.12 -m pip install pipenv

# Start pipenv
pipenv shell
```

Install python dependencies
```sh
pipenv install
```

Install the node dependencies
```sh
npm install
```

Run the migrations
```sh
python manage.py migrate
```

Launch the app
```sh
# Open a new terminal window each for the following commands

# Run the python server (backend)
python manage.py runserver
# Or, you can specify the address
python manage.py runserver localhost:8001

# Run the vite server (frontend)
npm run dev
```

## Contributing


## Licence
