from pydantic import BaseModel


class StrictInt(int):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, int):
            raise TypeError('{} is not a valid integer'.format(value))
        return value
