from azureml.core import Workspace,Datastore,Dataset,Experiment

ws = Workspace.from_config("./config")
az_store = Datastore.get(ws,'azure_sdk_blob01')
az_dataset = Dataset.get_by_name(ws,'Loan Application Using SDK')
az_default_store = ws.get_default_datastore()

ws = Workspace.from_config("./config")

new_experiment = Experiment(workspace=ws, name= "Loan_script")

script_config = ScriptRunConfig(source_directory=".",
                                script="180 - Script To run.py")

new_run = new_experiment.submit(config=script_config)
