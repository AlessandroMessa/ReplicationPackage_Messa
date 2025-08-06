**AS: God Component, package: com.mtcarpenter.mall.domain**



Nel modulo mall-admin-cms, il package model conteneva originariamente 26 classi sotto un unico namespace. Tramite analisi semantica dei nomi e del dominio di appartenenza, le classi sono state riorganizzate in 5 sotto-package concettuali:



help: gestione delle guide utente e relative categorie;



memberreport: gestione delle segnalazioni degli utenti;



prefrencearea: gestione delle aree promozionali e dei prodotti correlati;



subject: soggetti promozionali, commenti, categorie e prodotti associati;



topic: discussioni, commenti e categorie.



Questo refactoring ha aumentato la coesione semantica dei package e migliorato la manutenibilità del modulo, senza introdurre nuove dipendenze strutturali.





Nel modulo mall-admin-oms, il package model era composto da 16 classi, tutte posizionate in un unico namespace. È stata condotta un’analisi semantica sul nome delle classi per individuare gruppi concettuali coerenti:



cart: gestione degli articoli nel carrello;



address: indirizzi dell’azienda usati per spedizioni e resi;



order: entità legate all’ordine, agli articoli, alla cronologia e alle impostazioni;



returnorder: flusso di reso e motivazioni associate.



Questo refactoring ha portato a una suddivisione più logica e manutenibile del dominio, in linea con le pratiche consigliate nella documentazione Arcan per God Components con scarsa coesione strutturale ma alta densità semantica. 

Per rifinire ulteriormente la coesione interna dei package, si è scelto di annidare i sotto-package relativi all’ordine all’interno di un package order.

Questo approccio è in linea con il principio di modular decomposition, e consente una navigazione più chiara del modello dati.



La nuova struttura distingue chiaramente:



la parte principale (order)



le componenti secondarie come gli articoli (order.item), la cronologia (order.operate), le impostazioni (order.setting) e la gestione dei resi (order.return\_).



Tale riorganizzazione migliora ulteriormente la leggibilità e la responsabilità singola dei package. 


\# mall-admin-pms 


Il modulo mall-admin-pms rappresenta il cuore della gestione prodotti e contiene 36 classi sotto il package model. La struttura originaria presentava un evidente caso di God Component, con classi eterogenee e nessuna coesione strutturale.

Si è quindi proceduto con un refactoring semantico, organizzando le classi in 11 sotto-package tematici, basati su:



funzionalità (es. comment, price, feight)



dominio prodotto (es. product.attribute, product.sku, product.discount)



infrastruttura (es. product.log, product.category)



Questa struttura ad albero ha aumentato la coerenza semantica, migliorato la navigazione del modello e preparato il modulo a eventuali migrazioni verso microservizi verticali (es. scomposizione del catalogo). 

"Per prevenire la formazione di nuovi God Components secondari e garantire la massima coesione semantica, si è deciso di applicare un ulteriore refactoring al package product.attribute. In particolare, il dominio attributi prodotto è stato suddiviso in quattro ulteriori sotto-package, ciascuno dei quali incapsula un concetto ben definito:



Attributi generici (attribute)



Categorie degli attributi (attribute.category)



Valori degli attributi (attribute.value)



Tale strategia migliora ulteriormente modularità, leggibilità e mantenibilità del codice."


\# admin-sms 
Strategia adottata:

Il package model è stato riorganizzato secondo i concetti funzionali del dominio, suddividendo le entità in sotto-package annidati:



coupon: gestione dei coupon



coupon.history: storico dei coupon



coupon.product.category: relazione tra coupon e categorie



coupon.product.relation: relazione tra coupon e prodotti



promotion: gestione delle promozioni flash



promotion.log: log di attivazione



promotion.session: fasce orarie



promotion.product.relation: prodotti collegati



home: gestione dei contenuti promozionali nella home page



home.advertise: banner pubblicitari



home.brand: brand in evidenza



home.product: nuovi prodotti



home.recommend.product: prodotti consigliati



home.recommend.subject: soggetti consigliati



Risultati:

La coesione semantica è aumentata grazie al raggruppamento logico delle entità.



Il modulo è ora più facilmente estendibile e leggibile.



L’analisi Arcan post-refactoring ha confermato l’eliminazione del God Component e l’assenza di nuovi smell architetturali. 

#mall-portal-product



Il modulo mall-portal-product contiene i modelli relativi alla gestione dei prodotti lato utente. In origine, tutte le 19 classi si trovavano nel package model, causando un problema di God Component.



Dopo un'analisi semantica dei nomi e dei concetti rappresentati, si è proceduto a una riorganizzazione in 11 sotto-package:



album, brand, comment, feight, price: gestiscono componenti secondarie e metadati;



core: il modello principale del prodotto;



attribute, category, sku, discount, log: dettagliano vari aspetti del prodotto;



subject: contenuti promozionali o editoriali associati.



Il refactoring ha migliorato la leggibilità del package, la navigabilità del codice e ha eliminato lo smell del God Component, senza introdurre nuove dipendenze.

Dopo il refactoring semantico dei package model, il report Arcan evidenzia una riduzione da 6 a 5 smell complessivi:

È stato completamente rimosso il God Component relativo a com.mtcarpenter.mall.model.

È stata eliminata la Hublike Dependency su mall.portal.service.

È comparsa una nuova Hublike Dependency su mall.client, probabilmente a causa dell’introduzione di un nuovo modulo o di una riorganizzazione dei consumer.

Gli altri smell (due Hublike Dependency residue e due Cyclic Dependency) rimangono pressoché invariati in termini di entità coinvolte, dimostrando che il refactoring non ha introdotto cicli o hub indesiderati.

Complessivamente, il refactoring ha raggiunto l’obiettivo di eliminare i God Component e migliorare la struttura semantica del progetto, con un impatto minimale sugli altri smell architetturali.

