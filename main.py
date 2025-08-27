from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
from models import UserRegister, UserLogin, UserResponse, Token
from auth import (
    get_password_hash, 
    authenticate_user, 
    create_access_token, 
    create_user, 
    get_user_by_email,
    verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

# Create FastAPI instance
app = FastAPI(
    title="Hello World Backend API",
    description="A simple backend API with Hello World endpoint",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hello World endpoint
@app.get("/")
async def hello_world():
    """
    Hello World endpoint
    Returns a simple greeting message
    """
    return {"message": "Hello World!", "status": "success"}

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint
    Returns the status of the API
    """
    return {"status": "healthy", "message": "API is running"}

# Authentication endpoints
@app.post("/register", response_model=UserResponse)
async def register(user: UserRegister):
    """
    Register a new user
    """
    # Check if user already exists
    if get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash password and create user
    hashed_password = get_password_hash(user.password)
    user_data = {
        "email": user.email,
        "hashed_password": hashed_password,
        "fullname": user.fullname,
        "phone_number": user.phone_number,
        "birthday": user.birthday
    }
    
    new_user = create_user(user_data)
    
    # Return user without password
    return UserResponse(
        id=new_user["id"],
        email=new_user["email"],
        fullname=new_user["fullname"],
        phone_number=new_user["phone_number"],
        birthday=new_user["birthday"],
        created_at=new_user["created_at"]
    )


@app.post("/login", response_model=Token)
async def login(user: UserLogin):
    """
    Login user and return JWT token
    """
    authenticated_user = authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": authenticated_user["email"]}, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/profile", response_model=UserResponse)
async def get_profile(current_user: dict = Depends(verify_token)):
    """
    Get current user profile (protected endpoint)
    """
    return UserResponse(
        id=current_user["id"],
        email=current_user["email"],
        fullname=current_user["fullname"],
        phone_number=current_user["phone_number"],
        birthday=current_user["birthday"],
        created_at=current_user["created_at"]
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
