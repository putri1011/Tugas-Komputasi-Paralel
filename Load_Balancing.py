# Load Balancing - Round Robin

servers = ["Server A", "Server B", "Server C"]

jumlah_request = int(input("Masukkan jumlah request: "))

print("\nHasil Load Balancing:\n")

for i in range(jumlah_request):
    server = servers[i % len(servers)]
    print(f"Request {i+1} -> {server}")