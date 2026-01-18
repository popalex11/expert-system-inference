def backward_chaining(goal, rules, facts, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True, 1

    if goal in visited:
        return False, 1

    visited.add(goal)
    checks = 0

    for rule in rules:
        checks += 1
        if rule.conclusion == goal:
            all_true = True
            for cond in rule.conditions:
                result, sub_checks = backward_chaining(cond, rules, facts, visited)
                checks += sub_checks
                if not result:
                    all_true = False
                    break
            if all_true:
                return True, checks

    return False, checks
