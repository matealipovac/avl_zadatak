import hashlib
import logging
import sys

logger = logging.getLogger(__name__)

def create_hash(hash_func, message):
    try:
        supported_algorithms = hashlib.algorithms_available
        if hash_func not in supported_algorithms:
            raise ValueError("Unsupported hash function:", hash_func)
        h = hashlib.new(hash_func)
        h.update(message.encode('utf-8'))
        return h.hexdigest()
    except Exception as e:
        print(f"An error occurred while hashing: {e}")
        return None

if __name__ == "__main__":
    input = sys.stdin.readlines()
    hash_func = input[0].strip()
    message = '\n'.join(input[1:]).strip()

    hashed_content = create_hash(hash_func, message)
    if hashed_content:
        print(f"Hash: {hashed_content}")
    else:
        print("Error: Hashing failed.")
        