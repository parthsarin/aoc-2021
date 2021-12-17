"""
File: day-16.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from collections import namedtuple
from functools import reduce
from operator import mul
import pprint

DAY = 16
YEAR = 2021

DECODE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = ''.join(DECODE[ch] for ch in data)

Packet = namedtuple('Packet', ('version', 'type_id', 'payload', 'total_length'))

def parse_packet(data):
    if set(data) == {'0'}:
        return None, ''

    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)
    total_length = 6
    data = iter(data[6:])
    if type_id == 4:
        # literal value
        payload = ''
        while True:
            c = next(data)
            total_length += 1
            last_round = c == '0'
            
            for _ in range(4):
                total_length += 1
                payload += next(data)
            
            if last_round:
                break
        
        payload = int(payload, 2)
        o = Packet(version, type_id, payload, total_length)
        return o, ''.join(data)

    else:
        lti = int(next(data))
        total_length += 1
        if lti == 0:
            total_length += 15
            sp_length = ''.join(next(data) for _ in range(15))
            sp_length = int(sp_length, 2)

            sub_packets = []
            curr_len = 0
            while True:
                next_packet, data = parse_packet(''.join(data))

                total_length += next_packet.total_length
                curr_len += next_packet.total_length

                sub_packets.append(next_packet)
                if curr_len == sp_length:
                    break
                elif curr_len > sp_length:
                    raise ValueError(f'Subpacket length exceeded expected length: {sp_length=}, {curr_len=}')
            
            payload = sub_packets
            o = Packet(version, type_id, payload, total_length)
            return o, data

        elif lti == 1:
            total_length += 11
            nsp = ''.join(next(data) for _ in range(11))
            nsp = int(nsp, 2)

            sub_packets = []
            for _ in range(nsp):
                next_packet, data = parse_packet(''.join(data))
                if next_packet is None:
                    break

                sub_packets.append(next_packet)

                total_length += next_packet.total_length
            
            payload = sub_packets
            o = Packet(version, type_id, payload, total_length)
            return o, data
            
        else:
            raise ValueError(f'Invalid length type indicator: {lti}')


def sum_sub_vns(packet):
    if packet is None:
        return 0 

    vn = packet.version
    if vn is None:
        return 0
    if isinstance(packet.payload, list):
        return vn + sum(sum_sub_vns(p) for p in packet.payload)
    else:
        return vn

def test():
    t1 = '8A004A801A8002F478'
    packet, t1 = parse_packet(''.join(DECODE[ch] for ch in t1))
    print(packet, sum_sub_vns(packet))

    t2 = '620080001611562C8802118E34'
    packet, t2 = parse_packet(''.join(DECODE[ch] for ch in t2))
    print(packet, sum_sub_vns(packet))

    t3 = 'C0015000016115A2E0802F182340'
    packet, t3 = parse_packet(''.join(DECODE[ch] for ch in t3))
    print(packet, sum_sub_vns(packet))

    t4 = 'A0016C880162017C3686B18A3D4780'
    packet, t4 = parse_packet(''.join(DECODE[ch] for ch in t4))
    print(packet, sum_sub_vns(packet))


packet, _ = parse_packet(data)
ans_1 = sum_sub_vns(packet)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = ''.join(DECODE[ch] for ch in data)


def evaluate(packet):
    ti = packet.type_id
    if ti == 0:
        return sum(evaluate(p) for p in packet.payload)
    elif ti == 1:
        return reduce(mul, (evaluate(p) for p in packet.payload))
    elif ti == 2:
        return min(evaluate(p) for p in packet.payload)
    elif ti == 3:
        return max(evaluate(p) for p in packet.payload)
    elif ti == 4:
        return packet.payload
    elif ti == 5:
        a, b = packet.payload
        return int(evaluate(a) > evaluate(b))
    elif ti == 6:
        a, b = packet.payload
        return int(evaluate(a) < evaluate(b))
    elif ti == 7:
        a, b = packet.payload
        return int(evaluate(a) == evaluate(b))


def test2():
    i = [
        'C200B40A82',
        '04005AC33890',
        '880086C3E88112',
        'CE00C43D881120',
        'D8005AC2A8F0',
        'F600BC2D8F',
        '9C005AC2F8F0',
        '9C0141080250320F1802104A08'
    ]

    for packet in i:
        packet = ''.join(DECODE[ch] for ch in packet)
        packet, _ = parse_packet(packet)
        print(evaluate(packet))


packet, _ = parse_packet(data)
ans_2 = evaluate(packet)

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 16   00:43:17    971      0   01:10:48   1460      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)