import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print(f"Seraching for pattern {pat}")
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = 'aaabbb..abab..aaaaab.abbaa.aaab'

test_pattern = ['ab*']

multi_re_find(test_pattern,test_phrase)