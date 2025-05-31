from datetime import datetime

NOM = "djomo"
PRENOM = "carelle"
AGE = 30  

def generer_dictionnaire(nom, prenom, age):
    dictionnaire = []
    n, p = nom.lower(), prenom.lower()
    annee = datetime.now().year - age
    annees = [str(age), str(annee), str(annee)[-2:]]
    
    dictionnaire.extend([n, p, nom.upper(), prenom.upper()])
    dictionnaire.extend(annees)
    
    for info in [n, p]:
        for a in annees:
            dictionnaire.extend([info + a, a + info, info + "_" + a])
    
    dictionnaire.extend([n + p, p + n, n + "." + p])
    
    for base in [n, p]:
        for suf in ["123", "321", "!", "@", "12", "#"]:
            dictionnaire.extend([base + suf, suf + base])
    
    return sorted(list(set([m for m in dictionnaire if m and len(m) >= 3])))

def main():
    print("=== GÉNÉRATEUR DE DICTIONNAIRE ===")
    
    nom, prenom, age = NOM, PRENOM, AGE

    print(f"\nDonnées utilisées : {prenom} {nom}, {age} ans")
    print("Génération en cours...")
    dictionnaire = generer_dictionnaire(nom, prenom, age)
    
    fichier = f"dictionnaire_{nom.lower()}_{prenom.lower()}.txt"
    with open(fichier, 'w', encoding='utf-8') as f:
        for mot in dictionnaire:
            f.write(mot + '\n')
    
    print(f"\n✅ Fichier créé: {fichier}")
    print(f"🔢 Total: {len(dictionnaire)} mots de passe")

if __name__ == "__main__":
    main()
