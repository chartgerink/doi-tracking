# Tracking Digital Object Identifiers

Just like phonebooks 📗 resolve names to a phone 📞 number, Digital Object Identifiers (shorthand: DOI) resolve a stable URL to another, less stable URL. In order for this to function, we need to trust the middle-people who are involved in the resolving. Let's find out by seeing how often the DOIs resolve to something else 😊

__NOTE: This is a [Liberate Science](https://github.com/libscie/) project and will be moved to the organization account upon a v1.0.0__

## Roadmap

In chronological order, I think. 

- [ ] Set up proper calls to CrossRef per [their etiquette](https://github.com/CrossRef/rest-api-doc#etiquette)
- [ ] Setup script for downloading CrossRef DOIs responsibly
  - [ ] Ingest on day0
  - [ ] Update script for each day (`cron.daily`)
  - [ ] Ingest into MongoDB after each query
- [ ] Setup MongoDB instance on AWS
- [ ] Create backups of MongoDB
- [ ] Setup script for resolving
  - [ ] Ingest results into MongoDB
- [ ] Set up DataCite calls
- [ ] Repeat CrossRef steps
  - [ ] Ingest into MongoDB
- [ ] Make data publicly available

## Status

The project just started. 

## Render

```r
rmarkdown::render('doi-primer.Rmd', 'bookdown::html_document2')
```