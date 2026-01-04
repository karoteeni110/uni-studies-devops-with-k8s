import random
import time
from datetime import datetime, timezone

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
RANDOM_STR = "".join(random.choice(ALPHABET) for _ in range(10))

def get_timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace(
        "+00:00", "Z"
    )

def get_log_line(random_str=RANDOM_STR):
    return f"{get_timestamp()}: {random_str}"


def main():
    log_line = get_log_line()
    print(log_line, flush=True)
    while True:
        time.sleep(5)
        log_line = get_log_line()
        print(log_line, flush=True)

if __name__ == "__main__":
    main()
