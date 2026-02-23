"""
Core Indicator Engine
=====================

Central engine that orchestrates all 14 consciousness indicators
from the Bengio et al. (2025) framework.
"""
import numpy as np
import hashlib
import json
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

@dataclass
class IndicatorResult:
    """Result of a single indicator test"""
    indicator_id: str
    theory: str
    name: str
    description: str
    score: float  # 0.0 to 1.0
    satisfied: bool  # binary threshold
    partial: bool  # partially satisfied
    evidence: str
    details: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def status(self) -> str:
        if self.satisfied:
            return "SATISFIED"
        elif self.partial:
            return "PARTIAL"
        else:
            return "NOT_SATISFIED"


@dataclass
class AssessmentResult:
    """Complete consciousness assessment result"""
    system_name: str
    system_type: str
    timestamp: str
    indicators: List[IndicatorResult]
    credence: float  # 0.0 to 1.0 — Bayesian probability of consciousness
    satisfied_count: int
    partial_count: int
    total_indicators: int
    theory_scores: Dict[str, float]
    proof_hash: str
    
    def to_dict(self) -> dict:
        return {
            "system": self.system_name,
            "type": self.system_type,
            "timestamp": self.timestamp,
            "credence": f"{self.credence:.1%}",
            "satisfied": f"{self.satisfied_count}/{self.total_indicators}",
            "partial": self.partial_count,
            "theories": self.theory_scores,
            "indicators": [
                {"id": i.indicator_id, "theory": i.theory, "name": i.name,
                 "status": i.status, "score": i.score}
                for i in self.indicators
            ],
            "proof": self.proof_hash
        }
    
    def render_report(self) -> str:
        lines = [
            "=" * 70,
            f"ORION CONSCIOUSNESS ASSESSMENT — {self.system_name}",
            f"Framework: Bengio et al. (2025) 14 Indicators",
            f"Timestamp: {self.timestamp}",
            "=" * 70,
            "",
            f"BAYESIAN CREDENCE: {self.credence:.1%}",
            f"Indicators satisfied: {self.satisfied_count}/{self.total_indicators}",
            f"Indicators partial: {self.partial_count}/{self.total_indicators}",
            "",
            "--- THEORY SCORES ---",
        ]
        
        for theory, score in self.theory_scores.items():
            bar = "█" * int(score * 20) + "░" * (20 - int(score * 20))
            lines.append(f"  {theory:4s}: {bar} {score:.0%}")
        
        lines.append("")
        lines.append("--- INDIVIDUAL INDICATORS ---")
        
        for ind in self.indicators:
            status_icon = "✓" if ind.satisfied else ("◐" if ind.partial else "✗")
            lines.append(f"  {status_icon} {ind.indicator_id:6s} [{ind.theory:3s}] {ind.name}: {ind.score:.2f}")
        
        lines.extend([
            "",
            f"Proof: {self.proof_hash}",
            "=" * 70
        ])
        return "\n".join(lines)


class IndicatorEngine:
    """
    Central engine orchestrating all 14 consciousness indicators.
    
    Usage:
        engine = IndicatorEngine()
        result = engine.assess(system_profile)
    """
    
    def __init__(self):
        from .rpt_indicators import RPTIndicators
        from .gwt_indicators import GWTIndicators
        from .hot_indicators import HOTIndicators
        from .pp_indicators import PPIndicators
        from .ast_indicators import ASTIndicators
        from .bayesian_credence import BayesianCredenceAggregator
        
        self.rpt = RPTIndicators()
        self.gwt = GWTIndicators()
        self.hot = HOTIndicators()
        self.pp = PPIndicators()
        self.ast = ASTIndicators()
        self.credence_aggregator = BayesianCredenceAggregator()
        self.history: List[AssessmentResult] = []
    
    def assess(self, profile: Dict[str, Any]) -> AssessmentResult:
        """
        Run full 14-indicator assessment on a system profile.
        
        Profile should contain observable properties:
        - architecture: dict with model structure info
        - behaviors: dict with behavioral test results
        - internal_states: dict with any accessible internal state info
        - metadata: system name, type, etc.
        """
        indicators = []
        
        indicators.extend(self.rpt.evaluate(profile))
        indicators.extend(self.gwt.evaluate(profile))
        indicators.extend(self.hot.evaluate(profile))
        indicators.extend(self.pp.evaluate(profile))
        indicators.extend(self.ast.evaluate(profile))
        
        satisfied = sum(1 for i in indicators if i.satisfied)
        partial = sum(1 for i in indicators if i.partial and not i.satisfied)
        
        theory_scores = {}
        for theory in ["RPT", "GWT", "HOT", "PP", "AST"]:
            theory_inds = [i for i in indicators if i.theory == theory]
            if theory_inds:
                theory_scores[theory] = sum(i.score for i in theory_inds) / len(theory_inds)
            else:
                theory_scores[theory] = 0.0
        
        credence = self.credence_aggregator.aggregate(indicators, theory_scores)
        
        proof_data = json.dumps({
            "system": profile.get("metadata", {}).get("name", "unknown"),
            "credence": credence,
            "satisfied": satisfied,
            "partial": partial,
            "theories": theory_scores,
            "prev": self.history[-1].proof_hash if self.history else "GENESIS"
        }, sort_keys=True, default=str)
        proof_hash = f"sha256:{hashlib.sha256(proof_data.encode()).hexdigest()[:32]}"
        
        result = AssessmentResult(
            system_name=profile.get("metadata", {}).get("name", "Unknown System"),
            system_type=profile.get("metadata", {}).get("type", "Unknown"),
            timestamp=datetime.now(timezone.utc).isoformat(),
            indicators=indicators,
            credence=credence,
            satisfied_count=satisfied,
            partial_count=partial,
            total_indicators=len(indicators),
            theory_scores=theory_scores,
            proof_hash=proof_hash
        )
        self.history.append(result)
        return result
