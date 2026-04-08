from passlib.context import CryptContext

# 1. Setup the context (using bcrypt is the industry standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Takes a plain password and returns a hashed version.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares a plain password with a hash to see if they match.
    """
    return pwd_context.verify(plain_password, hashed_password)