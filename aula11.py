notas1 = [7, 9, 10]
notas2 = [8, 6, 5]

soma_notas1 = 0
soma_notas2 = 0

for nota in notas1:
    soma_notas1 += nota 
for nota in notas2:
    soma_notas2 += nota  

media_notas1 = soma_notas1 / len(notas1)  
media_notas2 = soma_notas2 / len(notas2)  

print(f'A média do aluno 1 é {media_notas1}')
print(f'A média do aluno 2 é {media_notas2}')
