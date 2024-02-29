chunk_size = 100  # Specify the size of each chunk in bytes

count = 1
with open('data.txt', 'r') as file:
    while True:
        # Read a chunk of data
        chunk = file.read(chunk_size)

        # Check if the chunk is empty, indicating the end of the file
        if not chunk:
            break

        # Process the chunk (replace this with your own logic)
        print(chunk)
        print('....................', count)
        count += 1