from pydantic import BaseModel

class Token(BaseModel):
   access_token: str
   token_type: str

class TokenData(BaseModel):
   username: str | None = None
   nome: str | None = None
   sobrenome: str | None = None