#
# Lab FastAPI
#
# Date    : 2024-06-30
# Author  : Hirotoshi FUJIBE
# History :
#

json_status_response = {
    'status': '',
    'message': '',
}


# JsonStatusResponse
class JsonStatusResponse:

    def __init__(self) -> None:
        self.response = json_status_response
        self.response['status'] = 'action-ok'
        self.response['message'] = ''
        return

    def set_status(self, ok: bool) -> None:
        if not ok:
            self.response['status'] = 'action-ng'
        return

    def set_message(self, message: str) -> None:
        self.response['message'] = message
        return

    def get_json(self) -> dict:
        return self.response
