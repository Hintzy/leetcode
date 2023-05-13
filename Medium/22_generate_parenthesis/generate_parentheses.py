"""
Given an integer 'n', write a function to generate all combinations of "well-formed" parentheses.  A well-formed
parentheses string is one where every close parenthesis is matched by an open parenthesis.

n is an integer from 1 to 8 (inclusive)

Cases:

1. n = 1
2. n = 8

Approach:

A recursive function can be written that will produce every combination of open and closed parentheses with the amount
of open or closed parentheses equal to n.  The return string will therefor have a lenght of 2n.  A helper function can
be created that will verify if a combination of parenthesis is valid.  If at any point in concatenation, a string is
 determined to not be valid, the recursion is broken.  If a string meets two criteria, len == 2n and is_valid (helper)
 then the result list is appended and the function returns, ending the recursion for that branch of the recursion.

"""

def generate_parenthesis(n: int) -> list[str]:
    # start with an empty string which will be built up into strings of parentheses, and an empty list to store valid
    # solutions in
    start = ''
    res = []

    def currently_valid(a_str):
        # iterate through the string character by character seeing if the closed parentheses outnumber the open each
        # step of the way.  If at any point the closed outnumber the open, it's no longer a valid solution.
        i = 0
        while i < len(a_str) + 1:
            if a_str[:i].count(')') > a_str[:i].count('('):
                return False
            i += 1
        return True

    def is_valid(a_str):
        # a final check to see if the amount of opens match the amount of closed.  If it's passed currently valid, and
        # in the end also has equal amounts of each, then the string is a valid solution
        if a_str.count(')') == a_str.count('('):
            return True
        return False

    def recurse(a_str):
        # recursively builds all potential combinations of opens and closed parentheses
        # if at any point a string is no longer valid, ends the recursion of that solution
        if not currently_valid(a_str):
            return

        # if length 2n has been reached and the solution is also equal amounts of closed and open, it's a valid solution
        # append the results list and end recursion by returning
        if len(a_str) == n * 2 and is_valid(a_str):
            res.append(a_str)
            return

        # if length 2n has been reached but wasn't tagged as valid, end the recursion
        elif len(a_str) == n * 2:
            return

        # if length 2n hasn't been reached yet and the string hasn't been flagged as not valid, recurse to build the
        # next two possible characters
        recurse(a_str + '(')
        recurse(a_str + ')')

    # call the recursion on the empty starting string and return the results list
    recurse(start)
    return res

print(generate_parenthesis(8))



