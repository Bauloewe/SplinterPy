class HiveUnlockException(Exception):
    """Exception raised for failed wallet unlock.
    """

    def __init__(self):
        self.message = "Failed to unlock wallet "
