import json
from Crypto.Cipher import AES
from kivy.storage.jsonstore import JsonStore

class SaveManager:
    def __init__(self):
        self.key = b'32-byte-long-secret-key-1234567890'
        self.cipher = AES.new(self.key, AES.MODE_EAX)
        
    def save_game(self, data):
        encrypted = self.cipher.encrypt(json.dumps(data).encode())
        JsonStore('user_data.sav').put('progress', data=encrypted.hex())
        
    def load_game(self):
        try:
            data = bytes.fromhex(JsonStore('user_data.sav').get('progress')['data'])
            return json.loads(self.cipher.decrypt(data).decode())
        except:
            return self.default_data()
            
    def default_data(self):
        return {'level': 1, 'coins': 0, 'skills': {}}
