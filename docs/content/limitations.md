# Limitations

:::{note}
_Almost_ all Python functionality is available in Brightway Live. However, there are some limitations. If you find that something is not working as expected, [please report it here](https://github.com/brightway-lca/brightway-live/discussions/new?category=report-limitation).
:::

## Filesystem (Data Storage)

### SQL Database Access

```{admonition} Related Issues
:class: note
https://github.com/brightway-lca/brightway-live/issues/10
```

Currently, an error is raised when trying to query a SQLite database in JupyterLite. This affects the use of Brightway, which stores data in sqlite databases through the `peewee` Python library. For instance, this simple test of the `peewee` library:

```python
from peewee import *

# Define a database object
db = SqliteDatabase('my_database.db')

# Define a model class
class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db

# Create the table in the database
db.connect()
db.create_tables([Person])

person1 = Person(name='Alice', age=25)
person1.save()
```

raises the following error:

```
DatabaseError: database disk image is malformed
```

Instead of the default storage location a different location at `/tmp/` must be specified for the database. This is done [by setting the `BRIGHTWAY_DIR` environment variable](https://docs.brightway.dev/en/latest/content/faq/data_management.html#how-do-i-change-my-data-directory).

### Searchable Databases

```{admonition} Related Issues
:class: note
https://github.com/pyodide/pyodide/discussions/4150 \
https://github.com/emscripten-core/emscripten/issues/11797
```

Brightway uses the `whoosh` package to index and search databases. Currently, an error is being raised when Brightway attempts to use the `whoosh` package. This is because `whoosh` attempts to use packages that are not available in WASM to lock files while accessing them. Emscripten currently does not have a "lock file" feature. Searching databases will therefore not work in Brightway Live.

### Restoring Brightway Project Backups (from `*.tar.gz`)

```{admonition} Related Issues
:class: note
https://github.com/brightway-lca/brightway-live/issues/37 \
https://github.com/jupyterlite/jupyterlite/issues/1153
```

Brightway can back up and restore projects using the 

```python
bw2io.backup_project_directory(project='default')
```

and

```python
bw2io.restore_project_directory(
    fp = '/brightway2-project-default-backup.14-September-2023-11-21AM.tar.gz',
    project_name = 'default',
    overwrite_existing = True
)
```

functions. The resulting backup file (`*.tar.gz`) can be as large as 300MB for a project based on Ecoinvent 3.9. Unfortunately, the current version of JupyterLite does not support the extraction of `*.tar.gz` files larger than ~1MB. This is likely due to a bug and does not present an inherent limitation of JupyterLite or WASM.

### Downloading Databases (eg. USEEIO)

```{admonition} Related Issues
:class: note
test
```