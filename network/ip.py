import argparse
from IPy import IP


def init() -> argparse.Namespace:
    """
    Take care of args
    """
    parser = argparse.ArgumentParser(
        description="Compare IPs to check if they are in a certain CIDR or if they are in the same CIDR"
    )
    parser.add_argument("-c", "--cidr", help="A.B.C.D/N", required=True)
    parser.add_argument("ips", nargs="+", help="ip list to check")
    return parser.parse_args()


def check_ip() -> str:
    args = init()
    result = {}
    cidr = IP(args.cidr)
    for ip in args.ips:
        if IP(ip) in cidr:
            result[ip] = "yes"
        else:
            result[ip] = "no"
    return result


if __name__ == "__main__":
    print(check_ip())