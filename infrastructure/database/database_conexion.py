from psycopg2.pool import SimpleConnectionPool
from typing import Optional
from psycopg2.extensions import connection

class DatabaseConexion:

    _connexionPool : Optional[SimpleConnectionPool] = None

    @classmethod
    def initialize(cls, mincoon : int, maxcoon : int):
        """
            This function initialize the connexions to the database
            :param mincoon: The minimum number of connexions
            :param maxcoon: The maximum number of connexions
            :return: Nothing
        """
        if cls._connexionPool is None:
            cls._connexionPool = SimpleConnectionPool(
                mincoon,maxcoon,
                user="postgres",
                password="Mifamili22.",
                host="localhost",
                port="5432",
                database = "Agent_Platform"
            )
        #Test the connection is working
        test_conn = cls._connexionPool.getconn()
        cls._connexionPool.putconn(test_conn)

    @classmethod
    def getConnection(cls) -> connection:
        """
            This function return one of the free connections to the database at that moment
            :return: The object connection
        """
        if cls._connexionPool is None:
            raise Exception("The pool is not initialized")
        return cls._connexionPool.getconn()

    @classmethod
    def putConnection(cls, conn: connection) -> None:
        """
            This function return a used connection to the list of free connections to the database
            :param conn: The object connection that was used previously to query
            :return: Nothing
        """
        if cls._connexionPool:
            cls._connexionPool.putconn(conn)

    @classmethod
    def closeConnection(cls):
        """
            This function shutdown all the connections and close the pool to the database
            :return: Nothing
        """
        if cls._connexionPool is not None:
            cls._connexionPool.closeall()
            cls._connexionPool = None