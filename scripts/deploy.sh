#!/usr/bin/env bash

set -e

# Get variables from terraform
cd ../terraform
backend_name="$(terraform output -raw backend-name)"
backend_url="$(terraform output -raw backend-url)"
account_name="$(terraform output -raw frontend-account-name)"
account_key="$(terraform output -raw frontend-account-key)"
frontend_url="$(terraform output -raw frontend-url)"

# Deploy the backend
cd ../backend
func azure functionapp publish $backend_name

# Build the frontend
cd ../frontend
echo "VITE_ROOT_API=https://${backend_url}/api" > .env
npm install
npm run build

# Deploy the frontend
cd dist
az storage blob upload-batch -d \$web -s . --account-name $account_user --account-key $account_key

# Clean up frontend dist
cd ../
rm -rf dist

echo "Please visit the website at: $frontend_url"