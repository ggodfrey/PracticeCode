import time
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
states = [i.lower() for i in states]
words = [line.strip() for line in open("words.txt", "r")]
freq = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split()
#words = ['Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Ntrogen','Oxygen','Fluorine','Neon','Sodium','Magnesium','Aluminum','Silicon','Phosphorus','Sulfur','Chlorine','Argon','Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt','Nickel','Copper','Zinc','Gallium','Germanium','Arsenic','Selenium','Bromine','Krypton','Rubidium','Strontium','Yttrium','Zirconium','Niobium','Molybdenum','Technetium','Ruthenium','Rhodium','Palladium','Silver','Cadmium','Indium','Tin','Antimony','Tellurium','Iodine','Xenon','Cesium','Barium','Lanthanum','Cerium','Praseodymium','Neodymium','Promethium','Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium','Hafnium','Tantalum','Tungsten','Rhenium','Osmium','Iridium','Platinum','Gold','Mercury','Thallium','Lead','Bismuth','Polonium','Astatine','Radon','Francium','Radium','Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium','Berkelium','Californium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium','Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadtium','Roentgenium','Copernicium','Flerovium','Livermorium']
words = [i.lower() for i in words]
start = time.time()
#end = filter(None, [word + " " + filter(None, [state if all([i not in state for i in word]) else '' for state in states])[0] if len(filter(None, [state if all([i not in state for i in word]) else '' for state in states]))==1 else '' for word in words])
#Above method takes 52 seconds or so on my current device

'''ans = []
for word in words:
    for state in states:
        for i in word:
            if i in state:
                break
        else:
            ans.append(word + " " + state)''' #This block takes 9.2 seconds

'''def sort_word(word):
    return [i for i in freq if i in word]
ans = []
for word in words:                  #This version attempts to search
    word = sort_word(word)          #By sorting each word in order
    t = []                          #Because I thought it might be faster
    for state in states:            #If it checked for the most likely word
        state = sort_word(state)    #Collisions first
        for i in word:              #...........
            if i in state:          #This takes 73 seconds. Oh well
                break
        else:
            t.append(state)
    ans.append(t)'''

'''end = sorted(end, key=lambda i:len(i.split()[0]))
print end[:100]
print end[-100:]'''

'''answer = file("final.txt", "w") #UNCOMMENT TO SAVE
for i in end:
    answer.write(i)
    answer.write("\n")'''

def getstates(word):
    return filter(None, [state if all([i not in state for i in word]) else '' for state in states])
