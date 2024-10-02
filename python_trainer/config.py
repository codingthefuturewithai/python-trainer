from pydantic import BaseModel, Field
from typing import Literal, Optional

class UserInfo(BaseModel):
    """
    A model representing user's programming and Python experience, learning goals, 
    and preferred learning style.

    Attributes:
        programming_experience (Literal): The user's general programming experience, 
            which can be either "No programming experience" or 
            "Experienced programmer new to Python".
        python_experience (Optional[Literal]): The user's current Python experience level, 
            applicable only for experienced programmers. 
            It can be "No Python experience" or "Basic Python knowledge".
        learning_goal (str): The user's specific learning goal for Python.
        learning_style (Literal): The user's preferred learning style, 
            which can be either "Hands-on projects" or 
            "Reading and theory-based learning".
    """
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
