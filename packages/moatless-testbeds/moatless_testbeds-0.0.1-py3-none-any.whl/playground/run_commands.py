import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from testbed.client.manager import TestbedManager
from testbed.schema import TestStatus, SWEbenchInstance
from testbed.swebench.utils import load_swebench_dataset

manager = TestbedManager(namespace="testbed-dev")


failing_tests = []

INSTANCES_FAIL = [
    "sympy__sympy-18199",
    "matplotlib__matplotlib-24970",
    "django__django-10924",
    "django__django-12113",
    "django__django-12915",
    "django__django-13448",
    "django__django-15400",
    "matplotlib__matplotlib-22711",
    "matplotlib__matplotlib-23299",
    "matplotlib__matplotlib-25079",
    "pallets__flask-4045",
    "psf__requests-1963",
    "psf__requests-2148",
    "psf__requests-2674",
    "psf__requests-3362",
    "psf__requests-2317",
    "pydata__xarray-4493",
    "pylint-dev__pylint-7114",
    "pytest-dev__pytest-11143",
    "pytest-dev__pytest-11148",
    "psf__requests-863",
    "pytest-dev__pytest-5495",
    "pytest-dev__pytest-7373",
    "pytest-dev__pytest-7432",
    "pytest-dev__pytest-7490",
    "pytest-dev__pytest-8365",
    "pytest-dev__pytest-8906",
    "scikit-learn__scikit-learn-10949"
]


def run_tests_instance(instance: SWEbenchInstance):
    instance_id = instance.instance_id
    print(f"\nSetting up {instance_id}")
    watch = time.time()
    testbed = manager.create_testbed(instance_id, timeout=1200)
    testbed.wait_until_ready()
    startup_time = time.time() - watch

    watch = time.time()

    test_runs = {}

    test_files = testbed.test_spec.get_test_patch_files()
    for i, test_file in enumerate(test_files):
        print(f"Running tests from {test_file} ({i+1}/{len(test_files)})")
        test_status, test_output = testbed.run_tests([test_file])
        if not test_status:
            print(f"No tests found in {test_file}. Output:\n{test_output}")
            continue

        test_runs[test_file] = []
        for r in test_status:
            if not r.file_path:
                r.file_path = test_file

            if r.file_path != test_file:
                print(f"Warning: {instance_id} Test {r.name} has file_path {r.file_path} different from test_file {test_file}")

            test_runs[test_file].append(r.model_dump())

        test_path = test_file.replace("/", "_")
        with open(f"test_logs/{instance_id}__{test_path}.log", "w") as f:
            f.write(test_output)

    test_time = time.time() - watch

    manager.delete_testbed(testbed.testbed_id)

    all_tests = [test for tests in test_runs.values() for test in tests]
    failures = [test for test in all_tests if test["status"] in [TestStatus.FAILED, TestStatus.ERROR]]

    if failures:
        print(f"{len(failures)} out of {len(all_tests)} tests failed.")
    else:
        print(f"All {len(all_tests)} tests passed.")

    return {
        "instance_id": instance_id,
        "startup_time": startup_time,
        "test_time": test_time,
        "total_tests": len(all_tests),
        "failed_tests": len(failures),
        "tests": test_runs
    }

def generate_csv(runs):
    with open("test_results.csv", "w") as f:
        f.write("instance_id,startup_time,test_time,total_tests,failed_tests,errors\n")
        for run in runs:
            # flat map

            errors = [test for tests in run["tests"].values() for test in tests if test["status"] == "ERROR"]

            failures = [test for tests in run["tests"].values() for test in tests if test["status"] == "ERROR"]

            f.write(f"{run['instance_id']},{run['startup_time']},{run['test_time']},{run['total_tests']},{len(failures)},{len(errors)}\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

    if not os.path.exists("test_logs"):
        os.makedirs("test_logs")

    if os.path.exists("tests.json"):
        with open("tests.json", "r") as f:
            runs = json.load(f)
    else:
        runs = []
    print(f"Loaded {len(runs)} runs")
    generate_csv(runs)
    exit(0)

    filtered_runs = []
    for run in runs:
        if run["instance_id"] not in INSTANCES_FAIL:
            filtered_runs.append(run)

        runs = filtered_runs

    print(f"Filtered to {len(runs)} runs")

    instances = load_swebench_dataset(name="princeton-nlp/SWE-bench_Lite")

    instances_to_run = [instance for instance in instances if instance.instance_id not in [f["instance_id"] for f in runs if [test for tests in f["tests"].values() for test in tests]]]

    print(f"Running {len(instances_to_run)} out of {len(instances)} instances")

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_instance = {executor.submit(run_tests_instance, instance): instance for instance in instances_to_run}
        
        for future in as_completed(future_to_instance):
            instance = future_to_instance[future]
            try:
                run = future.result()
                runs.append(run)
                # Write results to JSON file after each completed run
                with open("tests.json", "w") as f:
                    json.dump(runs, f, indent=2)
                logging.info(f"Completed and saved results for {instance.instance_id}")
            except Exception as exc:
                logging.exception(f"{instance.instance_id} generated an exception")

    logging.info("All instances completed")
