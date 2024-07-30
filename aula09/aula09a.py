frase = 'Curso em Video Python'
frase1 = '   Aprenda Python'

print(len(frase))
print(frase.count('o'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # Transforma para maiuscula somente a inicial de toda frase
print(frase.title()) # Transforma as iniciais de cada palavra em Maiuscula

# print(frase.split()) # Divide uma frase em pedaços a partir de espaços em branco encontrados
dividido = frase.split()
print(dividido[3])

print(frase1.strip()) # remove os espaços em branco antes e depois de uma frase

 