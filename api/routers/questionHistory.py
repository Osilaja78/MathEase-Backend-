from fastapi import APIRouter, Depends, HTTPException,status
from api.routers.auth import get_current_user
from sqlalchemy.orm import Session
from datetime import datetime
from api import models, schemas
from api.database import get_db


router = APIRouter(tags=['Question History'])

# Get all question history
@router.get('/question-history')
async def get_all_question_history(
        db: Session = Depends(get_db),
        user: schemas.Users = Depends(get_current_user)
    ):

    questions = db.query(models.QuestionHistory).all()

    return questions

# Get question history for specific user
@router.get('/question-history/{id}')
async def get_specific_question_history(
        id: str,
        db: Session = Depends(get_db),
        user: schemas.Users = Depends(get_current_user)
    ):

    question = db.query(models.QuestionHistory).filter(
        models.QuestionHistory.author_id == id
    ).all()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User id is not valid!"
        )

    return question

# Add question history to database
@router.post('/question-history')
async def add_question_history(
        request: schemas.QuestionHistory,
        db: Session = Depends(get_db),
        user: schemas.Users = Depends(get_current_user)
    ):

    user_id = user.id

    question = models.QuestionHistory(
        question=request.question,
        author_id = user_id,
        date_created = datetime.utcnow()
    )

    db.add(question)
    db.commit()
    db.close()

    return {
        "message": "Added successfully!",
    }