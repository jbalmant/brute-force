import logging
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor
# from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(filename='c:/brute-force.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

CORES = 30

values = range(1, 100, 1)

wait = False


def mount(passwd, volume="D:", path="C:/Program Files (x86)/Jetico/BestCrypt Volume Encryption"):
    password = '{:0>8d}'.format(passwd)
    try:
        # while (wait):
        #     pass
        p = subprocess.Popen([path + "/bcfmgr.exe", "-Mount", volume, "-P" + password], shell=False)
        p.communicate()
    except:
        logging.error(f'retry {password}')
    return password


def main():
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=CORES) as executor:
        results = executor.map(mount, values)
        for result in results:
            if int(result) % (CORES * 10) == 0:
                logging.debug(result)

                # print('Calm down')
                #
                # global wait
                # wait = True
                # time.sleep(2)
                # wait = False

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
