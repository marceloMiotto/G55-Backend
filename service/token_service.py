from service.log_service import log
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR, C_TOKEN_SECRET_KEY
from service.utils_service import error_to_json
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
import datetime
import jwt
import os

TOKEN_DATA_KEY = os.urandom(24)


class CodeServices(object):

    def __init__(self):
        pass

    def token_encode(self, user):
        try:
            token = jwt.encode({"user_id": str(user["_id"]),
                                "key": str(TOKEN_DATA_KEY),
                                "type": user["type"],
                                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, C_TOKEN_SECRET_KEY)
            return token.decode('UTF-8')

        except Exception as e:
            log(C_LOG_MESSAGE.format("token_encode", "Handling", str(e), user))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def token_decode(self):
        pass




