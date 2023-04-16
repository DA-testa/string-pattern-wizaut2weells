# python3

def read_input():
    input_method = input()

    if 'I' in input_method:
        pattern = input().rstrip()
        string = input().rstrip()       

    elif 'F' in input_method:
        filename = input()     
        if 'a' in filename:    
            return
        with open(f"./tests/{filename}", mode="r") as file:
            pattern = file.readline().rstrip()
            string = file.readline().rstrip()
    else: 
        print('wrong input')
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, string)

def print_occurrences(output):
    # zon't touch this 
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    window_hash = hash(text[:pattern_len])
    result = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i+pattern_len]:
                result.append(i)
        if i < text_len - pattern_len:
            window_hash = hash(text[i+1:i+1+pattern_len])
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

