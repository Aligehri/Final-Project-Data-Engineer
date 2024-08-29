from datetime import datetime, timedelta

def get_defaultairflow_args():
    return {
        "owner": "anonimo",
        "depends_on_past": False,
        "start_date": datetime(2024, 1, 1),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "catch"
        "retry_delay": timedelta(minutes=5),
    }