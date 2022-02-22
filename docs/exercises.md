# Opdrachten

Voer de onderstaande opdrachten in volgorde uit, iedere resource gebruikt informatie
van de vorige.
Gebruik https://registry.terraform.io/providers/hashicorp/azurerm/latest voor het
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
3. Voeg de `provider "azurerm"` toe aan `provider.tf`.

## Opdracht 2: Resource Group

Binnen Azure, alle resources vallen binnen een resource group. Iedereen heeft een
eigen resource group gekregen. Om resources naar deze resource group te laten
verwijzen, is het aan te raden hier een data source voor aan te maken.

**Voorbeeld: Gebruik van de data source**

```terraform
resource "resource_type" "example" {
  resource_group_name = data.azurerm_resource_group.iac.name
  location            = data.azurerm_resource_group.iac.location
}
```

## Opdracht 3: Database

Binnen Azure heet de NoSQL database "Cosmos". Deze biedt meerdere interfaces, maar
voor deze training gebruiken wij mongo.

## Opdracht 4: Back-end

De back-end applicatie is een "function app". Dit is een serverless offering van
Azure.

### Randvoorwaarden

1. Configuur de app dat hij Python draait.
2. Kies als SKU tier voor "dynamic" en size "Y1".
3. Voeg de connection string uit opdracht 3 als `MONGO_CONNECTION_STRING` toe aan de
   function app.

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

### Verwachte output

1. Output de url voor de frontend naar `frontend-url`.
2. Output de account name en account key naar `frontend-account-name` en `frontend-account-key`.

## Opdracht 6: Deployment

Als alle onderdelen draaien, kunnen de back-end en front-end gedeployed worden. Dit kan je doen door het convenience script in `scripts` te draaien.

```bash
cd scripts
./deploy.sh
```
