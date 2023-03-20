# Python Toolkit

## Goal
This toolkit is intended to provide you with easily-modifiable sample code and basic functions for processing data using Python. These files are intentionally structured to be easy for newer users to customize.

## Getting started
### Integrated development environment (IDE) configuration
You will need somwehere to write and test your code. A program called an Integrated Development Environment (IDE) provides exactly this. I recommend using Microsoft Visual Studio Code ("VS Code") because it is free, extensively customizable, and widely used. You can download this from Microsoft directly or install via a managed software center (if on a corporate or client device).

Once you have VS Code installed, follow these steps:
* In the "Extensions" section of VS Code, find and install the Python extension from Microsoft (Pylance should also automatically install alongside this extension).
* Ensure that VS Code is using the appropriate version of Python
   * [add detail].
* Set VS Code to run files in the file's own directory rather than the directory of the current open file.
   * Open File > Preferences > Settings (shortcut: `CTRL ,`) and search `executeinfiledir`
   * Ensure the box is checked.

### Python configuration
Depending on what you want to do, you may need to install additional code libraries to extend Python's functionality. You can do this by opening your terminal and typing `pip install pandas` or `conda install pandas` if you wanted to install the "pandas" library.

You will know if you are missing a necessary library because you will see an error like "ModuleNotFoundError: No module named 'pyarrow'". 

#### pip vs conda
[add detail]

## Contents
1. Parquet file processing
2. CSV file processing
3. Plotting toolbox
4. Querying Dremio via API 

## Notes
Many of these files began as responses to prompts given to chatGPT in February and March 2023. I am deeply grateful to OpenAI for developing this tool.

The LinkedIn Learning course "Learning Python" by Joe Marini was instrumental in helping me understand how to navigate basic Python features and demonstrating tips for working effectively in VS Code. His course files are also available on Github here: https://github.com/LinkedInLearning/learning-python-2896241
