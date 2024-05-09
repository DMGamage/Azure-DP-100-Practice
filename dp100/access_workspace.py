from azureml.core import Workspace,Datastore,Dataset

ws = Workspace.from_config("./config")

ws_list = Workspace.list(subcription_id="223434-44855-2232424-232323")
ws_list = list(ws_list)

for name in ws_list:
    print(name)


# Access the default datastores from workspace

az_default_store = ws.get_default_datastore()

#List all the datasores

store_list = list(ws.datastores)

#Get the datasets from workspace by name

az_dataset = Dataset.get_by_name(ws,"Loan application using SDK")

# list dataset froma worspace

ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)



