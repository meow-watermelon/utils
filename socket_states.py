#!/usr/bin/env python3

#ref.: https://github.com/torvalds/linux/blob/master/include/net/tcp_states.h
tcp_states = {
    '01': 'ESTABLISHED',
    '02': 'SYN_SENT',
    '03': 'SYN_RECV',
    '04': 'FIN_WAIT1',
    '05': 'FIN_WAIT2',
    '06': 'TIME_WAIT',
    '07': 'CLOSE',
    '08': 'CLOSE_WAIT',
    '09': 'LAST_ACK',
    '0A': 'LISTEN',
    '0B': 'CLOSING',
    '0C': 'NEW_SYN_RECV',
    '0D': 'MAX_STATES',
}

def get_socket_states(proc_filename):
    socket_states = {}

    try:
        with open(proc_filename, 'rt') as f:
            for line in f.readlines():
                cols = line.split()
                if cols:
                    state = cols[3]
                    if state in tcp_states:
                        if state in socket_states:
                            socket_states[tcp_states[state]] += 1
                        else:
                            socket_states[tcp_states[state]] = 1
    except Exception as e:
        print(e)

    return socket_states

if __name__ == '__main__':
    tcp = '/proc/net/tcp'
    tcp6 = '/proc/net/tcp6'

    # display IPv4 TCP socket states
    print('=== IPv4 TCP ===')
    for k,v in get_socket_states('/proc/net/tcp').items():
        print(f'{k}: {v}')
    print()

    # display IPv6 TCP socket states
    print('=== IPv6 TCP ===')
    for k,v in get_socket_states('/proc/net/tcp6').items():
        print(f'{k}: {v}')
    print()
