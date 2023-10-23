from cmath import sqrt
import pandas as pd


def main():
    # Membaca data
    data = pd.read_csv(
        "European-Hotel-Data.csv", delimiter=";")
    # Mencari korelasi semua kolom dengan kolom tersebut
    koefisien_korelasi = []
# Perbandingan semua kolom dengan kolom tersebut
    for col1 in data.columns:
        for col2 in data.columns:
            # Mencari rata-rata
            rata_var1 = sum(data[col1]) / len(data[col1])
            rata_var2 = sum(data[col2]) / len(data[col2])

            # Mencari simpangan baku
            sigma_var1 = sqrt(
                sum((x - rata_var1)**2 for x in data[col1]) / len(data[col1]))
            sigma_var2 = sqrt(
                sum((x - rata_var2)**2 for x in data[col2]) / len(data[col2]))

            # Mencari koefisien korelasi
            r = (sum((data[col1][i] - rata_var1)*(data[col2][i] - rata_var2)
                     for i in range(len(data))) / len(data)) / (sigma_var1 * sigma_var2)

            print("Koefisien korelasi", col1,
                  "dengan", col2, ":", r)
            # Mencegah perbandingan sama sama kolom
            if col1 != col2:
                koefisien_korelasi.append((r, col1, col2))

    # Mencari korelasi paling kuat
    koefisien_korelasi.sort(key=lambda x: x[0], reverse=True)

    # Menampilkan korelasi paling kuat
    print("Korelasi paling kuat:")
    for r, col1, col2 in koefisien_korelasi[:1]:
        print(f" {col1} dengan {col2} dengan koefisien korelasi : {r:.2f}")


if __name__ == "__main__":
    main()
