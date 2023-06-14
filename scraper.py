import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all(string='citation needed')
    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(response.content)
    citations = soup.find_all(string='citation needed')
    
    report = ""
    for citation in citations:
        relevant_passage = citation.find_parent('p').text
        report += f"{relevant_passage}\n\n"
    
    return report

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    citations_count = get_citations_needed_count(url)
    citations_report = get_citations_needed_report(url)

    print(f"Number of citations needed: {citations_count}\n")
    print("Citations report:")
    print(citations_report)