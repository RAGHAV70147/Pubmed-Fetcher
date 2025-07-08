import argparse
import csv
from pubmed_fetcher.fetch import search_pubmed, fetch_details
from pubmed_fetcher.parser import extract_company_affiliations

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with biotech/pharma affiliations.")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true")

    args = parser.parse_args()

    if args.debug:
        print(f"Querying PubMed for: {args.query}")

    ids = search_pubmed(args.query)
    papers = fetch_details(ids)

    results = []
    for paper in papers:
        companies = extract_company_affiliations(paper["Affiliations"])
        if companies:
            results.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Company Affiliation(s)": "; ".join(set(companies))
            })

    if not results:
        print("No results with non-academic authors found.")
        return

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()
