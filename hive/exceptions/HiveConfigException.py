from typing import List


class HiveConfigException(Exception):
    """Exception raised for faulty hive config.

    Attributes:
        fields -- all config values
    """

    def __init__(self, fields: List[str]):
        self.fields = fields
        self.message = "Invalid configuration "

        if fields:
            self.message += "\n".join(fields)
