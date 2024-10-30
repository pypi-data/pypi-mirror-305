from function import visualize_roi
import sys


cofactor=input("Saisir le cofacteur appliquer dans la transformation Arcsinh: ")
thresh=input("Saisir le seuil: ")
kernel=input("Saisir la taille du kernel: ")
path=input("Saisir le chemin d'acces du dossier crée: ")
path_raw=input("Saisir le chemin d'acces du dossier contenant les images brutes: ")


visualize_roi(int(cofactor),int(thresh),int(kernel),path,path_raw)
