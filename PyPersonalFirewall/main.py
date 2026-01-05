import tkinter as tk
from gui.dashboard import FirewallGUI
from core.system_detector import get_os
from core.rule_engine import load_rules
from backend import linux_firewall, windows_firewall

def apply_firewall():
    rules = load_rules()
    os_type = get_os()
    if os_type == "LINUX":
        linux_firewall.apply_all(rules)
    elif os_type == "WINDOWS":
        windows_firewall.apply_all(rules)
    else:
        print("macOS detected: running in monitoring-only mode")

if __name__ == "__main__":
    apply_firewall()
    root = tk.Tk()
    FirewallGUI(root)
    root.mainloop()