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
        try:
            password_hashed = Security.hash(user.password_hash.value)
            #Create the login of the new user
            with connection.cursor() as cursor:
                cursor.execute("SET search_path TO public")
                cursor.execute("""
                    INSERT INTO login_users (email, password_hash, tenant)
                    VALUES (%s, %s, %s)
                    """, (user.email, password_hashed,user.tenant))
                cursor.execute(f"SET search_path TO {user.tenant}")
                if user.tenant == "public":
                    cursor.execute("""
                        INSERT INTO users ( name, surname, email, password_hash, description, photo_url, refresh_token, secret)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id_user
                        """, (user.name, user.surname, user.email, password_hashed,user.description, user.photo_url, user.refresh_token, user.secret,user.secret))
                    connection.commit()
                else:
                    cursor.execute("""
                        INSERT INTO users ( name, surname, email, password_hash, description, photo_url, refresh_token, secret,id_rol,id_user_created)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id_user
                        """, (user.name, user.surname, user.email, password_hashed,user.description, user.photo_url, user.refresh_token, user.secret,user.secret,user.id_rol,user.id_user_created))
                    connection.commit()
                user_object = self.getUserByEmail(user.email)
                return user_object
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            DatabaseConexion.putConnection(connection)


    def usersWithAccesToAgent(self,id_agent) -> List[Users]:
        return self.userRepository.usersWithAccesToAgent(id_agent)