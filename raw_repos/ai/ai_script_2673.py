"""
Create a program to compute the checksum of a given data packet
"""

def compute_checksum(data_packet):
    checksum = 0
    for x in data_packet:
        checksum += x
    return checksum

if __name__ == '__main__':
    data_packet = [0xff, 0x0a, 0x1b, 0x3f]
    print(compute_checksum(data_packet))