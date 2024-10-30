import re

from testbed.schema import SWEbenchInstance
from testbed.swebench.test_spec import DIFF_MODIFIED_FILE_REGEX
from testbed.swebench.utils import load_swebench_instance, load_swebench_dataset


def check_test_file(instance: SWEbenchInstance):
    print("\n\nInstance", instance.instance_id)

    test_files = re.findall(DIFF_MODIFIED_FILE_REGEX, instance.test_patch)

    files = re.findall(DIFF_MODIFIED_FILE_REGEX, instance.patch)

    print("Testfiles", test_files)
    print("Files", files)


instances = load_swebench_dataset("princeton-nlp/SWE-bench_lite")

for instance in instances:
    check_test_file(instance)