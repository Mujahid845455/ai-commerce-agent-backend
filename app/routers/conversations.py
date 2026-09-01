from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from app.core.database import get_db
from app.models.conversation import Conversation


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


class TurnPayload(BaseModel):
    user_message: str
    assistant_message: str


@router.get("/{session_id}")
def get_conversation(session_id: str, db: Session = Depends(get_db)):
    conv = db.query(Conversation).filter(Conversation.session_id == session_id).first()
    if not conv:
        return {"session_id": session_id, "messages": []}
    return {"session_id": conv.session_id, "messages": conv.messages or []}


@router.post("/{session_id}/turn")
def add_turn(session_id: str, payload: TurnPayload, db: Session = Depends(get_db)):
    conv = db.query(Conversation).filter(Conversation.session_id == session_id).first()
    
    new_messages = [
        {"role": "user", "content": payload.user_message},
        {"role": "assistant", "content": payload.assistant_message}
    ]

    if not conv:
        conv = Conversation(
            session_id=session_id,
            messages=new_messages
        )
        db.add(conv)
    else:
        current_messages = list(conv.messages or [])
        current_messages.extend(new_messages)
        conv.messages = current_messages
        flag_modified(conv, "messages")

    db.commit()
    db.refresh(conv)
    return {"status": "success", "message_count": len(conv.messages)}


@router.get("/merchant/list")
def list_conversations(limit: int = Query(default=20, ge=1, le=100), db: Session = Depends(get_db)):
    convs = db.query(Conversation).order_by(Conversation.updated_at.desc()).limit(limit).all()
    result = []
    for c in convs:
        result.append({
            "session_id": c.session_id,
            "message_count": len(c.messages or []),
            "last_message": c.messages[-1]["content"] if c.messages else "",
            "created_at": c.created_at,
            "updated_at": c.updated_at,
            "messages": c.messages or []
        })
    return result
