import re

from utils.input_reader import read_file


def has_abba(string: str) -> bool:
    n = len(string)
    for i in range(n - 3):
        if string[i] != string[i + 1] and string[i] == string[i + 3] and string[i + 1] == string[i + 2]:
            return True
    return False


def has_aba(string: str) -> bool:
    n = len(string)
    for i in range(n - 2):
        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            return True
    return False


def find_babs(string: str) -> list:
    n = len(string)
    babs = []
    for i in range(n - 2):
        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            babs.append(string[i:i + 3])
    return babs


def support_TLS(ip_address: str) -> bool:
    """
    Tricky regex situation
    [^...] is a negated set, it matches any char that is not inside the set
    [^]]+ matches one more characters that are not a closing square bracket
    So the pattern r"\[([^]]+)]" matches string within []
    And then we split the original string by [...]
    This means, every other item in the splitted list will be either in [] or not in []
    """
    splits = re.split(r"\[([^]]+)]", ip_address)

    if ip_address[0] == "[":
        # every even item is hypernet and mush not contain ABBA, and just one of odd items must contain ABBA
        for i in range(0, len(splits), 2):
            if has_abba(splits[i]):
                return False
        for i in range(1, len(splits), 2):
            if has_abba(splits[i]):
                return True
    else:
        # every odd item is hypernet and mush not contain ABBA, and just one of even items must contain ABBA
        for i in range(1, len(splits), 2):
            if has_abba(splits[i]):
                return False
        for i in range(0, len(splits), 2):
            if has_abba(splits[i]):
                return True

    return False


def support_SSL(ip_address: str) -> bool:
    splits = re.split(r"\[([^]]+)]", ip_address)
    if ip_address[0] == "[":
        # every even item is hypernet and just one of them needs to contain BAB,
        # every odd item is supernet and just one of them needs to contain corresponding ABA
        for i in range(0, len(splits), 2):
            babs = find_babs(splits[i])
            for bab in babs:
                aba = bab[1] + bab[0] + bab[1]
                for j in range(1, len(splits), 2):
                    if aba in splits[j]:
                        return True

    else:
        # every odd item is hypernet and just one of them needs to contain BAB,
        # every even item is supernet and just one of them needs to contain corresponding ABA
        for i in range(1, len(splits), 2):
            babs = find_babs(splits[i])
            for bab in babs:
                aba = bab[1] + bab[0] + bab[1]
                for j in range(0, len(splits), 2):
                    if aba in splits[j]:
                        return True
    return False


def support_TLS_count(raw_input: str) -> int:
    ips = raw_input.split("\n")
    count = 0
    for ip in ips:
        count += 1 if support_TLS(ip) else 0
    return count


def support_SSL_count(raw_input: str) -> int:
    ips = raw_input.split("\n")
    count = 0
    for ip in ips:
        count += 1 if support_SSL(ip) else 0
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of IPs that support TLS: {support_TLS_count(file)}")
    print(f"Number of IPs that support SSL: {support_SSL_count(file)}")
