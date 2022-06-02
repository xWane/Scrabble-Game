# Fonction Scrabble

from random import *

def manche(point_global,tour):
  
  if tour == 3:  # si le nombre de tour est égale à 3 , alors la partie s'arrête et on affiche le nombre de points
    return fin_de_partie(point_global) 
  else:
    tour += 1 # on rajoute 1 tour au compteur a chaque fois
    liste_choisis = [] # liste vide qui sera remplis par les mots aléatoirement

    liste_mot = ["lait","mousse","clavier","chat","jour","livre","neige","tiroir","nuage","nuit","chien","carte","tour","table","sommet","boucle","tiramisu","trottoir","junior","noir","vert","verre","jaune","bleu","violet","rouge","jeu","million","milliard","soir","hiver","été","automne","printemps","jouet","lettre","porte","bureau","chaise","sourire","pile","haut","bas","eau","droite","gauche","larme"]
    nombre_de_mot = len(liste_mot) - 1 # on calcule le nombre de mot dans la liste moins 1 car il ne prend pas en compte l'indice 0

    mot1 = randint(0,nombre_de_mot) # choisis un nombre aléatoire entre 0  et le nombre de mot
    MOT1 = liste_mot[mot1] # choisis le mot dans la liste en fonction du raandint
    liste_choisis.append(MOT1) # rajoute le mot à la liste vide
    del liste_mot[mot1] # enleve le mot de la liste pour pas l'avoir une 2e fois

    mot2 = randint(0,nombre_de_mot - 1) # même chose
    MOT2 = liste_mot[mot2]
    liste_choisis.append(MOT2)
    del liste_mot[mot2]

    mot3 = randint(0,nombre_de_mot - 2) # même chose
    MOT3 = liste_mot[mot3]
    liste_choisis.append(MOT3)

    liste_lettre = list(liste_choisis[0]) + list(liste_choisis[1]) + list(liste_choisis[2]) # création de la liste avec les mots choisis
    liste_lettre_set = set(liste_lettre) # separation des mots pour avoir toute les lettres (mais n'est plus une liste [])
    liste_lettre_sans_doublon = list(liste_lettre_set) # met sous la forme de liste les lettre a cause de la fonctin set()
    random.shuffle(liste_lettre_sans_doublon) # mélange les lettres de façon aléatoire

    affichage_lettres ="".join(liste_lettre_sans_doublon) # affiche la liste sans les , et les []
    print( "Vous devez trouver les 3 mots cachés dans cette liste ,")
    print(" si vous ne trouvez pas tapez 'Quitter' pour passer à la prochaine manche .")
    print("  ")
    print(" Voici la liste de lettre : ",affichage_lettres)
    point = 0
    i = 0
    nombre_de_mot_choisis = len(liste_choisis) - 1 # on calcule le nombre de mot dans la liste choisis, on en aura besoin dans la fonction essaie
    return essaie(point,point_global,MOT1,MOT2,MOT3,tour,i,nombre_de_mot_choisis,liste_choisis) 

def essaie(point,point_global,MOT1,MOT2,MOT3,tour,i,nombre_de_mot_choisis,liste_choisis):

    if point == 3: # si les points de cette manche atteignent 3 la manche se termine et laisse la prochaine commencer
      print(" Vous avez trouvé les 3 mots . Bien joué ! ")
      print(" ")
      return manche(point_global,tour)

    else: # si le joueur n'a pas trouvé les 3 mots
      test_mot = input(" Alors , quel mot voulez-vous essayer ? ") 

      if test_mot == "Quitter": # passe la manche si vous faites quitter
        print(" Vous passez la manche .")
        print("  ")
        return manche(point_global,tour)

      elif test_mot == "/reveler": # commande cachée pour révéler la liste de mot
        print(liste_choisis)
        print(" ")
        return essaie(point,point_global,MOT1,MOT2,MOT3,tour,i,nombre_de_mot_choisis,liste_choisis)

      elif test_mot == "Terminer":
        return fin_de_partie(point_global)

      else: # si le joueur n'a pas utilisé les commande Quitter ou révéler et essaie un mot
        while i <= nombre_de_mot_choisis: # boucle qui vérifie si le mot est dans la liste , si oui il l'enlève de la liste pour éviter les doublons
          if test_mot == liste_choisis[i]:
            point += 1 # la variable point sert a calculer les points pour la manche en cours
            point_global += 1 # les points globaux sont les points qui seront affichés et le score total
            print("  ")
            print(" Bravo vous avez trouvé un mot ! Vous avez ",point_global," points .")
            print("  ")
            liste_choisis.remove(test_mot) # on enlève le mot
            nombre_de_mot_choisis -= 1 # et on baisse donc le nombre de mot dans la liste pour que la boucle ne compte pas d'indice n'existant plus
            i = 0 # et on remet a 0 le compteur
            return essaie(point,point_global,MOT1,MOT2,MOT3,tour,i,nombre_de_mot_choisis,liste_choisis)
            
          else: # on augmente le compteur pour verifier la présence du mot dans la liste si il n'est pas présent a l'indice[i]
            i += 1         
        else: # si le mot n'est pas présent dans la liste alors on relance juste la fonction
          i = 0
          print(" Le mot n'est pas dans la liste , réeesayer . ")
          print(" ")
          return essaie(point,point_global,MOT1,MOT2,MOT3,tour,i,nombre_de_mot_choisis,liste_choisis)



def fin_de_partie(point_global):
  print(" Fin de la partie , vous avez fais ",point_global," points .")

def commencement():    
  x = input(" Voulez-vous commencer ? (oui ou non) : ")
  print("   ") # les print vide sont juste la pour faire jolie et sauter des lignes 
  if x == "non":
    print(" Partie Terminée")
  elif x == "oui":
    point_global = 0
    tour = 0
    manche(point_global,tour)
  else:
    commencement()


def scrabble():

  print(" ")
  print("                                 ░██████╗░█████╗░██████╗░░█████╗░██████╗░██████╗░██╗░░░░░███████╗")
  print("                                 ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝")
  print("                                 ╚█████╗░██║░░╚═╝██████╔╝███████║██████╦╝██████╦╝██║░░░░░█████╗░░")
  print("                                 ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██║░░░░░██╔══╝░░")
  print("                                 ██████╔╝╚█████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗███████╗")
  print("                                 ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚══════╝")
  print(" ")

  print(" Voici les règles : la partie se joue en 3 manches , chaque manche peut apporter jusqu'à 3 points (pour un total de 9). ")
  print(" Le but du jeu est de trouver 3 mots caché dans une liste de lettre donné. La liste ne présente aucune lettre en doublon mais les mots peuvent eux")
  print(" avoir plusieurs fois la même lettre . Vous pouvez faire 'Quitter' pour passer à la prochaine manche ou faire 'Terminer' pour arrêter la partie , votre score sera")
  print(" alors directement affiché . (il existe également une fonction cachée : /reveler , qui vous donnera la liste des mots que vous n'avez pas trouvé)")
  print(" ")
  commencement()

