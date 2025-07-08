from typing import List, Tuple

def is_non_academic(affiliation: str) -> bool:
    if not affiliation:
        return False
    academic_terms = ["university", "college", "institute", "school", "hospital", "clinic", "department"]
    return not any(term in affiliation.lower() for term in academic_terms)

def extract_company_affiliations(affiliations: List[str]) -> List[str]:
    return [a for a in affiliations if is_non_academic(a)]
