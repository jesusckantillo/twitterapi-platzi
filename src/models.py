from datetime import date,datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from uuid import UUID

class UserInfo(BaseModel):
    user_id : UUID = Field(...)
    email: EmailStr = Field(...)
    pass 

class UserLogin(UserInfo):
    password: str = Field(... ,
                          min_length=8
                          )

class User(BaseModel):
    first_name: str = str(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = str(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)
    pass


class Tweet(BaseModel):
    tweet_id = UUID = Field(...)
    content: str = Field(..., min_length=1,max_length=256)
    created_at: datetime = Field(defalult = datetime.now())
    update_at: Optional[datetime] = Field()
    by: User = Field(...)
    pass