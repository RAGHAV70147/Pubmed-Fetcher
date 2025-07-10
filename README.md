# PubMed Fetcher

A command-line tool to fetch PubMed papers with non-academic (e.g., biotech/pharma/company) author affiliations.

## Features

- Search PubMed with a custom query
- Filter papers to include only those with non-academic/company affiliations
- Output results to CSV or print to console
- Simple and fast CLI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pubmed-fetcher.git
   cd pubmed-fetcher
   ```

2. Install dependencies (recommended: use a virtual environment):
   ```bash
   poetry install
   ```

## Usage

Run the CLI to search PubMed and extract papers with company affiliations:

```bash
poetry run get-papers-list "your search query"
```

### Options

- `-f, --file <filename>`: Output results to a CSV file
- `-d, --debug`: Print debug information

### Example

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv
```

This will search PubMed for "cancer immunotherapy" and save papers with non-academic author affiliations to `results.csv`.

## Output

The output CSV will contain:

- PubmedID
- Title
- Publication Date
- Company Affiliation(s)

## License

MIT License

---

Made with ❤️ for the scientific community.
