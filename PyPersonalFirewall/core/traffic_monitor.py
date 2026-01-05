import psutil
import time

class TrafficMonitor:
    def __init__(self):
        self.last = psutil.net_io_counters()
        self.last_time = time.time()

    def get_stats(self):
        now = time.time()
        current = psutil.net_io_counters()

        elapsed = now - self.last_time
        if elapsed <= 0:
            return {"bytes_recv": 0, "bytes_sent": 0}

        recv_rate = (current.bytes_recv - self.last.bytes_recv) / elapsed
        sent_rate = (current.bytes_sent - self.last.bytes_sent) / elapsed

        self.last = current
        self.last_time = now

        return {
            "bytes_recv": recv_rate,
            "bytes_sent": sent_rate
        }
