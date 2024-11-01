from cbr_shared.cbr_backend.user_personas.User__Persona import User__Persona
from osbot_utils.base_classes.Type_Safe                 import Type_Safe
from osbot_utils.helpers.Zip_Bytes                      import Zip_Bytes
from osbot_utils.utils.Json                             import json_to_bytes

class User__Persona__Zip(Type_Safe):
    user_persona : User__Persona = None

    def persona_to__zip_bytes(self):
        with self.user_persona as persona:
            persona__id          = persona.persona_id
            persona__all_files   = persona.all_files()
            persona__base_folder = persona.s3_folder__user_persona()
            persona__zip_bytes   = persona.db_user.zip_bytes__with_paths_bytes(persona__base_folder, persona__all_files)

        with self.user_persona.persona__db_user() as db_user:
            db_user__id          = db_user.user_id
            db_user__all_files   = db_user.s3_folder_user_data__all_files()
            db_user__base_folder = db_user.s3_folder_user_data()
            db_user__zip_bytes   = db_user.zip_bytes__with_paths_bytes(db_user__base_folder, db_user__all_files)

        persona_zip_config       = dict(persona__id = persona__id ,
                                        db_user__id = db_user__id )

        persona_zip_config_bytes = json_to_bytes(persona_zip_config)
        with Zip_Bytes() as _:
            _.add_file('persona_zip_config' , persona_zip_config_bytes)
            _.add_file('persona__zip_bytes' , persona__zip_bytes      )
            _.add_file('db_user__zip_bytes' , db_user__zip_bytes      )
            return _.zip_bytes

    def zip_bytes__from_s3_files(self, root_folder, target_files):
        pass