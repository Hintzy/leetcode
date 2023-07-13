import time


def test_series(func, test_list):
    print(f'\"{func}\" Results')
    print('______________________________\n')

    for i, case in enumerate(test_list):
        try:
            if func(**case['input']) == case['output']:
                print(f'Test Case {i + 1}: PASS')
            else:
                print(f'Test Case {i + 1}: FAIL')
            print(f'\nInput: {case["input"]}')
            print(f'Expected Output: {case["output"]}')
            print(f'Actual Output: {func(**case["input"])}\n')


        except IndexError:
            print(f'Index error.')

        except KeyError:
            print(f'Key does not exist.')

        finally:
            pass


def compare_runtimes(inputs, *args):
    for func_name in args:
        start = time.time()
        func_name(inputs)
        duration = time.time() - start
        print(f'{func_name} duration: {duration} s')
