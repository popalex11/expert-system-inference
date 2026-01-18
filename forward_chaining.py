def forward_chaining(rules, facts):
    inferred = set(facts)
    applied_rules = 0
    changed = True

    while changed:
        changed = False
        for rule in rules:
            applied_rules += 1
            if rule.conditions.issubset(inferred):
                if rule.conclusion not in inferred:
                    inferred.add(rule.conclusion)
                    changed = True

    return inferred, applied_rules
