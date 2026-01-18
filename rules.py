class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = set(conditions)
        self.conclusion = conclusion

    def __repr__(self):
        return f"IF {self.conditions} THEN {self.conclusion}"
