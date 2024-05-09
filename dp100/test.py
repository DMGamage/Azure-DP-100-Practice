from azureml.core import Workspace,Datastore,Dataset

ws = Workspace.create(name='Azureml-01',
                      subscription_id='freee',
                      resource_group='azureml-SDKRG01',
                      create_resource_group=True,   # True if it does not exist
                      location='eastus2')

ws = Workspace.from_config(path="./config")

az_store = Datastore.get(ws,"azure_sdk_blob01")

csv_path = [(az_store,"Loan Data/Loan Approval Prediction.csv")]

loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

loan_dataset = loan_dataset.register(workspace=ws,name="Loan application prediction SDK",
                                     create_new_version=True)

