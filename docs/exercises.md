# Opdrachten

Voer de onderstaande opdrachten in volgorde uit, iedere resource gebruikt informatie
van de vorige.

Start met het lezen van de README om te starten. Zorg dat je werkt in de Azure subscription genaamd "NAVARA Consulting Services".

Gebruik https://registry.terraform.io/providers/hashicorp/azurerm/2.99.0 voor het
bepalen van de argumenten en de dependencies voor jouw resource.

**Note:** Voor hulp, kijk in [references](./references.md) of vraag Yorick of Olaf.


## Opdracht 1: Provider

In Terraform wordt gewerkt met providers. Deze bevatten de "kennis" van de API's
waarmee gecommuniceerd wordt. Om bijvoorbeeld met Azure te praten, moet de provider
voor AzureRM toegevoegd worden.

### Randvoorwaarden

1. Voeg de `required_providers` toe aan `requirements.tf`.
2. Kies als versie `~> 2.99`. _Er is een versie 3.0, maar daar zitten de nodige
   wijzigingen in._
3. Voeg de `provider "azurerm"` toe aan `provider.tf`. Zorg dat je de property `skip_provider_registration = true` toevoegt, anders heb je meer rechten nodig dan je hebt gekregen.
4. In de terminal, ga naar de Terraform folder (`cd terraform`) en initialiseer Terraform (`terraform init`).

## Opdracht 2: Resource Group

Binnen Azure, alle resources vallen binnen een resource group. Iedereen heeft een
eigen resource group gekregen. Om resources naar deze resource group te laten
verwijzen, is het aan te raden hier een data source voor aan te maken. Voorbeelden van hoe data source van een resource group gedefinieerd moet worden kan je vinden in de Terraform documentatie.

NB Alle resources en data sources kunnen in main.tf toegevoegd worden.

**Voorbeeld: Gebruik van de data source in een andere resource**

```terraform
resource "resource_type" "example" {
  resource_group_name = data.azurerm_resource_group.iac.name
  location            = data.azurerm_resource_group.iac.location
}
```

Test of je geldige Terraform hebt geschreven met `terraform validate`.

Test wat je gaat deployen (en of je rechten goed staan) met `terraform plan`. Als het goed is, wordt er nog niks gepland.

## Opdracht 3: Database

Binnen Azure heet de NoSQL database "Cosmos". Deze biedt meerdere interfaces, maar
voor deze training gebruiken wij mongo. Je hebt twee resources nodig: een Cosmos DB Account en een Mongo Database die gelinkt is aan die account.

Tips: 
- De naam van de CosmosDB Account moet globaal uniek zijn.
- Er zijn 2 waardes van geo_location is verplicht. Gebruik voor de eerste  (`failover_priority = 0`) de locatie van de resource group. Gebruik voor de tweede  de waarde "northeurope". Dit is Ierland, de region twin van West Europe (Nederland).
- Gebruik `terraform plan` om te checken of je Terraform code geldig is en wat er gedeployed gaat worden. 
- **LET OP:** Doe de deploy stap (`terraform apply`) pas als laatste en wijzig deze niet meer. Deployen van deze resources kost 5-10 minuten. Bij veranderingen worden deze eerst verwijderd, dat kost 10-15 minuten.

## Opdracht 4: Back-end

De back-end applicatie is een "function app". Dit is een serverless offering van
Azure.

### Randvoorwaarden

1. Configuur de app dat hij Python draait.
2. Kies als SKU tier voor "dynamic" en size "Y1".
3. Voeg de connection string uit opdracht 3 als `MONGO_CONNECTION_STRING` toe aan de app_settings van de function app. Deze is te vinden in een Attribute van de Cosmos DB Account.

### Verwachte output

1. Output de url voor de backend naar `backend-url`.
2. Output de naam die je hebt toegekend aan de function app naar `backend-name`.

## Opdracht 5: Front-end

De front-end applicatie is geschreven in Vue en kan gedeployed worden op de CDN
(static site) van Azure. Gebruik hiervoor een storage account, en een storage blob met `storage_container_name=$web` en als naam `index.html`.

### Hint

Om een storage account een static website te laten serven moet het volgende block toegevoegd worden:

```terraform
static_website {
  index_document = "index.html"
}
```

Bij de storage blob, voeg toe:

```terraform
lifecycle {
    ignore_changes = [
      content_md5
    ]
  }
```

### Verwachte output

1. Output de url voor de frontend naar `frontend-url`.
2. Output de account name en account key naar `frontend-account-name` en `frontend-account-key`.

## Opdracht 6: Deployment van de applicatie code

Als alle onderdelen draaien, kunnen de back-end en front-end gedeployed worden. Dit kan je doen door het convenience script in `scripts` te draaien.

```bash
cd scripts
./deploy.sh
```
