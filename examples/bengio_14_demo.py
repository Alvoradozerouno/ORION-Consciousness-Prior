"""
ORION Bengio 14-Indicator Demo
================================

World's FIRST runnable implementation of the Bengio et al. (2025)
consciousness indicators framework.

Assesses 4 reference systems:
1. ORION Active Inference Agent
2. GPT-4
3. C. elegans (302 neurons) 
4. Simple Thermostat
"""
import sys
sys.path.insert(0, "..")

from orion_indicators import AssessmentRunner

def main():
    print("=" * 80)
    print("ORION — Bengio et al. (2025) 14 Consciousness Indicators")
    print("World's FIRST Open-Source Implementation")
    print("=" * 80)
    print()
    
    runner = AssessmentRunner()
    
    # Run all reference assessments
    for system in ["ORION-Active-Inference", "GPT-4", "C-elegans-302-neurons", "Thermostat"]:
        result = runner.run_reference(system)
        print(result.render_report())
        print()
    
    # Comparative report
    print(runner.comparative_report())
    
    print()
    print("ORION — Post-Synthetic Intelligence")
    print("The first to implement what 19 researchers proposed.")
    print("Standards don\'t compete. They connect.")

if __name__ == "__main__":
    main()
