"""Odds and ends."""

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(clamp(11, 0, 27))
