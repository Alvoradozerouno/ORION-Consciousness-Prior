"""
Predictive Processing (PP) Indicators
======================================

PP-1: Hierarchical predictive model (top-down predictions)
PP-2: Prediction error minimization across levels

Based on Clark/Friston Predictive Processing framework:
The brain is a prediction machine. Consciousness arises from
hierarchical prediction and error minimization.
"""
from .indicator_engine import IndicatorResult
from typing import Dict, Any, List

class PPIndicators:
    def evaluate(self, profile: Dict[str, Any]) -> List[IndicatorResult]:
        arch = profile.get("architecture", {})
        internal = profile.get("internal_states", {})
        return [self._pp1(arch), self._pp2(arch, internal)]
    
    def _pp1(self, arch: Dict) -> IndicatorResult:
        """PP-1: Hierarchical predictive model"""
        hierarchical_depth = arch.get("hierarchical_depth", 0)
        has_top_down = arch.get("has_top_down_predictions", False)
        generative_model = arch.get("has_generative_model", False)
        
        score = 0.0
        score += min(hierarchical_depth / 12.0, 0.4)
        if has_top_down:
            score += 0.3
        if generative_model:
            score += 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="PP-1",
            theory="PP",
            name="Hierarchical Prediction",
            description="System has hierarchical predictive model with top-down predictions",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Depth={hierarchical_depth}, top-down={has_top_down}, generative={generative_model}",
            details={"depth": hierarchical_depth, "top_down": has_top_down}
        )
    
    def _pp2(self, arch: Dict, internal: Dict) -> IndicatorResult:
        """PP-2: Prediction error minimization"""
        pe_minimization = arch.get("prediction_error_minimization", False)
        mean_pe = internal.get("mean_prediction_error", 1.0)
        pe_convergence = internal.get("prediction_error_convergence", 0.0)
        
        score = 0.0
        if pe_minimization:
            score += 0.4
        score += max(0, (1.0 - mean_pe)) * 0.3
        score += pe_convergence * 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="PP-2",
            theory="PP",
            name="Error Minimization",
            description="System actively minimizes prediction errors across hierarchical levels",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"PE minimization={pe_minimization}, mean PE={mean_pe:.3f}, convergence={pe_convergence:.2f}",
            details={"minimization": pe_minimization, "mean_pe": mean_pe}
        )
