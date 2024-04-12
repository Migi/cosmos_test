from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from datetime import datetime
import os

profile_config = ProfileConfig(
    profile_name="dbt_playground",
    target_name="airflow",
    profiles_yml_filepath=f"{os.environ['AIRFLOW_HOME']}/dags/dbt/profiles.yml",
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        f"{os.environ['AIRFLOW_HOME']}/dags/dbt",
    ),
    profile_config=profile_config,
    # execution_config=ExecutionConfig(
    #     dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    # ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="my_cosmos_dag",
    default_args={"retries": 2},
)

print(my_cosmos_dag)
