#!/usr/bin/env python3
"""
Download WORKBank Dataset Files

This script downloads the three main CSV files from the WORKBank dataset
hosted on Hugging Face and saves them locally for offline analysis.

Files downloaded:
1. domain_worker_desires.csv - Worker perceptions and ratings
2. expert_rated_technological_capability.csv - Expert assessments 
3. task_statement_with_metadata.csv - O*NET task data with wages/employment

Usage:
    python download_workbank_data.py [--output-dir data]
"""

import os
import argparse
from pathlib import Path
from datasets import load_dataset
import pandas as pd

def download_workbank_data(output_dir: str = "data"):
    """
    Download WORKBank dataset files from Hugging Face Hub.
    
    Args:
        output_dir: Directory to save the CSV files (default: "data")
    """
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    print("🔄 Downloading WORKBank dataset from SALT-NLP/WORKBank...")
    
    # Define the datasets to download
    datasets_info = [
        {
            "name": "domain_worker_desires",
            "data_file": "worker_data/domain_worker_desires.csv",
            "description": "Worker perceptions of automation desire and human agency"
        },
        {
            "name": "expert_rated_technological_capability", 
            "data_file": "expert_ratings/expert_rated_technological_capability.csv",
            "description": "Expert assessments of technological automation capacity"
        },
        {
            "name": "task_statement_with_metadata",
            "data_file": "task_data/task_statement_with_metadata.csv", 
            "description": "O*NET task information with wages, employment, and skill data"
        }
    ]
    
    for dataset_info in datasets_info:
        try:
            print(f"\n📥 Downloading {dataset_info['name']}.csv...")
            print(f"   Description: {dataset_info['description']}")
            
            # Load dataset from Hugging Face
            dataset = load_dataset(
                "SALT-NLP/WORKBank", 
                data_files=dataset_info["data_file"]
            )["train"]
            
            # Convert to pandas DataFrame
            df = dataset.to_pandas()
            
            # Save as CSV
            output_file = output_path / f"{dataset_info['name']}.csv"
            df.to_csv(output_file, index=False)
            
            print(f"   ✅ Saved: {output_file} ({df.shape[0]:,} rows, {df.shape[1]} columns)")
            
        except Exception as e:
            print(f"   ❌ Error downloading {dataset_info['name']}: {e}")
            continue
    
    print(f"\n✨ Download complete! Files saved to: {output_path.absolute()}")
    print(f"\n📊 Dataset Summary:")
    print(f"   • domain_worker_desires.csv: Worker survey responses (5,731 rows)")
    print(f"   • expert_rated_technological_capability.csv: Expert assessments (2,057 rows)")  
    print(f"   • task_statement_with_metadata.csv: O*NET metadata & wages (2,131 rows)")
    print(f"\n📖 Documentation:")
    print(f"   • README.md - Main project documentation")
    print(f"   • DATA_README.md - Detailed data guide and examples")
    print(f"   • BACKGROUND.md - Research methodology and findings")
    print(f"   • codebook.pdf - Complete variable documentation")
    print("\n💻 Quick Start:")
    print("```python")
    print("import pandas as pd")
    print(f"worker_desire = pd.read_csv('{output_dir}/domain_worker_desires.csv')")
    print(f"expert_ratings = pd.read_csv('{output_dir}/expert_rated_technological_capability.csv')")
    print(f"task_metadata = pd.read_csv('{output_dir}/task_statement_with_metadata.csv')")
    print("```")
    print(f"\n🔬 Analysis: See Jupyter notebooks in analysis/ directory")
    print(f"🌐 Web App: Run 'streamlit run bduk_app/streamlit_tasks.py'")

def main():
    parser = argparse.ArgumentParser(description="Download WORKBank dataset files")
    parser.add_argument(
        "--output-dir", 
        default="data",
        help="Directory to save CSV files (default: data)"
    )
    
    args = parser.parse_args()
    download_workbank_data(args.output_dir)

if __name__ == "__main__":
    main()
