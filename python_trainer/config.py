from pydantic import BaseModel, Field
from typing import Literal, Optional

class UserInfo(BaseModel):
    programming_experience: Literal["No programming experience", "Experienced programmer new to Python"] = Field(
        ..., description="User's general programming experience"
    )
    python_experience: Optional[Literal["No Python experience", "Basic Python knowledge"]] = Field(
        None, description="User's current Python experience level (only for experienced programmers)"
    )
    learning_goal: str = Field(..., description="User's learning goal for Python")
    learning_style: Literal["Hands-on projects", "Reading and theory-based learning"] = Field(
        ..., description="User's preferred learning style"
    )
