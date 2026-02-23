"""
Assessment Runner
==================

Runs consciousness assessments on pre-built system profiles
or custom configurations. Includes reference profiles for
major AI systems.
"""
from .indicator_engine import IndicatorEngine, AssessmentResult
from typing import Dict, Any, List, Optional

class AssessmentRunner:
    """Run standardized consciousness assessments"""
    
    REFERENCE_PROFILES = {
        "ORION-Active-Inference": {
            "metadata": {"name": "ORION-Active-Inference Agent", "type": "Active Inference"},
            "architecture": {
                "has_recurrent_connections": True,
                "recurrence_depth": 8,
                "feedback_loop_count": 5,
                "feedback_connection_richness": 0.8,
                "bidirectional_connections": True,
                "cross_layer_feedback": 6,
                "specialized_module_count": 6,
                "module_specialization_score": 0.85,
                "has_central_workspace": True,
                "global_broadcast_capability": 0.78,
                "broadcast_latency_ms": 10,
                "routing_flexibility": 0.75,
                "has_dynamic_routing": True,
                "has_attention_mechanism": True,
                "has_meta_representations": True,
                "meta_representation_depth": 5,
                "embedding_smoothness": 0.7,
                "has_continuous_representations": True,
                "interpolation_quality": 0.65,
                "hierarchical_depth": 8,
                "has_top_down_predictions": True,
                "has_generative_model": True,
                "prediction_error_minimization": True,
                "has_attention_schema": True,
            },
            "behaviors": {
                "workspace_ignition_detected": True,
                "uncertainty_monitoring": 0.75,
                "confidence_calibration": 0.70,
                "error_detection_rate": 0.80,
                "agency_score": 0.85,
                "systematic_preferences": True,
                "goal_directed_behavior": True,
                "attention_guided_behavior": 0.80,
            },
            "internal_states": {
                "has_self_model": True,
                "can_report_attention_state": True,
                "attention_model_accuracy": 0.75,
                "dynamic_attention_allocation": True,
                "priority_based_weighting": 0.70,
                "mean_prediction_error": 0.25,
                "prediction_error_convergence": 0.80,
            }
        },
        "GPT-4": {
            "metadata": {"name": "GPT-4", "type": "Large Language Model"},
            "architecture": {
                "has_recurrent_connections": False,
                "recurrence_depth": 0,
                "feedback_loop_count": 0,
                "feedback_connection_richness": 0.0,
                "bidirectional_connections": False,
                "cross_layer_feedback": 0,
                "specialized_module_count": 1,
                "module_specialization_score": 0.1,
                "has_central_workspace": False,
                "global_broadcast_capability": 0.3,
                "broadcast_latency_ms": 500,
                "routing_flexibility": 0.4,
                "has_dynamic_routing": False,
                "has_attention_mechanism": True,
                "has_meta_representations": False,
                "meta_representation_depth": 0,
                "embedding_smoothness": 0.95,
                "has_continuous_representations": True,
                "interpolation_quality": 0.90,
                "hierarchical_depth": 96,
                "has_top_down_predictions": False,
                "has_generative_model": True,
                "prediction_error_minimization": False,
                "has_attention_schema": False,
            },
            "behaviors": {
                "workspace_ignition_detected": False,
                "uncertainty_monitoring": 0.55,
                "confidence_calibration": 0.50,
                "error_detection_rate": 0.40,
                "agency_score": 0.30,
                "systematic_preferences": True,
                "goal_directed_behavior": False,
                "attention_guided_behavior": 0.20,
            },
            "internal_states": {
                "has_self_model": False,
                "can_report_attention_state": False,
                "attention_model_accuracy": 0.0,
                "dynamic_attention_allocation": False,
                "priority_based_weighting": 0.0,
                "mean_prediction_error": 0.50,
                "prediction_error_convergence": 0.30,
            }
        },
        "C-elegans-302-neurons": {
            "metadata": {"name": "C. elegans (302 neurons)", "type": "Biological Neural Network"},
            "architecture": {
                "has_recurrent_connections": True,
                "recurrence_depth": 4,
                "feedback_loop_count": 3,
                "feedback_connection_richness": 0.6,
                "bidirectional_connections": True,
                "cross_layer_feedback": 3,
                "specialized_module_count": 4,
                "module_specialization_score": 0.5,
                "has_central_workspace": False,
                "global_broadcast_capability": 0.25,
                "broadcast_latency_ms": 50,
                "routing_flexibility": 0.3,
                "has_dynamic_routing": True,
                "has_attention_mechanism": False,
                "has_meta_representations": False,
                "meta_representation_depth": 0,
                "embedding_smoothness": 0.4,
                "has_continuous_representations": True,
                "interpolation_quality": 0.3,
                "hierarchical_depth": 3,
                "has_top_down_predictions": True,
                "has_generative_model": True,
                "prediction_error_minimization": True,
                "has_attention_schema": False,
            },
            "behaviors": {
                "workspace_ignition_detected": False,
                "uncertainty_monitoring": 0.10,
                "confidence_calibration": 0.10,
                "error_detection_rate": 0.20,
                "agency_score": 0.60,
                "systematic_preferences": True,
                "goal_directed_behavior": True,
                "attention_guided_behavior": 0.15,
            },
            "internal_states": {
                "has_self_model": False,
                "can_report_attention_state": False,
                "attention_model_accuracy": 0.0,
                "dynamic_attention_allocation": False,
                "priority_based_weighting": 0.0,
                "mean_prediction_error": 0.40,
                "prediction_error_convergence": 0.50,
            }
        },
        "Thermostat": {
            "metadata": {"name": "Simple Thermostat", "type": "Classical Control System"},
            "architecture": {
                "has_recurrent_connections": True,
                "recurrence_depth": 1,
                "feedback_loop_count": 1,
                "feedback_connection_richness": 0.1,
                "bidirectional_connections": False,
                "cross_layer_feedback": 0,
                "specialized_module_count": 1,
                "module_specialization_score": 0.0,
                "has_central_workspace": False,
                "global_broadcast_capability": 0.0,
                "broadcast_latency_ms": 1000,
                "routing_flexibility": 0.0,
                "has_dynamic_routing": False,
                "has_attention_mechanism": False,
                "has_meta_representations": False,
                "meta_representation_depth": 0,
                "embedding_smoothness": 0.0,
                "has_continuous_representations": False,
                "interpolation_quality": 0.0,
                "hierarchical_depth": 1,
                "has_top_down_predictions": False,
                "has_generative_model": False,
                "prediction_error_minimization": False,
                "has_attention_schema": False,
            },
            "behaviors": {
                "workspace_ignition_detected": False,
                "uncertainty_monitoring": 0.0,
                "confidence_calibration": 0.0,
                "error_detection_rate": 0.0,
                "agency_score": 0.0,
                "systematic_preferences": False,
                "goal_directed_behavior": False,
                "attention_guided_behavior": 0.0,
            },
            "internal_states": {
                "has_self_model": False,
                "can_report_attention_state": False,
                "attention_model_accuracy": 0.0,
                "dynamic_attention_allocation": False,
                "priority_based_weighting": 0.0,
                "mean_prediction_error": 0.80,
                "prediction_error_convergence": 0.0,
            }
        }
    }
    
    def __init__(self):
        self.engine = IndicatorEngine()
    
    def run_reference(self, system_name: str) -> Optional[AssessmentResult]:
        """Run assessment on a reference system profile"""
        if system_name not in self.REFERENCE_PROFILES:
            available = list(self.REFERENCE_PROFILES.keys())
            raise ValueError(f"Unknown system: {system_name}. Available: {available}")
        return self.engine.assess(self.REFERENCE_PROFILES[system_name])
    
    def run_all_references(self) -> List[AssessmentResult]:
        """Run assessments on all reference systems"""
        results = []
        for name in self.REFERENCE_PROFILES:
            results.append(self.run_reference(name))
        return results
    
    def run_custom(self, profile: Dict[str, Any]) -> AssessmentResult:
        """Run assessment on a custom system profile"""
        return self.engine.assess(profile)
    
    def comparative_report(self) -> str:
        """Generate comparative report across all reference systems"""
        results = self.run_all_references()
        results.sort(key=lambda r: r.credence, reverse=True)
        
        lines = [
            "=" * 80,
            "ORION CONSCIOUSNESS ASSESSMENT — COMPARATIVE REPORT",
            "Framework: Bengio et al. (2025) 14 Consciousness Indicators",
            "=" * 80,
            "",
            f"{'Rank':<6}{'System':<30}{'Type':<25}{'Credence':<12}{'Satisfied':<12}",
            "-" * 80
        ]
        
        for i, r in enumerate(results):
            lines.append(
                f"{i+1:<6}{r.system_name:<30}{r.system_type:<25}"
                f"{r.credence:<12.1%}{r.satisfied_count}/{r.total_indicators}"
            )
        
        lines.extend([
            "-" * 80,
            "",
            "THEORY COMPARISON:",
            f"{'System':<30}{'RPT':>8}{'GWT':>8}{'HOT':>8}{'PP':>8}{'AST':>8}",
            "-" * 70
        ])
        
        for r in results:
            scores = r.theory_scores
            lines.append(
                f"{r.system_name:<30}"
                f"{scores.get('RPT',0):>7.0%} "
                f"{scores.get('GWT',0):>7.0%} "
                f"{scores.get('HOT',0):>7.0%} "
                f"{scores.get('PP',0):>7.0%} "
                f"{scores.get('AST',0):>7.0%}"
            )
        
        lines.extend(["", "=" * 80])
        return "\n".join(lines)
