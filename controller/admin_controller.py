from fastapi import APIRouter, Depends
from shared.database.get_db import get_db
from shared.database.repositories.User.UserRepository import UserRepository
from shared.database.schemas import UserLoginRequest,CurrentUser,CreateUserRequest
from starlette import status
from iam.token.generate_token import generate_token
from iam.auth import get_password_hash, verify_password,get_current_active_user
from starlette.requests import Request
from starlette.responses import JSONResponse

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/user-login")
def user_login(request: Request, user_details: UserLoginRequest, db: Session = Depends(get_db)):
    user_repo = UserRepository(db=db)
    user = user_repo.get_user_by_username(username=user_details.username)
    if user is not None:
        if verify_password(plain_password=str(user_details.password),hashed_password=user.password):
            token = generate_token(data={'user_id': user.user_id,
                                        'username':user.username,
                                        'is_active':user.is_active})
            welcomeData = {
                'authToken':token,
                'name':user.username,
                'user_id':user.user_id,
                'is_active':user.is_active
            }
            return JSONResponse(status_code=status.HTTP_200_OK,content={'data':welcomeData})
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content='Invalid Password')
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content='Invalid Username')
  
@router.get('/users-list')
def add_addon_course(request: Request,
               db: Session = Depends(get_db),
               currentUser:CurrentUser=Depends(get_current_active_user)):
    user_repo = UserRepository(db=db)
    users = [{'username':user.username} for user in user_repo.get_all_users()]
    return JSONResponse(status_code=status.HTTP_200_OK,content=users)
    
@router.post("/create-user")
def user_login(request: Request, user_details: CreateUserRequest, db: Session = Depends(get_db)):
    user_repository = UserRepository(db=db)
    hashed_password = get_password_hash(user_details.password)
    result = user_repository.create(username=user_details.username,password=hashed_password)
    if result:
        return JSONResponse(status_code=status.HTTP_200_OK,content='user created successfully.')
    