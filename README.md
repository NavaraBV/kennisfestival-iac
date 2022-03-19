# kennisfestival-iac

Demo repository for infrastructure as code.

## Installation

For the demonstration of this repository, the following tools should be installed.

- [Visual Studio Code](https://code.visualstudio.com/).
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Remote - Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Usage

Open the repository with Visual Studio Code and open the command palette (<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>p</kbd>). Search for "Remote-Containers: Reopen in Container" and hit enter. This will open the backend of Visual Studio Code in a Docker container. The frontend will still run on the host though. The container however will have all the necessary tools installed (e.g. Azure CLI and Terraform). The first installation can take a while (took 3 minutes on a MacBookPro16,1). To follow the progress, click on the pop-up at the bottom left.

The first time, you will need to log in to the Azure CLI. You can do this with the following command:

```bash
az login
```

This will open a browser in which you can log in with your NAVARA credentials. If the login was succesful, you will presented with something like (example from [Azure provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_cli)):

```
[
  {
    "cloudName": "AzureCloud",
    "id": "00000000-0000-0000-0000-000000000000",
    "isDefault": true,
    "name": "PAYG Subscription",
    "state": "Enabled",
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "user": {
      "name": "user@example.com",
      "type": "user"
    }
  }
]
```

## Development

The application to be deployed is a VueJs + Python + Azure functions + MongoDB application. To run this application locally, the following tools should be installed.

- NodeJS
- Python
- Docker + compose
- azure-functions-core-tools

After these tools are installed, the following three blocks should be executed in separate terminals.

**Terminal 1**

```bash
cd docker
docker-compose up -d
```

**Terminal 2**

```bash
cd backend
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
func start
```

**Terminal 3**

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
