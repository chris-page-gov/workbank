import streamlit as st
import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'bduk_tasks.csv')

st.set_page_config(page_title="BDUK Task Browser", layout="centered")
st.title("BDUK Task Browser")

# Load tasks from CSV
def load_tasks():
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

tasks = load_tasks()

# Sidebar: Task selection
st.sidebar.header("Browse Tasks")
task_names = [task['task'] for task in tasks]
selected_task = st.sidebar.selectbox("Select a task:", task_names)

# Main: Show research finding for selected task
if selected_task:
    task = next(t for t in tasks if t['task'] == selected_task)
    st.subheader(f"Research findings for: {task['task']}")
    st.write(task['research_finding'])

# Dataset loading section
st.sidebar.markdown("---")
st.sidebar.subheader("Full Dataset")

if st.sidebar.button("Load Full Dataset (from Hugging Face)"):
    try:
        from datasets import load_dataset
        with st.spinner("Loading WORKBank dataset from SALT-NLP..."):
            
            # Load the different components of the WORKBank dataset
            st.info("Loading worker desire data...")
            worker_desire = load_dataset("SALT-NLP/WORKBank", data_files="worker_data/domain_worker_desires.csv")["train"]
            
            st.info("Loading expert ratings data...")
            expert_ratings = load_dataset("SALT-NLP/WORKBank", data_files="expert_ratings/expert_rated_technological_capability.csv")["train"]
            
            st.info("Loading task metadata...")
            task_meta_data = load_dataset("SALT-NLP/WORKBank", data_files="task_data/task_statement_with_metadata.csv")["train"]
            
            st.success("Successfully loaded all WORKBank datasets!")
            
            # Store datasets in session state for later use
            st.session_state.worker_desire = worker_desire
            st.session_state.expert_ratings = expert_ratings
            st.session_state.task_meta_data = task_meta_data
            
            # Display dataset information
            st.subheader("WORKBank Dataset Information")
            
            # Overview metrics
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

# Display loaded datasets if they exist in session state
if 'worker_desire' in st.session_state:
    st.markdown("---")
    st.subheader("Explore WORKBank Data")
    
    dataset_choice = st.selectbox(
        "Choose dataset to explore:",
        ["Worker Desires & Human Agency", "Expert Automation Ratings", "Task Metadata & Wages"]
    )
    
    if dataset_choice == "Worker Desires & Human Agency":
        df = st.session_state.worker_desire.to_pandas()
        st.write("**Worker perceptions of automation desire and human agency requirements**")
        
        # Key columns for worker desires
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Automation Desire Rating', 
                   'Human Agency Scale Rating', 'Core Skill Rating', 'Job Security Rating', 'Enjoyment Rating']
        
        if st.checkbox("Show key columns only", value=True, key="worker_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Summary statistics
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Automation Desire Distribution**")
            st.bar_chart(df['Automation Desire Rating'].value_counts().sort_index())
        with col2:
            st.write("**Human Agency Scale Distribution**")
            st.bar_chart(df['Human Agency Scale Rating'].value_counts().sort_index())
    
    elif dataset_choice == "Expert Automation Ratings":
        df = st.session_state.expert_ratings.to_pandas()
        st.write("**Expert assessments of technological automation capacity**")
        
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Automation Capacity Rating',
                   'Physical Action Requirement', 'Involved Uncertainty', 'Domain Expertise Requirement']
        
        if st.checkbox("Show key columns only", value=True, key="expert_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Summary statistics
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Automation Capacity Distribution**")
            st.bar_chart(df['Automation Capacity Rating'].value_counts().sort_index())
        with col2:
            st.write("**Human Agency Scale Distribution**")
            st.bar_chart(df['Human Agency Scale Rating'].value_counts().sort_index())
    
    elif dataset_choice == "Task Metadata & Wages":
        df = st.session_state.task_meta_data.to_pandas()
        st.write("**O*NET task information with employment and wage data**")
        
        key_cols = ['Task ID', 'Occupation (O*NET-SOC Title)', 'Task', 'Occupation Mean Annual Wage',
                   'Occupation Employment', 'Category', 'Importance', 'Frequency']
        
        if st.checkbox("Show key columns only", value=True, key="task_key"):
            st.dataframe(df[key_cols].head(10), use_container_width=True)
        else:
            st.dataframe(df.head(10), use_container_width=True)
            
        # Summary statistics
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Task Categories**")
            st.bar_chart(df['Category'].value_counts().head(10))
        with col2:
            st.write("**Task Importance Distribution**")
            st.bar_chart(df['Importance'].value_counts().sort_index())
