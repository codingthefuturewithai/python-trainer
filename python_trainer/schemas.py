from pydantic import BaseModel
from typing import List

class Milestone(BaseModel):
    name: str
    objective: str
    topics: List[str]

class TrainingPlan(BaseModel):
    background: str
    milestones: List[Milestone]
