#!/usr/bin/env python3

import resource

if __name__ == "__main__":
    rlimits = {
        "RLIMIT_AS": resource.RLIMIT_AS,
        "RLIMIT_CORE": resource.RLIMIT_CORE,
        "RLIMIT_CPU": resource.RLIMIT_CPU,
        "RLIMIT_DATA": resource.RLIMIT_DATA,
        "RLIMIT_FSIZE": resource.RLIMIT_FSIZE,
        "RLIMIT_MEMLOCK": resource.RLIMIT_MEMLOCK,
        "RLIMIT_MSQUEUE": resource.RLIMIT_MSGQUEUE,
        "RLIMIT_NICE": resource.RLIMIT_NICE,
        "RLIMIT_NOFILE": resource.RLIMIT_NOFILE,
        "RLIMIT_NPROC": resource.RLIMIT_NPROC,
        "RLIMIT_RSS": resource.RLIMIT_RSS,
        "RLIMIT_RTPRIO": resource.RLIMIT_RTPRIO,
        "RLIMIT_RTTIME": resource.RLIMIT_RTTIME,
        "RLIMIT_SIGPENDING": resource.RLIMIT_SIGPENDING,
        "RLIMIT_STACK": resource.RLIMIT_STACK,
    }

    for rlimit in rlimits:
        try:
            rlimit_data = resource.getrlimit(rlimits[rlimit])
        except Exception as e:
            print(f"{rlimit} => soft limit: N/A; hard limit: N/A")
        else:
            soft_limit, hard_limit = rlimit_data

            if soft_limit == resource.RLIM_INFINITY:
                soft_limit = "infinity"

            if hard_limit == resource.RLIM_INFINITY:
                hard_limit = "infinity"

            print(f"{rlimit} => soft limit: {soft_limit}; hard limit: {hard_limit}")
