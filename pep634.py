"""
PEP 634 - Structural Pattern Matching
=====================================================
Python 3.10+ | Par Sana

Le PEP 634 introduit le "pattern matching" structurel en Python,
similaire au switch/case d'autres langages, mais BEAUCOUP plus puissant !

Prérequis : Python 3.10 ou supérieur
Vérifier : python --version
"""

# =============================================================================
#  PARTIE 1 : Les bases - match/case simple
# =============================================================================

def exemple_1_basique():
    """Match simple sur des valeurs littérales"""
    print("\n" + "="*50)
    print("EXEMPLE 1 : Match basique")
    print("="*50)
    
    def get_status_message(code):
        match code:
            case 200:
                return "✅ OK - Succès"
            case 404:
                return "❌ Not Found - Page introuvable"
            case 500:
                return "🔥 Internal Server Error"
            case _:  # Le wildcard _ capture tout le reste
                return f"❓ Code inconnu: {code}"
    
    # Tests
    for code in [200, 404, 500, 418]:
        print(f"Code {code}: {get_status_message(code)}")


# =============================================================================
#  PARTIE 2 : Match avec capture de variables
# =============================================================================

def exemple_2_capture():
    """Capturer des valeurs dans des variables"""
    print("\n" + "="*50)
    print("EXEMPLE 2 : Capture de variables")
    print("="*50)
    
    def analyser_commande(commande):
        match commande.split():
            case ["quit"]:
                return "👋 Au revoir!"
            case ["hello", nom]:  # Capture 'nom'
                return f"👋 Bonjour {nom}!"
            case ["add", x, y]:   # Capture x et y
                return f"➕ Résultat: {int(x) + int(y)}"
            case ["send", destinataire, *message]:  # *message capture le reste
                return f"📧 Envoi à {destinataire}: {' '.join(message)}"
            case _:
                return "❓ Commande non reconnue"
    
    # Tests
    commandes = [
        "quit",
        "hello Sana",
        "add 5 3",
        "send client@email.com Votre commande est prête",
        "unknown command"
    ]
    
    for cmd in commandes:
        print(f"'{cmd}' → {analyser_commande(cmd)}")


# =============================================================================
#  PARTIE 3 : Match sur des séquences (listes, tuples)
# =============================================================================

def exemple_3_sequences():
    """Pattern matching sur des séquences"""
    print("\n" + "="*50)
    print("EXEMPLE 3 : Séquences (listes/tuples)")
    print("="*50)
    
    def analyser_point(point):
        match point:
            case (0, 0):
                return "📍 Origine"
            case (0, y):
                return f"📍 Sur l'axe Y à y={y}"
            case (x, 0):
                return f"📍 Sur l'axe X à x={x}"
            case (x, y):
                return f"📍 Point quelconque ({x}, {y})"
            case (x, y, z):
                return f"📍 Point 3D ({x}, {y}, {z})"
            case _:
                return "❌ Format invalide"
    
    # Tests
    points = [(0, 0), (0, 5), (3, 0), (2, 4), (1, 2, 3), "invalid"]
    for p in points:
        print(f"{p} → {analyser_point(p)}")


# =============================================================================
#  PARTIE 4 : Match sur des dictionnaires
# =============================================================================

def exemple_4_dictionnaires():
    """Pattern matching sur des dictionnaires (très utile pour les API!)"""
    print("\n" + "="*50)
    print("EXEMPLE 4 : Dictionnaires (JSON/API)")
    print("="*50)
    
    def traiter_requete(data):
        match data:
            case {"action": "login", "username": user, "password": pwd}:
                return f"🔐 Tentative de connexion: {user}"
            case {"action": "signup", "email": email, **reste}:
                return f"📝 Inscription avec email: {email}"
            case {"action": "order", "items": [premier, *autres]}:
                return f"🛒 Commande de {len(autres) + 1} articles, premier: {premier}"
            case {"error": msg}:
                return f"❌ Erreur: {msg}"
            case {}:
                return "📭 Requête vide"
            case _:
                return "❓ Format de requête inconnu"
    
    # Tests
    requetes = [
        {"action": "login", "username": "sana", "password": "secret123"},
        {"action": "signup", "email": "dev@senegal.sn", "nom": "Diallo"},
        {"action": "order", "items": ["laptop", "souris", "clavier"]},
        {"error": "Token expiré"},
        {},
        "pas un dict"
    ]
    
    for req in requetes:
        print(f"{req}")
        print(f"  → {traiter_requete(req)}\n")


# =============================================================================
#  PARTIE 5 : Match avec guards (conditions)
# =============================================================================

def exemple_5_guards():
    """Ajouter des conditions avec 'if' (guards)"""
    print("\n" + "="*50)
    print("EXEMPLE 5 : Guards (conditions)")
    print("="*50)
    
    def classifier_age(personne):
        match personne:
            case {"nom": nom, "age": age} if age < 0:
                return f"❌ Âge invalide pour {nom}"
            case {"nom": nom, "age": age} if age < 13:
                return f"👶 {nom} est un enfant"
            case {"nom": nom, "age": age} if age < 20:
                return f"🧑 {nom} est adolescent"
            case {"nom": nom, "age": age} if age < 60:
                return f"👨 {nom} est adulte"
            case {"nom": nom, "age": age}:
                return f"👴 {nom} est senior"
            case _:
                return "❌ Format invalide"
    
    # Tests
    personnes = [
        {"nom": "Amadou", "age": 8},
        {"nom": "Fatou", "age": 16},
        {"nom": "Moussa", "age": 35},
        {"nom": "Mariama", "age": 70},
        {"nom": "Bug", "age": -5},
    ]
    
    for p in personnes:
        print(f"{p} → {classifier_age(p)}")


# =============================================================================
#  PARTIE 6 : Match sur des classes (très puissant!)
# =============================================================================

def exemple_6_classes():
    """Pattern matching sur des objets/classes"""
    print("\n" + "="*50)
    print("EXEMPLE 6 : Classes et objets")
    print("="*50)
    
    from dataclasses import dataclass
    
    @dataclass
    class Point:
        x: float
        y: float
    
    @dataclass
    class Cercle:
        centre: Point
        rayon: float
    
    @dataclass
    class Rectangle:
        coin: Point
        largeur: float
        hauteur: float
    
    def calculer_aire(forme):
        import math
        match forme:
            case Cercle(centre=Point(x, y), rayon=r) if r > 0:
                aire = math.pi * r ** 2
                return f"🔵 Cercle en ({x},{y}), aire = {aire:.2f}"
            case Rectangle(coin=Point(x, y), largeur=l, hauteur=h) if l > 0 and h > 0:
                aire = l * h
                return f"🟦 Rectangle en ({x},{y}), aire = {aire:.2f}"
            case Cercle(rayon=r) if r <= 0:
                return "❌ Rayon invalide"
            case Rectangle() as rect if rect.largeur <= 0 or rect.hauteur <= 0:
                return "❌ Dimensions invalides"
            case _:
                return "❓ Forme non reconnue"
    
    # Tests
    formes = [
        Cercle(Point(0, 0), 5),
        Rectangle(Point(1, 1), 4, 3),
        Cercle(Point(0, 0), -1),
        "triangle"
    ]
    
    for forme in formes:
        print(f"{forme}")
        print(f"  → {calculer_aire(forme)}\n")


# =============================================================================
#  PARTIE 7 : Pattern OR (|) et AS
# =============================================================================

def exemple_7_or_as():
    """Combinaisons avec OR (|) et alias avec AS"""
    print("\n" + "="*50)
    print("EXEMPLE 7 : OR (|) et AS")
    print("="*50)
    
    def classifier_http_code(code):
        match code:
            case 200 | 201 | 204:  # OR pattern
                return "✅ Succès"
            case 301 | 302 | 307 | 308 as redirect_code:  # OR + AS
                return f"↪️ Redirection ({redirect_code})"
            case 400 | 401 | 403 | 404 as client_error:
                return f"⚠️ Erreur client ({client_error})"
            case 500 | 502 | 503 as server_error:
                return f"🔥 Erreur serveur ({server_error})"
            case int() as code if 100 <= code < 200:
                return f"ℹ️ Information ({code})"
            case _:
                return "❓ Code inconnu"
    
    # Tests
    codes = [200, 201, 301, 404, 500, 100, 999]
    for code in codes:
        print(f"HTTP {code}: {classifier_http_code(code)}")


# =============================================================================
#  PARTIE 8 : Cas pratique Django - Traitement de formulaires
# =============================================================================

def exemple_8_django_forms():
    """Cas pratique : validation de données de formulaire style Django"""
    print("\n" + "="*50)
    print("EXEMPLE 8 : Cas pratique - Validation de formulaire")
    print("="*50)
    
    def valider_inscription(data):
        """Simule une validation de formulaire d'inscription"""
        match data:
            # Cas complet valide
            case {
                "email": str() as email,
                "password": str() as pwd,
                "password_confirm": str() as pwd_confirm,
                "telephone": str() as tel,
                **extras
            } if "@" in email and len(pwd) >= 8 and pwd == pwd_confirm:
                return {
                    "status": "success",
                    "message": f"✅ Inscription valide pour {email}",
                    "extras": list(extras.keys()) if extras else None
                }
            
            # Email invalide
            case {"email": email, **rest} if "@" not in str(email):
                return {"status": "error", "field": "email", "message": "❌ Email invalide"}
            
            # Mot de passe trop court
            case {"password": pwd, **rest} if len(str(pwd)) < 8:
                return {"status": "error", "field": "password", "message": "❌ Mot de passe trop court (min 8 caractères)"}
            
            # Mots de passe différents
            case {"password": pwd, "password_confirm": confirm, **rest} if pwd != confirm:
                return {"status": "error", "field": "password_confirm", "message": "❌ Les mots de passe ne correspondent pas"}
            
            # Champs manquants
            case {"email": _}:
                return {"status": "error", "message": "❌ Champs manquants"}
            
            case _:
                return {"status": "error", "message": "❌ Données invalides"}
    
    # Tests
    formulaires = [
        {
            "email": "sana@dev.sn",
            "password": "secure123",
            "password_confirm": "secure123",
            "telephone": "+221771234567",
            "newsletter": True
        },
        {"email": "invalid-email", "password": "test", "password_confirm": "test", "telephone": "123"},
        {"email": "ok@test.com", "password": "short", "password_confirm": "short", "telephone": "123"},
        {"email": "ok@test.com", "password": "longpassword", "password_confirm": "different", "telephone": "123"},
        {"email": "only@email.com"},
    ]
    
    for i, form in enumerate(formulaires, 1):
        print(f"\n📝 Formulaire {i}:")
        print(f"   Données: {form}")
        result = valider_inscription(form)
        print(f"   Résultat: {result}")


# =============================================================================
#  PARTIE 9 : Cas pratique - Parser de commandes CLI
# =============================================================================

def exemple_9_cli_parser():
    """Parser de commandes en ligne de commande"""
    print("\n" + "="*50)
    print("EXEMPLE 9 : Parser CLI")
    print("="*50)
    
    def executer_commande(args):
        """Simule un CLI pour gestion de projet"""
        match args:
            # Commandes sans arguments
            case ["help"] | ["-h"] | ["--help"]:
                return "📖 Affichage de l'aide..."
            
            case ["version"] | ["-v"]:
                return "📦 Version 1.0.0"
            
            # Commande avec sous-commande
            case ["project", "create", nom]:
                return f"🆕 Création du projet '{nom}'"
            
            case ["project", "delete", nom, "--force"]:
                return f"🗑️ Suppression forcée du projet '{nom}'"
            
            case ["project", "list"]:
                return "📋 Liste des projets..."
            
            # Gestion des fichiers avec options
            case ["file", "upload", *fichiers, "--to", destination]:
                return f"📤 Upload de {len(fichiers)} fichier(s) vers {destination}"
            
            case ["file", "upload", *fichiers] if fichiers:
                return f"📤 Upload de {len(fichiers)} fichier(s) vers ./uploads/"
            
            # Commande utilisateur
            case ["user", "add", email] if "@" in email:
                return f"👤 Ajout de l'utilisateur {email}"
            
            case ["user", "add", _]:
                return "❌ Email invalide"
            
            # Config avec clé=valeur
            case ["config", "set", setting] if "=" in setting:
                key, value = setting.split("=", 1)
                return f"⚙️ Configuration: {key} = {value}"
            
            case []:
                return "💡 Tapez 'help' pour voir les commandes disponibles"
            
            case [cmd, *_]:
                return f"❌ Commande inconnue: {cmd}"
    
    # Tests
    commandes = [
        ["help"],
        ["version"],
        ["project", "create", "kaay-signe"],
        ["project", "delete", "old-project", "--force"],
        ["project", "list"],
        ["file", "upload", "doc1.pdf", "doc2.pdf", "--to", "/documents"],
        ["file", "upload", "image.png"],
        ["user", "add", "dev@senegal.sn"],
        ["user", "add", "invalid"],
        ["config", "set", "DEBUG=True"],
        [],
        ["unknown", "command"]
    ]
    
    for cmd in commandes:
        print(f"$ app {' '.join(cmd) if cmd else ''}")
        print(f"  → {executer_commande(cmd)}\n")


# =============================================================================
#  PARTIE 10 : Résumé et bonnes pratiques
# =============================================================================

def resume():
    """Affiche un résumé des patterns disponibles"""
    print("\n" + "="*60)
    print("📚 RÉSUMÉ - PEP 634 Pattern Matching")
    print("="*60)
    
    resume_text = """
┌─────────────────────────────────────────────────────────────┐
│  PATTERN              │  EXEMPLE                            │
├─────────────────────────────────────────────────────────────┤
│  Literal              │  case 42:                           │
│  Capture              │  case x:                            │
│  Wildcard             │  case _:                            │
│  Sequence             │  case [a, b, *rest]:                │
│  Mapping              │  case {"key": value}:               │
│  Class                │  case Point(x=0, y=y):              │
│  OR                   │  case 1 | 2 | 3:                    │
│  AS (alias)           │  case [x, y] as point:              │
│  Guard                │  case x if x > 0:                   │
└─────────────────────────────────────────────────────────────┘

💡 BONNES PRATIQUES:
   1. Placer les cas les plus spécifiques EN PREMIER
   2. Toujours inclure un case _ (wildcard) à la fin
   3. Utiliser les guards (if) pour des conditions complexes
   4. Les dataclasses fonctionnent parfaitement avec match
   5. Idéal pour parser JSON/API, CLI, et validation de données

⚠️ ATTENTION:
   - Ne pas confondre avec switch/case d'autres langages
   - Les variables dans les patterns sont des CAPTURES (pas des comparaisons)
   - Pour comparer avec une variable, utiliser un guard ou des constantes
"""
    print(resume_text)


# =============================================================================
# MAIN - Exécution
# =============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║     🎬 PEP 634 - Structural Pattern Matching       ║
║                        Python 3.10+                               ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    import sys
    print(f"🐍 Python version: {sys.version}")
    
    if sys.version_info < (3, 10):
        print("❌ ERREUR: Python 3.10+ requis pour le pattern matching!")
        print("   Installer Python 3.10 ou supérieur")
        sys.exit(1)
    
    # Exécuter tous les exemples
    exemple_1_basique()
    exemple_2_capture()
    exemple_3_sequences()
    exemple_4_dictionnaires()
    exemple_5_guards()
    exemple_6_classes()
    exemple_7_or_as()
    exemple_8_django_forms()
    exemple_9_cli_parser()
    resume()
    
    print("\n" + "="*60)
    print("🎉 FIN DU LIVE CODING - Merci d'avoir suivi!")
    print("="*60)

