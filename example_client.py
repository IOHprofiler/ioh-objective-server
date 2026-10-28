#!/usr/bin/env python3
import json
import iohservice

if __name__ == "__main__":
    import random
    import sys

    # the named pipes of the server (e.g. ./build/ioh-server -t integer -d 10 query reply)
    dimension = 10
    fquery, freply = sys.argv[1:3] if len(sys.argv) > 2 else ("query", "reply")

    for i in range(5):

        if i == 3:
            jq = json.dumps( {"query_type":"new_run"} )
            iohservice.query(jq, fquery, freply)
        
        sol = [random.randint(0,1) for j in range(dimension)]

        val = iohservice.call(sol, fquery, freply)
        print("f({}) = {}".format(sol,val))

    # Nicely ask the server to stop.
    print("Send an EXIT query...", file=sys.stderr, end="")
    jq = json.dumps( {"query_type":"stop"}, indent=4)
    iohservice.query(jq, fquery, freply)

