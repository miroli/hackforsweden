**Välkommen till H4Qs repository för bearbetning av öppna data (fork till vienno)!**

Tanken med repositoryt och projektet är:
 * En sandlåda där man kan *experimentera* med att programmera mot öppna data
 * Samla kodsnuttar och goda exempel på *hur* man kan programmera mot de olika källorna till öppen data
 * Att *renodla* erfarenheter och experiment till inspirerande artiklar

Låter det spännande? [Läs vidare](https://github.com/H4Q/therepo/blob/master/introduktion.md)!

## Docker!

Du kan bygga om docker-bilden genom att clona detta repo från github och köra (det går tokfort om du rensar bort .git-katalogen först):

  $ docker build -t vienno/h4q . 

Kör docker-bilden som en container med:

  $ docker run -d -p 443:8888 -e "PASSWORD=foobar" vienno/h4q

Öppna sedan i webbläsare https://localhost, godkänn säkerhetsundantaget (TODO) och börja hacka på svenska öppna data! Förslag: Skapa en mapp "iPython Notebooks" och koda loss, kika på våra json-exempel och googla på vad man kan göra med matplotlib. Snart kommer entrypoint-stöd för att spara arbetet också (TODO, docker commit kommer fortsatt fungera). Notera att branchen i imagen (sandbox) inte är samma som för att skapa bilden (master), that's how we roll (TODO?).

TODO: Kanske installera java (med en curl-pipe) och dra igång Gephi grafiskt också. Vid närmare eftertanke ska det få bli sin egen image, behöver inte blanda det med scipylab

