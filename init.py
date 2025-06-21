from fastapi import FastAPI
import sys

from starlette.middleware.cors import CORSMiddleware
sys.path.append('.')
sys.path.append('../')

app = FastAPI(title="Internship BE")

# admin controller
from controller.admin_controller import router as program_router

app.include_router(program_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[r"http://localhost:4200", r"http://52.66.77.39", r"http://13.234.67.162"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
