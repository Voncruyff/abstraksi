from abc import ABC, abstractmethod

# Kelas abstrak
class Kendaraan(ABC):
    @abstractmethod
    def jumlah_roda(self):
        pass

    @abstractmethod
    def jenis_bahan_bakar(self):
        pass

    def deskripsi(self):
        return "Kendaraan adalah alat transportasi."

# Kelas konkret
class Mobil(Kendaraan):
    def jumlah_roda(self):
        return 4

    def jenis_bahan_bakar(self):
        return "Bensin atau Solar"

class Motor(Kendaraan):
    def jumlah_roda(self):
        return 2

    def jenis_bahan_bakar(self):
        return "Bensin"

# Contoh penggunaan
mobil = Mobil()
motor = Motor()

print(mobil.deskripsi())  # Output: Kendaraan adalah alat transportasi.
print(f"Mobil: {mobil.jumlah_roda()} roda, bahan bakar: {mobil.jenis_bahan_bakar()}")
# Output: Mobil: 4 roda, bahan bakar: Bensin atau Solar

print(f"Motor: {motor.jumlah_roda()} roda, bahan bakar: {motor.jenis_bahan_bakar()}")
# Output: Motor: 2 roda, bahan bakar: Bensin
