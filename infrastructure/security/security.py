from typing import re

import bcrypt
from cryptography.fernet import Fernet, InvalidToken

from infrastructure.env_loader.env_loader import EnvLoader


class Security:

    @staticmethod
    def hash(text :str) -> str:
        """
            Hashes a plain text string using bcrypt with a randomly generated salt.
            :rtype: str
            :param text: the text that will be hashed
            :return: The resulting bcrypt hash as a UTF-8 string.
        """
        hashed = bcrypt.hashpw(text.encode(), bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def checkHash(original_hash : str, plain_text :str) -> bool:
        """
            Verifies if the plain text matches the given bcrypt hash.
            :param plain_text: The plain text string to verify.
            :param original_hash: The hash of the original secret text.
            :return: True if the text matches the hash, False otherwise.
        """
        is_valid = bcrypt.checkpw(plain_text.encode("utf-8"), original_hash.encode("utf-8"))
        return is_valid
    @staticmethod
    def encrypt(text:str) ->str:
        """
        This function encrypts a text
        :param text: the text that will be encrypted
        :return: the text encrypted
        """
        fernet = Fernet(EnvLoader.get_encrypt_key())
        try:
            return fernet.encrypt(text.encode()).decode()
        except InvalidToken:
            raise ValueError("Encryption failed. Invalid token or key.")

    @staticmethod
    def decrypt(text: str) -> str:
        """
        This function decrypts a text
        :param text: the text that will be decrypted
        :return: the text decrypted
        """
        fernet = Fernet(EnvLoader.get_encrypt_key())
        try:
            return fernet.decrypt(text.encode()).decode()
        except InvalidToken:
            raise ValueError("Decryption failed. Invalid token or key.")

