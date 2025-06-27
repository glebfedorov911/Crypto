from typing import List
from datetime import datetime

from pydantic import BaseModel


class Status(BaseModel):
    accept: List[str]
    pay: List[str]

class Application(BaseModel):
    id_application: int
    from_bank: str
    to_bank: str
    date: datetime
    currency: str

class SellerApplication(Application):
    requisites: str
    amount_received: float
    amount_full: float

class PayApplication(Application):
    seller: List[SellerApplication]
    sum: float