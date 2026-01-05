import tkinter as tk
from tkinter import ttk, messagebox
from core.rule_engine import add_rule, load_rules
from gui.traffic_dashboard import TrafficDashboard

class FirewallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPersonalFirewall")
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        self.setup_style()
        self.build_header()
        self.build_tabs()

    # ---------------- STYLE ----------------
    def setup_style(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
        style.configure("Status.TLabel", font=("Segoe UI", 10))
        style.configure("Card.TFrame", background="#f4f6f8", padding=15)
        style.configure("CardTitle.TLabel", font=("Segoe UI", 11, "bold"))

        style.configure("Treeview", rowheight=28)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    # ---------------- HEADER ----------------
    def build_header(self):
        header = ttk.Frame(self.root, padding=10)
        header.pack(fill="x")

        title = ttk.Label(header, text="PyPersonalFirewall", style="Header.TLabel")
        title.pack(side="left")

        self.status = ttk.Label(
            header,
            text="Status: Monitoring Mode",
            style="Status.TLabel",
            foreground="green"
        )
        self.status.pack(side="right")

    # ---------------- TABS ----------------
    def build_tabs(self):
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.dashboard_tab = ttk.Frame(self.tabs)
        self.rules_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.dashboard_tab, text="Dashboard")
        self.tabs.add(self.rules_tab, text="Firewall Rules")

        self.build_dashboard()
        self.build_rules_tab()

    # ---------------- DASHBOARD TAB ----------------
    def build_dashboard(self):
        cards = ttk.Frame(self.dashboard_tab)
        cards.pack(fill="x", pady=10)

        self.in_card = self.create_card(cards, "Incoming Traffic", "0 KB/s")
        self.out_card = self.create_card(cards, "Outgoing Traffic", "0 KB/s")

        self.in_card.pack(side="left", expand=True, fill="x", padx=10)
        self.out_card.pack(side="left", expand=True, fill="x", padx=10)

        self.traffic = TrafficDashboard(self.dashboard_tab)

    def create_card(self, parent, title, value):
        frame = ttk.Frame(parent, style="Card.TFrame")

        ttk.Label(frame, text=title, style="CardTitle.TLabel").pack(anchor="w")
        label = ttk.Label(frame, text=value, font=("Segoe UI", 20, "bold"))
        label.pack(anchor="center", pady=10)

        frame.value_label = label
        return frame

    # ---------------- RULES TAB ----------------
    def build_rules_tab(self):
        form = ttk.LabelFrame(self.rules_tab, text="Add Firewall Rule", padding=10)
        form.pack(fill="x", padx=10, pady=10)

        self.direction = ttk.Combobox(form, values=["IN", "OUT"], width=10)
        self.protocol = ttk.Combobox(form, values=["tcp", "udp"], width=10)
        self.port = ttk.Entry(form, width=10)
        self.action = ttk.Combobox(form, values=["ALLOW", "BLOCK"], width=10)

        fields = [
            ("Direction", self.direction),
            ("Protocol", self.protocol),
            ("Port", self.port),
            ("Action", self.action)
        ]

        for i, (label, widget) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=0, column=i, padx=5)
            widget.grid(row=1, column=i, padx=5)

        ttk.Button(form, text="Add Rule", command=self.add_rule).grid(
            row=1, column=4, padx=10
        )

        self.table = ttk.Treeview(
            self.rules_tab,
            columns=("Direction", "Protocol", "Port", "Action"),
            show="headings"
        )

        for col in self.table["columns"]:
            self.table.heading(col, text=col)

        self.table.pack(fill="both", expand=True, padx=10, pady=10)
        self.refresh_table()

    # ---------------- LOGIC ----------------
    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for rule in load_rules():
            self.table.insert("", "end", values=(
                rule["direction"],
                rule["protocol"],
                rule["port"],
                rule["action"]
            ))

    def add_rule(self):
        try:
            rule = {
                "direction": self.direction.get(),
                "protocol": self.protocol.get(),
                "port": int(self.port.get()),
                "action": self.action.get()
            }
            add_rule(rule)
            self.refresh_table()
            messagebox.showinfo("Success", "Firewall rule added")
        except ValueError:
            messagebox.showerror("Error", "Invalid port number")
