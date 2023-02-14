from typing import NamedTuple, Optional


class Company(NamedTuple):
    id: Optional[int] = None
    name: Optional[str] = None
    ticker: Optional[str] = None
    news: Optional[dict] = {}
    country: Optional[str] = None
    city: Optional[str] = None
    industry: Optional[str] = None
    employees: Optional[str] = None
    business: Optional[str] = None


class User(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
