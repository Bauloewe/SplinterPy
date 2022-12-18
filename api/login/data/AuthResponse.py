class AuthResponse:

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.success: bool = values.get("success", None)