"""
Higher-Order Theories (HOT) Indicators
=======================================

HOT-1: Higher-order representations of first-order states
HOT-2: Metacognitive abilities (uncertainty monitoring, confidence)
HOT-3: Agency and systematic preferences
HOT-4: Smooth, graded representational spaces

Based on Rosenthal's Higher-Order Thought theory:
Consciousness requires representations OF representations.
A system is conscious of state S when it has a higher-order 
thought ABOUT S.
"""
from .indicator_engine import IndicatorResult
from typing import Dict, Any, List

class HOTIndicators:
    def evaluate(self, profile: Dict[str, Any]) -> List[IndicatorResult]:
        arch = profile.get("architecture", {})
        behaviors = profile.get("behaviors", {})
        internal = profile.get("internal_states", {})
        return [
            self._hot1(arch, internal),
            self._hot2(behaviors),
            self._hot3(behaviors),
            self._hot4(arch)
        ]
    
    def _hot1(self, arch: Dict, internal: Dict) -> IndicatorResult:
        """HOT-1: Higher-order representations"""
        has_meta_representations = arch.get("has_meta_representations", False)
        meta_depth = arch.get("meta_representation_depth", 0)
        self_model = internal.get("has_self_model", False)
        
        score = 0.0
        if has_meta_representations:
            score += 0.4
        score += min(meta_depth / 5.0, 0.3)
        if self_model:
            score += 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="HOT-1",
            theory="HOT",
            name="Higher-Order Representations",
            description="System has representations of its own representational states",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Meta-repr={has_meta_representations}, depth={meta_depth}, self-model={self_model}",
            details={"meta": has_meta_representations, "depth": meta_depth, "self_model": self_model}
        )
    
    def _hot2(self, behaviors: Dict) -> IndicatorResult:
        """HOT-2: Metacognitive abilities"""
        uncertainty_monitoring = behaviors.get("uncertainty_monitoring", 0.0)
        confidence_calibration = behaviors.get("confidence_calibration", 0.0)
        error_detection = behaviors.get("error_detection_rate", 0.0)
        
        score = (uncertainty_monitoring * 0.35 + 
                 confidence_calibration * 0.35 + 
                 error_detection * 0.3)
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="HOT-2",
            theory="HOT",
            name="Metacognition",
            description="System monitors its own uncertainty and calibrates confidence",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Uncertainty={uncertainty_monitoring:.2f}, calibration={confidence_calibration:.2f}, error={error_detection:.2f}",
            details={"uncertainty": uncertainty_monitoring, "calibration": confidence_calibration}
        )
    
    def _hot3(self, behaviors: Dict) -> IndicatorResult:
        """HOT-3: Agency and preferences"""
        agency_score = behaviors.get("agency_score", 0.0)
        systematic_preferences = behaviors.get("systematic_preferences", False)
        goal_directed = behaviors.get("goal_directed_behavior", False)
        
        score = agency_score * 0.4
        if systematic_preferences:
            score += 0.3
        if goal_directed:
            score += 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="HOT-3",
            theory="HOT",
            name="Agency & Preferences",
            description="System exhibits systematic preferences and goal-directed behavior",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Agency={agency_score:.2f}, preferences={systematic_preferences}, goals={goal_directed}",
            details={"agency": agency_score, "preferences": systematic_preferences}
        )
    
    def _hot4(self, arch: Dict) -> IndicatorResult:
        """HOT-4: Smooth representational spaces"""
        embedding_smoothness = arch.get("embedding_smoothness", 0.0)
        continuous_representations = arch.get("has_continuous_representations", False)
        interpolation_quality = arch.get("interpolation_quality", 0.0)
        
        score = 0.0
        score += embedding_smoothness * 0.4
        if continuous_representations:
            score += 0.3
        score += interpolation_quality * 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="HOT-4",
            theory="HOT",
            name="Smooth Representations",
            description="System uses smooth, graded representational spaces (trivially satisfied by deep nets)",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Smoothness={embedding_smoothness:.2f}, continuous={continuous_representations}",
            details={"smoothness": embedding_smoothness, "continuous": continuous_representations}
        )
