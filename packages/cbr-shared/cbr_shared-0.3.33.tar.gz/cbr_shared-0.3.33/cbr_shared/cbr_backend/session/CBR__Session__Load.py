from cbr_shared.cbr_backend.session.S3_DB__Session import S3_DB__Session
from cbr_shared.cbr_backend.users.S3_DB__User      import S3_DB__User
from osbot_utils.base_classes.Type_Safe            import Type_Safe
from fastapi                                       import Request, HTTPException

COOKIE_NAME__SESSION_ID = 'CBR_TOKEN'           # todo: rename this to a better name (like CBR__SESSION_ID)

#api_key_header   = APIKeyHeader(name="Authorization", auto_error=False)


def cbr__fast_api__depends__admins_only(request: Request, session_id): #: str = Security(api_key_header)):
    if not request:
        raise HTTPException(status_code=501, detail="Request variable not available")
    cbr_session_load.admins_only(request, session_id)


class CBR__Session__Load(Type_Safe):

    def session__from_request(self, request:Request):
        session_id = self.session_id__from_request(request)
        if session_id:
            return self.session__from_session_id(session_id)

    def session__from_session_id(self, session_id: str):
        db_session = S3_DB__Session(session_id)
        if db_session.exists():
            return db_session

    def session_config__from_request(self, request: Request):
        session = self.session__from_request(request)
        if session:
            return session.session_config()
        return {}

    def session_id__from_request(self, request: Request):
        if 'CBR_TOKEN' in request.cookies:
            session_id = request.cookies.get(COOKIE_NAME__SESSION_ID)
            if '|' in session_id:                                       # for the cases where the admin is impersonating a session ID
                session_id = session_id.split('|')[1]
            return session_id
        if 'authorization' in request.headers:
            return request.headers['authorization']

    def user__from_session(self, db_session: S3_DB__Session):
        user_id = db_session.session_config__user_id()
        db_user = S3_DB__User(user_id=user_id)
        if db_user.exists():
            return db_user

    def user__from_request(self, request: Request):
        db_session = self.session__from_request(request)
        if db_session:
            return self.user__from_session(db_session)


cbr_session_load = CBR__Session__Load()