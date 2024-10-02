from pydantic import BaseModel
from typing import List

class Milestone(BaseModel):
    name: str
    objective: str
    topics: List[str]

class TrainingPlan(BaseModel):
    milestones: List[Milestone]
