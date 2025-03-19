from typing import List

def longest_common_substring(strings: List[str]) -> str:
    if not strings:
        return ""
    
    shortest_string = min(strings, key=len)
    longest_substring = ""
    
    for i in range(len(shortest_string)):
        for j in range(i + 1, len(shortest_string) + 1):
            candidate = shortest_string[i:j]
            if all(candidate in s for s in strings):
                if len(candidate) > len(longest_substring):
                    longest_substring = candidate
    
    return longest_substring

def main():
    s1 = "apple building"
    s2 = "append building a big pen"
    strings = [s1, s2]
    lcs = longest_common_substring(strings)
    print(lcs)

if __name__ == "__main__":
    main()