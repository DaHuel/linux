import os
import sys
import time


def write_log(message, it_counter, file):
    file.write("iteration counter: " + str(it_counter) + "\n")
    i = 0
    while i < it_counter:
        file.write(str(i) + ' ' +  message + "\n")
        time.sleep(1)
        i = i + 1
    file.close()
    return 0


def make_fork(message, n, it):
    file = open('/root/Utils/log.txt', 'w')
    for i in n:
        new_proc = os.fork()
        if new_proc == 0:
            write_log(message, int(i) + 1, file)
            break
        else:
            if int(i) + 1 == it:
                os.wait(0)
    return 0


def main():
    for arg in sys.argv:
        if len(sys.argv) < 4 or len(sys.argv) > 4:
            print("usage: python3 main.py message proc_count iteration_count")
            exit()
        else:
            make_fork(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
