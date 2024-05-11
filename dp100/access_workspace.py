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


df = az_dataset.to_pandas_dataframe()

df_sub = df[["Married","Gender","Loan_Status"]]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
                dataframe=df_sub,
                target=az_default_store,
                name="Loan Dataset from Dataframe"

                )

files_list = ["./data/test.csv","./data/test1.csv"]
az_store.upload_files(files=files_list,
                      target_path="Loan Data/",
                      relative_root="./data/",
                      overite=True)


az_store.upload(src_dir="./data",
                target_path="Loan Data/data",
                overwrite=True)


