from dataclasses import dataclass


# A dataclass that stores person data.
@dataclass
class PersonData:
    name: str
    age: int
    gender: str
    country: str
