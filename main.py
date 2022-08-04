"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls': 1.48, 'bt': 134.01}
    hasil['pusat'] = 'Pusat gempa berada di darat 18 km barat laut Ransiki'
    hasil['dirasakan'] = 'DIrasakan (Skala MMI): II-III Manokwari'
    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal, {result['tanggal']}")
    print(f"Waktu, {result['waktu']}")
    print(f"Waktu, {result['waktu']}")
    print(f"Magnitudo, {result['magnitudo']}")
    print(f"Lokasi:, LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat, {result['pusat']}")
    print(f"Dirasakan, {result['dirasakan']}")



if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)