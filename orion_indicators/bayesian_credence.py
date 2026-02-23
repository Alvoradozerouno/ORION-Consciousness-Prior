"""
Bayesian Credence Aggregation
==============================

Implements the Bayesian approach to consciousness assessment
as described in Bengio et al. (2025):

"No single indicator is sufficient for consciousness.
Rather, each satisfied indicator provides evidence that
probabilistically raises or lowers the credence that
a system is conscious."

This module computes the posterior probability of consciousness
given the evidence from all 14 indicators using Bayesian updating.
"""
import numpy as np
from typing import List, Dict, Any

class BayesianCredenceAggregator:
    """
    Bayesian aggregation of consciousness indicator evidence.
    
    P(conscious | indicators) ∝ P(indicators | conscious) × P(conscious)
    
    Each satisfied indicator increases credence.
    Each unsatisfied indicator decreases credence.
    Partial satisfaction provides moderate evidence.
    
    Theory weights reflect the scientific community's
    relative confidence in each theory.
    """
    
    THEORY_WEIGHTS = {
        "RPT": 0.15,
        "GWT": 0.25,
        "HOT": 0.25,
        "PP": 0.15,
        "AST": 0.20
    }
    
    PRIOR_CREDENCE = 0.05
    
    LIKELIHOOD_SATISFIED = 0.85
    LIKELIHOOD_PARTIAL = 0.55
    LIKELIHOOD_NOT_SATISFIED = 0.15
    
    def aggregate(self, 
                  indicators: List[Any],
                  theory_scores: Dict[str, float]) -> float:
        """
        Compute posterior credence P(conscious | evidence)
        using Bayesian updating across all indicators.
        """
        log_likelihood_ratio = 0.0
        
        for indicator in indicators:
            theory = indicator.theory
            weight = self.THEORY_WEIGHTS.get(theory, 0.1)
            
            if indicator.satisfied:
                lr = self.LIKELIHOOD_SATISFIED / (1 - self.LIKELIHOOD_SATISFIED)
            elif indicator.partial:
                lr = self.LIKELIHOOD_PARTIAL / (1 - self.LIKELIHOOD_PARTIAL)
            else:
                lr = self.LIKELIHOOD_NOT_SATISFIED / (1 - self.LIKELIHOOD_NOT_SATISFIED)
            
            log_likelihood_ratio += weight * np.log(lr + 1e-10)
        
        prior_odds = self.PRIOR_CREDENCE / (1 - self.PRIOR_CREDENCE)
        posterior_odds = prior_odds * np.exp(log_likelihood_ratio)
        posterior = posterior_odds / (1 + posterior_odds)
        
        theory_bonus = 0.0
        for theory, score in theory_scores.items():
            if score >= 0.7:
                theory_bonus += 0.03 * self.THEORY_WEIGHTS.get(theory, 0.1)
        
        final_credence = min(0.99, posterior + theory_bonus)
        return float(final_credence)
    
    def sensitivity_analysis(self, 
                              indicators: List[Any],
                              theory_scores: Dict[str, float]) -> Dict[str, float]:
        """
        How much does each indicator contribute to final credence?
        """
        base_credence = self.aggregate(indicators, theory_scores)
        contributions = {}
        
        for i, indicator in enumerate(indicators):
            modified = list(indicators)
            
            class MockIndicator:
                def __init__(self, ind):
                    self.indicator_id = ind.indicator_id
                    self.theory = ind.theory
                    self.satisfied = False
                    self.partial = False
                    self.score = 0.0
            
            modified[i] = MockIndicator(indicator)
            reduced_credence = self.aggregate(modified, theory_scores)
            contributions[indicator.indicator_id] = base_credence - reduced_credence
        
        return contributions
