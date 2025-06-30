from abc import ABC, abstractmethod
from typing import List, Optional

from app.users.domain.entities.users import Users


class UsersRepository(ABC):
    @abstractmethod
    def getAllUsersFromSchema(self,schema: str) -> List[Users]:
        """
            This function return a list of users saved in a certain schema
            :param schema: The schema where the users are saved
            :return: List of Users registered in that schema
        """
        pass
    @abstractmethod
    def getAllUsersFromEnvironment(self,schema: str,id_environment :int)-> List[Users]:
        """
            This function return a list of users from one environment in a certain schema.
            :param schema: The schema where the users and the environment are saved.
            :param id_environment: The id of the environment.
            :return: List of Users which have access on that environment.
        """
        pass
    @abstractmethod
    def getUserByEmail(self,email : str)-> Optional[Users]:
        """
            This function return a user who has a certain email.
            :param email: The email that we are looking for.
            :return: A object of Users with that email.
        """
        pass
    @abstractmethod
    def getUserById(self,id_user :int,schema : str)-> Optional[Users]:
        """
            This function return a user who has a certain id_user.
            :param id_user: The id_user that we are looking for.
            :param schema: The schema where the user is saved.
            :return: A object of Users with that id_user.
        """
        pass

    @abstractmethod
    def updateUser(self,user:Users)-> Optional[Users]:
        """
            This function update the user data in the database.
            :param user: The Users object with the new data.
            :return: The new object Users updated on the database.
        """
        pass
    @abstractmethod
    def deleteUser(self,user:Users)-> bool:
        """
            This function delete the user from the database.
            :param user: The object Users it will be deleted.
            :return: True or False depends if the operation was succesfuly or not.
        """
        pass
    @abstractmethod
    def createUser(self,user:Users)-> Optional[Users]:
        """
            This function insert a new user in to the database.
            :param user: The object Users with the data.
            :return: A object from Users with all the data.
        """
        pass
    @abstractmethod
    def usersWithAccesToAgent(self,id_agent) -> List[Users]:
        """
        This function return a list of users with access to a certain agent
        :param id_agent: The id of the agent looking for.
        :return: A list of objects Users with acces to this agent
        """
        pass



