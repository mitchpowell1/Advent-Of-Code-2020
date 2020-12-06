import re


def main():
    with open('input.txt', 'r') as f:
        groups = re.compile(r'\n{2,}').split(f.read())

        total1 = 0
        total2 = 0
        for group in groups:
            group_sets = [set(line) for line in group.split('\n')]
            total1 += len(set.union(*group_sets))
            total2 += len(set.intersection(*group_sets))

        print(total1)
        print(total2)


if __name__ == '__main__':
    main()