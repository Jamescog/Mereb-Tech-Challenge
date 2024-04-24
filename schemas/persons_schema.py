from typing import List, Optional
from random import randint
from uuid import uuid4


from faker import Faker
from pydantic import BaseModel

faker = Faker()


class Person(BaseModel):
    """
    Represents a person with a unique identifier, name, age,
    and a list of hobbies.

    Attributes:
        id (UUID): A unique identifier for the person.
        name (str): The name of the person.
        age (int): The age of the person.
        hobbies (List[str]): A list of hobbies.
    """
    id: str
    name: str
    age: int
    hobbies: List[str] = []

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "id": str(uuid4().hex),
                    "name": faker.unique.name(),
                    "age": randint(20, 60),
                    "hobbies": [faker.unique.job() for _ in range(3)]
                }
            ]
        }

class PersonsList(BaseModel):
    """
    Represents a list of persons.

    Attributes:
        persons (List[Person]): A list of persons.
    """
    persons: List[Person]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "persons": [
                        {
                            "id": str(uuid4().hex),
                            "name": faker.unique.name(),
                            "age": randint(20, 60),
                            "hobbies": [faker.unique.job() for _ in range(3)]
                        }
                    ]
                }
            ]
        }

class PersonCreate(BaseModel):
    """
    Represents a person with a name, age, and a list of hobbies.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        hobbies (List[str]): A list of hobbies.
    """
    name: str
    age: int
    hobbies: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": faker.unique.name(),
                    "age": randint(20, 60),
                    "hobbies": [faker.unique.job() for _ in range(3)]
                }
            ]
        }
class PersonUpdate(BaseModel):
    """
    Represents a person with a name, age, and a list of hobbies.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        hobbies (List[str]): A list of hobbies.
    """
    name: Optional[str]
    age: Optional[int]
    hobbies: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": faker.unique.name(),
                    "age": randint(20, 60),
                    "hobbies": [faker.unique.job() for _ in range(3)]
                }
            ]
        }