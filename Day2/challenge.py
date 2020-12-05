"""
Parses a password policy string and yields a password policy dict
{
  num1: Integer
  num2: Integer
  char: Character
}
"""


def parse_password_policy(length_range: str, char_str: str):
    num1, num2 = length_range.split('-')
    char = char_str[0]

    policy = {
        'num1': int(num1),
        'num2': int(num2),
        'char': char
    }

    return policy


"""
Parses a line from the input file and returns a tuple containing a password policy and a password:
(password, password_policy)
"""


def parse_line(line: str):
    length_range, character, password = line.split(' ')
    policy = parse_password_policy(length_range, character)
    return password, policy


"""
Accepts a password policy and a password and returns a boolean indicating
whether or not the password is compliant with the policy according to the
rules in challenge part 1
"""


def is_password_compliant_1(password: str, policy: dict):
    compliance_char = policy['char']
    password_char_count = password.count(compliance_char)
    min_count = policy['num1']
    max_count = policy['num2']

    return min_count <= password_char_count <= max_count


"""
Accepts a password policy and a password and returns a boolean indicating
whether or not the password is compliant with the policy according to the
rules in challenge part 2
"""


def is_password_compliant_2(password: str, policy: dict):
    compliance_char = policy['char']
    # Policies are 1-indexed so positions must be converted to 0-indexed position
    pos_1 = policy['num1'] - 1
    pos_2 = policy['num2'] - 1

    # Check both positions for the character and XOR the two evaluations
    return (password[pos_1] == compliance_char) ^ (password[pos_2] == compliance_char)


def main():
    with open('input.txt', 'r') as file:
        pass_tuples = [parse_line(line) for line in file]

    compliance_count_1 = sum(is_password_compliant_1(*pass_tup) for pass_tup in pass_tuples)
    compliance_count_2 = sum(is_password_compliant_2(*pass_tup) for pass_tup in pass_tuples)

    print('Solution 1: {}'.format(compliance_count_1))
    print('Solution 2: {}'.format(compliance_count_2))


if __name__ == "__main__":
    main()
