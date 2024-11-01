# create a folder named snapdiff and inside it a folder called snapshots
# create a file called snapdiff_config.yaml and add the following content:
# snap_dir: snapshots
# state: dev
# if get ignore the paths before the current directory
# add snapdiff to the path and snapdiff_config.yaml also


# command for adding @snapper decorator to all functions in a file
# command for removing @snapper decorator from all functions in a file with id
# command to add ids to all decorators in a file or group of files

from invoke import task
from invoke_utils import add_decorator_to_functions


@task
def add_snappers(c, file_path, decorator_name="@snapper", decorator_params=None):
    add_decorator_to_functions(file_path, decorator_name, decorator_params)
