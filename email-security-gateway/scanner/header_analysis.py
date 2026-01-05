from email import message_from_string

def analyze_headers(raw_email):
    msg = message_from_string(raw_email)
    from_addr = msg.get('From', '')
    reply_to = msg.get('Reply-To', '')
    received = msg.get_all('Received', [])
    return {
        "from_reply_mismatch": bool(reply_to and from_addr not in reply_to),
        "received_hops": len(received)
    }