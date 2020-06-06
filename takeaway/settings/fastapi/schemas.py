schema = '''

# write your schemas in this files. Use pydantic

from pydantic import BaseModel,constr,validator,ValidationError,EmailStr
from uuid import UUID
from typing import Optional,List,Union
import pydantic.json
import asyncpg.pgproto.pgproto
pydantic.json.ENCODERS_BY_TYPE[asyncpg.pgproto.pgproto.UUID] = str


# Write your pydantic models here
'''