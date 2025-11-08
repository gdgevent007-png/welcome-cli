# utils.py

def compose(prefix: str, name: str, suffix: str = "") -> str:
    """
    Compose prefix and name. Ensure punctuation spacing is correct.
    """
    # avoid duplicate punctuation
    if suffix and suffix.startswith("!"):
        return f"{prefix}, {name}{suffix}"
    if suffix:
        return f"{prefix}, {name} {suffix}"
    return f"{prefix}, {name}"
