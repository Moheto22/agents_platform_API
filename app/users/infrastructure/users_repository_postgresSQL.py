from typing import List, Optional

from app.users.aplication.service.users_service import UsersService
from app.users.domain.entities.users import Users
from infrastructure.database.database_conexion import DatabaseConexion
from infrastructure.security.security import Security


class UsersRespositoryPostgresSQL(UsersService):
    def getAllUsersFromSchema(self,schema: str) -> List[Users]:


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
        connection = DatabaseConexion.getConnection()
        password_hashed = Security.hash(user.password_hash.value)
        with connection.cursor() as cursor:
            cursor.execute("SET search_path TO public")
            cursor.execute("""
        INSERT INTO users (name, surname, email, password_hash)
        VALUES (%s, %s, %s, %s)
        RETURNING id_user
    """, (name, surname, email, password_hashed))

    def usersWithAccesToAgent(self,id_agent) -> List[Users]:
        return self.userRepository.usersWithAccesToAgent(id_agent)