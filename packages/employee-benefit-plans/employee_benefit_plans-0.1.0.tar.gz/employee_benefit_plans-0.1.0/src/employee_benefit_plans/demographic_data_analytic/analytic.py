from typing import Optional
import datetime
import decimal

from pydantic import BaseModel

class DemographicData(BaseModel):
    id: str
    name: Optional[str]
    sex: Optional[str]
    status: Optional[str]
    beneficiary_sex: Optional[str]
    salary_amount: Optional[decimal.Decimal]
    benefit_amount: Optional[decimal.Decimal]
    date_of_birth: Optional[datetime.date]
    date_of_hire: Optional[datetime.date]
    date_of_retire: Optional[datetime.date]
    date_of_termination: Optional[datetime.date]
    beneficiary_date_of_birth: Optional[datetime.date]
