
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel 
from typing import Optional, List 

from apps import users, courses, catalogs

app = FastAPI(
    title="Fast API SMS",
    description="SMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Chris", 
        "email": "potentialsunny47@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(users.router)
app.include_router(catalogs.router)
app.include_router(courses.router)