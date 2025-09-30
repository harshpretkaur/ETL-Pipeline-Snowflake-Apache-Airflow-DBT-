import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",   # must exist in Airflow Connections
        profile_args={
            "database": "dbt_db",
            "schema": "dbt_schema"
        },
    ),
)

dbt_snowflake_dag = DbtDag(
    dag_id="dbt_dag",
    project_config=ProjectConfig(
        "/usr/local/airflow/dags/dbt/data_pipeline"  # path to your dbt project
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"
    ),
    operator_args={"install_deps": True},
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 30),
    catchup=False,
)
