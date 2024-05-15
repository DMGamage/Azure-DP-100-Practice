from azureml.core import workspace,Datastore,Dataset,Experiment

ws = workspace.from_config("./config")
az_store = Datastore.get(ws,'azure_sdk_blob01')
az_dataset = Dataset.get_by_name(ws,'Loan Application Using SDK')
az_default_store = ws.get_default_datastore()


experiment = Experiment(workspace=ws,
                        name = "Load-SDK-Exp01")

new_run = experiment.start_logging()

new_run.complete()