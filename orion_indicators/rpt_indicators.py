"""
Recurrent Processing Theory (RPT) Indicators
=============================================

RPT-1: Algorithmic recurrence in processing
RPT-2: Rich feedback connections between processing levels

Based on Victor Lamme's recurrent processing theory:
Consciousness requires recurrent (feedback) processing,
not just feedforward sweeps.
"""
from .indicator_engine import IndicatorResult
from typing import Dict, Any, List

class RPTIndicators:
    def evaluate(self, profile: Dict[str, Any]) -> List[IndicatorResult]:
        arch = profile.get("architecture", {})
        return [self._rpt1(arch), self._rpt2(arch)]
    
    def _rpt1(self, arch: Dict) -> IndicatorResult:
        """RPT-1: Algorithmic recurrence"""
        has_recurrence = arch.get("has_recurrent_connections", False)
        recurrence_depth = arch.get("recurrence_depth", 0)
        feedback_loops = arch.get("feedback_loop_count", 0)
        
        score = 0.0
        if has_recurrence:
            score += 0.4
        score += min(recurrence_depth / 10.0, 0.3)
        score += min(feedback_loops / 5.0, 0.3)
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="RPT-1",
            theory="RPT",
            name="Algorithmic Recurrence",
            description="System implements recurrent processing with feedback loops",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Recurrence: {has_recurrence}, depth={recurrence_depth}, loops={feedback_loops}",
            details={"recurrence": has_recurrence, "depth": recurrence_depth, "loops": feedback_loops}
        )
    
    def _rpt2(self, arch: Dict) -> IndicatorResult:
        """RPT-2: Rich feedback connections"""
        feedback_richness = arch.get("feedback_connection_richness", 0.0)
        bidirectional = arch.get("bidirectional_connections", False)
        layer_feedback = arch.get("cross_layer_feedback", 0)
        
        score = 0.0
        score += feedback_richness * 0.4
        if bidirectional:
            score += 0.3
        score += min(layer_feedback / 8.0, 0.3)
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="RPT-2",
            theory="RPT",
            name="Rich Feedback Connections",
            description="Rich feedback connections between processing hierarchy levels",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Richness={feedback_richness:.2f}, bidirectional={bidirectional}",
            details={"richness": feedback_richness, "bidirectional": bidirectional}
        )
