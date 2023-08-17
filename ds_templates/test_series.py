import time
import traceback as tb


def test_series(func, test_list):
    print(f'\"{func.__name__}\" Results')
    print('______________________________\n')

    for i, case in enumerate(test_list):
        try:
            actual_output = func(**case['input'])
            result = 'PASS' if actual_output == case['output'] else 'FAIL'

        except Exception:
            result, actual_output = 'ERROR', None
            tb_str = tb.format_exc()

        finally:
            print(f'Test Case {i + 1}: {result}')
            print(f"\nInput: {case['input']}")
            print(f"Expected Output: {case['output']}")
            print(f'Actual Output: {actual_output}\n')
            if result == 'ERROR':
                print(f'\033[91m{tb_str}\033[0m')

def test_case(func, test_list, case_num):
    print(f'\"{func.__name__}\" Results')
    print('______________________________\n')

    case = test_list[case_num-1]
    try:
        actual_output = func(**case['input'])
        result = 'PASS' if actual_output == case['output'] else 'FAIL'

    except Exception:
        result, actual_output = 'ERROR', None
        tb_str = tb.format_exc()

    finally:
        print(f'Test Case {case_num}: {result}')
        print(f"\nInput: {case['input']}")
        print(f"Expected Output: {case['output']}")
        print(f'Actual Output: {actual_output}\n')
        if result == 'ERROR':
            print(f'\033[91m{tb_str}\033[0m')


def compare_runtimes(inputs, test_runs: int=1000, *functions):
    runtimes = {}
    for func in functions:
        start = time.time()
        for _ in range(test_runs):
            func(*inputs)
        duration = time.time() - start
        runtimes[func.__name__] = duration
        print(f'{func.__name__} duration: {duration:.5f} s')
