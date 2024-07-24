#
# Lab FastAPI
#
# Date    : 2024-06-30
# Author  : Hirotoshi FUJIBE
# History :
#

json_list_response = {
    'status': '',
    'message': '',
    'list': []
}


# JsonListResponse
class JsonListResponse:

    def __init__(self) -> None:
        self.response = json_list_response
        self.response['status'] = 'action-ok'
        self.response['message'] = ''
        self.response['list'] = []
        return

    def set_status(self, ok: bool) -> None:
        if not ok:
            self.response['status'] = 'action-ng'
        return

    def set_message(self, message: str) -> None:
        self.response['message'] = message
        return

    def set_list(self, _list: []) -> None:
        self.response['list'] = _list
        return

    def get_json(self) -> dict:
        return self.response
