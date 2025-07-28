# BDUK Task Browser Applications

This directory contains applications for Building Digital UK (BDUK) staff to browse candidate tasks, view associated research findings, and explore the comprehensive WORKBank dataset for workforce automation analysis.

## 🚀 Applications Overview

### 1. Command Line Browser (`browse_tasks.py`)
**Best for**: Quick task browsing in terminal environments

```bash
python bduk_app/browse_tasks.py
```

**Features**:
- Interactive numbered menu system
- Browse 3 local BDUK tasks with research findings
- Press Enter to continue after viewing each finding
- Enter `0` to exit
- Enhanced formatting with visual separators

**Use Case**: Terminal-based environments, quick access to research findings

---

### 2. GUI Browser (`gui_tasks.py`) 
**Best for**: Desktop environments with display capability

```bash
python bduk_app/gui_tasks.py
```

**Features**:
- Tkinter-based desktop GUI
- Browse local BDUK tasks
- Optional WORKBank dataset loading from Hugging Face
- Graphical interface with buttons and selections

**Limitations**: 
- Requires display environment (X11/GUI)
- Not suitable for headless containers or remote environments
- Limited data exploration capabilities

---

### 3. Web Application (`streamlit_tasks.py`) ⭐ **RECOMMENDED**
**Best for**: Container environments, collaborative use, comprehensive data analysis

```bash
streamlit run bduk_app/streamlit_tasks.py
```

**Features**:
- Modern web-based interface accessible via browser (`http://localhost:8501`)
- **Local BDUK Data**: Browse tasks with research findings via sidebar
- **WORKBank Integration**: Load and explore comprehensive datasets
- **Interactive Visualizations**: 
  - Automation desire distributions
  - Expert capacity assessments  
  - Human agency scale analysis
  - Task category breakdowns
  - Employment and wage data analysis
- **Smart Data Display**: Toggle between key columns and full dataset views
- **Session Management**: Persistent data access without re-downloading
- **Responsive Design**: Works on desktop and mobile browsers

## 📊 Data Sources

### Local BDUK Tasks (`bduk_tasks.csv`)
```csv
id,task,research_finding
1,Review broadband policy compliance,"Staff reported difficulties tracking policy updates. Research suggests using automated compliance monitoring tools."
2,Coordinate fibre rollout with local councils,"Stakeholder interviews indicated improved outcomes when dedicated communication channels were established."
3,Maintain project documentation,"Research found teams benefited from standardized templates and regular audits to ensure documentation completeness."
```

### WORKBank Dataset (SALT-NLP/WORKBank)
Comprehensive research dataset with three main components:

1. **Worker Desires** (5,731 records)
   - Worker perceptions of automation desire (1-5 scale)
   - Human agency requirements and preferences
   - Job security, enjoyment, and core skill ratings
   - Detailed reasoning for automation preferences

2. **Expert Ratings** (2,057 records)
   - Expert assessments of technological automation capacity
   - Physical requirements and uncertainty evaluations
   - Domain expertise and communication needs analysis

3. **Task Metadata** (2,131 records)
   - O*NET occupational task information
   - Employment numbers and annual wage data
   - Task importance, frequency, and category classifications

## 🛠️ Technical Requirements

### Dependencies
```toml
# Core dependencies (see pyproject.toml)
pandas          # Data manipulation and analysis
numpy           # Numerical computing
matplotlib      # Basic plotting
seaborn         # Statistical visualization
jupyter         # Notebook environment
streamlit       # Web application framework
datasets        # Hugging Face dataset integration
```

### Environment Setup
Using **uv** (recommended):
```bash
uv sync                    # Install all dependencies
uv run streamlit run bduk_app/streamlit_tasks.py
```

Using **pip**:
```bash
pip install streamlit datasets pandas numpy matplotlib seaborn
streamlit run bduk_app/streamlit_tasks.py
```

### Container Environment
The applications are optimized for dev container usage:
- Pre-configured Python 3.12 environment
- All dependencies installed automatically
- Port forwarding for Streamlit (8501)
- VS Code integration with extensions

## 🎯 Use Cases and Workflows

### Research Analysis Workflow
1. **Start with Streamlit app** for comprehensive overview
2. **Load WORKBank data** to explore automation research
3. **Analyze distributions** of worker desires vs expert assessments
4. **Examine specific occupations** and task categories
5. **Cross-reference** with BDUK-specific findings

### Quick Task Review
1. **Use command line browser** for rapid task scanning
2. **Review research findings** for specific BDUK tasks
3. **Note recommendations** for policy or process improvements

### Collaborative Research
1. **Deploy Streamlit app** on shared server or container
2. **Share browser URL** with team members
3. **Explore datasets together** during meetings
4. **Generate insights** from interactive visualizations

## 🔮 Future Enhancements

The codebase architecture supports planned LLM integration:

- **Automated Task Classification**: AI-powered categorization of new tasks
- **Intelligent Recommendations**: Context-aware automation suggestions
- **Natural Language Queries**: Ask questions about the data in plain English
- **Predictive Analytics**: Forecast automation impact across roles
- **Personalized Insights**: Tailored analysis based on user role and industry

### Example Future Features
```python
# Planned LLM integration examples
llm_analysis = analyze_task_with_ai(
    task="Review broadband policy compliance",
    context="government_regulatory"
)

recommendations = get_automation_recommendations(
    occupation="Policy Analyst", 
    expertise_level="intermediate"
)

insights = query_workbank(
    "What tasks do workers most want to automate in government roles?"
)
```

## 📁 File Structure
```
bduk_app/
├── README.md              # This documentation
├── bduk_tasks.csv         # Local BDUK task data (3 records)
├── browse_tasks.py        # Command-line interface
├── gui_tasks.py           # Desktop GUI (Tkinter)
└── streamlit_tasks.py     # Web application (recommended)
```

## 💡 Tips for Best Experience

1. **Start with Streamlit**: Most comprehensive features and best user experience
2. **Load WORKBank data once**: It persists in session state for exploration
3. **Use key columns view**: Easier to understand large datasets initially
4. **Explore distributions**: Great for understanding automation landscape
5. **Container friendly**: All apps work well in dev containers and remote environments

## 🐛 Troubleshooting

### Common Issues

**Streamlit app won't start**:
```bash
# Ensure streamlit is installed
pip install streamlit
# Run with explicit Python module
python -m streamlit run bduk_app/streamlit_tasks.py
```

**GUI app fails with display error**:
```bash
# GUI requires display environment - use Streamlit instead
streamlit run bduk_app/streamlit_tasks.py
```

**Dataset loading fails**:
- Check internet connection
- Verify `datasets` library is installed: `pip install datasets`
- Network/firewall may block Hugging Face access

**Container port access**:
- Ensure port 8501 is forwarded in your dev container
- Use VS Code "Ports" panel to open forwarded port
- Access via `http://localhost:8501` or forwarded URL
