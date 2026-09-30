def find_all_valid_ip_addresses(string):
    valid_ips = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if i+j+k == len(string):
                    ip_string = string[:i]+"."+string[i:i+j]+"."+string[i+j:i+j+k]+"."+string[i+j+k:]
                    if is_valid_ip_address(ip_string):
                        valid_ips.append(ip_string)
    return valid_ips

def is_valid_ip_address(ip_string):
    nums = ip_string.split(".")
    for num in nums:
        if (int(num) < 0 or int(num) > 255):
            return False
    return True