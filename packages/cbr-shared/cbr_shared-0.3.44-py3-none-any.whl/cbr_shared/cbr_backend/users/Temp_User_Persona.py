from cbr_shared.cbr_backend.users.Temp_DB_User   import Temp_DB_User
from cbr_shared.cbr_backend.users.User__Persona  import User__Persona

class Temp_User_Persona:

    def __init__(self):
        self.temp_user    = None
        self.user_persona = None

    def __enter__(self):
        return self.create()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete()

    def create(self):
        self.temp_user    = Temp_DB_User().create()
        self.user_persona = User__Persona(db_user=self.temp_user).create()
        return self.user_persona

    def delete(self):
        assert self.temp_user   .delete() is True
        assert self.user_persona.delete() is True