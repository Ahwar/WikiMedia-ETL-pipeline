## Business Context

`FlavorWiki` is a digital market research company that is revolutionizing the way the food industry collects, analyzes and leverages consumer insights across all relevant purchase drivers. As a Data Scientist, your jobs in tech will be related to developing any feature related to sensory analysis. This includes data processing, data analysis and some basic statistical analysis.  

Specifically, the role of a Data Scientist is to do research together with Consumer Scientists, and then write code/script to be deployed then in the `FlavorWiki`’s application as a new feature or even a new tool. Your assignment here is to provide  code/scripts that can be used for analyzing the sensory data collected by `FlavorWiki`.

## Data Source

The data will be available via CSV files:

-  `flavorwiki.csv`
-  `jar.csv`
-  `penalty.csv`


## Instruction  

The state of sensory analysis is mostly related to basic statistical analysis such as descriptive, significance and/or comparison analysis. We encourage you to do basic statistical analysis from the data. There will be 2 different analyses you need to complete.
### Analysis
#### Statistical Significance of Difference:  
Please use a csv file named `flavorwiki.csv`. In the file, you will find consumer responses data related to some products. There is a column `Product` which indicates the product names available in the survey and Answer Value which contains the product’s overall liking score.

In this first section, you must create a Python script to analyze the data. The analysis works by comparing the average overall liking scores between the products to see whether it's significantly different or not. You can choose one of two statistical tests (`Tukey` or `Fisher`) with alpha level either at `5%` or `10%`. If you want to code both tests, it is fine too.

#### Sensory Penalty Analysis:
In the second section, you need to create a Python script to be used to run an analysis named `Penalty Analysis`. `Penalty analysis` is one of the common analyses used in the sensory analytic industry. Basically, it used to assist in identifying decreases in acceptability associated with sensory attributes not at optimal levels in a product. You can find a detailed description and the formula of penalty analysis here. 

For penalty analysis, you will used 2 different csv files:
-  `jar.csv`: a file contains Just About Right (JAR) data  
-  `penalty.csv`: a file contains data about Overall Liking score

Please write a Python code to run a `Penalty Analysis`` separately for each product available in the file.

 

## Submission Requirements
-  Please write the code using Python version 3.6x or above

-  The output of your code should be files in 2 different format: Excel (or CSV) file and JSON

-  You can customize the format/template of your output files. However, please also provide a brief explanation about how to read those files

-  Provide the output for each analysis separately



## Terms & Conditions

-  Don’t make the problem statement, dataset and your submission publicity available, for by example posting this problem on blog, forum, etc
-  The candidate is expected to finish the test within 72 hours, started from the candidate received the instructions and dataset