"""
BDUK Task Browser - Streamlit Web Application

This application provides a web-based interface for browsing BDUK (Building Digital UK) 
tasks and their associated research findings. It also integrates with the WORKBank dataset
from Hugging Face to provide comprehensive automation and task analysis capabilities.

Author: BDUK Team
Date: 2025
"""

import streamlit as st
import csv
import os

# Path to the local BDUK tasks CSV file
DATA_FILE = os.path.join(os.path.dirname(__file__), 'bduk_tasks.csv')

# Configure the Streamlit page with title and layout
st.set_page_config(page_title="BDUK Task Browser", layout="centered")
st.title("BDUK Task Browser")

def load_tasks():
    """
    Load BDUK tasks from the local CSV file.
    
    Returns:
        list: List of dictionaries containing task data with keys:
              'id', 'task', 'research_finding'
    """
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Load the local BDUK tasks data
tasks = load_tasks()

# === SIDEBAR: LOCAL BDUK TASK SELECTION ===
st.sidebar.header("Browse Tasks")
task_names = [task['task'] for task in tasks]
selected_task = st.sidebar.selectbox("Select a task:", task_names)

# === MAIN AREA: DISPLAY SELECTED TASK RESEARCH FINDINGS ===
if selected_task:
    # Find the selected task in the data
    task = next(t for t in tasks if t['task'] == selected_task)
    st.subheader(f"Research findings for: {task['task']}")
    st.write(task['research_finding'])

# === SIDEBAR: WORKBANK DATASET LOADING ===
st.sidebar.markdown("---")
st.sidebar.subheader("Full Dataset")

if st.sidebar.button("Load Full Dataset (from Hugging Face)"):
    """
    Load the complete WORKBank dataset from Hugging Face Hub.
    
    The WORKBank dataset contains three main components:
    1. Worker Desires (5,731 records) - Worker perceptions of automation
    2. Expert Ratings (2,057 records) - Expert assessments of automation capacity  
    3. Task Metadata (2,131 records) - O*NET task data with wages and employment
    """
    try:
        from datasets import load_dataset
        with st.spinner("Loading WORKBank dataset from SALT-NLP..."):
            
            # Load worker desire data - contains worker ratings on automation desire and human agency
            st.info("Loading worker desire data...")
            worker_desire = load_dataset("SALT-NLP/WORKBank", data_files="worker_data/domain_worker_desires.csv")["train"]
            
            # Load expert ratings data - contains expert assessments of technological automation capacity
            st.info("Loading expert ratings data...")
            expert_ratings = load_dataset("SALT-NLP/WORKBank", data_files="expert_ratings/expert_rated_technological_capability.csv")["train"]
            
            # Load task metadata - contains O*NET task information with employment and wage data
            st.info("Loading task metadata...")
            task_meta_data = load_dataset("SALT-NLP/WORKBank", data_files="task_data/task_statement_with_metadata.csv")["train"]
            
            st.success("Successfully loaded all WORKBank datasets!")
            
            # Store datasets in session state for persistent access across interactions
            st.session_state.worker_desire = worker_desire
            st.session_state.expert_ratings = expert_ratings
            st.session_state.task_meta_data = task_meta_data
            
            # Display overview metrics for the loaded datasets
            st.subheader("WORKBank Dataset Information")
            
            # Create three columns for dataset metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Worker Desires", f"{len(worker_desire):,}", 
                         help="Worker ratings on automation desire and human agency for various tasks")
            
            with col2:
                st.metric("Expert Ratings", f"{len(expert_ratings):,}",
                         help="Expert assessments of technological automation capacity")
            
            with col3:
                st.metric("Task Metadata", f"{len(task_meta_data):,}",
                         help="O*NET task information with wages, employment, and skill data")
                
    except ImportError:
        st.error("The 'datasets' library is not installed. Please install it to use this feature.")
    except Exception as e:
        st.error(f"Failed to load WORKBank dataset: {e}")
        st.info("This may be due to network issues or the dataset being temporarily unavailable.")

# === WORKBANK DATA EXPLORATION INTERFACE ===
# Only show this section if datasets have been loaded into session state
if 'worker_desire' in st.session_state:
    st.markdown("---")
    st.subheader("Explore WORKBank Data")
    
    # Dropdown to select which dataset to explore
    dataset_choice = st.selectbox(
        "Choose dataset to explore:",
        ["Worker Desires & Human Agency", "Expert Automation Ratings", "Task Metadata & Wages"]
    )
    
    # === WORKER DESIRES & HUMAN AGENCY DATASET ===
    if dataset_choice == "Worker Desires & Human Agency":
        # Convert dataset to pandas DataFrame for easier manipulation
        df = st.session_state.worker_desire.to_pandas()
        st.write("**Worker perceptions of automation desire and human agency requirements**")
        
        # Define key columns that are most relevant for analysis
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Automation Desire Rating', 
                   'Human Agency Scale Rating', 'Core Skill Rating', 'Job Security Rating', 'Enjoyment Rating']
        
        # Toggle between showing key columns or all columns
        if st.checkbox("Show key columns only", value=True, key="worker_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Display summary statistics as bar charts
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Automation Desire Distribution**")
            # Show distribution of automation desire ratings (1-5 scale)
            st.bar_chart(df['Automation Desire Rating'].value_counts().sort_index())
        with col2:
            st.write("**Human Agency Scale Distribution**")
            # Show distribution of human agency scale ratings (1-5 scale)
            st.bar_chart(df['Human Agency Scale Rating'].value_counts().sort_index())
    
    # === EXPERT AUTOMATION RATINGS DATASET ===
    elif dataset_choice == "Expert Automation Ratings":
        # Convert dataset to pandas DataFrame
        df = st.session_state.expert_ratings.to_pandas()
        st.write("**Expert assessments of technological automation capacity**")
        
        # Define key columns for expert ratings analysis
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Automation Capacity Rating',
                   'Physical Action Requirement', 'Involved Uncertainty', 'Domain Expertise Requirement']
        
        # Toggle between showing key columns or all columns
        if st.checkbox("Show key columns only", value=True, key="expert_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Display summary statistics as bar charts
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Automation Capacity Distribution**")
            # Show distribution of expert automation capacity ratings
            st.bar_chart(df['Automation Capacity Rating'].value_counts().sort_index())
        with col2:
            st.write("**Human Agency Scale Distribution**")
            # Show distribution of human agency ratings from experts
            st.bar_chart(df['Human Agency Scale Rating'].value_counts().sort_index())
    
    # === TASK METADATA & WAGES DATASET ===
    elif dataset_choice == "Task Metadata & Wages":
        # Convert dataset to pandas DataFrame
        df = st.session_state.task_meta_data.to_pandas()
        st.write("**O*NET task information with employment and wage data**")
        
        # Define key columns for task metadata analysis
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Occupation Mean Annual Wage',
                   'Occupation Employment', 'Category', 'Importance', 'Frequency']
        
        # Toggle between showing key columns or all columns
        if st.checkbox("Show key columns only", value=True, key="task_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Display summary statistics as bar charts
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Task Categories**")
            # Show top 10 most common task categories
            st.bar_chart(df['Category'].value_counts().head(10))
        with col2:
            st.write("**Task Importance Distribution**")
            # Show distribution of task importance ratings
            st.bar_chart(df['Importance'].value_counts().sort_index())
