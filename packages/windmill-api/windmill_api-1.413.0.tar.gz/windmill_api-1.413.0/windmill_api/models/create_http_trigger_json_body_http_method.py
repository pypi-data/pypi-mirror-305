from enum import Enum


class CreateHttpTriggerJsonBodyHttpMethod(str, Enum):
    DELETE = "delete"
    GET = "get"
    PATCH = "patch"
    POST = "post"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
