PATTERNS ={ 
    "AWS Access Key": r"\b(AKIA|ASIA)[0-9A-Z]{16}\b",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Slack Token": r"xox[bpr]-[a-zA-Z0-9-]{10,}",
    "Stripe (Secret Key)" : r"(?<prefijo>\bsk_live_)(?<resto>[0-9A-Za-z]{24,34})",
    "Github Token": r"\bghp_[A-Za-z0-9_]{36}\b"
} 
    
