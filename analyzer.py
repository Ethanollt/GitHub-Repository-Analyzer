import requests
import sys


def analyze_repository(repo):
    # Get basic repository information
    repo_url = f"https://api.github.com/repos/{repo}"
    response = requests.get(repo_url)

    if response.status_code == 404:
        print("\n Repository not found.")
        return

    if response.status_code != 200:
        print(f"\n GitHub API error: {response.status_code}")
        return

    data = response.json()

    # Get language information
    languages_url = f"https://api.github.com/repos/{repo}/languages"
    languages_response = requests.get(languages_url)

    if languages_response.status_code == 200:
        languages = languages_response.json()
    else:
        languages = {}

    # Calculate language percentages
    total_bytes = sum(languages.values())

    print("\n" + "=" * 55)
    print("              GITHUB REPOSITORY ANALYZER")
    print("=" * 55)

    print(f"\n Repository")
    print(f"   {data['full_name']}")

    print(f"\n Description")
    print(f"   {data['description'] or 'No description available'}")

    print(f"\n Statistics")
    print(f"    Stars:        {data['stargazers_count']:,}")
    print(f"    Forks:        {data['forks_count']:,}")
    print(f"    Open Issues:  {data['open_issues_count']:,}")
    print(f"    Size:         {data['size']:,} KB")

    print(f"\n Dates")
    print(f"   Created:         {data['created_at'][:10]}")
    print(f"   Last Updated:    {data['updated_at'][:10]}")

    print(f"\n Languages")

    if languages:
        for language, bytes_used in languages.items():
            percentage = (bytes_used / total_bytes) * 100
            bar_length = int(percentage / 5)

            bar = "█" * bar_length

            print(f"   {language:<15} {bar:<20} {percentage:5.1f}%")
    else:
        print("   No language data available.")

    print("\n Repository URL")
    print(f"   {data['html_url']}")

    print("\n" + "=" * 55)


# Make sure the user provided a repository
if len(sys.argv) != 2:
    print("\nUsage:")
    print("   py analyzer.py <owner/repository>")
    print("\nExample:")
    print("   py analyzer.py facebook/react")
else:
    analyze_repository(sys.argv[1])