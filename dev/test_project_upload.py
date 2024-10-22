# %%

import bw2data as bd
import bw2io as bi

def check_for_useeio_brightway_project():
    """
    Checks if the USEEIO-1.1 Brightway project is installed.
    If not, installs it. Shows Panel notifications for the user.

    Returns
    -------
    SQLiteBackend
        bw2data.backends.base.SQLiteBackend of the USEEIO-1.1 database
    """
    if 'USEEIO-1.1' not in bd.projects:
        bi.install_project(project_key="USEEIO-1.1", overwrite_existing=True)
    else:
        pass
    bd.projects.set_current(name='USEEIO-1.1')


check_for_useeio_brightway_project()

bi.backup.backup_project_directory(
    project=bd.projects.current,
)