from fastapi import HTTPException, status


class CoGymException(HTTPException):
    def __init__(self, status_code: int, detail: str, code: str = None):
        super().__init__(status_code=status_code, detail=detail)
        self.code = code


class UserAlreadyExistsException(CoGymException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists.",
            code="USER_ALREADY_EXISTS"
        )


class InvalidCredentialsException(CoGymException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials.",
            code="INVALID_AUTH"
        )