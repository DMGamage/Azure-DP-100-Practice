from azureml.core import Workspace,Datastore,Dataset,Experiment,ScriptRunConfig
from azureml.core import Run

ws = Workspace.from_config("./config")


new_experiment = Experiment(workspace=ws, name= "training_script")
#Create custom environment
from azureml.core import Environment
from azureml.core.environment import CondaDependencies

myenv2 = Environment(name="MyEnvironment")

# Create dependencies 
myenv2_dep = CondaDependencies.create(conda_packages=['scikit-learn'])

myenv2.python.conda_dependencies = myenv2_dep


myenv2.register(ws)


script_config = ScriptRunConfig(source_directory=".",
                                script="200 - Training Script.py",
                                environment=myenv1)

new_run = new_experiment.submit(config=script_config)

new_run.wait_for_completion()
