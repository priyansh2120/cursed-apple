# initialize.py
from db.connector import init 

if __name__ == "__main__":
    index = init()
    print("Initialization complete.")
