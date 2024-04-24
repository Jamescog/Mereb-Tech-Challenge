from os import getenv
from redis import Redis, ConnectionPool

class DBDependencies:
    """
    A class that provides database dependencies using Redis.

    Attributes:
        host (str): The hostname of the Redis server.
        port (int): The port number of the Redis server.
        db (int): The database number to connect to in the Redis server.
    """

    # Create a class-level connection pool
    connection_pool = ConnectionPool(
        host=getenv("DB_HOST", "localhost"),
        port=int(getenv("DB_PORT", 6379)),
        db=int(getenv("DB", 0)),
        decode_responses=True
    )

    def __init__(self):
        """
        Initializes the DBDependencies object.
        """
        self.redis_client = Redis(connection_pool=self.connection_pool)

    def generate_key(self, object_type, object_id):
        """
        Generates a key based on the provided object type and ID.

        Args:
            object_type (str): The type of the object.
            object_id (str): The ID of the object.

        Returns:
            str: The generated key.
        """
        return f"{object_type}_{object_id}"

    def set_key(self, key, value, ex=None):
        """
        Sets the value of a key in Redis.

        Args:
            key (str): The key to set.
            value (str): The value to set for the key.
            ex (int, optional): The expiration time for the key in seconds.
            Defaults to None.
        """
        self.redis_client.set(key, value, ex=ex)

    def get_key(self, key):
        """
        Retrieves the value of a key from Redis.

        Args:
            key (str): The key to retrieve.

        Returns:
            str: The value of the key.
        """
        return self.redis_client.get(key)

    def delete_key(self, key):
        """
        Deletes a key from Redis.

        Args:
            key (str): The key to delete.
        """
        return self.redis_client.delete(key)

    def get_keys(self, pattern):
        """
        Retrieves keys matching the specified pattern from Redis.

        Args:
            pattern (str): The pattern to match keys against.

        Returns:
            list: A list of keys matching the pattern.
        """
        return self.redis_client.keys(pattern)
