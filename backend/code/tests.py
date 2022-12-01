from input_code import solution
import sys

test_cases = [{"Test1": [1, 2, 3], "Test2": [1, 2, 3] * 1000 + [4]},{"Test1": [1, 4, 3], "Test2": [2, 4] * 1000 + [3]}]
answers=[{ "Test1": 3,"Test2": 4},{ "Test1": 1,"Test2": 2}]

def get_test_cases(x):
    return test_cases[x]

def get_expected_outputs(x):
    return answers[x]


def test_code(x):
    test_cases = get_test_cases(x)
    expected = get_expected_outputs(x)
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = solution(test_cases[label])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases=label
            break

    print("Passed", passed_test_cases, "out of",
          test_cases_count, "test cases.")

    if failed_test_cases :
        print("\nTest cases not passed:", failed_test_cases)
        print("\n",test_cases[failed_test_cases])
        print("\n\nOutput: ",code_result)
        print("\nExpected: ",expected[failed_test_cases])

test_code(int(sys.argv[1]))
