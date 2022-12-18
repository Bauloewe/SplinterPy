class LoginRequest:
    name: str
    ts: int
    sig: str

    def __init__(self, name: str, ts: int, sig: str):
        self.name = name
        self.ts = ts
        self.sig = sig
