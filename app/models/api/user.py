from app.models.api.base import Base


class UserBase(Base):
    """
    User
    """

    username: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
