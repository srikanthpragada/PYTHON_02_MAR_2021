import threading
from threading import Thread


def print_numbers():
    ct = threading.current_thread()
    for n in range(1, 11):
        print(f"{ct.name} - {n}")


print(threading.current_thread())
ct = Thread(target=print_numbers)
ct.name = "PrintThread"
ct.start()
print(f"No. of threads : {threading.active_count()}")
print_numbers()
