from fastapi import HTTPException, Request
from config.db import SECRET


def verify_token(req: Request):
    token = req.headers.get("Secret_Code")
    if token:
        token = token.replace("\"","")
    print(token)
    print(f"Secret {SECRET}" )
    valid = (token == SECRET)
    if not valid:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
