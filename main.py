print("Hello from repository!")
print("Wind.")

import os
from dotenv import load_dotenv

load_dotenv('secret_1.env')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()