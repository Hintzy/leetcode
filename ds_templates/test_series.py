if __name__ == '__main__':

    def test_series(func, test_list):
        for i, case in enumerate(test_list):
            try:
                if func(**case['input']) == case['output']:
                    print(f'Test Case {i + 1}: PASS')
                else:
                    print(f'Test Case {i + 1}: FAIL')
                print(f'Input: {case["input"]}')
                print(f'Expected Output: {case["output"]}')
                print(f'Actual Output: {func(**case["input"])}')

            except IndexError:
                print(f'Index error.')

            except KeyError:
                print(f'Key does not exist.')

            finally:
                pass