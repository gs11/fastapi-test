from app import controller
from fastapi import FastAPI, Request, Depends, HTTPException
#from fastapi.exceptions import RequestValidationError
#from fastapi.responses import JSONResponse
import os

TOKEN = os.getenv('API_TOKEN', 'dummy')


async def verify_api_token(request: Request):
    try:
        if request.headers['x-token'] != TOKEN:
            raise
    except:
        raise HTTPException(status_code=401, detail='invalid auth')


app = FastAPI(
    title="Installation API",
    description="FastAPI test",
    version="0.0.1",
)
app.include_router(
    controller.installation,
    tags=["Installation"],
    dependencies=[Depends(verify_api_token)]
)

# Custom validation handler
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return JSONResponse({'detail': str(exc)}, status_code=400)
