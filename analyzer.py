import requests
import sys


def analyze_repository(repo):
    url = f"https://api.github.com/repos/{repo}"

    response = requests.get(url)

    if response.status_code == 404:
        print("Repository not found.")
        return

    if response.status_code != 200:
        print(f"GitHub API error: {response.status_code}")
        return

    data = response.json()

    print("=" * 50)
    print("GitHub Repository Analyzer")
    print("=" * 50)

    print(f"\nRepository: {data['full_name']}")
    print(f"Description: {data['description']}")
    print(f"Language: {data['language']}")

    print(f"\n⭐ Stars: {data['stargazers_count']:,}")
    print(f"🍴 Forks: {data['forks_count']:,}")
    print(f"🐛 Open Issues: {data['open_issues_count']:,}")

    print(f"\nCreated: {data['created_at'][:10]}")
    print(f"Last Updated: {data['updated_at'][:10]}")

    print(f"\nRepository URL:")
    print(data['html_url'])

    print("=" * 50)


if len(sys.argv) != 2:
    print("Usage: python analyzer.py <owner/repository>")
else:
    analyze_repository(sys.argv[1])