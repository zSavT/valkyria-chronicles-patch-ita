import os
import subprocess

def get_csv_file_names(folder_path):
    """ Restituisce un elenco di nomi di file CSV senza estensione nella cartella dello script """
    return [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.csv') and os.path.isfile(os.path.join(folder_path, f))]

def write_ini_file(ini_path, file_name):
    """ Sovrascrive il file ini con il nuovo nome del file """
    with open(ini_path, 'w') as ini_file:
        ini_file.write(f"{file_name}\n")

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))  # Cartella dello script
    ini_file_path = "mtp_write.ini"  # Percorso del file ini
    exe_path = "mtp_write.exe"  # Percorso del file exe
    
    # Colori ANSI per la shell
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    # 1. Leggere i nomi dei file CSV nella stessa cartella dello script
    file_names = get_csv_file_names(folder_path)
    
    for file_name in file_names:
        # 2. Scrivere il file ini per ogni file
        write_ini_file(ini_file_path, file_name)
        print(f"{GREEN}File {ini_file_path} aggiornato con {file_name}.{RESET}")
        
        # 3. Eseguire il file exe e attendere la fine
        print(f"{YELLOW}Eseguendo {exe_path} per {file_name}...{RESET}")
        subprocess.run(exe_path, shell=True)
        print(f"{GREEN}{exe_path} completato per {file_name}.{RESET}")
        
        # 4. Riscrivere il file ini dopo l'esecuzione
        write_ini_file(ini_file_path, file_name)
        print(f"{RED}File {ini_file_path} riscritto dopo l'esecuzione di {exe_path} per {file_name}.{RESET}")
    print(f"\n{GREEN}Terminato")
    
if __name__ == "__main__":
    main()