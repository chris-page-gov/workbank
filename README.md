<p align="center">
<img src="assets/workbank-text.svg" style="width: 40%; height:auto" />
</p>
<h3 align="center">
<p>Large-scale audit of worker desire and technological capability of AI agents for work
</h3>
<p align="center">
| <a href="https://arxiv.org/abs/2506.06576"><b>Paper</b></a> | <a href="https://futureofwork.saltlab.stanford.edu/"><b>Website</b></a> | <a href="https://huggingface.co/datasets/SALT-NLP/WORKBank"><b>HF Dataset</b></a> |
</p>
<img src="assets/workbank.png" style="width: 100%; height: auto" />

**Latest News** 🔥
- [2025/07] Our project is featured by <a href="https://hai.stanford.edu/news/what-workers-really-want-from-artificial-intelligence">Stanford HAI</a> and <a href="https://www.forbes.com/sites/moinroberts-islam/2025/06/30/future-of-work-41-of-ai-startups-build-automation-workers-dont-want/">Forbes</a> - check out the coverage!

## Overview

**WORKBank** (AI Agent Worker Outlook and Readiness Knowledge Bank) is a database that captures worker desire and technological capability of AI agents for occupational tasks.

The current version of WORKBank includes preferences from 1,500 U.S. domain workers and capability assessments from AI experts, covering over 844 tasks across 104 occupations collected between January and May 2025. This database stems from our project detailed in [Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce](https://arxiv.org/abs/2506.06576) that introduces a novel auditing framework to assess which occupational tasks workers want AI agents to automate or augment, and how those desires align with the current technological capabilities.

## Getting Started

### 1. Download the Data
```bash
# Clone this repository
git clone https://github.com/SALT-NLP/WORKBank.git
cd WORKBank

# Download WORKBank dataset files locally
python download_workbank_data.py
```

### 2. Explore the Data
```bash
# Launch interactive Streamlit app
streamlit run bduk_app/streamlit_tasks.py

# Or run Jupyter notebooks
jupyter notebook analysis/
```

### 3. Read the Documentation
- 📖 [BACKGROUND.md](BACKGROUND.md) - Research methodology and key findings
- 📖 [DATA_README.md](DATA_README.md) - Data structure and usage examples  
- 📖 [FIELD_DOCUMENTATION.md](FIELD_DOCUMENTATION.md) - Complete data dictionary with column descriptions

## Database Access

We host our database on Hugging Face. All variables are documented and explained in the [Code Book](codebook.pdf).

### Quick Start: Download Dataset Locally

For offline analysis and faster access, use our download script:

```bash
# Download all three main CSV files to ./data/ directory
python download_workbank_data.py

# Or specify a custom directory
python download_workbank_data.py --output-dir my_data
```

📖 **See [DATA_README.md](DATA_README.md) for detailed documentation on the download script and data structure.**

This downloads:
- `domain_worker_desires.csv` (5,731 rows) - Worker perceptions of automation desire and human agency
- `expert_rated_technological_capability.csv` (2,057 rows) - Expert assessments of technological automation capacity  
- `task_statement_with_metadata.csv` (2,131 rows) - O*NET task information with wages, employment, and skill data

### Alternative: Load Directly from Hugging Face

```python
from datasets import load_dataset

worker_desire = load_dataset("SALT-NLP/WORKBank", data_files="worker_data/domain_worker_desires.csv")["train"]

expert_ratings = load_dataset("SALT-NLP/WORKBank", data_files="expert_ratings/expert_rated_technological_capability.csv")["train"]

task_meta_data = load_dataset("SALT-NLP/WORKBank", data_files="task_data/task_statement_with_metadata.csv")["train"]
```

You can also manually download the CSV files [here](https://huggingface.co/datasets/SALT-NLP/WORKBank/tree/main).

## Data Analysis Code

- [automation_desire.ipynb](analysis/automation_desire.ipynb): Analysis of the distribution of automation desire ratings, analysis of the reason behind automation desire.
- [automation_viability.ipynb](analysis/automation_viability.ipynb): Analysis of the automation desire-capability landscape.
- [human_agency_scale.ipynb](analysis/human_agency_scale.ipynb): Analysis of the worker-desired human agency level and the expert-assessed feasible human agency level for different tasks.
- [human_skill_shift.ipynb](analysis/human_skill_shift.ipynb): Analysis of demographic and occupational coverage of WORKBank and mixed-effects model regression on worker responses.

## Repository Structure

```
workbank/
├── 📄 README.md                    # This file - main project documentation
├── 📄 BACKGROUND.md                # Research background and methodology
├── 📄 DATA_README.md               # Detailed data download and usage guide
├── 📄 FIELD_DOCUMENTATION.md       # Complete data dictionary with field descriptions
├── 📄 download_workbank_data.py    # Script to download WORKBank dataset locally
├── 📄 codebook.pdf                 # Data dictionary and variable documentation
├── 📄 pyproject.toml               # Python dependencies and project configuration
├── 📄 relevant_tasks.xlsx          # BDUK subset of relevant tasks (3,652 tasks)
│
├── 📁 analysis/                    # Jupyter notebooks for data analysis
│   ├── automation_desire.ipynb     # Automation desire patterns analysis
│   ├── automation_viability.ipynb  # Desire-capability landscape analysis
│   ├── human_agency_scale.ipynb    # Human agency scale analysis
│   ├── human_skill_shift.ipynb     # Skill transition analysis
│   ├── robustness.ipynb            # Dataset robustness and demographic analysis
│   └── README.md                   # Analysis notebooks documentation
│
├── 📁 data/                        # WORKBank dataset files (created by download script)
│   ├── domain_worker_desires.csv           # Worker perceptions (5,731 rows)
│   ├── expert_rated_technological_capability.csv  # Expert assessments (2,057 rows)
│   └── task_statement_with_metadata.csv    # Task metadata & wages (2,131 rows)
│
├── 📁 bduk_app/                    # BDUK Task Browser applications
│   ├── streamlit_tasks.py          # Web-based Streamlit interface
│   ├── browse_tasks.py             # Command-line task browser
│   ├── gui_tasks.py                # GUI task browser (tkinter)
│   ├── bduk_tasks.csv              # Sample BDUK tasks for demo
│   └── README.md                   # Application documentation
│
├── 📁 external_data/               # Additional datasets and external sources
│   ├── onet_data/                  # O*NET occupational data
│   ├── bls_*.csv                   # Bureau of Labor Statistics data
│   └── usage_from_anthropic.csv    # Claude.ai usage statistics
│
├── 📁 local/                       # Generated analysis outputs
│   ├── automation_desire/          # Automation desire plots by sector
│   ├── skill_info.csv             # Skill transition data
│   └── sector_dist.pdf            # Sector distribution analysis
│
└── 📁 assets/                      # Project assets and images
    ├── workbank.png               # Main project image
    └── workbank-text.svg          # Project logo
```

### Key Files

- **`download_workbank_data.py`**: Downloads the three main WORKBank CSV files for offline analysis
- **`relevant_tasks.xlsx`**: BDUK-specific subset of 3,652 tasks across 137 occupations  
- **`BACKGROUND.md`**: Comprehensive background on the research methodology and findings
- **`codebook.pdf`**: Complete data dictionary explaining all variables and scales

### Data Flow

1. **Raw Data**: O*NET occupational tasks → Worker surveys + Expert assessments → WORKBank dataset
2. **Download**: `download_workbank_data.py` → Local CSV files in `data/` directory  
3. **Analysis**: Jupyter notebooks in `analysis/` → Results and plots in `local/`
4. **Applications**: BDUK apps in `bduk_app/` provide interactive interfaces to explore the data

## Want to Launch the Audit in Your Organization?

Unlike traditional surveys, our auditing framework features an audio-enhanced interface and combines quantitative ratings with analysis of audio transcripts. This approach enables more calibrated and context-rich responses. We are also working to support input from additional modalities.

**If you're interested in deploying the audit to explore the future of work within your organization, feel free to fill out [the interest form](https://forms.gle/hFGyhYkD1VwMLVj59).**


## Citation

Please cite our paper if you use WORKBank database or analysis code in your work:

```
@misc{shao2025futureworkaiagents,
      title={Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce}, 
      author={Yijia Shao and Humishka Zope and Yucheng Jiang and Jiaxin Pei and David Nguyen and Erik Brynjolfsson and Diyi Yang},
      year={2025},
      eprint={2506.06576},
      archivePrefix={arXiv},
      primaryClass={cs.CY},
      url={https://arxiv.org/abs/2506.06576}, 
}
```
