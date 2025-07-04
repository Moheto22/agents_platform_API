from dotenv import load_dotenv
import os

load_dotenv()

class EnvLoader:

    @staticmethod
    def get_ip_database() -> str:
        ip = os.getenv("DATABASE_IP")
        if not ip:
            raise EnvironmentError("Missing the DATABASE_IP in .env")
        return ip

    @staticmethod
    def get_user_database() -> str:
        user = os.getenv("USER_DATABASE")
        if not user:
            raise EnvironmentError("Missing the USER_DATABASE in .env")
        return user

    @staticmethod
    def get_password_database() -> str:
        pw = os.getenv("PASSWORD_DATABASE")
        if not pw:
            raise EnvironmentError("Missing the PASSWORD_DATABASE in .env")
        return pw

    @staticmethod
    def get_name_database() -> str:
        db = os.getenv("NAME_DATABASE")
        if not db:
            raise EnvironmentError("Missing the NAME_DATABASE in .env")
        return db

    @staticmethod
    def get_port_database() -> str:
        port = os.getenv("PORT_DATABASE")
        if not port:
            raise EnvironmentError("Missing the PORT_DATABASE in .env")
        return port
    @staticmethod
    def get_encrypt_key()-> str:
        key = os.getenv("ENCRYPTION_KEY")
        if not key:
            raise EnvironmentError("Missing the ENCRYPTION_KEY in .env")
        return key
    @staticmethod
    def get_secret_jwt()-> str:
        key = os.getenv("JWT_SECRET_KEY")
        if not key:
            raise EnvironmentError("Missing the JWT_SECRET_KEY in .env")
        return key