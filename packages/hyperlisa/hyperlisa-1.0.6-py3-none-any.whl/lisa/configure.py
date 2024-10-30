import os
import shutil


def main():
    # Definisci la directory di destinazione per la cartella "hyperlisa"
    destination_dir = os.path.join(os.getcwd(), "hyperlisa")
    config_file_name = "config.yaml"

    # Definisci il percorso del file di configurazione sorgente
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, config_file_name)

    # Crea la cartella "hyperlisa" se non esiste
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copia il file di configurazione nella cartella "hyperlisa"
    destination = os.path.join(destination_dir, config_file_name)
    shutil.copy(source, destination)
    print(f"Configuration file has been copied to {destination}")

    # Modifica il file .gitignore, se presente
    gitignore_path = os.path.join(os.getcwd(), ".gitignore")
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            lines = gitignore_file.readlines()

        if "hyperlisa\n" not in lines and "hyperlisa" not in [
            line.strip() for line in lines
        ]:
            with open(gitignore_path, "a") as gitignore_file:
                gitignore_file.write("\nhyperlisa\n")
            print("Added 'hyperlisa' to .gitignore")


if __name__ == "__main__":
    main()
