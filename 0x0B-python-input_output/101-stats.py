#!/usr/bin/env python3
"""
101-stats.py is a program that reads IP logs from stdin and
prints metrics every ten lines or until EOF or Ctrl-C.
"""

import sys

def print_dict_sorted_nonzero(status_codes):
    """
    Print status codes with nonzero values in numerical order.

    Args:
        status_codes (dict): Dictionary of status codes and the
        number of times each one has been returned.
    """
    sorted_keys = sorted(status_codes.keys())
    print('\n'.join(["{:d}: {:d}".format(k, status_codes[k])
                     for k in sorted_keys if status_codes[k] != 0]))

if __name__ == "__main__":
    try:
        total = 0
        status_codes = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
        
        for n, line in enumerate(sys.stdin, 1):
            words = line.split()
            
            if len(words) >= 2:
                total += int(words[-1])
                status_code = int(words[-2])
                
                if status_code in status_codes:
                    status_codes[status_code] += 1

                if n % 10 == 0:
                    print("File size: {:d}".format(total))
                    print_dict_sorted_nonzero(status_codes)
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {:d}".format(total))
        print_dict_sorted_nonzero(status_codes)

