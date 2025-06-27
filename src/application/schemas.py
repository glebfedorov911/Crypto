from typing import List
from datetime import datetime

from pydantic import BaseModel


class Status(BaseModel):
    accept: List[str]
    pay: List[str]

class Application(BaseModel):
    bank: str
    sum: float
    date: datetime
    currency: str

class SellerApplication(Application):
    requisites: str

class PayApplication(Application):
    id_application: int
    seller: List[SellerApplication]