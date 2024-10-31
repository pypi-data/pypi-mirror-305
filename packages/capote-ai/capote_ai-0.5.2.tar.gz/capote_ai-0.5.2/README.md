# Capote AI Package Documentation

This document details how to setup the environment for the AI component.

## Building the environment
1. Create an `.env` file and add the following:
```.env
OPENAI_API_KEY = __input_here__
organization = __input_here__
project = __input_here__
```
2. Setup a virtual environment using the following command:
```powershell
py -3.12 -m venv venv_name
```
- Make sure to update `.gitignore` if you set the `venv_name` to anything other than `venv`.

3. Activate the virtual environment:
```powershell
.\venv_name\Scripts\activate
```
<!-- 4. Install all requirements using `pip`:
```powershell
pip install -r .\requirements.txt
```
- Make sure to `cd AI/src` before running this. -->

## Calling the AI Package
Make sure you have activated your virtual environment. A sample implementation has been shown in `package_test.py`.