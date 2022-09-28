# ms-openhack-serverless-team-2-sept-2022

az group create -n rg-clesne -l francecentral

az storage account create -g rg-clesne -n storageclesne

az storage account update -g rg-clesne -n storageclesne --set kind=StorageV2

az functionapp create -c francecentral -n fa-clesne-step2 --os-type linux -g rg-clesne --runtime python -s storageclesne --functions-version 4

func azure functionapp publish fa-clesne-step2

az logic workflow create -l francecentral -g rg-clesne -n la-clesne-step2 --definition la-clesne-step2.json
