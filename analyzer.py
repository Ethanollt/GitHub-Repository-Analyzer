import requests
import sys


def analyze_repository(repo):
    # --------------------------------------------------
    # 1. Get basic repository information
    # --------------------------------------------------

    repo_url = f"https://api.github.com/repos/{repo}"
    response = requests.get(repo_url)

    if response.status_code == 404:
        print("\n Repository not found.")
        return

    if response.status_code != 200:
        print(f"\n GitHub API error: {response.status_code}")
        return

    data = response.json()

    # --------------------------------------------------
    # 2. Get language information
    # --------------------------------------------------

    languages_url = f"https://api.github.com/repos/{repo}/languages"
    languages_response = requests.get(languages_url)

    if languages_response.status_code == 200:
        languages = languages_response.json()
    else:
        languages = {}

    # Calculate total bytes
    total_bytes = sum(languages.values())

    # --------------------------------------------------
    # 3. Get contributors
    # --------------------------------------------------

    contributors_url = f"https://api.github.com/repos/{repo}/contributors"
    contributors_response = requests.get(contributors_url)

    if contributors_response.status_code == 200:
        contributors = contributors_response.json()
    else:
        contributors = []

    # --------------------------------------------------
    # 4. Get recent commits
    # --------------------------------------------------

    commits_url = f"https://api.github.com/repos/{repo}/commits"
    commits_response = requests.get(commits_url)

    if commits_response.status_code == 200:
        commits = commits_response.json()
    else:
        commits = []

    # --------------------------------------------------
    # 5. Display repository information
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("              GITHUB REPOSITORY ANALYZER")
    print("=" * 60)

    print("\n Repository")
    print(f"   {data['full_name']}")

    print("\n Description")
    print(f"   {data['description'] or 'No description available'}")

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    print("\n Statistics")

    print(f"    Stars:        {data['stargazers_count']:,}")
    print(f"    Forks:        {data['forks_count']:,}")
    print(f"    Open Issues:  {data['open_issues_count']:,}")
    print(f"    Size:         {data['size']:,} KB")

    # --------------------------------------------------
    # Dates
    # --------------------------------------------------

    print("\n Dates")

    print(f"   Created:         {data['created_at'][:10]}")
    print(f"   Last Updated:    {data['updated_at'][:10]}")

    # --------------------------------------------------
    # Languages
    # --------------------------------------------------

    print("\n Languages")

    if languages:

        for language, bytes_used in languages.items():

            percentage = (bytes_used / total_bytes) * 100

            # Only show languages that represent at least 0.1%
            if percentage >= 0.1:

                bar_length = int(percentage / 5)

                bar = "█" * bar_length

                print(
                    f"   {language:<20}"
                    f"{bar:<20}"
                    f"{percentage:5.1f}%"
                )

    else:
        print("   No language data available.")

    # --------------------------------------------------
    # Contributors
    # --------------------------------------------------

    print("\n Contributors")

    if contributors:

        print(f"   Showing top {min(5, len(contributors))} contributors:")

        for index, contributor in enumerate(contributors[:5], start=1):

            username = contributor["login"]
            contributions = contributor["contributions"]

            print(
                f"   {index}. "
                f"{username:<25}"
                f"{contributions:,} contributions"
            )

    else:
        print("   Contributor data unavailable.")

    # --------------------------------------------------
    # Recent commits
    # --------------------------------------------------

    print("\n Recent Commits")

    if commits:

        for commit in commits[:5]:

            sha = commit["sha"][:7]

            message = commit["commit"]["message"]

            # Only display the first line of a commit message
            message = message.split("\n")[0]

            # Prevent extremely long messages
            if len(message) > 60:
                message = message[:57] + "..."

            print(f"   {sha}  {message}")

    else:
        print("   Commit data unavailable.")

    # --------------------------------------------------
    # Repository URL
    # --------------------------------------------------

    print("\n Repository URL")

    print(f"   {data['html_url']}")

    print("\n" + "=" * 60)


# ------------------------------------------------------
# Command-line argument handling
# ------------------------------------------------------

if len(sys.argv) != 2:

    print("\nUsage:")
    print("   py analyzer.py <owner/repository>")

    print("\nExample:")
    print("   py analyzer.py microsoft/vscode")

else:

    analyze_repository(sys.argv[1])