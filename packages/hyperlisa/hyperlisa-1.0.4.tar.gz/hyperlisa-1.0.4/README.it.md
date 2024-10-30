[English](README.md) | [Italiano](README.it.md)

# Lisa - Analizzatore di Codice per LLM

Lisa (ispirato a Lisa Simpson) è uno strumento progettato per semplificare l'analisi del codice sorgente attraverso i Large Language Models (LLM). Intelligente e analitica come il personaggio da cui prende il nome, Lisa aiuda a studiare e interpretare il codice con logica e metodo.

## Lisa in breve

Ecco i passaggi essenziali per iniziare subito:

1. **Installazione**:
   ```bash
   pip install hyperlisa
   ```

2. **Configurazione**:
   ```bash
   hyperlisa-configure
   ```

3. **[Opzionale] Personalizzazione**:
   Modifica il file di configurazione:
   - Windows: `C:\Users\<username>\AppData\Local\hyperlisa\combine_config.yaml`
   - Linux/MacOS: `~/.config/hyperlisa/combine_config.yaml`
   ```yaml
   includes:
     - "*.py"    # aggiungi altre estensioni se necessario
     - "*.java"
   excludes:
     - ".git"
     - "venv"
   ```

4. **Uso**:
   ```bash
   # Dalla directory del progetto
   cmb                            # nome file predefinito
   # oppure
   cmb --output NOME_ANALISI     # nome file personalizzato
   ```

Il file generato sarà nella directory corrente con formato: `NOME_YYYYMMDD_HHMM.txt`

## Descrizione

Lisa è uno strumento essenziale per chi vuole analizzare il proprio codice o studiare progetti open source attraverso i Large Language Models. Il suo principale obiettivo è generare un unico file di testo che mantiene tutti i riferimenti e la struttura del codice originale, rendendolo facilmente interpretabile da un LLM.

Questo approccio risolve uno dei problemi più comuni nell'analisi del codice con gli LLM: la frammentazione dei file e la perdita dei riferimenti tra i diversi componenti del progetto.

## Installazione e Configurazione

### 1. Prerequisiti
Prima di iniziare, assicurati di avere:
- Python 3.6 o superiore installato nel tuo sistema
- Un editor di codice (consigliamo Visual Studio Code, o VSCode)
- Accesso al terminale (vedremo come usarlo sia da VSCode che dal sistema)

### 2. Installazione del pacchetto

#### Usando Visual Studio Code (Raccomandato per principianti)
1. Apri VSCode
2. Apri la cartella del tuo progetto usando `File > Apri Cartella` 
   (esempio: seleziona `C:\progetti\mio_progetto` su Windows o `/home/utente/progetti/mio_progetto` su Linux/MacOS)
3. Apri il terminale integrato in VSCode:
   - Premi `Ctrl + ` (backtick, il tasto sotto Esc)
   oppure
   - Dal menu: `Visualizza > Terminale`
4. Nel terminale vedrai qualcosa di simile a:
   ```bash
   # Windows
   C:\progetti\mio_progetto>

   # Linux/MacOS
   user@computer:~/progetti/mio_progetto$
   ```
5. Esegui il comando di installazione:
   ```bash
   pip install hyperlisa
   ```

#### Usando il Terminale di Sistema
1. Apri il terminale del tuo sistema operativo:
   - **Windows**: Cerca "cmd" o "PowerShell" nel menu Start
   - **MacOS**: Cerca "Terminal" in Spotlight (Cmd + Spazio)
   - **Linux**: Usa la scorciatoia Ctrl + Alt + T o cerca "Terminal"
2. Naviga nella cartella del tuo progetto:
   ```bash
   # Windows
   cd C:\progetti\mio_progetto

   # Linux/MacOS
   cd ~/progetti/mio_progetto
   ```
3. Esegui il comando di installazione:
   ```bash
   pip install hyperlisa
   ```

### 3. Configurazione Post-Installazione
Dopo l'installazione, è **necessario** eseguire il comando di configurazione. 

#### Dal terminale di VSCode o del sistema:
```bash
# Il prompt potrebbe apparire così su Windows:
C:\progetti\mio_progetto> hyperlisa-configure

# O così su Linux/MacOS:
user@computer:~/progetti/mio_progetto$ hyperlisa-configure
```

Questo comando dovrebbe mostrare una serie di messaggi simili a questi:
```
Configurazione di HyperLisa in corso...
✓ Creazione directory di configurazione
✓ Generazione file di configurazione predefinito
✓ Impostazione permessi
Configurazione completata con successo!
```

Il comando di configurazione esegue le seguenti operazioni:
1. Crea la directory di configurazione di Lisa:
   - Windows: `C:\Users\<username>\AppData\Local\hyperlisa\`
   - Linux/MacOS: `~/.config/hyperlisa/`
2. Genera il file di configurazione predefinito `combine_config.yaml` nella directory creata
3. Imposta i permessi corretti per i file e le directory:
   - Windows: permessi di lettura e scrittura per l'utente corrente
   - Linux/MacOS: permessi 755 per le directory e 644 per i file

Se esegui il comando e vedi errori relativi ai permessi:
- **Windows**: Esegui il Prompt dei comandi o PowerShell come amministratore
- **Linux/MacOS**: Usa `sudo hyperlisa-configure` (ti verrà chiesta la password)

> **IMPORTANTE**: 
> - Questo comando deve essere eseguito una sola volta dopo l'installazione
> - Se viene eseguito nuovamente, il comando verificherà prima l'esistenza della configurazione:
>   - Se trova una configurazione esistente, chiederà conferma prima di sovrascriverla
>   - In caso di sovrascrittura, le personalizzazioni precedenti andranno perse
>   - Se si desidera mantenere le personalizzazioni, fare una copia di backup del file `combine_config.yaml` prima di rieseguire il comando

### 4. File di Configurazione
Il file `combine_config.yaml` permette di personalizzare quali file includere o escludere dall'analisi. La configurazione predefinita è:

```yaml
# Pattern di inclusione (estensioni o directory da includere)
includes:
  - "*.py"  
  # È possibile aggiungere altre estensioni o directory

# Pattern di esclusione (directory o file da escludere)
excludes:
  - ".git"
  - "__pycache__"
  - "*.egg-info"
  - "venv*"
  - ".vscode"
  - "agents*"
  - "log"
```

#### Pattern di Inclusione/Esclusione
- I pattern in `includes` determinano quali file verranno processati (es: "*.py" include tutti i file Python)
- I pattern in `excludes` specificano quali file o directory ignorare
- È possibile utilizzare il carattere * come carattere jolly
- I pattern vengono applicati sia ai nomi dei file che ai percorsi delle directory
- **Importante**: Le regole di esclusione hanno sempre la priorità su quelle di inclusione

#### Esempi di Pattern
```
Esempio 1:
C:\progetti\mio_progetto    # Windows
/progetti/mio_progetto      # Linux/MacOS
    /src_code
        /utils
            /logs
                file1.py
                file2.py
            helpers.py
```
Se nelle regole abbiamo:
- includes: ["*.py"]
- excludes: ["*logs"]

In questo caso, `file1.py` e `file2.py` NON verranno inclusi nonostante abbiano l'estensione .py, perché si trovano in una directory che soddisfa il pattern di esclusione "*logs". Il file `helpers.py` invece verrà incluso.

```
Esempio 2:
C:\progetti\mio_progetto    # Windows
/progetti/mio_progetto      # Linux/MacOS
    /includes_dir
        /excluded_subdir
            important.py
```
Se nelle regole abbiamo:
- includes: ["includes_dir"]
- excludes: ["*excluded*"]

In questo caso, `important.py` NON verrà incluso perché si trova in una directory che soddisfa un pattern di esclusione, anche se la sua directory padre soddisfa un pattern di inclusione.

## Utilizzo

Il programma può essere eseguito utilizzando uno dei seguenti comandi dal terminale:

```bash
# Windows
C:\progetti\mio_progetto> cmb [opzioni]

# Linux/MacOS
user@computer:~/progetti/mio_progetto$ cmb [opzioni]
```

Sono disponibili anche comandi alternativi:
- `combine-code`: comando originale completo
- `lisacmb`: alias descrittivo
- `hyperlisacmb`: alias ancora più descrittivo

### Struttura e Nome Predefinito
Per comprendere quale nome file verrà utilizzato di default, consideriamo questa struttura:

```
# Windows
C:\progetti
    \mio_progetto_test     <- Questa è la directory root
        \src
            main.py
        \tests
            test_main.py

# Linux/MacOS
/home/user/progetti
    /mio_progetto_test     <- Questa è la directory root
        /src
            main.py
        /tests
            test_main.py
```

In questo caso, il nome predefinito sarà "MIO_PROGETTO_TEST" (il nome della directory root in maiuscolo).

### Parametri disponibili:

- `--clean`: Rimuove i file di testo precedentemente generati
- `--output NOME`: Specifica il prefisso del nome del file di output
  ```bash
  # Windows
  # Esempio con nome predefinito
  C:\progetti\mio_progetto> cmb
  # Output: MIO_PROGETTO_20240327_1423.txt

  # Esempio con nome personalizzato
  C:\progetti\mio_progetto> cmb --output ANALISI_PROGETTO
  # Output: ANALISI_PROGETTO_20240327_1423.txt

  # Linux/MacOS
  # Esempio con nome predefinito
  user@computer:~/progetti/mio_progetto$ cmb
  # Output: MIO_PROGETTO_20240327_1423.txt

  # Esempio con nome personalizzato
  user@computer:~/progetti/mio_progetto$ cmb --output ANALISI_PROGETTO
  # Output: ANALISI_PROGETTO_20240327_1423.txt
  ```

### Output

Lo script genera un file di testo con il formato:
`NOME_YYYYMMDD_HHMM.txt`

dove:
- `NOME` è il prefisso specificato con --output o quello predefinito
- `YYYYMMDD_HHMM` è il timestamp di generazione

## Utilizzo con Progetti GitHub

Per utilizzare Lisa con un progetto GitHub, segui questi passaggi:

1. **Preparazione dell'ambiente**:
   ```bash
   # Windows
   C:> mkdir C:\progetti
   C:> cd C:\progetti

   # Linux/MacOS
   $ mkdir ~/progetti
   $ cd ~/progetti
   ```

2. **Clona il progetto da analizzare**:
   ```bash
   # Esempio con un progetto ipotetico "moon_project"
   # Windows/Linux/MacOS
   git clone https://github.com/utente/moon_project.git
   ```

3. **Installa e configura Lisa**:
   ```bash
   # Windows/Linux/MacOS
   pip install hyperlisa
   hyperlisa-configure
   ```

4. **Esegui l'analisi**:
   ```bash
   # Windows
   C:\progetti\moon_project> cmb

   # Linux/MacOS
   user@computer:~/progetti/moon_project$ cmb
   ```

### Migliori Pratiche per l'Analisi
- Prima di eseguire Lisa, assicurati di essere nella directory root del progetto da analizzare
- Controlla e personalizza il file `combine_config.yaml` in base alle specifiche necessità del progetto
- Utilizza l'opzione `--clean` per mantenere ordinata la directory quando generi multiple versioni

## Note Aggiuntive

- Lisa mantiene la struttura gerarchica dei file nel documento generato
- Ogni file viene chiaramente delimitato da separatori che ne indicano il percorso relativo
- Il codice viene organizzato mantenendo l'ordine di profondità delle directory
- I file generati possono essere facilmente condivisi con gli LLM per l'analisi

## Utilizzare il File Generato con gli LLM

Lisa genera un file che può essere utilizzato efficacemente con vari Large Language Models. Ecco un esempio pratico di come sfruttare al meglio questo strumento.

### Esempio: Analisi di LangChain
Supponiamo di voler utilizzare la libreria LangChain ma di non avere familiarità con la sua struttura o le sue funzionalità più recenti.

1. **Preparazione**:
   ```bash
   # Clona LangChain
   git clone https://github.com/langchain-ai/langchain.git
   cd langchain

   # Genera il file di analisi con Lisa
   cmb --output LANGCHAIN_ANALYSIS
   ```

2. **Utilizzo con ChatGPT/Claude**:
   Carica il file generato `LANGCHAIN_ANALYSIS_20240327_1423.txt` nella chat. Puoi utilizzare prompt come questi:

   ```
   Ho generato un'analisi del codice sorgente di LangChain usando Lisa. 
   Il file contiene la struttura completa del codice con tutti i riferimenti.
   Per favore:
   1. Analizza la struttura del codice
   2. Identifica i moduli principali
   3. Suggerisci il modo migliore per implementare [descrivi il tuo caso d'uso]
   ```

   Esempi specifici di prompt:

   **Per esplorare funzionalità recenti**:
   ```
   Nel codice che ti ho fornito, cerca le implementazioni più recenti 
   per l'integrazione con modelli di OpenAI. Vorrei creare una catena 
   che utilizza GPT-4 per analizzare documenti PDF, estraendo 
   informazioni chiave e generando un sommario. Puoi mostrarmi il 
   codice necessario utilizzando le ultime API disponibili?
   ```

   **Per comprendere parti specifiche**:
   ```
   Analizza come LangChain implementa la gestione della memoria nelle 
   conversazioni. Voglio creare un chatbot che mantiene il contesto 
   delle conversazioni precedenti ma ottimizza l'utilizzo dei token. 
   Puoi spiegarmi come funziona e fornirmi un esempio di 
   implementazione basato sul codice attuale?
   ```

   **Per progetti personalizzati**:
   ```
   Basandoti sul codice sorgente fornito, aiutami a creare un agente 
   personalizzato che:
   1. Accede a un database SQL
   2. Elabora query in linguaggio naturale
   3. Genera e esegue query SQL appropriate
   4. Formatta i risultati in modo user-friendly
   Mostrami il codice necessario utilizzando i componenti più adatti 
   di LangChain.
   ```

### Vantaggi di Questo Approccio
- **Accesso alle Ultime Funzionalità**: L'LLM può vedere il codice più recente, anche se non ancora documentato
- **Comprensione Profonda**: Avendo accesso al codice sorgente completo, l'LLM può fornire suggerimenti più precisi e contestualizzati
- **Debugging Efficace**: Se incontri problemi, puoi chiedere all'LLM di analizzare le implementazioni specifiche
- **Personalizzazione Informata**: Puoi creare soluzioni personalizzate basate sulle effettive implementazioni interne

### Suggerimenti per l'Uso Efficace
1. **Sii Specifico**: Descrivi chiaramente il tuo caso d'uso e le funzionalità desiderate
2. **Chiedi Spiegazioni**: Se qualcosa non è chiaro, fai domande sul funzionamento interno
3. **Itera**: Usa le risposte dell'LLM per raffinare le tue domande e ottenere soluzioni migliori
4. **Verifica**: Testa sempre il codice generato e chiedi chiarimenti se necessario
5. **Esplora Alternative**: Chiedi all'LLM di suggerirti approcci diversi basati sul codice sorgente

## Contribuire

Se vuoi contribuire al progetto, puoi:
- Aprire segnalazioni per riportare bug o proporre miglioramenti
- Proporre richieste di integrazione con nuove funzionalità
- Migliorare la documentazione
- Condividere i tuoi casi d'uso e suggerimenti

## Licenza

Licenza MIT

Copyright (c) 2024

È concesso gratuitamente il permesso a chiunque ottenga una copia
di questo software e dei relativi file di documentazione (il "Software"), di trattare
il Software senza restrizioni, inclusi, senza limitazioni, i diritti
di utilizzare, copiare, modificare, unire, pubblicare, distribuire, concedere in sublicenza e/o vendere
copie del Software, e di permettere alle persone a cui il Software è
fornito di farlo, alle seguenti condizioni:

L'avviso di copyright sopra riportato e questo avviso di permesso devono essere inclusi in
tutte le copie o parti sostanziali del Software.

IL SOFTWARE VIENE FORNITO "COSÌ COM'È", SENZA GARANZIE DI ALCUN TIPO, ESPLICITE O
IMPLICITE, INCLUSE, MA NON SOLO, LE GARANZIE DI COMMERCIABILITÀ,
IDONEITÀ PER UN PARTICOLARE SCOPO E NON VIOLAZIONE. IN NESSUN CASO GLI
AUTORI O I TITOLARI DEL COPYRIGHT SARANNO RESPONSABILI PER QUALSIASI RECLAMO, DANNO O ALTRA
RESPONSABILITÀ, SIA IN UN'AZIONE DI CONTRATTO, ILLECITO O ALTRO, DERIVANTE DA,
FUORI O IN CONNESSIONE CON IL SOFTWARE O L'USO O ALTRE OPERAZIONI NEL
SOFTWARE.