# Snowflake + dbt + Airflow Data Pipeline

This repository contains an automated data pipeline orchestrated using Apache Airflow, dbt, and Snowflake, leveraging the Astronomer Cosmos SDK. The pipeline facilitates efficient data transformation workflows, integrating Snowflake as the data warehouse, dbt for data modeling, and Airflow for orchestration.

# 🛠️ Technologies Used

Apache Airflow: Orchestration of data workflows.

dbt (Data Build Tool): Data transformation and modeling.

Snowflake: Cloud data warehouse for storage.

Astronomer Cosmos SDK: Integration between Airflow and dbt.

# 🚀 Getting Started
## Prerequisites

Ensure the following are set up:

Airflow Connections: Configure the snowflake_conn in Airflow to connect to your Snowflake instance.

Environment Variables: Set necessary environment variables, such as AIRFLOW_HOME.

## Installation

Clone the repository:

git clone https://github.com/harshpretkaur/ETL-Pipeline-Snowflake-Apache-Airflow-DBT.git
cd ETL-Pipeline-Snowflake-Apache-Airflow-DBT

## Set up the virtual environment:

python3 -m venv venv
source venv/bin/activate


## Install dependencies:

pip install -r requirements.txt

# 🧪 Usage

To run the pipeline:

Ensure Airflow is running.

Trigger the DAG dbt_dag from the Airflow UI or CLI.

The DAG will execute dbt models defined in the project directory, using the Snowflake connection specified.

🧩 Project Structure
├── dags/
│   └── dbt_dag.py          # Airflow DAG definition
├── dbt_project/
│   ├── models/
│   │   └── stg_tpch_line_items.sql  # Example dbt model
│   └── dbt_project.yml      # dbt project configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

# 📄 License

This project is licensed under the MIT License
