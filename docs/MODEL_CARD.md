# Model / Logic Card

## Component

ALIS uses a simple rule-based retention score rather than a trained machine-learning model.

## Formula

`Retention = (Score × 0.8) + (Revision Count × 5)`

The implementation clips the result to `[0, 100]`.

## Status Rules

- Retention < 40 → Revise Now
- 40 ≤ Retention < 70 → Revise Soon
- Retention ≥ 70 → Good

## Important Limitation

The supplied implementation does not learn model parameters from historical student data and does not use elapsed time in its retention formula. Therefore, it should be described as a rule-based adaptive learning prototype, not as a validated predictive learning model.
