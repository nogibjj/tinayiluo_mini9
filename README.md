## Mini Project 9 Cloud Host Notebook Data Manipulation

[![Install](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/lint.yml)

[![Format](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/format.yml)

[![Test](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/tinayi_individual_project1/actions/workflows/test.yml)

IDS 706 Mini Project 9

### Cloud Host Notebook

[Google Colab](https://colab.research.google.com/github/nogibjj/tinayiluo_mini9/blob/main/script.ipynb)

### Goal

+ Set up a cloud-hosted Jupyter Notebook (Google Colab)

+ Perform data manipulation tasks on a sample dataset

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the nogibjj/tinayi_Continuous_Integration_Python for this project. 

+ I used the `Heart Attack Analysis & Prediction Dataset`.

### Dataset Description

`Heart Attack Analysis & Prediction Dataset` (simplify as `heart.csv`) is a csv file containing related information of 302 randomly picked people and their respective information including age, sex, exercise induced angina, number of major vessels, chest pain type, resting blood pressure, cholestoral, fasting blood sugar, resting electrocardiographic results, and chances of heart attack.

#### [Resources](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) 

### Overview

+ Setup and configuration 

+ Data manipulation tasks 

### Description

+ Create a Jupyter Notebook `script.ipynb`

  + Ingest

    + Read and view `Heart Attack Analysis & Prediction Dataset`

  + EDA

    + Generate summary statistics (mean, median, standard deviation)

    + Filter the Data

  + Create aata visualizations (histogram, scatter plot)
    
+ In `Makefile` run Jupyter Notebook
       
  + Install all the requirements

  + Test Jupyter Notebook and script and lib

  ```
  test:
	python -m pytest -vv --nbval --cov=script --cov=mylib test_*.py *.ipynb
  ```

  + Formats code with Python black
       
  + Lints code with Ruff

  + All Inclusive Tasks

  + Generate and Push to Create Output in the Markdown File
       
+ Four `yml` files in Github Actions

### Summary Report and Data Visualizations 

Generated the summary report (PDF) from Jupyter Notebook

#### [Summary Report PDF](./Summary-Report.pdf)

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


### Check Format and Test Approval Images

