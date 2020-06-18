import logging
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from datetime import datetime

logging.basicConfig(filename='c:/bf-errors.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

CORES = 127
START = 1
END = 100
VOLUME = "E:"

values = range(START, END, 1)

wait = False


def mount(passwd, volume=VOLUME, path="C:/Program Files (x86)/Jetico/BestCrypt Volume Encryption"):
    password = '{:0>8d}'.format(passwd)
    try:
        if passwd % 10 == 0:
            message = f'{datetime.now()} - {password}'
            print(message)
            with open('c:/bf.log', 'a') as f:
                f.write(message + '\n')

        p = subprocess.Popen([path + "/bcfmgr.exe", "-Mount", volume, "-P" + password],
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate()

    except:
        logging.error(f'exception retry {password}')
    return password


def main():
    start_time = time.time()

    print(f"VOLUME {VOLUME} CPU {CORES} - START {START} - END {END} - {datetime.utcnow()}")

    with ThreadPoolExecutor(max_workers=CORES) as executor:
        executor.map(mount, values)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
