# ShieldScrape: Cloud Data Collection

Collect and process football standings with archived scraping code and an AWS-oriented project design.

## How It Works

The main source archive contains Scrapy spiders for league statistics, an HTTP-fetching Lambda example, S3 cleaning code, and a DynamoDB-loading script. The reports discuss container execution, storage, query, and visualization components. The smaller web-scraper archive contains an earlier job-listing example, while scraper_test.py and teams.jsonl provide a separate scraping experiment and sample output.

## Main Tasks

- Inspect the league-statistic extraction and output fields in the source archive.
- Follow the S3 transformation and database-loading code.
- Compare source components with the architecture and submitted reports.

## Files

- [scraper_test.py](scraper_test.py): Python implementation or analysis script.
- [ShieldScrape_Final_Report.pdf](ShieldScrape_Final_Report.pdf): assignment instructions or submitted report in PDF format.
- [ShieldScrape_Midterm_Report.pdf](ShieldScrape_Midterm_Report.pdf): assignment instructions or submitted report in PDF format.
- [ShieldScrape_Midterm_Report.docx](ShieldScrape_Midterm_Report.docx): editable assignment or report document.
- [shieldscraper-main.zip](shieldscraper-main.zip): archived source or supporting submission files.
- [web scraper.zip](web%20scraper.zip): archived source or supporting submission files.
- [ECC presentation.pptx](ECC%20presentation.pptx): supporting lab file.
- [Final_Architecture.png](Final_Architecture.png): supporting lab file.
- [diagram-export-5-2-2025-8_59_14-PM.png](diagram-export-5-2-2025-8_59_14-PM.png): supporting lab file.
- [teams.jsonl](teams.jsonl): supporting lab file.

## Related Design

The [proposal](../Project_Proposal/) describes the intended architecture and project goals. The reports and archived source should be read separately when assessing which components are demonstrated by code.
