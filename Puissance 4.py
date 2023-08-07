import pygame

#donné
colonne=6
ligne=7
x=y=0
jetonJaune=1
jetonRouge=-1
joueur=-1
victoireRouge=-4
victoireJaune=4
n=5
victoire = False
img = print("gagné")

def victoireDiagonal(tab,victoire):
    """
    entrée : la matrice
    sortie : jaune ou rouge gagne ou aucun
    """
    for i in range(3):
        for j in range(4):
            if tab[i][j] + tab[i+1][j+1] + tab[i+2][j+2] + tab[i+3][j+3] == victoireJaune:
                victoire = True
                return victoire



            if tab[i][j] + tab[i+1][j+1] + tab[i+2][j+2] + tab[i+3][j+3] == victoireRouge:
                victoire = True
                return victoire



    for i in range(6):
        for j in range(4):
            if tab[i][j] + tab[i-1][j+1] + tab[i-2][j+2] + tab[i-3][j+3] == victoireJaune:
                victoire = True
                return victoire

            if tab[i][j] + tab[i-1][j+1] + tab[i-2][j+2] + tab[i-3][j+3] == victoireRouge:
                victoire = True
                return victoire





def victoireHorizontal(tab,victoire):
    """
    entrée : la matrice
    sortie : jaune ou rouge gagne ou aucun
    """
    for i in range(3):
        for j in range(7):
            if tab[i][j]+tab[i+1][j] + tab[i+2][j] + tab[i+3][j] == victoireJaune:
                victoire = True
                return victoire

            if tab[i][j]+tab[i+1][j] + tab[i+2][j] + tab[i+3][j] == victoireRouge:
                victoire = True
                return victoire







def victoireVertical(tab,victoire):
    """
    entrée : la matrice
    sortie : jaune ou rouge gagne ou aucun
    """
    for i in range(6):
        for j in range(4):
            if tab[i][j]+tab[i][j+1]+tab[i][j+2]+tab[i][j+3] == victoireJaune:
                print("gagnant jaune")
                victoire = True
                return victoire
            if tab[i][j]+tab[i][j+1]+tab[i][j+2]+tab[i][j+3] == victoireRouge:
                print("gagnant rouge")
                victoire = True
                return victoire



surf = pygame.display.set_mode((800,600))
run = True
#matrice
tab=[[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],]



while run :
    if victoireDiagonal(tab,victoire)==True:
        surf.blit(img,(0,20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.flip()


    elif victoireHorizontal(tab,victoire)==True:
        surf.blit(img,(0,20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    elif victoireVertical(tab,victoire)==True:
        surf.blit(img,(0,20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



    else:



#plateau de jeu
        surf.fill((0,0,139))
        for i in range(colonne):
            for j in range(ligne):
             x=j*100+100
             y=i*100+50
             pygame.draw.circle(surf, (0,0,0), (x, y), 40,40)

    #afficher les pions

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0) :
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    x1=(pos[0]-50)//100
                    if x1<0:
                     x1=0
                    if x1>6:
                     x1=6
                    print(x1)

                    while tab[n][x1]!=0:
                     if n>0:
                        n-=1
                     else:
                        break
                    if tab[n][x1]==0:
                        tab[n][x1]=joueur
                        joueur=joueur*-1
                    n=5
        for i in range(y//50):
            for x1 in range(len(tab)):
                for y1 in range(len(tab)+1):
                    if tab[x1][y1]==-1:
                        pygame.draw.circle(surf,(200,0,0),(y1*100+100,x1*100+50),40,40)
                    elif tab[x1][y1]==1:
                        pygame.draw.circle(surf,(250,250,0),(y1*100+100,x1*100+50),40,40)
                    victoireDiagonal(tab,victoire)
                    victoireHorizontal(tab,victoire)
                    victoireVertical(tab,victoire)


        pygame.display.flip()
pygame.quit()






