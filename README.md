# Python pitfalls

Description here...

# Prerequisites

## Windows
Install the following prerequisites:
- [Visual Studio Code](https://code.visualstudio.com/)
- [Windows Subsystem for Linux 2 (WSL 2)](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Docker desktop](https://www.docker.com/products/docker-desktop)

# Setup the project

## Clone repository
Open WSL terminal and create directory :
```
mkdir ~/myprojects
cd ~/myprojects
git clone git@gitlab.com:conscia.com/si/sw-kt/python-pitfalls.git
cd python-pitfalls
code .
```

## Open in container
Once visual studio code opens, select `Extensions` in the left menu and type `Remote Development` into search field and install the one at the top (it should be authored by Microsoft).

Once the extension is installed, select `Remote explorer` from the left menu and select `Containers` from the drop-down menu at the top of the navigation pane. Click the + sign and select `Open current folder in container`. The container should be built and started.
