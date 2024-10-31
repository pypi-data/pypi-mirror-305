import time

def chrono_s(fonction):
    """Décorateur qui affiche le temps d'exécution d'une fonction en seconde."""
    def fonction_decoree(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution de {fonction.__name__}: {fin - debut:.6f} secondes")
        return resultat
    return fonction_decoree

def chronometrage(n=1):
    def decorateur(fonction):
        def fonction_decoree(*args, **kwargs):
            total_time = 0
            for _ in range(n):
                debut = time.time()
                resultat = fonction(*args, **kwargs)
                fin = time.time()
                total_time += (fin - debut)
            moyenne = total_time / n
            if n == 1:
                print(f"Temps d'exécution de {fonction.__name__}: {moyenne:.6f} secondes")
            else:
                print(f"Temps d'exécution moyen de {fonction.__name__} sur {n} essais : {moyenne:.6f} secondes")
            return resultat
        return fonction_decoree
    return decorateur