class CondyConfig:
    BASE_URL = "https://api.condensation.ai"
    DEFAULT_TIMEOUT = 9000
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }