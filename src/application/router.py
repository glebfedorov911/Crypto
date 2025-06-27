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
                from_bank="Any",
                to_bank="Liberty Bank",
                amount_received=999.77 * 80.0,
                amount_full=5999 * 80.0,
                currency="USD-T",
                date=datetime.today(),
                requisites="12345678900987654321",
            ),
            SellerApplication(
                id_application=99095,
                to_bank="JSC Isbank Georgia",
                from_bank="JSC Isbank Georgia",
                amount_received=412.12 * 80.0,
                amount_full=412.12 * 80.0,
                currency="USD-T",
                date=datetime.today(),
                requisites="13579086422468097531",
            ),
        ],
        from_bank="Сбербанк",
        to_bank="Any",
        sum=120000.0,
        date=datetime.today(),
        ),

        PayApplication(
            id_application=74099,
            currency="Рубль",
            seller=[
                SellerApplication(
                    id_application=99092,
                    from_bank="Any",
                    to_bank="Т-Банк",
                    amount_received=6543,
                    amount_full=11111.12,
                    currency="Рубль",
                    date=datetime.today(),
                    requisites="123456654321178900987",
                ),
                SellerApplication(
                    id_application=99094,
                    from_bank="ВТБ",
                    to_bank="ВТБ",
                    amount_received=3457,
                    amount_full=21331.12,
                    currency="Рубль",
                    date=datetime.today(),
                    requisites="54546363727291910808",
                ),
            ],
            from_bank="JSC Isbank Georgia",
            to_bank="Any",
            sum=125.0,
            date=datetime.today(),
        )
    ]