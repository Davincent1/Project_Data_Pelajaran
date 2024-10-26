import os
import random
import string
os.system("cls")# Win
print(f"{'Data Tentara ':-^50}")
data = dict()
while True:
    Kunci = "".join(random.choice(string.ascii_uppercase)for i in range(3))
    print(f"Kunci = {Kunci}")
    Nama = input("Nama Pelajaran\t:")
    Kelas = input("Kelas \t:")
    Jam = input("Jam\t:")
    Jawaban = input("Siapa yang mau mulai ikut Pelajaran iya atau tidak ").lower()
    data[Kunci] = {'Nama':Nama, 'Kelas':Kelas,'Jam': Jam }
    if Jawaban == 't':
        break
    elif Jawaban == 'y':
        continue
    

print("-"*40)
print(f"Key\t Nama\t Kelas\t Jam")
print("-"*40)
for k,v in data.items():
    print(f"{Kunci}.\t{data[Kunci]['Nama']}\t {data[Kunci]['Kelas']}\t \t{data[Kunci]['Jam']}")