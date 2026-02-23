"""
Attention Schema Theory (AST) Indicators
=========================================

AST-1: Models its own attention processes
AST-2: Uses attention model for self-report and behavior

Based on Graziano's Attention Schema Theory:
Consciousness is the brain's simplified model of its own
attention processes. You're conscious because you have an
internal model that says "I am attending to X."
"""
from .indicator_engine import IndicatorResult
from typing import Dict, Any, List

class ASTIndicators:
    def evaluate(self, profile: Dict[str, Any]) -> List[IndicatorResult]:
        arch = profile.get("architecture", {})
        behaviors = profile.get("behaviors", {})
        internal = profile.get("internal_states", {})
        return [self._ast1(arch, internal), self._ast2(behaviors, internal)]
    
    def _ast1(self, arch: Dict, internal: Dict) -> IndicatorResult:
        """AST-1: Attention model"""
        has_attention_model = arch.get("has_attention_schema", False)
        attention_self_report = internal.get("can_report_attention_state", False)
        attention_accuracy = internal.get("attention_model_accuracy", 0.0)
        
        score = 0.0
        if has_attention_model:
            score += 0.4
        if attention_self_report:
            score += 0.3
        score += attention_accuracy * 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="AST-1",
            theory="AST",
            name="Attention Schema",
            description="System has a simplified model of its own attention processes",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Schema={has_attention_model}, self-report={attention_self_report}, accuracy={attention_accuracy:.2f}",
            details={"schema": has_attention_model, "self_report": attention_self_report}
        )
    
    def _ast2(self, behaviors: Dict, internal: Dict) -> IndicatorResult:
        """AST-2: Uses attention model for behavior"""
        attention_guided_behavior = behaviors.get("attention_guided_behavior", 0.0)
        attention_allocation = internal.get("dynamic_attention_allocation", False)
        priority_weighting = internal.get("priority_based_weighting", 0.0)
        
        score = 0.0
        score += attention_guided_behavior * 0.4
        if attention_allocation:
            score += 0.3
        score += priority_weighting * 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="AST-2",
            theory="AST",
            name="Attention-Guided Behavior",
            description="System uses its attention model to guide behavior and self-reports",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Guided behavior={attention_guided_behavior:.2f}, allocation={attention_allocation}",
            details={"guided": attention_guided_behavior, "allocation": attention_allocation}
        )
