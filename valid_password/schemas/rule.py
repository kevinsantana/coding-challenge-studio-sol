from typing import List, Dict

from pydantic import BaseModel


class RuleRequest(BaseModel):
    password: str
    rules: List[Dict]
