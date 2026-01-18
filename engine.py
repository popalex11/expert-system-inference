from rules import Rule

def load_rules():
    return [
        Rule(["fever", "cough"], "flu"),
        Rule(["flu"], "rest"),
        Rule(["flu"], "medicine"),
        Rule(["headache", "stress"], "migraine"),
        Rule(["migraine"], "rest")
    ]
