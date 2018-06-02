# Coursera Dump

Script takes 20 random courses from [Coursera feed](https://www.coursera.org/sitemap~www~courses.xml) and 
pull out summary about them into *.xlsx file.

## Requirements
Python 3 required.
 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt
```
For better interaction is recommended to use [virtualenv](https://github.com/pypa/virtualenv).


### Example input
```bash
python coursera.py
```
### Example output
Output file *courses-info.xlsx* will be created with summary about 20 random courses from 
[Coursera feed](https://www.coursera.org/sitemap~www~courses.xml).


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
