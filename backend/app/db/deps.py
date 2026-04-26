from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()

    print("DB ACTUAL:", db.bind.url) 
    
    try:
        yield db
    finally:
        db.close()