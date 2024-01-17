# takehome-data-engineering-2024
## Task  


### Background
You will work with the Wikimedia Clickstream dataset, available at [Wikimedia Dumps](https://dumps.wikimedia.org/other/clickstream/)
The datasets contain monthly Wikipedia clickstream data dumps for a selection of top Wikipedia languages by Wikipedia size.
Each file contains counts of (referrer, resource) pairs extracted from the request logs of Wikipedia. 
Since the datasets are large, you may consider using [the latest dump only](https://dumps.wikimedia.org/other/clickstream/2023-12/). 

### Objectives 
1. Develop an ETL pipeline to ingest this clickstream data to a database of your choice. The raw dumps might include missing values or some irrelevant data. 
Transform the data into a suitable format and document all steps. 
2. Assuming the clickstream data will be updated periodically, the data ingestion should run automatically (e.g., daily or weekly) as part of a cron job. 
3. Propose methods to ensure data quality and consistency across the pipeline. Describe how you would handle issues like duplicate data, missing values, and schema changes. If you are a data quality ninja, be bold and add test cases for your pipeline as part of an automated Github Actions!
4. Explain (writeup only, no code) how your design scales with increasing data volumes and what strategies you would employ to ensure performance is not compromised. This includes considerations for data partitioning, indexing, and caching.
5. Explain (writeup only, no code) how would you modify the pipeline to support streaming data ingestion in real time.
6. (Optional/Bonus) Data Analysis and Machine Learning: Perform exploratory data analysis (EDA) on your dataset. Identify trends, patterns, and anomalies. Implement a machine learning model using the dataset. Possible tasks might include predicting future click patterns or classifying types of clicks.

### Deliverables
1. Code: Push all code to this GitHub repository. We should be able to run your pipeline and replicate your steps on our end, from db setup, to data ingestion.
2. Documentation: Include a README with an overview, setup instructions, and a detailed explanation of your approach.
3. Report: Submit a report detailing your ETL process, scalability considerations, streaming modifications, a high-level architecture diagram of the ETL pipeline, 
 and findings from the data analysis/machine learning phase.

### Evaluation Criteria
There is no right or wrong way to accomplish this task. Your goal should be to show off your Data Engineering skills and demonstrate a thorough analysis of the problem during the review session. 
If you're a data wizard, you can show off your deep familiarity with data processing, architecture choices, fault tolerance, and scalability. 
If you're a modeling/analytics expert, show us a deep understanding of the models you use and show us how you'd set up metrics. Play to your strengths!

### Requirements:
Please make your first commit when you start working on the exercise and your second commit exactly 1 hour after the start. After 1 hour you are free to continue working on the problem for up to 48 hours. We ask that you add a commit any time you stop or restart working on the problem within those 48 hours.

Please let us know by email when this is ready for review.

Best of luck!


## Install


### Installing PostgreSQL

Follow these steps to install `PostgreSQL` on Ubuntu (Linux):

1. Update your local `apt` package cache:
   ```
   sudo apt update
   ```

2. Install PostgreSQL with:
   ```
   sudo apt install postgresql postgresql-contrib
   ```

3. Ensure that the service is started:
   ```
   sudo systemctl start postgresql.service
   ```

4. To start using PostgreSQL, you can switch to the postgres account (which was created during the installation process) with:
   ```
   sudo -i -u postgres
   ```
5. now default user postgres is being used, now you will have to set password to the user

    ```
    \password postgres
    ```
6. create database using 

    ```
    createdb wikimedia
    ```

5. Install apt package to 
```
sudo apt install build-essential libpq-dev postgresql postgresql-contrib python3-venv python3-dev
```

Now make sure that you have set the password to the config.ini file under [DATABASE] section like following:

```
[DATABASE]
database=wikimedia
user=postgres
password=fea#23#@feFFEd
host=localhost
port=5432
```

you will have set the password, other values are good as it is

### Setup Python Virtual Environment

Follow the steps below to setup a Python virtual environment using `venv`.

1. Open your terminal.

2. Navigate to the project directory.

    ```bash
    cd /path/to/your/project
    ```

3. Create a new virtual environment inside your project folder. Here, we name our virtual environment `venv`.

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment. The command to activate the virtual environment will depend on your operating system:

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```cmd
        .\venv\Scripts\activate
        ```

5. Once the virtual environment is activated, you can install the required packages using pip.

    ```bash
    pip install -r requirements.txt
    ```