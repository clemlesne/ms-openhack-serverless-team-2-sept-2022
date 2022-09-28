# Microsoft OpenHack Serverless - Team 2 - Stept 2022

## Development

### Continuous deployment

#### Usage

Each time a commit is pushed:

1. Git repository is cloned
2. Python is installed
3. Python dependencies are installed
4. The Function App is pushed to Azure

#### Pipeline first setup

```
# Generate the credentials for deploying the Function App

az ad sp create-for-rbac --name "fa-rating-team2-oh-fc" --role contributor --scopes /subscriptions/40b7492d-d085-4700-9d53-59c0db2e7e3c/resourceGroups/rg-team2/providers/Microsoft.Web/sites/fa-rating-team2-oh-fc --sdk-auth
```

Store the output secret from the CLI. Create a new secret fir GitHub Actions named `AZURE_CREDENTIALS` with that content.
