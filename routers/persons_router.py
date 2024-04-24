"""Router that handles the requests for the persons endpoints."""


from json import loads, dumps
from uuid import uuid4

from fastapi import(
    APIRouter,
    Depends,
    HTTPException,
    status,
    
)
from fastapi.responses import JSONResponse


from schemas.persons_schema import(
    Person,
    PersonsList,
    PersonCreate,
    PersonUpdate
)
from utlis.db_connection import DBDependencies

persons_router = APIRouter(tags=["persons"])
db_dependencies = Depends(DBDependencies)

@persons_router.get(
        "/person", 
        response_model=PersonsList,
        status_code=status.HTTP_200_OK
    )
def get_persons(db=db_dependencies):
    """
    Retrieves a list of persons from the database.

    Args:
        db (DBDependencies, optional): The database dependency. Defaults to Depends(db).

    Returns:
        PersonsList: A list of persons.
    """
    persons = []
    keys = db.get_keys("person_*")
    for key in keys:
        person = loads(db.get_key(key))
        persons.append(person)
    return PersonsList(persons=persons)


@persons_router.get("/person/{person_id}",
                    response_model=Person,
                    status_code=status.HTTP_200_OK)

def get_person(person_id: str, db=db_dependencies):
    """
    Retrieves a person from the database.

    Args:
        person_id (str): The ID of the person to retrieve.
        db (DBDependencies, optional): The database dependency.
        Defaults to Depends(db).

    Returns:
        Person: The person.
    """
    person = db.get_key(f"person_{person_id}")
    if person:
        return loads(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Person not found")

@persons_router.post("/person")
def create_person(person: PersonCreate, db=db_dependencies):
    """
    Creates a person in the database.

    Args:
        person (PersonCreate): The person to create.
        db (DBDependencies, optional): The database dependency. Defaults to Depends(db).

    Returns:
        Person: The created person.
    """
    person_id = str(uuid4().hex)
    print(person_id)

    key = db.generate_key("person", person_id)
    data = dict(person)
    data["id"] = person_id
    db.set_key(key, dumps(data))
    return JSONResponse(
        content={
            "message": "Person created successfully",
            "id": person_id
        },
        status_code=status.HTTP_201_CREATED
    )

@persons_router.put("/person/{person_id}")
def person_update(person_id: str, person: PersonUpdate, db=db_dependencies):
    """
    Updates a person in the database.

    Args:
        person_id (str): The ID of the person to update.
        person (PersonUpdate): The updated person.
        db (DBDependencies, optional): The database dependency. Defaults to Depends(db).

    Returns:
        Person: The updated person.
    """
    key = db.generate_key("person", person_id)
    person_data = db.get_key(key)
    if not person_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Person not found")

    person_data = loads(person_data)
    person_data.update(person.model_dump(exclude_unset=True))
    db.set_key(key, dumps(person_data))
    return JSONResponse(
        content={
            "message": "Person updated successfully",
            "id": person_id
        },
        status_code=status.HTTP_200_OK
    )

@persons_router.delete("/person/{person_id}")
def delete_person(person_id: str, db=db_dependencies):
    """
    Deletes a person from the database.

    Args:
        person_id (str): The ID of the person to delete.
        db (DBDependencies, optional): The database dependency. Defaults to Depends(db).

    Returns:
        JSONResponse: The response message.
    """
    key = db.generate_key("person", person_id)

    if db.delete_key(key) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Person not found")
    return JSONResponse(
        content={
            "message": "Person deleted successfully",
            "id": person_id
        },
        status_code=status.HTTP_200_OK
    )

