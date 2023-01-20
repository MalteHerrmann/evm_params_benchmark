#!/usr/bin/python3
import os
import subprocess
import timeit
import sys


# Setup binary to call local host
os.system("evmosd config node http://localhost:26657")


def query_params():
    # os.system("evmosd q evm params")
    result = subprocess.call(
        "evmosd q evm params".split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result != 0:
        sys.exit("Call failed!")


duration = timeit.timeit(query_params, number=100)
print(f"Execution took: {duration} seconds")
