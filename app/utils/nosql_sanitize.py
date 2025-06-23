from fastapi import HTTPException

def check_for_nosql_injection(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if "$" in key or "." in key:
                raise HTTPException(status_code=400, detail="Invalid key in input.")
            check_for_nosql_injection(value)
    elif isinstance(data, list):
        for item in data:
            check_for_nosql_injection(item) 