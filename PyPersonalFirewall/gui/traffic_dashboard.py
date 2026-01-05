from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from core.traffic_monitor import TrafficMonitor

class TrafficDashboard:
    def __init__(self, parent, update_callback=None):
        self.monitor = TrafficMonitor()
        self.update_callback = update_callback

        self.fig = Figure(figsize=(6, 3))
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.in_data = []
        self.out_data = []

        self.update()

    def update(self):
        stats = self.monitor.get_stats()

        in_kb = stats["bytes_recv"] / 1024
        out_kb = stats["bytes_sent"] / 1024

        self.in_data.append(in_kb)
        self.out_data.append(out_kb)

        self.in_data = self.in_data[-20:]
        self.out_data = self.out_data[-20:]

        self.ax.clear()
        self.ax.plot(self.in_data, label="Incoming KB/s")
        self.ax.plot(self.out_data, label="Outgoing KB/s")
        self.ax.legend()
        self.ax.set_title("Live Network Traffic")

        self.canvas.draw_idle()

        if self.update_callback:
            self.update_callback(in_kb, out_kb)

        # 🔑 Schedule next update (DO NOT LOOP / SLEEP)
        self.canvas.get_tk_widget().after(1000, self.update)
