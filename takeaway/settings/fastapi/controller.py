controller = '''
from fastapi import APIRouter, HTTPException,Cookie, Depends,Header,File, Body,Query
from starlette.responses import JSONResponse
from core.factories import settings
import  httpx

router = APIRouter()

'''