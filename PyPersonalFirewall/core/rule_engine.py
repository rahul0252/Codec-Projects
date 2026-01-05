import json
from pathlib import Path

RULE_FILE = Path("rules/firewall_rules.json")

def load_rules():
    if not RULE_FILE.exists():
        return []
    with open(RULE_FILE, "r") as f:
        return json.load(f)

def save_rules(rules):
    with open(RULE_FILE, "w") as f:
        json.dump(rules, f, indent=4)

def add_rule(rule):
    rules = load_rules()
    rules.append(rule)
    save_rules(rules)