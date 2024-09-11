from datetime import datetime, timedelta

def get_defaultairflow_args():
    return {
        "owner": "anonimo",
        "depends_on_past": False,
        "start_date": datetime(2024, 9, 9),
        "email_on_failure": True,
        "email_on_retry": True,
        "retries": 10,
        "catch"
        "retry_delay": timedelta(minutes=1),
    }