def bankers():
    processes = ["P0", "P1", "P2", "P3", "P4"]

    avail = [3, 3, 2]

    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    alloc = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    n = len(processes)
    m = len(avail)

    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(max_need[i][j] - alloc[i][j])
        need.append(row)

    finish = [False] * n
    safe_seq = []
    work = avail.copy()

    print("=== BANKER ===")

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    print(processes[i], "dieksekusi")
                    for j in range(m):
                        work[j] += alloc[i][j]
                    safe_seq.append(processes[i])
                    finish[i] = True
                    found = True

        if not found:
            print("Tidak safe")
            return

    print("Safe Sequence:", safe_seq)


def deadlock():
    print("\n=== DEADLOCK ===")

    processes = {
        "P1": {"holding": "R1", "waiting": "R2"},
        "P2": {"holding": "R2", "waiting": "R1"}
    }

    p1 = processes["P1"]
    p2 = processes["P2"]

    print("P1 pegang", p1["holding"], "menunggu", p1["waiting"])
    print("P2 pegang", p2["holding"], "menunggu", p2["waiting"])

    if p1["waiting"] == p2["holding"] and p2["waiting"] == p1["holding"]:
        print("Deadlock terjadi")
    else:
        print("Tidak deadlock")


bankers()
deadlock()