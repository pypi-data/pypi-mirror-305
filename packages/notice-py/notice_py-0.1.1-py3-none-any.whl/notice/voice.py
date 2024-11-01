import requests

voice_url = "http://api.vm.ihuyi.com/webservice/voice.php?method=Submit"
voice_headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}


class Voice:

    def __init__(self, account: str, password: str) -> None:
        self.account = account
        self.password = password

    def send(self, mobile_num, content: str, format: str = 'json'):
        data = {
            'account': self.account,
            'password': self.password,
            'mobile': str(mobile_num),
            'content': content,
            'format': format,
        }
        try:
            response = requests.post(url=voice_url,
                                     headers=voice_headers,
                                     data=data)
            if response.json()['code'] != 2:
                return response.json()['msg']
            return None
        except Exception as e:
            return f'{e}'
