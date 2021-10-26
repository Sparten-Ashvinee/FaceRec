from azureml.core import Workspace

subscription_id = '95d10a9c-129c-417e-bbcc-f2b3cb9853fc'
resource_group  = 'facerec-rg'
workspace_name  = 'facerec-ws'

try:
    ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
    ws.write_config()
    print('Library configuration succeeded')
except:
    print('Workspace not found')