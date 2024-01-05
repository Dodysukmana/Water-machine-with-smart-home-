import time
import openpyxl

# Pin mapping
trig_pin = 5  # D1
echo_pin = 4  # D2
relay_pin = 14  # D5

def get_distance():
    # Simulasi fungsi get_distance karena modul machine tidak tersedia
    # Anda mungkin ingin menggunakan library seperti RPi.GPIO untuk mendukung GPIO di Python standar
    return 0

def read_excel_data(file_path, sheet_name, row_number, column_number):
    # Baca data dari file Excel
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = sheet.cell(row=row_number, column=column_number).value
    workbook.close()
    return data

file_path = 'data_air.xlsx'
sheet_name = 'Sheet1'  # Ganti dengan nama sheet yang sesuai
row_number = 2  # Ganti dengan nomor baris yang sesuai untuk jam
column_number = 1  # Ganti dengan nomor kolom yang sesuai untuk jam

while True:
    # Baca jarak dari sensor ultrasonik (simulasi)
    distance = get_distance()

    print("Distance:", distance)

    # Baca jam dari file Excel
    current_time = read_excel_data(file_path, sheet_name, row_number, column_number)
    print("Current Time:", current_time)

    # Sesuaikan nilai ini berdasarkan kebutuhan Anda
    threshold_low = 20.0  # Jarak rendah, nyalakan pompa
    threshold_high = 10.0  # Jarak tinggi, matikan pompa

    # Logika kontrol pompa
    if distance <= threshold_low:
        # Matikan pompa (simulasi)
        print("Pompa OFF")
    elif distance >= threshold_high:
        # Nyalakan pompa (simulasi)
        print("Pompa ON")
    else:
        # Jarak berada di antara threshold_low dan threshold_high
        # Tidak melakukan apa-apa, biarkan status pompa seperti sebelumnya
        pass

    time.sleep(1)  # Beri jeda untuk stabilitas
