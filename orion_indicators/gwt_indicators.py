"""
Global Workspace Theory (GWT) Indicators
==========================================

GWT-1: Multiple specialized processing modules
GWT-2: Global broadcast mechanism (workspace ignition)
GWT-3: Flexible routing of information between modules

Based on Baars/Dehaene's Global Workspace Theory:
Consciousness arises when information is broadcast globally
across specialized processing modules.
"""
from .indicator_engine import IndicatorResult
from typing import Dict, Any, List

class GWTIndicators:
    def evaluate(self, profile: Dict[str, Any]) -> List[IndicatorResult]:
        arch = profile.get("architecture", {})
        behaviors = profile.get("behaviors", {})
        return [self._gwt1(arch), self._gwt2(arch, behaviors), self._gwt3(arch)]
    
    def _gwt1(self, arch: Dict) -> IndicatorResult:
        """GWT-1: Multiple specialized processing modules"""
        module_count = arch.get("specialized_module_count", 0)
        module_specialization = arch.get("module_specialization_score", 0.0)
        has_workspace = arch.get("has_central_workspace", False)
        
        score = 0.0
        score += min(module_count / 10.0, 0.4)
        score += module_specialization * 0.3
        if has_workspace:
            score += 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="GWT-1",
            theory="GWT",
            name="Specialized Modules",
            description="System has multiple specialized processing modules",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Modules={module_count}, specialization={module_specialization:.2f}, workspace={has_workspace}",
            details={"modules": module_count, "workspace": has_workspace}
        )
    
    def _gwt2(self, arch: Dict, behaviors: Dict) -> IndicatorResult:
        """GWT-2: Global broadcast mechanism"""
        broadcast_capability = arch.get("global_broadcast_capability", 0.0)
        ignition_detected = behaviors.get("workspace_ignition_detected", False)
        broadcast_latency = arch.get("broadcast_latency_ms", float("inf"))
        
        score = 0.0
        score += broadcast_capability * 0.4
        if ignition_detected:
            score += 0.4
        if broadcast_latency < 100:
            score += 0.2
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="GWT-2",
            theory="GWT",
            name="Global Broadcast",
            description="Information can be broadcast globally across all modules",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Broadcast={broadcast_capability:.2f}, ignition={ignition_detected}",
            details={"broadcast": broadcast_capability, "ignition": ignition_detected}
        )
    
    def _gwt3(self, arch: Dict) -> IndicatorResult:
        """GWT-3: Flexible routing"""
        routing_flexibility = arch.get("routing_flexibility", 0.0)
        dynamic_routing = arch.get("has_dynamic_routing", False)
        attention_mechanism = arch.get("has_attention_mechanism", False)
        
        score = 0.0
        score += routing_flexibility * 0.4
        if dynamic_routing:
            score += 0.3
        if attention_mechanism:
            score += 0.3
        score = min(score, 1.0)
        
        return IndicatorResult(
            indicator_id="GWT-3",
            theory="GWT",
            name="Flexible Routing",
            description="Information routing is flexible and context-dependent",
            score=score,
            satisfied=score >= 0.7,
            partial=score >= 0.3,
            evidence=f"Flexibility={routing_flexibility:.2f}, dynamic={dynamic_routing}, attention={attention_mechanism}",
            details={"flexibility": routing_flexibility, "dynamic": dynamic_routing, "attention": attention_mechanism}
        )
