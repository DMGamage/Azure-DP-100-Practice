from azureml.core import Workspace,Datastore,Dataset,Experiment
from azureml.core import Run

ws = Workspace.from_config("./config")
az_store = Datastore.get(ws,'azure_sdk_blob01')
az_dataset = Dataset.get_by_name(ws,'Loan Application Using SDK')
az_default_store = ws.get_default_datastore()

ws = Workspace.from_config("./config")

new_experiment = Experiment(workspace=ws, name= "Loan_SDK_Exp-01")

new_run= Run.get_context()

script_config = ScriptRunConfig(source_directory=".",
                                script="180 - Script To run.py")

new_run = new_experiment.submit(config=script_config)
