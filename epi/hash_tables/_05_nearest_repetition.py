def find_nearest_repetition(paragraph):
    word_latest_index = {}
    nearest_dist = float('inf')
    for idx, word in enumerate(paragraph):
        if word in word_latest_index:
            diff = idx - word_latest_index[word]
            word_latest_index[word] = idx
            if diff < nearest_dist:
                nearest_dist = diff                
        else:
            word_latest_index[word] = idx
    return nearest_dist if nearest_dist != float('inf') else -1

if __name__ == "__main__":
    text = "All work and no play makes for no work no fun and no results"
    paragraph = text.split()
    print "Text -", text
    print find_nearest_repetition(paragraph) 