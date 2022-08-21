# Web Scraping Tool
A web scraping tool that gathers all COVID-19 related information from the University of Waterloo’s News website.

For more information, visit: https://devpost.com/software/uwaterloo-safe-ready

## Table of Contents
* [Setup](#setup)
  * [For Linux](#for-linux)
  * [For MacOS](#for-macos)
  * [After Installing Initial Requirements](#after-installing-initial-requirements)
* [How to Use This Web Scraping Tool](#how-to-use-this-web-scraping-tool)

## Setup 
### For Linux
If Python has not been previously installed, run the following:
```
$ sudo apt install python3.9
$ python3.9 --version
```
If pip has not been previously installed, run the following:
```
$ sudo apt-get install python3-pip 
$ pip --version
```
If the libraries, Beautiful Soup 4 and lxml, have not been installed, run the following:
```
pip install beautifulsoup4
pip install lxml
```

### For MacOS
If Homebrew has not been previously installed, follow the instructions listed [here](https://brew.sh/).

If Python has not been previously installed, run the following:
```
$ brew install python@3.9
$ python3.9 --version
```
If pip has not been previously installed, run the following:
```
$ python3.9 -m ensurepip --upgrade
```
If the libraries, Beautiful Soup 4 and lxml, have not been installed, run the following:
```
pip3.9 install beautifulsoup4
pip3.9 install lxml
```

### After Installing Initial Requirements
Clone this repository:
```
$ git clone <web-scraping-tool URL>
``` 
When asked to enter credentials, input your username and personal access token.

## How to Use This Web Scraping Tool
Each time you would like to use this web scraping tool, run the following command:
```
$ python3.9 <file path>
```
