def minsToTime(mins: int): # parveido minutes uz cilvekiem izlasamu laiku
    m_left = mins % 60
    h_left = int( (mins - m_left) / 60 )
    if m_left == 0:
        m_left = "00"
    return f"{h_left}:{m_left}" # matemātika ir grūta

class Filma():

    visas_filmas = []

    def __init__(self, name, start_time, run_time, day, min_vec): 
        self.name = name # movie name
        self.start_time = start_time # time in which the movie begins in minutes ( 16:00 = 960 minutes, 18:30 = 1100 minutes)
        self.run_time = run_time # movie runtime (in minutes)
        self.day = day # day of the week ( aka 1 - mon, 2 - tue, 3 - wed ... 7 - sun )
        self.min_vec = min_vec # cik vecam jabut lai varetu skatities filmu
        Filma.visas_filmas.append(self) # automatiski pievieno filmu iekš saraksta 'visas_filmas', kurs tiek lietots lai taja saglabatu visas filmas

    def __str__(self): # izmantojot filmu kaa variable print funkcija izdod actual filmas vardu nevis kkadu memory adresi
        sakums = minsToTime(self.start_time) # parvers doto laiku no minutem uz lasāmu formātu
        ret_val = str(f'{self.name}, plkst: {sakums}, diena: {self.day}, runtime: {self.run_time}m')
        return ret_val


    
filma1 = Filma("Bērni Internetā", 840, 113, 1, 12)
filma2 = Filma("Bērni Internetā", 840, 113, 2, 12)
filma3 = Filma("Bērni Internetā", 840, 113, 3, 12)
filma4 = Filma("Bērni Internetā", 840, 113, 4, 12)
filma5 = Filma("Bērni Internetā", 840, 113, 5, 12)
filma6 = Filma("Bērni Internetā", 1295, 113, 6, 12)
filma7 = Filma("Bērni Internetā", 1295, 113, 7, 12)
# visi "Bērni Internetā" seansi

filma8 = Filma("Dzelmes Briesmoņi", 1195, 164, 6, 18)
filma9 = Filma("Dzelmes Briesmoņi", 1195, 164, 7, 18)
# visi "Dzelmes Briesmoņi" seansi

filma10 = Filma("Cilvēkēdājs", 1110, 148, 1, 18)
filma11 = Filma("Cilvēkēdājs", 1110, 148, 2, 18)
filma12 = Filma("Cilvēkēdājs", 1110, 148, 3, 18)
filma13 = Filma("Cilvēkēdājs", 1110, 148, 4, 18)
filma14 = Filma("Cilvēkēdājs", 1110, 148, 5, 18)
filma15 = Filma("Cilvēkēdājs", 1110, 148, 6, 18)
filma16 = Filma("Cilvēkēdājs", 1110, 148, 7, 18)
# visi "Cilvēkēdājs" seansi

filma17 = Filma("Pokemons", 820, 105, 1, 18)
filma18 = Filma("Pokemons", 820, 105, 2, 18)
filma19 = Filma("Pokemons", 820, 105, 3, 18)
filma20 = Filma("Pokemons", 820, 105, 4, 18)
filma21 = Filma("Pokemons", 820, 105, 5, 18)
filma22 = Filma("Pokemons", 820, 105, 6, 18)
filma23 = Filma("Pokemons", 820, 105, 7, 18)

filma24 = Filma("Pokemons", 995, 105, 1, 18)
filma25 = Filma("Pokemons", 995, 105, 2, 18)
filma26 = Filma("Pokemons", 995, 105, 3, 18)
filma27 = Filma("Pokemons", 995, 105, 4, 18)
filma28 = Filma("Pokemons", 995, 105, 5, 18)
filma29 = Filma("Pokemons", 995, 105, 6, 18)
filma30 = Filma("Pokemons", 995, 105, 7, 18)
# visi "Pokemons" seansi

filma31 = Filma("Lielais noslēpums", 900, 144, 1, 12)
filma32 = Filma("Lielais noslēpums", 900, 144, 2, 12)
filma33 = Filma("Lielais noslēpums", 900, 144, 3, 12)
filma34 = Filma("Lielais noslēpums", 900, 144, 4, 12)
filma35 = Filma("Lielais noslēpums", 900, 144, 5, 12)
filma36 = Filma("Lielais noslēpums", 1080, 144, 6, 12)
filma37 = Filma("Lielais noslēpums", 1080, 144, 7, 12)
# visi "Lielais noslēpums" seansi

filma38 = Filma("Savvaļas karalis", 875, 144, 1, 1)
filma39 = Filma("Savvaļas karalis", 875, 144, 2, 1)
filma40 = Filma("Savvaļas karalis", 875, 144, 3, 1)
filma41 = Filma("Savvaļas karalis", 875, 144, 4, 1)
filma42 = Filma("Savvaļas karalis", 875, 144, 5, 1)
filma43 = Filma("Savvaļas karalis", 1130, 144, 6, 1)
filma44 = Filma("Savvaļas karalis", 1130, 144, 7, 1)
# visi "Savvaļas karalis" seansi


seansi_uz_kuriem_tiek = []

for filma in Filma.visas_filmas:
    if filma.min_vec <= 15: # vini nevar iet uz filmam kuras nav vini vecumam
        if filma.name != "Pokemons" and filma.day != 7: # Elvis šādos apstaklos netiek vai negrib
            beigu_laiks = filma.start_time + filma.run_time
            if beigu_laiks < 1320: # pec 22:00 (1320 minutes) vecaki nebrauks pakaļ
                seansi_uz_kuriem_tiek.append(filma)

print("Seansi, kuri atbilst nosacījumiem:")
for filma in seansi_uz_kuriem_tiek: # izprinte katru filmu kas ir saraksta
    print(filma)
