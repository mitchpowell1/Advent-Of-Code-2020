import re
from functools import reduce

rule_regex = re.compile(r'(.+): (\d+-\d+) or (\d+-\d+)')


def parse_rule(rule):
    name, range1, range2 = rule_regex.match(rule).groups()
    r1_min, r1_max = range1.split('-')
    r2_min, r2_max = range2.split('-')
    return {
        'name': name,
        'values': set.union(
            set(i for i in range(int(r1_min), int(r1_max) + 1)),
            set(i for i in range(int(r2_min), int(r2_max) + 1))
        )
    }


def part_one(rules, tickets):
    all_values = reduce(set.union, [r['values'] for r in rules])
    return sum(v for t in tickets for v in t if v not in all_values)


def evaluate_field_order(rules, tickets):
    fields = [None for _ in tickets[0]]
    for i in range(len(tickets[0])):
        fields[i] = set([t[i] for t in tickets])

    potential_field_names = [
        set([r['name'] for r in rules if f.issubset(r['values'])])
        for f in fields
    ]

    resolved_field_names = set()
    while len(resolved_field_names) < len(fields):
        for p in potential_field_names:
            if len(p) == 1:
                (f, ) = p
                resolved_field_names.add(f)
            else:
                p.difference_update(resolved_field_names)

    final_field_names = [f for (f,) in potential_field_names]

    return final_field_names


def part_two(rules, tickets, my_ticket):
    all_values = reduce(set.union, [r['values'] for r in rules])
    valid_tickets = [t for t in tickets if all_values.issuperset(t)]
    field_order = evaluate_field_order(rules, valid_tickets)

    product = 1
    for i, f in enumerate(field_order):
        if f.startswith('departure'):
            product *= my_ticket[i]
    return product


def main():
    with open('input.txt', 'r') as f:
        rules, your_ticket, other_tickets = [line.split('\n') for line in re.split(r'\n{2,}', f.read())]

    rules = [parse_rule(r) for r in rules]
    tickets = [[int(val) for val in ticket.split(',')] for ticket in other_tickets[1:]]
    my_ticket = [int(val) for val in your_ticket[1].split(',')]

    print(part_one(rules, tickets))
    print(part_two(rules, tickets, my_ticket))


if __name__ == '__main__':
    main()