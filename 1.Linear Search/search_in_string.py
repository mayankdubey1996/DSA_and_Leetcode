def search_in_string(string, target):
    """
    Given the string, this function checks if the target character is in the
    string or not.
    ARGS:
        string -> str
        target -> str
    OUTPUT:
        BOOL 
    """
    if len(string) == 0:
        return False
    for i in range(len(string)):
        if string[i].lower() == target:
            return True
    return False

if __name__ == "__main__":
    string = "LeetCode"
    print("Eneter char you eant to search in: ",string)
    target = input().lower()
    ISpresent = search_in_string(string, target)
    
    print(ISpresent)
