from typing import List
from datetime import datetime

from fastapi import APIRouter, Query

from src.application.schemas import (
    Status,
    SellerApplication, PayApplication
)


router = APIRouter(prefix="/api/v1/application", tags=["application"])

@router.get("/statuses/")
async def statuses() -> Status:
    return Status(
        accept=[
            "new",
            "coldnew",
            "coldpay",
            "verify",
            "payed",
            "realpay",
            "success",
            "coldsuccess",
            "error",
            "cancel",
            "delete",
        ],
        pay=[
            "new",
            "coldnew",
            "coldpay",
            "verify",
            "payed",
            "realpay",
            "success",
            "coldsuccess",
            "error",
            "cancel",
            "delete"
        ]
    )

@router.get("/applications/")
async def applications(filters: List[str] = Query(None)) -> List[PayApplication]:
    return [
        PayApplication(
        id_application=74098,
        currency="Рубль",
        seller=[
            SellerApplication(
                id_application=99090,
                bank="Liberty Bank",
                sum=999.77,
                currency="USD-T",
                date=datetime.today(),
                requisites="12345678900987654321",
            ),
            SellerApplication(
                id_application=99095,
                bank="JSC Isbank Georgia",
                sum=412.12,
                currency="USD-T",
                date=datetime.today(),
                requisites="13579086422468097531",
            ),
        ],
        bank="Сбербанк",
        sum=120000.0,
        date=datetime.today(),
        ),

        PayApplication(
            id_application=74099,
            currency="Доллар",
            seller=[
                SellerApplication(
                    id_application=99092,
                    bank="Т-Банк",
                    sum=6543,
                    currency="Рубль",
                    date=datetime.today(),
                    requisites="123456654321178900987",
                ),
                SellerApplication(
                    id_application=99094,
                    bank="ВТБ",
                    sum=3457,
                    currency="Рубль",
                    date=datetime.today(),
                    requisites="54546363727291910808",
                ),
            ],
            bank="JSC Isbank Georgia",
            sum=125.0,
            date=datetime.today(),
        )
    ]