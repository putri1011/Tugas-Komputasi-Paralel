from multiprocessing import Pool

# Data berat badan manusia (kg)
berat_badan = [38, 52, 90, 67, 44, 81, 73, 100]

def cek_berat(data):

    nomor_orang, berat = data

    if berat < 45:
        status = "KURANG"

    elif berat <= 80:
        status = "IDEAL"

    else:
        status = "BERLEBIH"

    return f"Orang {nomor_orang} | Berat: {berat} kg -> {status}"


if __name__ == "__main__":

    print("=== ANALISIS BERAT BADAN ===")

    data_orang = list(enumerate(berat_badan))

    # Paralelisme Data
    with Pool() as p:
        hasil = p.map(cek_berat, data_orang)

    for h in hasil:
        print(h)