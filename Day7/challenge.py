import re


def parse_bag_rule(rule):
    raw_container, raw_containing = rule.split('contain')

    container = raw_container.replace(' bags ', '')

    # Handle bags that contain no other bags
    if not re.match(r'^\d', raw_containing.strip()):
        return {
            'bag_type': container,
            'contained': {}
        }

    contained_strings = [
        re.sub(r' bags?\.?', '', contained).strip()
        for contained in raw_containing.split(', ')
    ]

    return {
        'bag_type': container,
        'contained': {
            ''.join(bag_type).strip(): int(count)
            for count, *bag_type in contained_strings
        }
    }


def part_one(rules, start_node='shiny gold'):
    nodes = [start_node]
    container_set = set()
    while len(nodes):
        for rule in rules:
            if nodes[0] in rule['contained'].keys():
                nodes.append(rule['bag_type'])
        container_set.add(nodes.pop(0))
    return len(container_set)


def part_two(rules, start_node='shiny gold'):
    rule = next(rule for rule in rules if rule['bag_type'] == start_node)
    if not rule['contained']:
        return 1

    return 1 + sum([
        rule['contained'][bag_type] * part_two(rules, bag_type)
        for bag_type in rule['contained']
    ])


def main():
    with open('input.txt', 'r') as f:
        rules = [parse_bag_rule(line) for line in f]

    print(part_one(rules))

    # Part two solution returns total number of bags but we are looking for the number inside the shiny gold
    # bag so subtract one here
    print(part_two(rules) - 1)


if __name__ == '__main__':
    main()
