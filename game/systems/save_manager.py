import json
from Crypto.Cipher import AES
from kivy.storage.jsonstore import JsonStore

class SaveManager:
    def __init__(self):
        self.key = b'YourSecureKey123'
        self.nonce = b'UniqueNonce456'
        self.cipher = AES.new(self.key, AES.MODE_EAX, self.nonce)
        
    def encrypt_data(self, data):
        return self.cipher.encrypt(json.dumps(data).encode()).hex()

    def decrypt_data(self, encrypted):
        return json.loads(self.cipher.decrypt(bytes.fromhex(encrypted)).decode())

    def save_game(self, progress):
        JsonStore('saves/game.sav').put('progress', 
            data=self.encrypt_data(progress))

    def load_game(self):
        try:
            return self.decrypt_data(
                JsonStore('saves/game.sav').get('progress')['data'])
        except:
            return self.default_progress()

    @staticmethod
    def default_progress():
        return {
            'level': 1,
            'coins': 0,
            'skills': {},
            'unlocked': []
        }
