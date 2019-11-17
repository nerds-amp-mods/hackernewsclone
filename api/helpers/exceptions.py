from flask import jsonify

class Error(Exception):
    def __init__(self, code, message, status_code):
        self.code = code
        self.message = message
        self.status_code = status_code
    
    def json_response(self):
        res = jsonify({
            'code': self.code,
            'message': self.message
        })
        res.status_code = self.status_code
        return res

    def __str__(self):
        return f'Code: {self.code}, Message: {self.message}'