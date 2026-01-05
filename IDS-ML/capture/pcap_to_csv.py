import subprocess

def pcap_to_csv(pcap_file, output_csv):
    cmd = [
        "tshark", "-r", pcap_file,
        "-T", "fields",
        "-e", "frame.len",
        "-e", "ip.proto",
        "-e", "tcp.srcport",
        "-e", "tcp.dstport",
        "-e", "tcp.flags",
        "-E", "header=y",
        "-E", "separator=,"
    ]
    with open(output_csv, "w") as f:
        subprocess.run(cmd, stdout=f)

if __name__ == "__main__":
    pcap_to_csv("traffic.pcap", "../data/raw/traffic.csv")
