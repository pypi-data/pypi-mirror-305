from dataclasses import dataclass
from typing import Optional


@dataclass
class ProfanityResult:
    result: str
    reason: Optional[str]
    is_clean: bool
    problematic_score: int
