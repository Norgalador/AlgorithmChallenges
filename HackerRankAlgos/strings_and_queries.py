# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
# sample String list: 4 ["aba", "baba", "aba", "xzxb"]
# sample Query list: 3 ["aba", "xzxb", "ab"]

def matchingStrings(strings, queries):
    matches = dict()
    results = []
    
    for query in range(len(queries)):
        if query in matches.keys():
            matches[query] = 0
        else:
            matches[query] = 0
        
        for string in strings:
            if string == queries[query]:
                matches[query] += 1
    for match in matches.values():
        results.append(match)
    return results
