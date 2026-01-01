from passlib.context import CryptContext
            # managing hashing algorithms secure, let's upgrade
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    # print(type(password), repr(password))
    # safe_password = password.strip()[:72]
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return 
    pwd_context.verify(plain_password, hashed_password)