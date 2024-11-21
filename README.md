# pyanakit
DataToolbox is a versatile data analysis toolkit with a user-friendly GUI. Simplify your data tasks with pyanakit.

## Data Analysis GUI 

### Overview
This project features a graphical user interface (GUI) for performing data analysis using Principal Component Analysis (PCA) and data visualization using different plot types. It is designed for users who want to analyze datasets visually without deep programming expertise. 

### Features
- Visualize data through plots, heatmaps, and PCA plots.
- Interactive GUI built with Tkinter.

### Requirements
- Python 3.x (must be installed)
- Packages (explain in the next step):
  - matplotlib
  - numpy
  - scikit-learn
  - scipy
  - seaborn
  - statsmodels
  - tkinter (usually included with Python)

## Installation 

### Step 1: Download Application
1. Open a command line interface: 
- For Windows: Git Bash, Anaconda PowerShell or Command Prompt
- For macOS/Linux: Terminal  
- Commands are applicable across all operating systems
2. Navigate to the folder where you want to save the application. Replace the path with your desired directory: 
```bash
cd C:/Path/to/directory
```
2. Clone the repository / Download the application using the following command: 
```bash 
git clone https://github.com/Pastfran/pyanakit.git
```
### Step 2: Install required Packages: 
1. Open your command line interface
- For Windows: Command Prompt or Anaconda PowerShell Prompt
- For macOS/Linux: Terminal
- Commands are applicable across all operating system  
2. Ensure Python is properly set up on your system and recognized in the Command Prompt. You can check this by using the command below. \
If Python is installed and the version displayed, you are good to go. If not, ensure Python is installed and added to your system's PATH.
```bash 
python --version
```
Note: On Linux systems, the command python may point to Python 2.x or may not be available at all. To ensure that Python 3 is used, always use `python3`. You can check the Python version with:
```bash 
python3 --version
```
3. If the required packages are not already installed, you can add them using pip. 
```bash
pip install matplotlib numpy pandas scikit-learn scipy seaborn statsmodels
```

## Starting the Application 
1. Open your command line interface
- For Windows: Command Prompt or Anaconda PowerShell Prompt
- For macOS/Linux: Terminal
- Commands are applicable across all operating system  
2. Navigate to the folder where the application is located and into the `src` folder. Replace the path accordingly:
```bash	
cd C:/Path/to/file/src
```
4. Launch the application with using this command:
```bash	
python gui.py
```
Note: On Linux systems, the command python may point to Python 2.x or may not be available at all. To ensure that Python 3 is used, always use `python3`.
```bash 
python3 gui.py
```

### Getting Started
Once the application is open: 
- Load your data using the "Load Data" button. 
- Choose your desired analysis/visualisation option (e.g. PCA).
- Explore the generated visuals and uncover patterns in your data. 

## Sample Datasets
To help to get started quickly, we have included sample datasets for testing the application. These datasets are included in the `examples` folder. 
Navigate to and select the sample data via the GUI. \
These datasets demonstrate the various features of the tool, allowing you to explore different plots and visualize how they represent your data. They are ideal for experimentation and learning.


