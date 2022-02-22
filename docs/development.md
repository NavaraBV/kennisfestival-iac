# Development

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
