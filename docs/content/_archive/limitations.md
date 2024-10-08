# Limitations (ARCHIVED)

## Network Connections

### Downloading Databases (eg. USEEIO)

Some functions of `bw2io` can download databases from the internet. For instance, [the following command](https://docs.brightway.dev/en/latest/api/bw2io/index.html#bw2io.useeio11) will download the USEEIO database:

```python
bw2io.useeio11()
```

Unfortunately, due to [a limitation of Pyodide](https://pyodide.org/en/stable/project/roadmap.html#write-http-client-in-terms-of-web-apis):

> Python packages make an extensive use of packages such as `requests` to synchronously fetch data. We currently can’t use such packages since sockets are not available in Pyodide. 

this command will fail with the following error:

```python
ImportError: Can't connect to HTTPS URL because the SSL module is not available.
```