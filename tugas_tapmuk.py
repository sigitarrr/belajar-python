suhu = [28, 30, 32, 34]
curah_hujan = [200, 250, 300]

for s in suhu:
    for h in curah_hujan:
        hasil_panen = (s * 0.15) + (h * 0.08)

        print(f"Suhu: {s}°C | Curah hujan: {h} mm")
        print(f"Prediksi hasil panen: {hasil_panen:.2f} ton/hektar")
        print("-" * 40)
