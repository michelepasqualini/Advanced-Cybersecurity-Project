# Progetto Advanced Cybersecurity
<a><img src="images/logo-univpm.png" height='60' align="right"/></a>
Progetto realizzato per il corso di "Advanced Cybersecurity" presso l'Università politecnica delle Marche nell'anno accademico 2021/2022.


## About The Project
In questo progetto viene posta l’attenzione sui malware che permettono di creare le "Botnet", ovvero reti di macchine infette il quale vengono coordinate da un hacker attraverso un server di comando e controllo. Solitamente, per arginare questo tipo di infezione, si cerca di individuare e offuscare il server di comando e con
trollo. Questa operazione, però, non è molto semplice, perchè come contromisura vengono adottate delle strategie che ne rendono difficile l’individuazione. Una di
queste tecniche consiste nel modificare il nome di dominio dopo un certo intervallo di tempo, attraverso un DGA (Domain name Generation Algorithm).

## 📦 Built With

* [Google Colab](https://colab.research.google.com/?hl=it)
* [Python 3.11](https://www.python.org/)
* [FastText](https://fasttext.cc/)

## Prerequisites
* Per lo sviluppo del progetto è necessaria l'installazione dei seguenti pacchetti: FastText, Keras, TensorFlow, h5py e wandb.
Per installarli basta eseguire il comando:

```sh
    pip install fasttext tensorflow-gpu==1.15.3 keras==2.3.1 h5py==2.10.0 wandb
```

## 👩‍💻 Getting Started
1. Nella prima fase del progetto vengono scaricati i log dalla rete GARR secondo le specifiche di progetto:
    - 10 giorni al mese per 12 mesi;
    - 20% di ciscun log. (Tale specifica sarà soddisfatta nella fase successiva durante l'estrazione dei DNS) 
    - Ogni fascia oraria è rappresentata dai vari log.

L’estrazione dei vari log è stata effettuata tramite il seguente [script](https://github.com/MassimoCiaffoni/Progetto_Advanced_Cybersecurity/blob/main/download_log.py) python. 
Per eseguire lo script è necessario lanciare il seguente comando da terminale specificando le varie opzioni:
```sh
    python3 ../download_log.py --ip-address <ip_del_server> --host <host @studenti>
    --psw <password> --year <anno> --out-dir <output_directory>
```
I vari indirizzi IP, porta e password del server da cui sono stati scaricati i dati GARR sono stati volutamente omessi per questione di sicurezza e confidenzialità di tali informazioni. 

2. Una volta estratti i file GARR è necessario estrarre i log e successivamente inserirli in un archivio .zip in modo tale da poterli facilmente elaborare nel [notebook](https://github.com/MassimoCiaffoni/Progetto_Advanced_Cybersecurity/blob/main/Progetto_ADC.ipynb) messo a disposizione nella repository.

3. Una volta inserito il file .zip dei log è sufficente eseguire le sezioni del notebook messo a disposizione:
    - **Estrazione DNS dai file di log**: In questa sezione una volta ottenuti i log si vanno ad estrarre per ogni file di log il 20% dei record di DNS filtrando prima quelli con lunghezza superiore ai 100 caratteri e quelli espressi tramite indirizzi IP. 
    - **Suddivisione in n-grams**: Una volta estratti i DNS, essi sono stati divisi rispettivamenti in 1-grams, 2-grams e 3-grams
    - **Implementazione ed allenamento di FastText**: le varie divisioni sono state utilizzate per addestrarre tre modelli unsupervised tramite Fasttext (per maggiori informazioni sul suo utilizzo vedere la relazione). I tre modelli ottenuti poi sono stati trasformati in formato .vec per il successivo utilizzo della fase di addestramento generale.
    - **Addestramento**: Una volta ottenuti i tre modelli in formato .vec si è utilizzata un'architettura Stacked disponibile presso una repository GitLab per l'addestramento del modello finale in grado di riconoscere i DNS malevoli. In particolare si è utilizzato un dataset UMDGA contenente 50 classi di domini malevoli e si sono addestrati 4 modelli con tagli crescenti.
    - **Test**: Una volta addestrati i diversi modelli con tagli diversi si sono effettuati dei test su dati non utilizzati durante la fase di training per valutare la correttezza dei modelli (I risultati sono presenti nella cartella Reports della repository).

## Links

<a href="https://github.com/MassimoCiaffoni/Progetto_Advanced_Cybersecurity/tree/main/Relazione.pdf"><strong>Reference</strong></a>
<br/>
<a href="https://github.com/MassimoCiaffoni/Progetto_Advanced_Cybersecurity/tree/main/Reports/Report"><strong>Reports</strong></a>
<br/>
<a href="https://drive.google.com/drive/folders/1wVrIYQYJnXYo5k4x2caQPwSjvxGTWX6T?usp=sharing"><strong>Domains Extracted</strong></a>
  


## ✍️ Author
#### [Massimo Ciaffoni](mailto:s1102853@studenti.univpm.it) (Matricola 1102853) 
#### [Denil Nicolosi](mailto:s1100331@studenti.univpm.it) (Matricola 1100331)
#### [Michele Pasqualini](mailto:s1101226@studenti.univpm.it) (Matricola 1101226) 
#### [Francesco Zerbino Di Bernardo](mailto:s1102495@studenti.univpm.it) (Matricola 1102495) 


## 🔒 License
Apache License 2.0
