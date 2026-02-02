PATTERNS ={ 
    "AWS Access Key": r"(?P<prefijo>\b(AKIA|ASIA))(?P<resto>[0-9A-Z]{16}\b)",
    "Google API Key": r"(?P<prefijo>AIza)(?P<resto>[0-9A-Za-z\-_]{35})",
    "Slack Token": r"(?P<prefijo>xox[bpr]-)(?P<resto>[a-zA-Z0-9-]{10,})",
    "Stripe (Secret Key)" : r"(?P<prefijo>\bsk_live_)(?P<resto>[0-9A-Za-z]{24,34})",
    "Github Token": r"(?P<prefijo>\bghp_)(?P<resto>[A-Za-z0-9_]{36}\b)"
} 
    
