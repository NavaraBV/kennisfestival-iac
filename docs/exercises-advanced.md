# Opdrachten (optional, advanced)

Met het werk wat wij gedaan hebben in de [vorige opdrachten](exercises.md), kan alle infra beschreven worden. Er zijn echter nog andere onderwerpen die nuttig zijn, zoals modules. Dit zijn (herbruikbare) stukken code, vergelijkbaar aan classes.

In ons geval is een module het beste te beschrijven als een folder binnen onze terraform directory, waar de input geregeld wordt door `vars` en de output door `output`. Dit levert dus bijvoorbeeld een dergelijke structuur op:

```
terraform/
├─ module1/
│  ├─ main.tf
│  ├─ output.tf
│  ├─ vars.tf
├─ main.tf
├─ output.tf
├─ provider.tf
├─ requirements.tf
├─ vars.tf
```

**Voorbeeld 1**

Stel, we hebben een module `module1` met als variabele `servers`. Deze module moeten wij vanuit de `main.tf` in de root directory aanroepen. Deze aanroep zou eruit zien als:

```terraform
module "servers" {
  source = "./module1"
  servers = 5
}
```

De `source` verwijst naar de map waar de code voor de module staat, terwijl `server` verwijst naar de variabelen die de module wilt weten.


**Voorbeeld 2**

De code binnen de module werkt verder exact hetzelfde als in de vorige opdrachten. Het teruggeven van informatie gebeurt echter via `output`. Stel, we hebben een `output` gedefinieerd met de naam `url`, ziet dit eruit als:

```terraform
resource "some_resource" "example" {
    url = module.servers.url
}
```

Om aan te geven dat je geinteresseerd bent in waardes uit een entiteit `module`, begin je de aanroep hiermee. De rest van de verwijzing is zoals standaard. 

**Note:** Mocht je nog steeds geinteresseerd zijn in bepaalde output, zal je deze dus 2 keer in output moeten opnemen. De eerste keer "exporteer" je het alleen tot buiten de module.

## Opdracht

Wij gaan in deze opdracht er van uit dat er een volledig draaiende omgeving staat. Omdat de database zou verhuizen binnen de state naar een andere module, zou deze gestopt en opnieuw gebouwd moeten worden. Dit kost ongeveer een half uur. Daarom laten we de database voor wat het is.

Herschrijf, met bovenstaande informatie over modules, de frontend en backend code naar aparte modules. Aan het einde moet het geheel nog steeds werken.