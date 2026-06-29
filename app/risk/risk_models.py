from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class RiskFactor:
    category: str
    name: str
    score: int


@dataclass
class RiskAnalysisResult:
    risk_score: int = 0
    risk_level: str = "LOW"
    recommendation: str = "APPROVE"

    category_scores: Dict[str, int] = field(default_factory=dict)

    triggered_factors: List[RiskFactor] = field(default_factory=list)