# takehome-data-engineering-2024
## Overview:
In this project, I will be working with the Wikimedia Clickstream dataset, which is available at Wikimedia Dumps. This dataset includes monthly Wikipedia clickstream data dumps for a selection of top Wikipedia languages, ranked by Wikipedia size. Each file in the dataset contains counts of (referrer, resource) pairs, extracted from the request logs of Wikipedia. Given the large size of these datasets, I will be focusing on using the latest dump only.

> The current data includes the following 4 fields:

`prev`: the result of mapping the referrer URL to the fixed set of values described above
`curr`: the title of the article the client requested
`type`: describes `(prev, curr)`
    `link`: if the referrer and request are both articles and the referrer links to the request
    `external`: if the referrer host is not `en(.m)?.wikipedia.org`
    `other`: if the referrer and request are both articles but the referrer does not link to the `request`. This can happen when clients search or spoof their refer.
`n`: the number of occurrences of the (referrer, resource) pair

## Install and Setup


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

## Run code
to run code, run this command 
    ```
    python main.py
    ```

## Run code periodically
To run your code automatically each month on the third day at 12 AM, you can use a cron job if you're on a Unix-based system. The rationale behind choosing the third day for data loading is to account for potential delays in Wikimedia's data upload process, which may not occur promptly on the first day.

```shell
0 0 3 * * /usr/bin/python3 /path/to/your/script.py
```

## ETL Approach

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


## Optional Task

### Show EDA (Exploratory Data Analysis)  

In the notebook `EDA.ipynb`, we have writen a code which load data from database and shows link_type distribution for each language in specific month.  

This notebook can be used to visualize distribution of any categorical column our target database.