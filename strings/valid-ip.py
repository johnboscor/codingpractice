#https://www.interviewbit.com/problems/valid-ip-addresses/
from ipaddress import ip_address
a = "25525511135"


def is_valid_ip(ip):
    # Splitting by "."
    ip = ip.split(".")
    # Checking for the corner cases

    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True

def restoreIpAddresses(A):
    lg = len(A)
    if lg > 12:
        return []
    B = []
    new = A
    for i in range(1, lg - 2):
        for j in range(i + 1, lg - 1):
            for k in range(j + 1, lg):
                new = new[:k] + '.' + new[k:]
                new = new[:j] + '.' + new[j:]
                new = new[:i] + '.' + new[i:]

                if is_valid_ip(new):
                    B.append(new)
                new = A

    return B

print(restoreIpAddresses(a))