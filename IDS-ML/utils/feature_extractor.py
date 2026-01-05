def extract_features(packet):
    frame_len = len(packet)

    ip_proto = packet.proto if packet.haslayer("IP") else 0

    src_port = packet.sport if hasattr(packet, "sport") else 0
    dst_port = packet.dport if hasattr(packet, "dport") else 0

    # TCP flags (important)
    tcp_flags = packet.flags if packet.haslayer("TCP") else 0

    return [
        frame_len,
        ip_proto,
        src_port,
        dst_port,
        tcp_flags
    ]
