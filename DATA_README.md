# WORKBank Data Download Script

This directory contains the main script for downloading and managing WORKBank dataset files.

## Quick Start

```bash
# Download all WORKBank CSV files to ./data/ directory
python download_workbank_data.py

# Download to a custom directory
python download_workbank_data.py --output-dir my_custom_folder
```

## What Gets Downloaded

The script downloads three core CSV files from the [SALT-NLP/WORKBank](https://huggingface.co/datasets/SALT-NLP/WORKBank) dataset on Hugging Face:

### 1. `domain_worker_desires.csv` (1.7MB, 5,731 rows)
**Worker perceptions of automation desire and human agency**

Contains worker survey responses including:
- Automation Desire Rating (1-5 scale)
- Human Agency Scale Rating (H1-H5) 
- Job Security Concerns
- Task Enjoyment Ratings
- Detailed reasoning for preferences

Key columns:
- `Task ID`, `Occupation (O*NET-SOC Title)`, `Task`
- `Automation Desire Rating`, `Human Agency Scale Rating`
- `Core Skill Rating`, `Job Security Rating`, `Enjoyment Rating`
- Various reason codes for automation preferences

### 2. `expert_rated_technological_capability.csv` (341KB, 2,057 rows)
**Expert assessments of technological automation capacity**

Contains AI expert evaluations including:
- Current automation capability assessments
- Technical feasibility ratings
- Human agency requirements from technology perspective

Key columns:
- `Task ID`, `Occupation (O*NET-SOC Title)`, `Task`
- `Automation Capacity Rating`, `Human Agency Scale Rating`
- Task characteristic ratings (Physical Actions, Uncertainty, Domain Expertise, etc.)

### 3. `task_statement_with_metadata.csv` (541KB, 2,131 rows)
**O*NET task information with wages, employment, and skill data**

Contains occupational metadata including:
- Task descriptions from O*NET database
- Wage and employment statistics
- Work activity classifications
- Task importance and frequency ratings

Key columns:
- `O*NET-SOC Code`, `Occupation (O*NET-SOC Title)`, `Task`
- `Occupation Mean Annual Wage`, `Occupation Employment`
- `Skill (O*NET Work Activity)`, `Category`, `Importance`, `Frequency`

## File Structure After Download

```
data/
├── domain_worker_desires.csv              # Worker survey responses
├── expert_rated_technological_capability.csv   # Expert technical assessments  
└── task_statement_with_metadata.csv       # O*NET metadata & wages
```

## Usage Examples

### Loading Data for Analysis

```python
import pandas as pd

# Load all three datasets
worker_desire = pd.read_csv('data/domain_worker_desires.csv')
expert_ratings = pd.read_csv('data/expert_rated_technological_capability.csv') 
task_metadata = pd.read_csv('data/task_statement_with_metadata.csv')

# Basic info
print(f"Worker responses: {len(worker_desire):,} records")
print(f"Expert ratings: {len(expert_ratings):,} records") 
print(f"Task metadata: {len(task_metadata):,} records")
```

### Finding High Automation Desire Tasks

```python
# Tasks workers most want automated (rating >= 4)
high_desire = worker_desire[worker_desire['Automation Desire Rating'] >= 4]
top_tasks = high_desire.groupby('Task')['Automation Desire Rating'].mean().sort_values(ascending=False)
print("Top 10 tasks workers want automated:")
print(top_tasks.head(10))
```

### Analyzing Human Agency Scale

```python
# Distribution of Human Agency Scale preferences
has_distribution = worker_desire['Human Agency Scale Rating'].value_counts().sort_index()
print("Human Agency Scale Distribution:")
for level, count in has_distribution.items():
    print(f"H{level}: {count:,} responses")
```

## Data Sources

- **Original Research**: [Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce](https://arxiv.org/abs/2506.06576)
- **Dataset Repository**: [SALT-NLP/WORKBank on Hugging Face](https://huggingface.co/datasets/SALT-NLP/WORKBank)
- **Task Definitions**: U.S. Department of Labor's O*NET Database
- **Survey Period**: January - May 2025

## Script Options

```bash
python download_workbank_data.py --help
```

```
usage: download_workbank_data.py [-h] [--output-dir OUTPUT_DIR]

Download WORKBank dataset files

options:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Directory to save CSV files (default: data)
```

## Dependencies

The script requires:
- `datasets` - For downloading from Hugging Face Hub
- `pandas` - For data manipulation and CSV export
- `pathlib` - For file system operations (built-in)

These are automatically managed by the project's `pyproject.toml` configuration.

## Troubleshooting

### Network Issues
If download fails due to network connectivity:
```bash
# Retry with different timeout
python download_workbank_data.py
```

### Permission Issues
If you get permission errors:
```bash
# Use a different output directory
python download_workbank_data.py --output-dir ~/workbank_data
```

### Missing Dependencies
If you get import errors:
```bash
# Install dependencies
pip install datasets pandas
# Or using uv
uv add datasets pandas
```

## Data Updates

The WORKBank dataset is versioned. To get the latest version:
1. Delete the existing `data/` directory
2. Re-run the download script
3. Check the [Hugging Face repository](https://huggingface.co/datasets/SALT-NLP/WORKBank) for update notes

## Related Files

- [`BACKGROUND.md`](../BACKGROUND.md) - Research methodology and findings
- [`codebook.pdf`](../codebook.pdf) - Complete variable documentation  
- [`analysis/`](../analysis/) - Jupyter notebooks using this data
- [`relevant_tasks.xlsx`](../relevant_tasks.xlsx) - BDUK-specific task subset
