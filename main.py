import networkx as nx

def pagerank(sentence: str) -> dict:
    """
    Calculates PageRank scores for each character in the given sentence.
    
    Args:
    - sentence (str): The input sentence to calculate the PageRank scores for.
    
    Returns:
    - A dictionary containing the PageRank scores for each character in the input sentence.
    """
    # Remove spaces from the sentence
    sentence = sentence.replace(" ", "")
    
    # Build a directed graph with each character as a node and edges between adjacent characters
    graph = nx.DiGraph()
    for i in range(len(sentence)-1):
        graph.add_edge(sentence[i], sentence[i+1])
    
    # Calculate PageRank scores for each node in the graph
    return nx.pagerank(graph)


def sort_dict_by_values(d: dict) -> dict:
    """
    Sorts a dictionary in ascending order of values.
    
    Args:
    - d (dict): The input dictionary to be sorted.
    
    Returns:
    - A dictionary containing the same key-value pairs as the input dictionary, sorted in ascending order of values.
    """
    # Sort the dictionary by values and convert the resulting list of items back to a dictionary
    sorted_items = sorted(d.items(), key=lambda x: x[1])
    sorted_dict = {k: v for k, v in sorted_items}
    
    return sorted_dict


def char_frequency(string: str) -> dict:
    """
    Calculates the frequency of each character in the given string.
    
    Args:
    - string (str): The input string to calculate character frequency for.
    
    Returns:
    - A dictionary containing the frequency of each character in the input string.
    """
    # Remove spaces from the string
    string = string.replace(" ","")
    
    # Initialize an empty dictionary to hold character frequencies
    freq_dict = {}
    
    # Iterate over each character in the string and update the frequency count in the dictionary
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict


def huffman_code(pagerank_dict: dict) -> dict:
    """
    Generates a Huffman code for the given set of characters, based on their PageRank scores.
    
    Args:
    - pagerank_dict (dict): A dictionary containing the PageRank scores for each character.
    
    Returns:
    - A dictionary containing the Huffman code for each character in the input dictionary.
    """
    # Get the sorted list of characters by descending order of PageRank values
    chars = [item[0] for item in sorted(pagerank_dict.items(), key=lambda item: item[1], reverse=True)]

    # Initialize the code dictionary with empty strings for each character
    codes = {char: "" for char in chars}

    # Build the Huffman code by combining the two lowest frequency characters until only one is left
    while len(chars) > 1:
        # Get the two lowest frequency characters
        low_chars = chars[-2:]
        # Combine their codes
        for char in low_chars[0]:
            codes[char] = "0" + codes[char]
        for char in low_chars[1]:
            codes[char] = "1" + codes[char]
        # Remove the low frequency characters and add the combined character
        chars = chars[:-2] + [low_chars[0] + low_chars[1]]

    # Return the Huffman codes for each character
    return codes

def encode_string(string, huffman_code):
    """
    Encodes a given string using the provided Huffman encoding dictionary.

    Args:
    string (str): The string to be encoded.
    huffman_code (dict): A dictionary containing the Huffman encoding for each character.

    Returns:
    str: The encoded binary string.
    """
    string = string.replace(" ", "")  # Remove all spaces from the string
    encoded_string = ""  # Initialize the encoded string
    for char in string:
        encoded_string += huffman_code[char]  # Append the Huffman code for each character in the string to the encoded string
    return encoded_string


def decode_string(huffman_dict, encoded_str):
    """
    Decodes a given Huffman-encoded string using the provided Huffman encoding dictionary.

    Args:
    huffman_dict (dict): A dictionary containing the Huffman encoding for each character.
    encoded_str (str): The Huffman-encoded binary string.

    Returns:
    str: The decoded string.
    """
    decoded_str = ''  # Initialize the decoded string
    code = ''  # Initialize the Huffman code
    for bit in encoded_str:
        code += bit  # Append each bit of the Huffman-encoded string to the Huffman code
        for char, c in huffman_dict.items():
            if c == code:  # If the Huffman code matches the encoding for a character
                decoded_str += char  # Append the character to the decoded string
                code = ''  # Reset the Huffman code
                break  # Move on to the next bit of the Huffman-encoded string
    return decoded_str


def string_to_binary(string):
    """
    Converts a given string to its binary representation.

    Args:
    string (str): The string to be converted.

    Returns:
    str: The binary representation of the string.
    """
    string = string.replace(" ","")  # Remove all spaces from the string
    return ''.join(format(ord(char), '08b') for char in string)  # Use the 'ord' function to convert each character to its ASCII code, format it as a binary string with 8 digits, and concatenate all the binary strings into one.


def compression_ratio(orig, comp):
    """
    Calculates the compression ratio between the original and compressed strings.

    Args:
    orig (str): The original string.
    comp (str): The compressed string.

    Returns:
    float: The compression ratio (compressed size / original size).
    """
    return len(comp) / len(orig)  # Calculate the ratio of the length of the compressed string to the length of the original string.

if __name__ == '__main__':
    # read input text file
    with open('input.txt', 'r') as f:
        input_str = f.read()

    # get frequency dictionary
    freq_dict = char_frequency(input_str)

    # get huffman codes for frequency dictionary
    huffman_code_freq = huffman_code(freq_dict)

    # get encoded string using frequency dictionary huffman codes
    encoded_str_freq = encode_string(input_str, huffman_code_freq)

    # get compression ratio using frequency dictionary huffman codes
    compression_ratio_freq = compression_ratio(string_to_binary(input_str), encoded_str_freq)

    # get pagerank dictionary for the input string
    pagerank_dict = pagerank(input_str)

    # get huffman codes for pagerank dictionary
    huffman_code_pagerank = huffman_code(pagerank_dict)

    # get encoded string using pagerank dictionary huffman codes
    encoded_str_pagerank = encode_string(input_str, huffman_code_pagerank)

    # get compression ratio using pagerank dictionary huffman codes
    compression_ratio_pagerank = compression_ratio(string_to_binary(input_str), encoded_str_pagerank)

    # print compression ratios for both cases
    print("Compression ratio using frequency dictionary huffman codes:", compression_ratio_freq)
    print("Compression ratio using pagerank dictionary huffman codes:", compression_ratio_pagerank)