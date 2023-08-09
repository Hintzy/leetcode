import time
import traceback as tb


def test_series(func, test_list):
    print(f'\"{func}\" Results')
    print('______________________________\n')

    for i, case in enumerate(test_list):
        try:
            result = func(**case['input'])
            if result == case['output']:
                print(f'Test Case {i + 1}: PASS')
            else:
                print(f'Test Case {i + 1}: FAIL')
            print(f"\nInput: {case['input']}")
            print(f"Expected Output: {case['output']}")
            print(f'Actual Output: {result}\n')

        except IndexError as error:
            print(f'Test Case {i + 1}: FAIL')
            print(f"\nInput: {case['input']}")
            print(f"Expected Output: {case['output']}")
            print(f'Actual Output: {error}', flush=True)
            tb.print_exc()

        except KeyError as error:
            print(f'Test Case {i + 1}: FAIL')
            print(f"\nInput: {case['input']}")
            print(f"Expected Output: {case['output']}")
            print(f'Actual Output: {error}', flush=True)
            tb.print_exc()

        finally:
            pass


def test_case(func, test_list, case_num):
    print(f'\"{func}\" Results')
    print('______________________________\n')

    case = test_list[case_num-1]
    try:
        result = func(**case['input'])
        if result == case['output']:
            print(f'Test Case {case_num}: PASS')
        else:
            print(f'Test Case {case_num}: FAIL')
        print(f"\nInput: {case['input']}")
        print(f"Expected Output: {case['output']}")
        print(f'Actual Output: {result}\n')

    except IndexError:
        print(f'Test Case {case_num}: FAIL')
        print(f"\nInput: {case['input']}")
        print(f"Expected Output: {case['output']}")
        print(f'Actual Output: ', flush=True)
        tb.print_exc()

    except KeyError as error:
        print(f'Test Case {case_num}: FAIL')
        print(f"\nInput: {case['input']}")
        print(f"Expected Output: {case['output']}")
        print(f'Actual Output: ', flush=True)
        tb.print_exc()

    finally:
        pass


def compare_runtimes(inputs, *args):
    for func_name in args:
        start = time.time()
        func_name(inputs)
        duration = time.time() - start
        print(f'{func_name} duration: {duration} s')
