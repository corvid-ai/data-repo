## PROJECT NIGHTINGALE DATA REPOSITORY

- This repo contains the compressed format of our current dataset
- NB: This is currently under testing, wait for final release for deployment, in the meantime you can test it out

### Installing package

```bash
pip install corvidData==0.0.1
```

### Testing package

```
from corvidData import twi_data

df = twi_data.dataset()
print(df)
```
