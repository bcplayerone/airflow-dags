from datetime import datetime
from airflow.sdk import dag, task


@dag(
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["smoke-test"],
)
def hello_oke():
    @task
    def greet():
        print("airflow on oke is running")
        return "ok"

    @task
    def confirm(value: str):
        print(f"received: {value}")

    confirm(greet())


hello_oke()
