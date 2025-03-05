import json
import os

VERSION_FILE = "version.json"

# Charger la version actuelle
def load_version():
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as file:
            return json.load(file)
    else:
        return {"version": [0, 1, 0], "modules": {"personnel": [1, 0]}}

# Sauvegarder la version mise à jour
def save_version(data):
    with open(VERSION_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Afficher la version actuelle
def display_version(data):
    version_str = f"V{'.'.join(map(str, data['version']))} - " + \
                  "[" + ", ".join(f"{mod}: {'.'.join(map(str, ver))}" for mod, ver in data['modules'].items()) + "]"
    print("\n🚀 Version actuelle :", version_str)

# Ajouter un module
def add_module():
    data = load_version()
    module_name = input("Nom du module à ajouter : ").strip()
    
    if module_name in data["modules"]:
        print(f"⚠️ Le module '{module_name}' existe déjà.")
        return

    data["modules"][module_name] = [1, 0]  # Nouvelle version du module
    data["version"][1] += 1  # Incrémentation de la version mineure
    data["version"][2] = 0  # Réinitialisation du patch

    save_version(data)
    print(f"✅ Module '{module_name}' ajouté avec succès !")
    display_version(data)

# Mettre à jour un module
def update_module():
    data = load_version()
    module_name = input("Nom du module à mettre à jour : ").strip()

    if module_name not in data["modules"]:
        print(f"⚠️ Le module '{module_name}' n'existe pas.")
        return

    data["modules"][module_name][1] += 1  # Incrémentation de la version du module
    save_version(data)
    print(f"✅ Module '{module_name}' mis à jour !")
    display_version(data)

# Appliquer un patch
def apply_patch():
    data = load_version()
    data["version"][2] += 1  # Incrémentation du patch
    save_version(data)
    print("✅ Patch appliqué !")
    display_version(data)

# Refonte majeure
def major_update():
    data = load_version()
    data["version"][0] += 1  # Incrémentation de la version majeure
    data["version"][1] = 0
    data["version"][2] = 0
    save_version(data)
    print("🚀 Refonte majeure effectuée !")
    display_version(data)

# Menu interactif
def interactive_menu():
    while True:
        print("\n=== Gestionnaire de Version ===")
        print("1️⃣  Afficher la version actuelle")
        print("2️⃣  Ajouter un module")
        print("3️⃣  Mettre à jour un module")
        print("4️⃣  Appliquer un patch")
        print("5️⃣  Refonte majeure")
        print("0️⃣  Quitter")

        choice = input("Sélectionne une option : ").strip()

        if choice == "1":
            display_version(load_version())
        elif choice == "2":
            add_module()
        elif choice == "3":
            update_module()
        elif choice == "4":
            apply_patch()
        elif choice == "5":
            major_update()
        elif choice == "0":
            print("👋 Bye !")
            break
        else:
            print("❌ Option invalide, réessaye.")

# Lancer le menu interactif
if __name__ == "__main__":
    interactive_menu()
