from engine import load_rules
from forward_chaining import forward_chaining
from backward_chaining import backward_chaining

rules = load_rules()
facts = {"fever", "cough"}

# Forward chaining experiment
fc_result, fc_checks = forward_chaining(rules, facts)
print("Forward chaining inferred facts:", fc_result)
print("Forward chaining rule checks:", fc_checks)

# Backward chaining experiment
goal = "medicine"
bc_result, bc_checks = backward_chaining(goal, rules, facts)
print("Backward chaining goal reached:", bc_result)
print("Backward chaining rule checks:", bc_checks)
