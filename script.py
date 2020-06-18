import logging
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

from datetime import datetime

logging.basicConfig(filename='c:/brute-force.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

CORES = 127
START = 1
END = 100000000
VOLUME = "E:"

values = range(START, END, 1)

wait = False


def mount(passwd, volume=VOLUME, path="C:/Program Files (x86)/Jetico/BestCrypt Volume Encryption"):
    password = '{:0>8d}'.format(passwd)
    try:
        p = subprocess.Popen([path + "/bcfmgr.exe", "-Mount", volume, "-P" + password],
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate()

        #logging.error(f'err {stderr.decode("utf-8")} out {stdout.decode("utf-8")} rcode {p.returncode}')
    except:
        logging.error(f'exception retry {password}')
    return password


def main():
    start_time = time.time()

    print(f"VOLUME {VOLUME} CPU {CORES} - START {START} - END {END} - {datetime.utcnow()}")

    with ThreadPoolExecutor(max_workers=CORES) as executor:
        results = executor.map(mount, values)
        for result in results:
            if int(result) % (1000) == 0:
                logging.debug(result)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
