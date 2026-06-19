import json
from typing import List, Dict, Any

SITE_DATA = {
    "site_name": "HTH Home",
    "url": "https://home-ssl-hth.com",
    "keywords": ["hth", "home", "ssl", "secure"],
    "tags": ["technology", "security", "homepage"],
    "description": "A secure home page with SSL support and core hth services."
}

EXTRA_SITES: List[Dict[str, Any]] = [
    {
        "name": "HTH Docs",
        "url": "https://docs.hth.com",
        "keywords": ["hth", "documentation", "guide"],
        "tags": ["docs", "reference"],
        "description": "Official documentation for hth platform."
    },
    {
        "name": "HTH Blog",
        "url": "https://blog.hth.com",
        "keywords": ["hth", "blog", "news"],
        "tags": ["blog", "updates"],
        "description": "Latest news and articles about hth."
    }
]


def format_keywords(keywords: List[str]) -> str:
    """Format a list of keywords into a readable string."""
    if not keywords:
        return "N/A"
    return ", ".join(keywords)


def format_tags(tags: List[str]) -> str:
    """Format a list of tags into a readable string."""
    if not tags:
        return "N/A"
    return " | ".join(tags)


def generate_site_summary(site: Dict[str, Any]) -> str:
    """Generate a structured summary for a single site entry."""
    separator = "-" * 50
    lines = [
        separator,
        f"Site Name: {site.get('name', site.get('site_name', 'Unknown'))}",
        f"URL: {site.get('url', 'N/A')}",
        f"Keywords: {format_keywords(site.get('keywords', []))}",
        f"Tags: {format_tags(site.get('tags', []))}",
        f"Description: {site.get('description', 'No description available.')}",
        separator,
    ]
    return "\n".join(lines)


def generate_full_summary(
    primary_site: Dict[str, Any],
    extra_sites: List[Dict[str, Any]]
) -> str:
    """Generate a full structured summary including primary and extra sites."""
    sections = [
        "=== HTH Sites Summary ===",
        "",
        "-- Primary Site --",
        generate_site_summary(primary_site),
        "",
        "-- Additional Sites --",
    ]

    if not extra_sites:
        sections.append("No additional sites registered.")
    else:
        for idx, site in enumerate(extra_sites, start=1):
            sections.append(f"Site #{idx}:")
            sections.append(generate_site_summary(site))
            sections.append("")

    sections.append("=== End of Summary ===")
    return "\n".join(sections)


def save_summary_to_file(content: str, filename: str = "site_summary.txt") -> None:
    """Save the generated summary to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Summary saved to {filename}")
    except OSError as e:
        print(f"Error saving file: {e}")


def display_summary(summary: str) -> None:
    """Print the summary to console."""
    print(summary)


def main() -> None:
    """Main entry point to generate and display site summary."""
    summary = generate_full_summary(SITE_DATA, EXTRA_SITES)
    display_summary(summary)
    save_summary_to_file(summary)


if __name__ == "__main__":
    main()