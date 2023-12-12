def run_length_encode(data):
    encoded_data = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data.append((data[i - 1], count))
            count = 1
    encoded_data.append((data[-1], count))
    return encoded_data

def run_length_decode(encoded_data):
    decoded_data = []
    for symbol, count in encoded_data:
        decoded_data.extend([symbol] * count)
    return decoded_data

# Example usage
original_data = "aaabbcccccc"
encoded_data = run_length_encode(original_data)
decoded_data = run_length_decode(encoded_data)

print("Original data:", original_data)
print("Encoded data:", encoded_data)
print("Decoded data:", ''.join(decoded_data))
