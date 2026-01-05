import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def reset():
    run("iptables -F")
    run("iptables -X")

def apply_rule(rule):
    chain = "INPUT" if rule["direction"] == "IN" else "OUTPUT"
    action = "DROP" if rule["action"] == "BLOCK" else "ACCEPT"
    cmd = f"iptables -A {chain} -p {rule['protocol']} --dport {rule['port']} -j {action}"
    run(cmd)

def apply_all(rules):
    reset()
    for rule in rules:
        apply_rule(rule)