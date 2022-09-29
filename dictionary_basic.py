
### erstelle ein leeres Dictionary
dictionary1 = {}

### füge die Key-Value Paare x : 2^x hinzu
for i in range(1,11):
    dictionary1[i] = 2**i

### Variante: comprehension
dictionary2 = {key:2**key for key in range(1,11)}

print(dictionary1)
print(dictionary2)
###



### erstelle ein leeres Dictionary
occurrences = {}

### Für jeden Buchstaben im Satz (ohne leerzeichen)
for letter in "Simple is better than complex.Complex is better than complicated.".replace(' ',''):
    # wenn der Buchstabe schon im Dictionary ist:
    if letter in occurrences:
        # erhöhe den Wert an der Stelle des Buchstabens um 1 und mache beim nächsten Buchstaben weiter
        occurrences[letter] = occurrences[letter] + 1
        continue
    # setze den Wert an der Stelle des Buchstabens auf 1
    occurrences[letter] = 1

print(occurrences)

# suche den maximal Wert (key=occurrences.get -> sucht den Maximalwert der Values)
print(max(occurrences))

max_count = max(occurrences,key=occurrences.get)

print(max_count,occurrences[max_count])