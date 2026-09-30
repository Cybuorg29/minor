import socket

def get_IPv6_address(domain_name):
    """
    Function to get the IPv6 address of a given domain name
    """

    # get the ip_addres
    ip_address = socket.getaddrinfo(domain_name, 0, socket.AF_INET6)

    # return the ip address
    return ip_address[0][4][0]