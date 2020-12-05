import re


def empty_passport():
    fields = [
        ('byr', True, lambda v: re.match(r'^(19[2-9]\d|200[0-2])$', v)),
        ('iyr', True, lambda v: re.match(r'^(201\d|2020)$', v)),
        ('eyr', True, lambda v: re.match(r'^(202\d|2030)$', v)),
        ('hgt', True, lambda v: re.match(r'^((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$', v)),
        ('hcl', True, lambda v: re.match(r'^#[a-f0-9]{6}$', v)),
        ('ecl', True, lambda v: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', v)),
        ('pid', True, lambda v: re.match(r'^\d{9}$', v)),
        ('cid', False, lambda v: True),
    ]
    return {
        key: {'value': None, 'required': required, 'isValid': validator}
        for key, required, validator in fields
    }


def build_passport(data_blob):
    passport = empty_passport()
    k_v_pairs = [dp.split(':') for dp in data_blob]
    for key, value in k_v_pairs:
        passport[key]['value'] = value
    return passport


def is_passport_valid_1(passport):
    for key in passport:
        if passport[key]['required'] and passport[key]['value'] is None:
            return False
    return True


def is_passport_valid_2(passport):
    for key in passport:
        if passport[key]['required'] and passport[key]['value'] is None\
                or not passport[key]['isValid'](passport[key]['value']):
            return False
    return True


def process_passport_lines(raw_file_input):
    blobs = re.compile(r'\n{2,}').split(raw_file_input)
    processed_blobs = [re.compile(r'\s+').split(blob) for blob in blobs]
    return [build_passport(blob) for blob in processed_blobs]


def main():
    with open('input.txt', 'r') as file:
        raw_passport_input = file.read()

    passports = process_passport_lines(raw_passport_input)
    print(sum(is_passport_valid_1(ppt) for ppt in passports))
    print(sum(is_passport_valid_2(ppt) for ppt in passports))


if __name__ == '__main__':
    main()
