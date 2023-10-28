## Continuous Integration using GitHub Actions of Python Data Science Project

[![Install](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/lint.yml)

[![Format](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/format.yml)

[![Test](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/test.yml)

IDS 706 Individual Project 1

Continuous Integration using GitHub Actions of Python Data Science Project

Demo Video: https://youtu.be/ZCTx2F_Q30Q

### Goal

+ establish a CodeSpaces environment that automates the process of loading a dataset, generating descriptive statistics on the dataset, and creating data visualizations of the dataset using `Pandas` and `matplotlib`, utilizing GitHub Actions. 

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the IDS-706-Python-GitHub-template for this project. This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

+ I downloaded the `Heart Attack Analysis & Prediction Dataset` from Kaggle.

### Dataset Description

`Heart Attack Analysis & Prediction Dataset` (simplify as `heart.csv`) is a csv file containing related information of 302 randomly picked people and their respective information including age, sex, exercise induced angina, number of major vessels, chest pain type, resting blood pressure, cholestoral, fasting blood sugar, resting electrocardiographic results, and chances of heart attack.


#### [Resources](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) 

### Overview

This project creates a Python script using Pandas for descriptive statistics. The specific steps involve: 

+ Create `lib.py` file
  
  + Read a dataset (CSV) using `Pandas`

+ Create a Jupyter Notebook `script.ipynb`

  + import `readfile` function from `lib.py`

  + Generate summary statistics (mean, median, standard deviation)

  + Create data visualizations

+ Create a test for Jupyter Notebook
  
  + Using nbval plugin for `pytest`
    
+ Create a Phython script `script.py`
  
  + import `readfile` function from `lib.py`

  + Generate summary statistics (mean, median, standard deviation)

  + Create data visualizations

  + Save summary statistics as `html` file into `output` folder

  + Save the data visualizations as image into `output` folder
    
  + Save summary statistics and data visualizations into `markdown` file

+ Create a `test_script.py` file 
  
  + Test Python script

+ Create a `test_lib.py` file 
  
  + Test library

+ Generate a summary report (PDF)
  
### Description

Step 1: In the `requirements.txt`, I pinned the following: 

+ #devops

+ black==22.3.0

+ click==8.1.3 

+ pytest==7.1.3

+ pytest-cov==4.0.0

+ #pylint==2.15.3

+ #rust based linter

+ ruff==0.0.284

+ boto3==1.24.87

+ #web

+ fastapi==0.85.0
  
+ uvicorn==0.18.3
  
+ #func
  
+ pandas == 2.0.3
  
+ matplotlib == 3.7.3
  
+ nbval == 0.10.0
  
+ jupyter == 1.0.0
  
+ tabulate == 0.9.0

Step 2: In the `Makefile`, I include the following:
       
       + Install all the requirements

       + Test Jupyter Notebook and script and lib

       + Formats code with Python black
       
       + Lints code with Ruff

       + All Inclusive Tasks

       + Generate and Push to Create Output in the Markdown File
       
<img width="659" alt="Screen Shot 2023-09-16 at 6 05 06 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/5a9dabfe-6c4c-4ebc-be67-cf31a700e1b1">

<img width="677" alt="Screen Shot 2023-09-20 at 10 23 37 PM" src="https://github.com/nogibjj/tinayi_Continuous_Integration_Python/assets/143360909/17648602-bd11-4eab-851e-92f120e61c53">

All of these are later run in the four `yml` files in Github Actions

Step 3: In the `lib.py` under the mylib folder, I include:

       + a `readfile` function, which reads a CSV file.

<img width="397" alt="Screen Shot 2023-09-16 at 9 44 50 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/de5a7135-1b7e-4e41-9433-f20c8a7e2a1e">

Step 4: In the `script.ipynb`, I create a scrapbook for my Python Script. It includes:
       
       + import `readfile` function from `lib.py`

<img width="841" alt="Screen Shot 2023-09-16 at 9 46 57 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/75f6b195-d9f2-4904-8c9b-a85aa2b22bcb">

       + a 'summary' function which generates summary statistics for the numeric columns in the DataFrame heart.csv.

<img width="1120" alt="Screen Shot 2023-09-16 at 9 47 58 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/620ca963-f852-4166-bedc-6699f3dbf2d3">

       + a 'median' function which calculate the median value for each column in heart.csv

<img width="1023" alt="Screen Shot 2023-09-16 at 9 48 32 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/2d5f9d4e-bbc8-4e1a-b65c-2fbb6d453521">

       + a 'histogram' function which generate histogram for each column in heart.csv

<img width="1044" alt="Screen Shot 2023-09-16 at 9 49 05 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/dc5c194e-8641-44d1-a4ab-7591f9c27b24">

       + a 'scatter_age_blood_pressure' function which generate scatter plot with fitted line for the 4th column (resting blood pressure) and the 1st column (age) in heart.csv

<img width="914" alt="Screen Shot 2023-09-16 at 9 52 05 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/444064eb-211b-43cb-82b6-e85d6db51c97">

Step 5: In the `script.py`, I created a Python Script. It includes: 
       
       + import `readfile` function from `lib.py`

       + a 'summary' function which generates summary statistics for the numeric columns in the DataFrame heart.csv. 
       
         + It is saved as a `html` file in my output folder.

       + a 'median' function which calculate the median value for each column in heart.csv. 
       
         + It is saved as a `html` file in my output folder.

       + a 'histogram' function which generate histogram for each column in heart.csv. 
       
         + It is saved as a series of graphs in the `png` form in my output folder.

       + a 'scatter_age_blood_pressure' function which generate scatter plot with fitted line for the 4th column (resting blood pressure) and the 1st column (age) in heart.csv. 
       
         + It is saved in the `png` form in my output folder.

       + a `create_output_directory` function which generates output directory to save `html` and `png`

       + a `save_to_markdown` function which creates a markdown file that summarizes all of the data summary statistics and visualization for heart.csv

<img width="909" alt="Screen Shot 2023-09-16 at 9 53 22 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/6cffd478-5ebf-4895-b238-354ab66dcce3">
       
<img width="922" alt="Screen Shot 2023-09-16 at 9 54 19 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/7c6b3fa2-3875-467d-8b1d-6a54e520f127">
       
<img width="830" alt="Screen Shot 2023-09-16 at 9 55 04 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/53719450-1e81-4b20-b892-9793e4651cb7">

<img width="707" alt="Screen Shot 2023-09-20 at 11 23 24 PM" src="https://github.com/nogibjj/tinayi_Continuous_Integration_Python/assets/143360909/3b8dbd38-a95f-4cda-a8a4-80c12abae73f">

Step 7: In the `test_lib.py`, I wrote a test function `test_readfile` which checks the function in `lib.py` 

       + check that the `readfile` function successfully reads the CSV file specified by file_path and returns a non-empty Pandas DataFrame.

<img width="737" alt="Screen Shot 2023-09-16 at 9 57 16 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/326cf62b-0e5c-4165-a58a-15d88c061dde">


Step 8: In the `test_script.py`, I wrote six test functions `test_output_directory_exists`, `test_summary`, `test_median`, `test_histogram`,`test_scatter_age_blood_pressure`, `test_save_to_mark_down` which checks the output folder and the markdown file for the summary statistics and data visualizations of `heart.csv`.

       + check the output directory exists

       + check the mean value of the fourth column (resting blood pressure)
       
       + check the median value of the fourth column (resting blood pressure)
       
       + check the standard deviation value of the fourth column (resting blood pressure)

       + check histogram for each column

       + check scatter plot for age and resting blood pressure

       + check markdown file summary report

<img width="938" alt="Screen Shot 2023-09-16 at 9 59 38 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/2db28f06-cc34-4d45-9424-4a830b9411f2">
       
<img width="921" alt="Screen Shot 2023-09-16 at 10 00 00 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/bfdc270f-8f2b-41ae-8730-d1b64f28153a">
       
<img width="346" alt="Screen Shot 2023-09-20 at 10 35 31 PM" src="https://github.com/nogibjj/tinayi_Continuous_Integration_Python/assets/143360909/fa47c7fe-022d-49b5-8052-5d4b7a9a64d4">

Step 9: I generated Data Visualizations in the output folder and the Summary Report in markdown file 

+ summary statistics

<img width="1013" alt="Screen Shot 2023-09-11 at 1 12 52 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/c0027011-01fa-4641-b1db-2bc16fc0b837">

+ median values

<img width="916" alt="Screen Shot 2023-09-11 at 1 13 15 AM" src="https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/50e1b86f-4158-4333-984a-4d32e5b2fb42">

+ histogram of each column

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/698dc927-6391-4266-8dcc-fa475a9df65a)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/658fd114-57b4-4d5d-a65a-a4f397e38248)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/aded97be-f769-47a9-81b1-4f5efe5118a5)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/46f27fd7-f0ab-45af-9ecd-33a0403cc631)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/bbe3d598-306d-4ed3-b3dc-61c8a37438a5)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/0ad57724-7e35-4d8a-8f8f-a50541f7a050)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/212788dc-c385-4953-a8d8-c8fc8cceac6f)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/861c299c-d037-45b4-9d0f-de29e1ca4de7)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/f4d65bca-c483-4866-a734-0576b5076cdb)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/c8c2ae73-95c9-410f-849b-4880bbcdcb66)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/e786fbf7-f238-48ef-9f26-705967b8843a)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/4f775859-6b73-4cfa-af1b-0e8bdd34b7b3)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/46be7348-fd3c-41c9-a608-bd1c8921c1f7)

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/2c5310b6-e218-4727-8c7f-59072ff97f8d)

+ scatter plot for resting blood pressure and age in heart.csv

![image](https://github.com/nogibjj/tinayi_week2_mini_project/assets/143360909/31a73193-129e-47dd-ac9b-d7a87e974f84)


Step 5: I generated the summary report (PDF) from Jupyter Notebook

#### [Summary Report PDF](./Summary-Report.pdf)

### Check Format and Test Approval Images

+ install code `make install`
  
<img width="1033" alt="Screen Shot 2023-09-16 at 5 28 02 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/190bdd58-e7e7-46e6-bcbc-ef0341884c95">

+ lint code `make lint`
+ format code `make format`
+ test code `make test`

<img width="1023" alt="Screen Shot 2023-09-16 at 6 46 49 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/3b218acf-5a3e-4577-89b7-e3b75556596b">

+ code `make all` executes install, lint, format, and test targets

<img width="1020" alt="Screen Shot 2023-09-16 at 6 47 15 PM" src="https://github.com/nogibjj/tinayi_individual_project1/assets/143360909/773f9d6f-6fe2-46a8-872d-9b9f47c1fd94">
