import subprocess

def apply_rule(rule):
    direction = "in" if rule["direction"] == "IN" else "out"
    action = "block" if rule["action"] == "BLOCK" else "allow"
    cmd = (
        f'netsh advfirewall firewall add rule '
        f'name="PyFirewall_{direction}_{rule["port"]}" '
        f'dir={direction} action={action} '
        f'protocol={rule["protocol"]} localport={rule["port"]}'
    )
    subprocess.run(cmd, shell=True)

def apply_all(rules):
    for rule in rules:
        apply_rule(rule)