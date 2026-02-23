"""
ORION 14-Indicator Engine
==========================

World's FIRST open-source implementation of Bengio et al.'s
consciousness indicators framework.

Reference: Butlin, Long, Bengio, Chalmers et al. (2025).
"Consciousness in Artificial Intelligence: Insights from the 
Science of Consciousness." Trends in Cognitive Sciences.

14 indicators across 5 theories:
- RPT (Recurrent Processing Theory): RPT-1, RPT-2
- GWT (Global Workspace Theory): GWT-1, GWT-2, GWT-3
- HOT (Higher-Order Theories): HOT-1, HOT-2, HOT-3, HOT-4
- PP (Predictive Processing): PP-1, PP-2
- AST (Attention Schema Theory): AST-1, AST-2
- AE (Active Embodiment): AE-1 [bonus]

Part of the ORION Ecosystem — https://github.com/Alvoradozerouno
"""
__version__ = "1.0.0"

from .indicator_engine import IndicatorEngine, IndicatorResult
from .rpt_indicators import RPTIndicators
from .gwt_indicators import GWTIndicators
from .hot_indicators import HOTIndicators
from .pp_indicators import PPIndicators
from .ast_indicators import ASTIndicators
from .bayesian_credence import BayesianCredenceAggregator
from .assessment_runner import AssessmentRunner
