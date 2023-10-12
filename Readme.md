# Anomaly Detection in CodeUp Curriculum Access Logs

## Project Description
In this project, we set out to answer some questions regarding the access logs of the CodeUp curriculum.

## Project Goals
- Identify the lesson that attracts the most traffic consistently across cohorts.
- Discover any cohorts that refer to a lesson significantly more than others.
- Identify students who, when active, hardly access the curriculum.
- Detect any suspicious activity in the curriculum access logs.
- Verify changes in curriculum access for students and alumni in 2019.
- Identify the topics that grads continue to reference after graduation.
- Determine the least accessed lessons.

## Table of Contents
- [Project Description](#project-description)
- [Project Goals](#project-goals)
- [Data Dictionary](#data-dictionary)
- [Project Planning](#project-planning)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Visualizations](#visualizations)
- [Steps to Reproduce](#steps-to-reproduce)
- [Initial Questions/Hypotheses](#initial-questionshypotheses)
- [Additional Findings](#additional-findings)

## Data Dictionary
To be populated based on the data used in the project.

## Project Planning
1. Acquire the data from a .csv file.
2. Prepare the data by dropping and renaming columns and filling null values.
3. Perform exploratory data analysis to answer the project questions.

## Data Preparation
1. Read data from CSV files.
2. Rename columns and merge tables.
3. Drop null values and convert columns to appropriate data types.
4. Introduce an `activity` column to specify student activity status.
5. Filter out irrelevant paths (homepages and JSON files).

## Exploratory Data Analysis
1. Identify the most accessed pages per program.
2. Explore unique users and their activity.
3. Detect any abnormal IP access.
4. Group data to identify most visited lessons per program.
5. Create a DataFrame to track path access by cohort.
6. Create a function to identify top cohorts for specific lessons.

## Visualizations
1. Bar plots for the top 5 most visited lessons by program.

## Steps to Reproduce
1. Clone this repository.
2. Run the `Final_Notebook.ipynb` Jupyter Notebook.

## Initial Questions/Hypotheses
### Which lesson appears to attract the most traffic consistently across cohorts (per program)?
- Findings: There are 4 different programs. The lesson that appears the most for each program is:
  - Program 1: `javascript-i`
  - Program 2: `javascript-i`
  - Program 3: `content/html-css`
  - Program 4: `classification/overview`

### Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
- Findings: Cohort access varies. Specific findings are available in the notebook.

### Are there students who, when active, hardly access the curriculum?
- Findings: There are 911 unique users. Additional details are available in the notebook.

### Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be?
- Findings: Two IPs accessed the curriculum an extraordinary number of times. Further analysis did not reveal abnormal activity.

### At some point in 2019, the ability for students and alumni to access both curricula (web dev to ds, ds to web dev) should have been shut off.
- Findings: Data Science access seems to have stopped in 2019, but Dev access continued.

### What topics are grads continuing to reference after graduation and into their jobs (for each program)?
- Findings: Topics accessed post-graduation are detailed in the notebook.

### Which lessons are least accessed?
- Findings: To be populated based on the notebook.

### Anything else I should be aware of?
- Findings: To be populated based on the notebook.

## Additional Findings
To be populated with any other important findings from the project.