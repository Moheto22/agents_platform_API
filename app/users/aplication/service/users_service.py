from typing import Optional, List

from app.users.domain.entities.users import Users
from app.users.domain.repository.users_repository import UsersRepository


class UsersService(UsersRepository):
    def __init__(self,user_repository : UsersRepository):
        self.userRepository = user_repository

    def getAllUsersFromSchema(self,schema: str) -> List[Users]:
        return self.userRepository.getAllUsersFromSchema(schema)

    def getAllUsersFromEnvironment(self,schema: str,id_environment :int)-> List[Users]:
        return self.userRepository.getAllUsersFromEnvironment(schema, id_environment)

    def getUserByEmail(self,email : str)-> Optional[Users]:
        return self.userRepository.getUserByEmail(email)

    def getUserById(self,id_user :int,schema : str)-> Optional[Users]:
        return self.userRepository.getUserById(id_user, schema)

    def updateUser(self,user:Users)-> Optional[Users]:
        return self.userRepository.updateUser(user)

    def deleteUser(self,user:Users)-> bool:
        return self.userRepository.deleteUser(user)

    def createUser(self,user:Users)-> Optional[Users]:
        return self.userRepository.createUser(user)

    def usersWithAccesToAgent(self,id_agent) -> List[Users]:
        return self.userRepository.usersWithAccesToAgent(id_agent)