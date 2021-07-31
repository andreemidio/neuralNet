import arxivscraper.arxivscraper as ax
import pandas as pd



scraper = ax.Scraper(category='cs', date_from='1991-08-14', date_until='2021-06-21', t=10,
                     # filters={'categories': ['stat.ml'], 'abstract': ['learning']}
                     )
output = scraper.scrape()

cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
df = pd.DataFrame(output, columns=cols)

df.to_csv('dataframe_2012_2021___.csv')
