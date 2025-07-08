import requests
from typing import List, Dict
from xml.etree import ElementTree

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, max_results: int = 50) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "xml"
    }
    response = requests.get(BASE_URL + "esearch.fcgi", params=params)
    tree = ElementTree.fromstring(response.content)
    return [id_elem.text for id_elem in tree.findall(".//Id")]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(BASE_URL + "efetch.fcgi", params=params)
    return parse_papers(ElementTree.fromstring(response.content))

def parse_papers(xml_root) -> List[Dict]:
    papers = []
    for article in xml_root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "Publication Date": article.findtext(".//PubDate/Year"),
            "Authors": [],
            "Emails": [],
            "Affiliations": []
        }
        for author in article.findall(".//Author"):
            name = author.findtext("LastName") or ""
            affils = author.findall(".//AffiliationInfo/Affiliation")
            paper["Authors"].append(name)
            paper["Affiliations"].extend([a.text for a in affils if a is not None])
        papers.append(paper)
    return papers
