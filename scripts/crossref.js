#!/bin/node

const https = require('https')

let frompubdate = process.argv[1]
let untilpubdate = process.argv[2]
let base = `https://api.crossref.org/works?filter=from-pub-date:${frompubdate},until-pub-date:${untilpubdate}`
let ua = 'Liberate Science (https://github.com/chartgerink/doi-tracking; mailto:chris@libscie.org)'

// incorporate rate limiting
// headers X-Rate-Limit-Limit and X-Rate-Limit-Interval