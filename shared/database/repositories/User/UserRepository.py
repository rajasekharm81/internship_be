from sqlalchemy import func
from sqlalchemy.orm import Session

from shared.database.repositories.Repository import Repository
from shared.database.models import User


class UserRepository(Repository):
    def __init__(self, db: Session, model_class=User):
        super().__init__(model_class, db)

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()
    
    def get_all_users(self):
        return self.session.query(User.username,User.user_id).all()
