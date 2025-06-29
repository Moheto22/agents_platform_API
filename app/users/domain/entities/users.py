from pydantic import BaseModel,Field
from  datetime import datetime
from typing import Optional


from app.users.domain.value_objects.timestamp import Timestamp
from app.users.domain.value_objects.user_description import UserDescription
from app.users.domain.value_objects.user_email import UserEmail
from app.users.domain.value_objects.user_id import UserId
from app.users.domain.value_objects.user_name import UserName
from app.users.domain.value_objects.string_cheker import UserStringData
from app.users.domain.value_objects.user_photo import UserPhotoUrl
from app.users.domain.value_objects.user_surname import UserSurname
from app.users.domain.value_objects.user_tenant import UserTenant


class Users(BaseModel):
    id_user : Optional[UserId] = Field(default=None,description="The id of the user")
    name : UserName = Field(...,description="Real name of the user")
    surname : UserSurname = Field(..., description="Real surname of the user")
    email : UserEmail = Field(..., description="The email of the user")
    password_hash : UserStringData = Field(...,description="The password of the user encripted")
    last_update : Optional[Timestamp] = Field(default=None,description="The last update of the user data")
    created_at : Optional[Timestamp] = Field(default=None,description="The date since the user was created")
    description : Optional[UserDescription] = Field(default=None,description="The user self description")
    tenant : UserTenant = Field(...,description = "The schema where is the user saved")
    photo_url : UserPhotoUrl = Field(...,description= "The url of the avatar image of the user")
    deleted_at : Optional[Timestamp] =Field(default=None,description="The date since the user was deleted")
    refresh_token : UserStringData = Field(description="The refresh token of the user to get a new JWT token")

    # El constructor que se usa cuando procede de la BDD
    @classmethod
    def from_raw_data(
            cls,
            id_user: int,
            name: str,
            surname: str,
            email: str,
            password_hash: str,
            last_update: Optional[datetime],
            created_at: datetime,
            description: Optional[str],
            tenant: str,
            photo_url: str,
            deleted_at: Optional[datetime],
            refresh_token: str
    ) -> "Users":
        """
            Create a new User instance which comes from database.

            Args:
                id_user (int): The user id.
                name (str): Real name of the user.
                surname (str): Real surname of the user.
                email (str): Email address.
                password_hash (str): Encrypted password.
                last_update (datetime): The date when happend the last user update.
                created_at (datetime): The date since the user was created.
                deleted_at (datetime): The date when the user was deleted.
                description (str): Self-description of the user.
                tenant (str): Schema identifier (multi-tenant system).
                photo_url (str): URL of the user’s avatar image.
                refresh_token (str): JWT refresh token for session management.

            Returns:
                Users: A complete User domain entity persisted in the database.
        """
        return cls(
            id_user=UserId(id_user),
            name=UserName(name),
            surname=UserSurname(surname),
            email=UserEmail(email),
            password_hash=UserStringData(password_hash),
            last_update=Timestamp(last_update),
            created_at=Timestamp(created_at),
            description=UserDescription(description),
            tenant=UserTenant(tenant),
            photo_url=UserPhotoUrl(photo_url),
            deleted_at=Timestamp(deleted_at),
            refresh_token=UserStringData(refresh_token)
        )


    @classmethod
    def from_new_instance(
            cls,
            name: str,
            surname: str,
            email: str,
            password_hash: str,
            description: str,
            tenant: str,
            photo_url: str,
            refresh_token: str
            )-> "Users":
        """
            Create a new User instance that has not yet been persisted in the database.

            Args:
                name (str): Real name of the user.
                surname (str): Real surname of the user.
                email (str): Email address.
                password_hash (str): Encrypted password.
                description (str): Self-description of the user.
                tenant (str): Schema identifier (multi-tenant system).
                photo_url (str): URL of the user’s avatar image.
                refresh_token (str): JWT refresh token for session management.

            Returns:
                Users: A complete User domain entity ready to be persisted.
        """
        return cls(
            name=UserName(name),
            surname=UserSurname(surname),
            email=UserEmail(email),
            password_hash=UserStringData(password_hash),
            description=UserDescription(description),
            tenant=UserTenant(tenant),
            photo_url=UserPhotoUrl(photo_url),
            refresh_token=UserStringData(refresh_token)
        )


    def to_raw_dict(self) -> dict:
        """
            Create a dictionary with the data of the Users object.

            Args:
                None
            Returns:
                dict: A dictionary with te data of the object Users
        """
        return {
            "id_user": self.id_user.value if self.id_user else None,
            "name": self.name.value,
            "surname": self.surname.value,
            "email": self.email.value,
            "password_hash": self.password_hash.value,
            "last_update": self.last_update.value.isoformat() if self.last_update else None,
            "created_at": self.created_at.value.isoformat() if self.created_at else None,
            "description": self.description.value if self.description else None,
            "tenant": self.tenant.value,
            "photo_url": self.photo_url.value,
            "deleted_at": self.deleted_at.value.isoformat() if self.deleted_at else None,
            "refresh_token": self.refresh_token.value
        }



