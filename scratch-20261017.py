# small utilities, no deps

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

if __name__ == "__main__":
    print(clamp(7, 0, 4))

# works for now
