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

    instance_by_id = {instance["instance_id"]: instance for instance in instances}

    with open(f"report.csv", "w") as f:
        f.write("instance_id,resolved_by,startup_time,test_time,total_tests,failed_tests\n")
        for run in runs:
            resolved_by = instance_by_id[run["instance_id"]]["resolved_by"]

            f.write(f"{run['instance_id']},{len(resolved_by)},{run['startup_time']},{run['test_time']},{run['total_tests']},{run['failed_tests']}\n")

