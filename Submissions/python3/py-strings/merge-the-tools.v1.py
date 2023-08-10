def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        print("".join(dict.fromkeys(string[i:i+k])))
    # your code goes here

