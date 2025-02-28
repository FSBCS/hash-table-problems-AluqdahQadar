def k_most_frequent(lst, k):
    if not lst:
        return []
    counts = {}
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return [i for i, _ in sorted(counts.items(), key=lambda x: x[1], reverse=True)][:k]