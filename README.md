# GitHub Repository Analyzer

A Python-based command-line tool that retrieves and analyzes GitHub repository information using the **GitHub API**. The application provides an overview of repository statistics, programming languages, activity, and contributor information in a structured and readable format.

## Overview

The GitHub Repository Analyzer was developed for practice by building a practical tool for analyzing public GitHub repositories.

Users can provide a GitHub repository, and the application retrieves relevant information and presents it through a formatted command-line interface.

## Features

- Retrieve GitHub repository information
- Display repository description and statistics
- Retrieve star, fork, issue, and repository size information
- Display repository creation and last-update dates
- Analyze programming language usage
- Retrieve contributor information
- Present results in a structured command-line interface

## Example Output

The analyzer was tested using the `microsoft/vscode` repository.

```text
============================================================
              GITHUB REPOSITORY ANALYZER
============================================================

 Repository
   microsoft/vscode

 Description
   Visual Studio Code

 Statistics
    Stars:        192,891
    Forks:        43,247
    Open Issues:  21,188
    Size:         1,500,500 KB

 Dates
    Created:      2015-09-03
    Last Updated: 2026-09-25

 Languages
    TypeScript:   96.1%
    CSS:           1.6%
    JavaScript:   0.6%
    Rust:         0.5%
    HTML:         0.4%

 Top Contributors
    bpasero
    jrieken
    Tyriar
```

*Example values may change as GitHub repository statistics are updated.*

## Technologies

- **Python**
- **GitHub REST API**
- **Requests**
- **JSON**
- **Git**
- **GitHub**

## How It Works

The application follows a simple workflow:

```text
User enters repository
        ↓
GitHub API request
        ↓
Retrieve repository data
        ↓
Process API response
        ↓
Analyze languages & contributors
        ↓
Display repository statistics
```

## Project Structure

```text
GitHub-Repository-Analyzer/
│
├── analyzer.py
├── README.md
```

Enter the GitHub repository you want to analyze when prompted.

For example:

```text
Enter repository: microsoft/vscode
```

The application will retrieve the available repository information and display the results in the terminal.

## Future Improvements

Potential improvements include:

- Adding a graphical or web-based interface
- Adding repository comparison functionality
- Generating visualizations of repository statistics
- Adding historical tracking of repository metrics
- Supporting GitHub authentication for higher API rate limits
- Exporting analysis results to CSV or JSON
- Adding automated tests

## Author
Ethan Tai
https://github.com/Ethanollt
