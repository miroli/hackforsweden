**Välkommen till H4Qs repository för bearbetning av öppna data!**

Tanken med repositoryt och projektet är:
 * En sandlåda där man kan *experimentera* med att programmera mot öppna data
 * Samla kodsnuttar och goda exempel på *hur* man kan programmera mot de olika källorna till öppen data
 * Att *renodla* erfarenheter och experiment till inspirerande artiklar

Låter det spännande? [Läs vidare](https://github.com/H4Q/therepo/blob/master/introduktion.md)!

 
## Uppdateringar

 * *2015-10-15, lite senare* Bilden finns nu på dockerhub, det räcker att installera docker och vrida om nyckeln så laddas bilden ned, med nödvändiga beroenden och startar en lokal notebook-server!
 * *2015-10-15* Vi är igång igen, den här gången med Docker i högsta hugg! Installera bara Docker på din host och bygg bilden (det borde gå igenom med bara publika beroenden) och ha en användarvänlig utvecklingsmiljö att hacka öppna data på fem minuter!
 * *2015-03-14* Hack For Sweden är i full gång! Vi skapar projektet, 
 kollar på spännande hack och länkar dem härifrån

## Docker!

Kör docker-bilden från dockerhub (baserad på den erkänt lite för stora ipython/scipylab) som en container med:

  $ docker run -d -p 443:8888 -e "PASSWORD=foobar" unclecj/h4q

Öppna sedan i webbläsare https://localhost, godkänn säkerhetsundantaget (TODO) och börja hacka på svenska öppna data! Förslag: Skapa en mapp "iPython Notebooks" och koda loss, kika på våra json-exempel och googla på vad man kan göra med matplotlib. Snart kommer entrypoint-stöd för att spara arbetet också (TODO, docker commit kommer fortsatt fungera). Notera att branchen i imagen (sandbox) inte är samma som för att skapa bilden (docker), that's how we roll (TODO?).

(Skulle det behövas kan du bygga om docker-bilden genom att clona detta repo från github och köra (det går tokfort om du rensar bort .git-katalogen först):

  $ docker build -t h4q . 

)

TODO: Kanske installera java (med en curl-pipe) och dra igång Gephi grafiskt också. Vid närmare eftertanke ska det få bli sin egen image, behöver inte blanda det med scipylab

