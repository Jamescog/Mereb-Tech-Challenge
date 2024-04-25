# Mereb Tech Challenge

Mereb Tech Challenge is a RESTful API built using FastAPI and Redis. It is inspired by a Node.js challenge and provides various endpoints for managing a database of persons.

## Live Demo

You can explore the live demo of Mereb Tech Challenge and interact with its endpoints through the following links:

- **Swagger Documentation:** [https://mereb.jamescog.com/docs](https://mereb.jamescog.com/docs)
- **Redoc Documentation:** [https://mereb.jamescog.com/redoc](https://mereb.jamescog.com/redoc)

## Endpoints

- **GET /person:** Returns all persons in the database.
- **GET /person/:id:** Returns the person with the specified ID if found, otherwise returns a 404 error.
- **POST /person:** Creates a new person in the database.
- **PUT /person/:id:** Updates information about the specified person if found, otherwise returns a 404 error.
- **DELETE /person/:id:** Deletes the specified person if found.
- **GET /raise-500:** Simulates an internal server error and provides a user-friendly error message.
- **GET /non-existing/page:** Requests to non-existing routes are handled gracefully with a 404 page.

## Running the Application

To run Mereb Tech Challenge locally, follow these steps:

1. Ensure that you have Redis server installed and running on your machine.

2. Clone this repository to your local machine:
    ```
    git clone https://github.com/Jamescog/Mereb-Tech-Challenge.git
    ```

3. Navigate to the project directory:
    ```
    cd Mereb-Tech-Challenge
    ```

4. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Unix/Mac
    .\venv\Scripts\activate   # On Windows
    ```

5. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

6. Start the FastAPI server:
    ```
    uvicorn app:app
    ```

7. Once the server is running, you can access the API endpoints locally at `http://127.0.0.1:8000`.

8. Explore the API using tools like Swagger UI or Redoc, or send requests directly to the endpoints using tools like Browser or Postman.