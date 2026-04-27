from fabric_cicd import FabricWorkspace, publish_all_items
import os

workspace = FabricWorkspace(
    workspace_id=os.environ["FABRIC_WORKSPACE_ID"],
    repository_directory="./",
    item_type_in_scope=["Notebook"]
)

publish_all_items(workspace)
