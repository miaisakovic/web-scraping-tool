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
$ pip3 --version
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
$ pip3 --version
```

### After Installing Initial Requirements
Clone this repository:
```
$ git clone https://github.com/miaisakovic/web-scraping-tool.git
``` 
When asked to enter credentials, input your username and personal access token.

If the libraries, BeautifulSoup 4, lxml, or Requests, have not been installed, run the following:
```
pip3 install beautifulsoup4
pip3 install lxml
pip3 install requests
```

## How to Use This Web Scraping Tool
Each time you would like to use this web scraping tool, run the following command:
```
$ python3.9 <relative path to uw_news.py>
```
