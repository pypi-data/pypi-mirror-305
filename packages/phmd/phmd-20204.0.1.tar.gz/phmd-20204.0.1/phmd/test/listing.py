from phmd import metadata

#datasets.describe('CMAPSS')

#datasets.search()

metadata.search(domain="drive", nature='time-series')

print(metadata.search(domain="drive", nature='time-series', return_names=True))

metadata.describe('CWRU')