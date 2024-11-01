from cbr_shared.cbr_backend.users.User__Persona         import SECTION__NAME__USER__PERSONAS, User__Persona
from cbr_shared.cbr_backend.users.User__Section_Data    import User__Section_Data
from osbot_utils.helpers.Random_Guid                    import Random_Guid


class User__Personas(User__Section_Data):
    section_name = SECTION__NAME__USER__PERSONAS

    def persona(self, persona_id: Random_Guid):
        kwargs = dict(db_user=self.db_user, persona_id=persona_id)
        return User__Persona(**kwargs)

    def personas_ids(self):
        return self.section_folder_files()

