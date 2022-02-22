# References

## Woordenlijst

| Term        | Betekenis|
| --- | --- |
| Argument | Informatie die doorgegeven wordt in resources of data sources. Een argument volgt altijd een `=` teken. Dit kan een enkele waarde zoals een string zijn, of een object. Argumenten komen als eerste in de documentatie van Terraform. |
| Attribute | Zodra een resource gemaakt of een data source geladen is, kan informatie uit dit object gehaald worden. Dit zijn de attributen. Deze staan onderaan de docs van Terraform. Niet alle argumenten zijn uit te lezen als attributen. |
| Block | Een (herhaalbaar), genest object. Deze blokken werken niet met een assignment, maar zien eruit als een resource; `block-name {}`. |
| Data source | Als een object al bestaat in Azure en je het object toch wilt gebruiken in terraform, e.g. een resource group, kan een data source gebruikt worden. Met een identifier koppelt Terraform het remote object aan de data source, waarna de attributen aangesproken kunnen worden. |
| Output | Een entity in terraform waarmee data vanuit een resource of data source op de commandline geprint kan worden. Hiermee is hij vervolgens in een script te gebruiken. |
| Provider | Deze plugins beschrijven de interface met API's voor Terraform. Voor het gebruik van AWS moet bijvoorbeeld een andere provider gebruikt worden dan voor Azure. Terraform kan ook voor lokale API's gebruikt worden, zoals voor de Docker Engine API. |
| Requirement | In het provider block worden argumenten voor de provider aangegeven. In de `required_providers` wordt gedefinieerd welke provider precies gebruikt moet worden. Dit gebeurt op basis van een source en een versie. |
| Resource | Resources zijn definities van remote objecten die nog niet bestaan en door Terraform aangemaakt worden. Met argumenten kan het object geconfigureerd worden, en met `terraform apply` wordt deze vervolgens aangemaakt. |
| Variable | Via variabelen is dynamisch input in te voeren. |

## Commando's

- `terraform init`: Initialiseert de benodigde mappen en download de required providers.
- `terraform fmt`: Het commando voor het correct formatten van de code. Met de flag `-recursive` wordt de code in subdirectories ook geformat.
- `terraform validate`: Een lokaal commando waarmee de validiteit van de objecten wordt gevalideerd. Dit zal niet checken of bijvoorbeeld een naming collision op een resouce zal optreden.
- `terraform plan`: Bij het opstellen van een plan wordt gecommuniceerd met de API. De output geeft een gedetailleerde weergave van de acties die doorgevoerd worden (e.g. aantal resources toegevoegd, aangepast en verwijderd). Met `-out` kan een plan opgeslagen worden in een file.
- `terraform apply`: Een apply voert de veranderingen beschreven in het plan door. Door `terraform apply` uit te voeren zonder argumenten, wordt een plan gegenereerd en meteen uitgevoerd. De file uit het vorige commando kan ook als argument gegeven worden en dan wordt dit plan uitgevoerd.
- `terraform destroy`: Verwijdert alle resources die beschreven staan in Terraform.

## Syntax

De verschillende entiteiten in Terraform hebben hun eigen syntax en manieren om aangeroepen te worden.

### Data source

**Declaratie**

```
data "azurerm_app_service" "example" {
  name                = "search-app-service"
  resource_group_name = "search-service"
}
```

**Referentie**

```
output "app_service_id" {
  value = data.azurerm_app_service.example.id
}
```

### Output

**Declaratie**

```
output "app_service_id" {
  value = data.azurerm_app_service.example.id
}
```

### Resource

**Declaratie**

```
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}
```

**Referentie**

```
output "app_service_id" {
  value = azurerm_resource_group.example.name
}
```

### Variable

Waardes voor de variable zijn op 4 manieren te zetten:

1. Een default waarde in de variable declaratie. _Deze gebruiken we gedurende deze sessie._
2. Via een `terraform.tfvars.json` file.
3. Een environment variable met de naam `TF_VAR_resource_group_name`.
4. Input vanuit de command line (als geen andere waarde gezet is).

**Declaratie**

```
variable "resource_group_name" {
  default     = "example-resources"
  description = "Name of the resource group"
}
```

**Referentie**

```
output "app_service_id" {
  value = var.resource_group_name
}
```

### Modules

Voor deze module gaan we er even vanuit dat er een variabele `servers` en een output `url` gedefinieerd is. Verder is de module gedefinieerd in de directory `module1`. In dit geval gebruiken wij een lokale module, maar het is ook heel goed mogelijk om een module van iemand anders te gebruiken. Deze is dan published in de registry van Terraform en als zodanig aan te roepen. Dit zullen wij hier echter verder niet gebruiken.

**Declaratie**

```
module "servers" {
  source = "./module1"
  servers = 5
}
```

**Referentie**

```
output "module_url" {
  value = module.servers.url
}
```