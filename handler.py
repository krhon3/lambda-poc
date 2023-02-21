import logging
from multiprocessing import Process
import time
import requests
import json


logger = logging.getLogger(__name__)

url = "https://services.talma.com.pe:8015/srvTCMV/api/volantevalida"
headers = {"Content-type": "application/json"}

req_body = {
    "rugAgenteAduana": "20100246768",
    "listVolantes": [
        {"strvolante": "07681958"},
        {"strvolante": "07681959"},
        {"strvolante": "07681960"},
        {"strvolante": "076819635"},
        {"strvolante": "076819647"},
    ],
}

def process_function(index):
    response = requests.get(url, data=json.dumps(req_body), headers=headers)
    print("#" * 100)
    print(response.json())
    print(index)
    print("$" * 100)
    time.sleep(10)


def handler(event, context):
    start_time = time.perf_counter()

    processes = []
    # 3 procesos
    for index in range(3):
        x = Process(target=process_function, args=(index,))
        processes.append(x)
        x.start()
        
    for process in processes:
        process.join()

    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.info(f"...............Finished execution in {run_time:.4f} seg")
    return {
        "status_code": 200,
        "output": f"...............Finished execution in {run_time:.4f} seg",
    }

