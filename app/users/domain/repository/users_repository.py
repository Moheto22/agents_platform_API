from abc import ABC, abstractmethod
from typing import List, Optional

from app.users.domain.entities.users import Users


class UsersRepository(ABC):
    @abstractmethod
    def getAllUsersFromSchema(self,schema: str) -> List[Users]:
        """
            This function return a list of users saved in a certan schema
            :param schema: The schema where the user is saved
            :return: List of Users registred in that schema
        """
        pass
    @abstractmethod
    def getAllUsersFromEnvironment(self,schema: str,id_environment :int)-> List[Users]:
        pass
    @abstractmethod
    def getUserByEmail(self,email : str)-> Optional[Users]:
        pass
    @abstractmethod
    def getUserById(self,id_user :int,schema : str)-> Optional[Users]:
        pass

    @abstractmethod
    def updateUser(self,user:Users)-> Optional[Users]:
        pass
    @abstractmethod
    def deleteUser(self,user:Users)-> bool:
        pass
    @abstractmethod
    def createUser(self,user:Users)-> Optional[Users]:
        pass

