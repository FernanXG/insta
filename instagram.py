import os
if __name__ == "__main__":
        try:
                __import__("fernan").checkin()
        except Exception as e:
                exit(str(e))
