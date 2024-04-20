## Background
You will work with the `Wikimedia Clickstream dataset`, available at `Wikimedia Dumps` The datasets contain monthly Wikipedia clickstream data dumps for a selection of top Wikipedia languages by Wikipedia size. Each file contains `counts of (referrer, resource)` pairs extracted from the request logs of Wikipedia. Since the datasets are large, you may consider using the latest dump only.

## Objectives
Develop an `ETL pipeline` to ingest this clickstream data to a database of your choice. The raw dumps might include missing values or some irrelevant data. `Transform` the data into a suitable format and document all steps.
Assuming the `clickstream` data will be updated periodically, the data ingestion should run automatically (e.g., daily or weekly) as part of a `cron job`.
Propose methods to ensure `data quality` and `consistency` across the `pipeline`. Describe how you would handle issues like duplicate data, missing values, and schema changes.
`Explain` (writeup only, no code) how your design scales with increasing data volumes and what strategies you would employ to ensure performance is not compromised. This includes considerations for `data partitioning`, `indexing`, and `caching`.
Explain (writeup only, no code) how would you modify the pipeline to support `streaming data ingestion` in real time.
(Optional/Bonus) `Data Analysis` and `Machine Learning`: Perform `exploratory data analysis (EDA)` on your dataset. Identify trends, patterns, and anomalies. Implement a machine learning model using the dataset. Possible tasks might include predicting future click patterns or classifying types of clicks.
Deliverables  
## Code: 
Push all code to this GitHub repository. We should be able to run your pipeline and replicate your steps on our end, from db setup, to data ingestion.
## Documentation:  
Include a `README` with an overview, setup instructions, and a detailed explanation of your approach.
### Report:  
Submit a report detailing your ETL process, scalability considerations, streaming modifications, a high-level architecture diagram of the `ETL pipeline`, and findings from the data analysis/machine learning phase.
## Evaluation Criteria
There is no right or wrong way to accomplish this task. Your goal should be to show off your Data Engineering skills and demonstrate a thorough analysis of the problem during the review session. If you're a data wizard, you can show off your deep familiarity with data processing, architecture choices, fault tolerance, and scalability. If you're a modeling/analytics expert, show us a deep understanding of the models you use and show us how you'd set up metrics. Play to your strengths!

### Requirements:
Please make your first commit when you start working on the exercise and your second commit exactly 1 hour after the start. After 1 hour you are free to continue working on the problem for up to 48 hours. We ask that you add a commit any time you stop or restart working on the problem within those 48 hours.

Please let us know by email when this is ready for review.

Best of luck!