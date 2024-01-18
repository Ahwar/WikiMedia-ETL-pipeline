# Report

This report provides a detailed description of the ETL process, considerations for scalability, and a high-level architecture diagram of the ETL pipeline.

## ETL Approach
Here I describe my ETL pipeline in detail:  

**Data Retrieval**

First, I retrieved a list of directories from the homepage and selected the most recent month. I then navigated into that directory and compiled a list of all the files it contained.

**Extraction Phase**

For the extraction phase, I processed each file. This involved downloading the compressed .gz files and saving them in a directory structured as 'download/month/language'. After downloading, I extracted these files and stored them in the same directory.

**Transformation Phase**

During the transformation phase, I loaded the saved file using the pandas library and cleaned the loaded pandas dataframe. 

**Loading Phase**

I used the PostgreSQL Python library to create a table named 'wiki', and loaded the transformed dataframe into this table. To identify the month and language the data belonged to in future analyses, I included new columns for the month and language during the loading process.

**Data Duplication Check**

To avoid loading the data again, if we run a new pipeline, the data won't be loaded if the target table already contains the data of the month.

**Automation**

To ensure the code runs each month to load the data of the last month, we set up a cron job that will run the ETL pipeline code each month at the third day. The rationale behind choosing the third day for data loading is to account for potential delays in Wikimedia's data upload process, which may not occur promptly on the first day.

### ETL Diagram

![ETL Diagram](bin/ETL_diagram.png)

This is a diagram providing a simplified overview of our ETL approach.  

