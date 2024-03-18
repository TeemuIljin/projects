import datetime

def laske_kulunut_aika(aloitusaika, lopetusaika):
    erotus = lopetusaika - aloitusaika
    kulunut_paivat = erotus.days
    kulunut_tunnit, kulunut_sekunnit = divmod(erotus.seconds, 3600)
    kulunut_minuutit, kulunut_sekunnit = divmod(kulunut_sekunnit, 60)
    print(f"Kulunut aika: {kulunut_paivat} päivää, {kulunut_tunnit} tuntia, {kulunut_minuutit} minuuttia, {kulunut_sekunnit} sekuntia.")

def laske_kestoaika(aloitusaika, kesto):
    lopetusaika = aloitusaika + datetime.timedelta(seconds=kesto)
    return lopetusaika

if __name__ == "__main__":
    aloitusaika_str = input("Syötä aloitusaika (muodossa YYYY-MM-DD HH:MM:SS): ")
    lopetusaika_str = input("Syötä lopetusaika (muodossa YYYY-MM-DD HH:MM:SS): ")

    aloitusaika = datetime.datetime.strptime(aloitusaika_str, "%Y-%m-%d %H:%M:%S")
    lopetusaika = datetime.datetime.strptime(lopetusaika_str, "%Y-%m-%d %H:%M:%S")

    laske_kulunut_aika(aloitusaika, lopetusaika)

    kesto_tunnit = int(input("Syötä keston tuntimäärä: "))
    kesto_minuutit = int(input("Syötä keston minuuttimäärä: "))
    kesto_sekunnit = int(input("Syötä keston sekuntimäärä: "))

    kesto = datetime.timedelta(hours=kesto_tunnit, minutes=kesto_minuutit, seconds=kesto_sekunnit)
    lopetusaika_kestoaika = laske_kestoaika(aloitusaika, kesto)
    print(f"Ajastettu lopetusaika keston mukaan: {lopetusaika_kestoaika}")
