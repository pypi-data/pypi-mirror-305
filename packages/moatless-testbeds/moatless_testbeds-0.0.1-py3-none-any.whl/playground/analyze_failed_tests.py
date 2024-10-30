import json
import logging
import os

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

    if os.path.exists("tests.json"):
        with open("tests.json", "r") as f:
            runs = json.load(f)
    else:
        raise Exception("No tests.json file found")

    with open("/home/albert/repos/albert/swe-planner/moatless/benchmark/swebench_lite_all_evaluations.json", "r") as f:
        instances = json.load(f)

    instances_with_run = []
    for instance in instances:
        for run in runs:
            if run["instance_id"] == instance["instance_id"]:
                instance.update(run)
                instances_with_run.append(instance)
                break

    for run in instances_with_run:
        if run["failed_tests"] > 0 and run["instance_id"].startswith("pytest"):
            print(f"\n\n\nInstance {run['instance_id']} failed {run['failed_tests']} tests")
            print(f"Startup time: {run['startup_time']}")
            print(f"Test time: {run['test_time']}")
            print(f"Total tests: {run['total_tests']}")
            print(f"Failed tests: {run['failed_tests']}")

            for test in run["tests"]:
                if test["status"] in ["FAILED", "ERROR"]:
                    print(f"Test {test['name']} failed with status {test['status']}")
                    print(f"File: {test['file_path']}, Method: {test['method']}")
                    print(f"Logs: {test['failure_output']}")
                    print(f"---")

