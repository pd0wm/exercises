#!/usr/bin/env python3
import re

def expand_rule(rules, rule, part2):
    result = ""
    for r in rule.split(" "):
        if r.isdigit():
            n = int(r)
            if n == 8 and part2:
                result += "(" + expand_rule(rules, rules[42], part2) + ")+"
            elif n == 11 and part2:
                result += "(" + expand_rule(rules, rules[42], part2) + "){" + str(part2) + "}"
                result += "(" + expand_rule(rules, rules[31], part2) + "){" + str(part2) + "}"
            else:
                result += "(" + expand_rule(rules, rules[n], part2) + ")"
        else:
            if r.startswith('"') and r.endswith('"'):
                result += r[1]
            else:
                result += r # ( or ) or )|(

    return result




if __name__ == "__main__":
    rules = {}

    with open('input_19') as f:
        for line in f:
            line = line.strip()

            if not line:
                break

            n, rule = line.split(": ")

            if '|' in rule:
                r = rule.split(' | ')
                rule = f'( {r[0]} )|( {r[1]} )'
            rules[int(n)] = rule


        # Parse messages
        messages = [l.strip() for l in f]

        solution_01 = 0
        r = expand_rule(rules, rules[0], 0)
        p = re.compile(r)

        for m in messages:
            if re.fullmatch(p, m) is not None:
                solution_01 += 1
        print(solution_01)

        solution_02 = 0
        for n in range(1, 50):
            r = expand_rule(rules, rules[0], n)
            p = re.compile(r)
            for m in messages:
                if re.fullmatch(p, m) is not None:
                    solution_02 += 1

        print(solution_02)
