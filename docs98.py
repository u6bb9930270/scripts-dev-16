# small utilities, no deps

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

if __name__ == "__main__":
    print(clamp(9, 0, 19))

# quick sketch
