import pandas as pd

tornado_data = pd.read_csv("./tornados.csv")

# 7 sor (1F)
# print(tornado_data[:7])
print(tornado_data.head(7))

# Milyen oszlopok találhatóak a datasetben? Jelenítsd meg az oszlopok nevét! (2F)
print(tornado_data.keys())

# Hány sor és hány oszlop van az adathalmazban? Jelenítsd meg ezeket az értékeket! (3F)
counted = tornado_data.shape
print(f"Rows: {counted[0]}, Columns: {counted[1]}")

# A továbbiakban a következő adatoszlopokra nem lesz szükség, ezeket töröld: stf, ns, sn, f1-f4 (4F)
cols_to_drop = ["stf", "ns", "sn", "f1", "f2", "f3", "f4"]
tornado_data.drop(cols_to_drop, axis=1, inplace = True)

print(tornado_data.keys())

# Jelenítsd meg, hogy államonként hány tornádó fordult elő! (5F)
states_by_data = tornado_data["st"].value_counts()
print(states_by_data)

# Szűrd le az adathalmazt úgy, hogy csak a Texas államban (TX) történt tornádókat jelenítse meg! (6F)
print((tornado_data[tornado_data["st"] == "TX"])["st"].value_counts())

# 7. Államonként készíts egy átlagos szélességi (slat és elat) és hosszúsági (slon és elon) fokot tartalmazó táblázatot, amely megmutatja, hogy az egyes államokban hol kezdődtek és hol végződtek a tornádók! (7F)
coords_by_state = tornado_data.groupby("st")[["slat", "elat", "slon", "elon"]].mean()
print(coords_by_state)

# 8. Államonként jelenítsd meg a tornádók hosszának (len) km-ben mért minimum, maximum és átlagos értékét! (1 km = 0.621371192 miles) (8F)
tornado_data["len_km"] = tornado_data["len"] / 0.621371192
length_by_state = tornado_data.groupby("st")["len_km"].agg(["min", "max", "mean"])
print(length_by_state)

# 9. Jelenítsd meg az év és a tornádók száma közötti összefüggést! Melyik évben történt a legtöbb tornádó az Egyesült Államokban? (9F)
tornados_by_year = tornado_data["yr"].value_counts().sort_index()
print(tornados_by_year)
max_year = tornados_by_year.idxmax()
print(f"A legtöbb tornádó az Egyesült Államokban {max_year}-ben történt ({tornados_by_year[max_year]} db).")

# 10. Évtől függetlenül jelenítsd meg a hónapok átlagos tornádószámait! Átlagosan melyik hónapban van a legtöbb tornádó? (10F)
monthly_avg = tornado_data["mo"].value_counts().sort_index() / tornado_data["yr"].nunique()
print(monthly_avg)
max_month = monthly_avg.idxmax()
print(f"Átlagosan a legtöbb tornádó a(z) {max_month}. hónapban van ({monthly_avg[max_month]:.2f} db).")

# 11. Hozz létre egy új oszlopot, amely a tornádó bekövetkezésének évszakát (dec-febr: tél, márc-máj: tavasz, jún-aug: nyár, szept-nov: ősz) adja meg. (11F)
season_map = {
    12: "tél", 1: "tél", 2: "tél",
    3: "tavasz", 4: "tavasz", 5: "tavasz",
    6: "nyár", 7: "nyár", 8: "nyár",
    9: "ősz", 10: "ősz", 11: "ősz"
}
tornado_data["evszak"] = tornado_data["mo"].map(season_map)
print(tornado_data[["mo", "evszak"]].head())

# 12. Melyik évszakban történt a legtöbb tornádó? (12F)
tornados_by_season = tornado_data["evszak"].value_counts()
print(tornados_by_season)
max_season = tornados_by_season.idxmax()
print(f"A legtöbb tornádó a(z) {max_season} évszakban történt ({tornados_by_season[max_season]} db).")


# Hány esetben rendelkezünk információval a tornádó intenzitásáról /mag/ és hány esetben nincs róla adatunk? (13F)
# print(tornado_data.)