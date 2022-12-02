from typing import NamedTuple, Optional

class Company(NamedTuple):
    id: Optional[int] = None
    name: Optional[str] = None

class User(NamedTuple):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None