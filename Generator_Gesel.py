import random
from tkinter import *
from winsound import *


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

play = lambda: PlaySound('zvok.wav', SND_FILENAME)
#vrstice 3-10 so kopirane iz interneta(dovoljeno z licenco)


def izhod():
    exit()


def odgovor():
    text = Label(master, text="42", fg="Grey", font=("Helvetica", 8))
    text.pack()
    #odgovor se skriva na dnu GUI-a


def prikazi_geslo():
    prikazano_geslo = Text(master, height=1, borderwidth=0, fg="MediumOrchid", font=("Helvetica", 24), bd=4,
             selectborderwidth=20
             )
    prikazano_geslo.insert(1.0, generiraj_geslo(TIP.get(), drsnik.get()))
    prikazano_geslo.pack(anchor=E)
    prikazano_geslo.configure(state="normal") # da uporabnik lahko notri še piše če mu geslo ni povsem všeč
    return prikazano_geslo


def generiraj_geslo(TIP, DOLZINA):
    števke = '0123456789'
    črke = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    števke_in_črke = števke + črke
    vsi_znaki = števke + črke + '“”‘’«»…°©®™•½¼¾⅓⅔№†‡µ¢£€♠♣♥♦✓✨�'           \
                                '×÷±∞π∅≤≥≠≈∧∨∩∪∈∀∃∄∑∏←↑→↓↵↔↕↖↗↘↙↺↻⇒⇔.'   \
                                '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁽⁾ⁿⁱ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎'                        \
                                'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'                    \
                                'αβγδεζηθικλμνξοπρστυφχψω'
                                #vključenih je zelo malo znakov, ampak je bistvo(cilj) dosežen
                                #znakov je cca 350, torej je kombinacij gesla == 350 ^ len(geslo)
    braille =       '⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟'\
                    '⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿'\
                    '⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟'\
                    '⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿'\
                    '⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟'\
                    '⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿'\
                    '⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟'\
                    '⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'
                    #nisem čisto prepričan, če je to res braillova pisava ampak izgleda že tako
    if TIP == 'Števila':
        TIP = števke
    if TIP == 'Črke':
        TIP = črke
    if TIP == 'Črke in Števila':
        TIP = števke_in_črke
    if TIP == 'Črke, Števila in Posebni_Znaki':
        TIP = vsi_znaki
    if TIP == 'Nemogoče Geslo':
        TIP = braille
    geslo = ''

    while len(geslo) < DOLZINA:
        geslo = geslo + random.choice(TIP)
    return geslo


# def shrani(datoteka, TIP = "Števila", DOLZINA = 10):
#     geslo = generiraj_geslo(TIP, DOLZINA)
#     with open(datoteka, "a") as dat:
#         print(str(geslo), file=dat)



#GUI
master = Tk()
master.title("Generator Gesel")
master.geometry('580x650')
master.resizable(width=True,height=True)
#master.configure(background='grey99')


menu = Menu()
master.config(menu=menu)

file = Menu(menu)
file.add_command(label="Zakaj ni več widgetov?", command = odgovor)
file.add_command(label="Izhod", command=izhod)
# file.add_command(label="Shrani", command=shrani("shranjeno_geslo.txt"))
menu.add_cascade(label="File", menu=file)

naslov = Label(master, text="Generator Gesel", fg="DarkOrchid4", font=("Helvetica", 32, "bold", "italic"))
naslov.pack()

dolzina = Label(master, text="Dolžina Gesla", font=("Helvetica", 24))
dolzina.pack()

drsnik = Scale(master, from_=0, to=32, orient=HORIZONTAL, length=32 * 10)
drsnik.pack()

vrsta = Label(master, text="\n" "Vrsta Gesla", font=("Helvetica", 24))
vrsta.pack()

TIP = StringVar()
Radiobutton(master, text="Števila", variable=TIP, value='Števila', font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Črke", variable=TIP, value="Črke", font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Črke in Števila", variable=TIP, value="Črke in Števila",
            font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Črke, Števila in Posebni Znaki", variable=TIP, value="Črke, Števila in Posebni_Znaki",
            font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Nemogoče Geslo", variable=TIP, value="Nemogoče Geslo",
            font=("Helvetica", 24)).pack(anchor=W)

generator = Button(master, text="Generiraj geslo", command=combine_funcs(play, prikazi_geslo), font=("Helvetica", 14))
generator.pack()


master.mainloop()