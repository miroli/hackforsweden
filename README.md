**Välkommen till H4Qs repository för bearbetning av öppna data!**

Tanken med repositoryt och projektet är:
 * En sandlåda där man kan *experimentera* med att programmera mot öppna data
 * Samla kodsnuttar och goda exempel på *hur* man kan programmera mot de olika källorna till öppen data
 * Att *renodla* erfarenheter och experiment till inspirerande artiklar

Låter det spännande? [Läs vidare](https://github.com/H4Q/therepo/blob/master/introduktion.md)!

 
## Uppdateringar

 * *2015-10-15* Vi är igång igen, den här gången med Docker i högsta hugg! Installera bara Docker på din host och bygg bilden (det borde gå igenom med bara publika beroenden) och ha en användarvänlig utvecklingsmiljö att hacka öppna data på fem minuter!
 * *2015-03-14* Hack For Sweden är i full gång! Vi skapar projektet, 
 kollar på spännande hack och länkar dem härifrån

## Docker!

Bygg docker-bilden med (det går tokfort om du rensar bort .git-katalogen först):

$ docker build -t h4q .

Kör docker-bilden som en container med:

$ docker run -d -p 443:8888 -e "PASSWORD=foobar" h4q

Öppna sedan i webbläsare https://localhost, godkänn säkerhetsundantaget (TODO) och börja hacka på svenska öppna data! Förslag: Skapa en mapp "iPython Notebooks" och koda loss, kika på våra json-exempel och googla på vad man kan göra med matplotlib. Snart kommer entrypoint-stöd för att spara arbetet också (TODO, docker commit kommer fortsatt fungera). Notera att branchen i imagen (sandbox) inte är samma som för att skapa bilden (docker), that's how we roll (TODO?).
