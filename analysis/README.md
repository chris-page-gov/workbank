# Analysis Notebooks

This directory contains Jupyter notebooks for analyzing work automation data and related economic impacts.

## Notebooks Overview

### 1. `automation_desire.ipynb`
- **Purpose**: Analysis of automation desire patterns
- **Outputs**: Plots saved to `../local/automation_desire/` directory
- **Status**: ✅ Fixed - Directory creation implemented

### 2. `automation_viability.ipynb`
- **Purpose**: Automation capability vs desire analysis with sector-specific visualizations
- **Outputs**: SVG plots saved to `../local/automation_viability/` directory
- **Status**: ✅ Already had proper directory creation in `plot_sector_landscape` function

### 3. `human_agency_scale.ipynb`
- **Purpose**: Human agency scale analysis with occupation-specific visualizations
- **Outputs**: PNG plots saved to `../local/has/` subdirectories
- **Status**: ✅ Fixed - Updated `plot_has_for_occupation` function with directory creation

### 4. `human_skill_shift.ipynb`
- **Purpose**: Skill transition analysis with wage correlation
- **Outputs**: CSV file saved to `../local/skill_info.csv`
- **Status**: ✅ Fixed - Added directory creation before CSV export

### 5. `robustness.ipynb`
- **Purpose**: Dataset robustness and demographic analysis
- **Outputs**: Various plots including sector distribution analysis
- **Status**: ✅ Fixed - Added directory creation before sector_dist.pdf save

## Recent File Dependency Fixes

### Issue
Several notebooks were experiencing `FileNotFoundError` when attempting to save plots and data files because the target directories (`../local/*`) did not exist.

### Solution Applied
Implemented consistent directory creation pattern across all notebooks:

```python
import os

# Before saving any file
os.makedirs(os.path.dirname(file_path), exist_ok=True)
```

### Specific Changes Made

1. **automation_desire.ipynb**: Added directory creation for plot output directories
2. **human_agency_scale.ipynb**: Updated `plot_has_for_occupation` function to include:
   ```python
   import os  # Added to imports
   os.makedirs(os.path.dirname(filename), exist_ok=True)  # Added before plt.savefig
   ```
3. **human_skill_shift.ipynb**: Added directory creation before CSV export:
   ```python
   os.makedirs(os.path.dirname('../local/skill_info.csv'), exist_ok=True)
   skill_info_df.to_csv("../local/skill_info.csv", index=False)
   ```
4. **robustness.ipynb**: Added directory creation before PDF plot save:
   ```python
   os.makedirs(os.path.dirname("../local/sector_dist.pdf"), exist_ok=True)
   plt.savefig("../local/sector_dist.pdf", bbox_inches='tight')
   ```

### Dependencies and File Structure

All notebooks now safely create the following directory structure as needed:
- `../local/` - Root directory for all analysis outputs
- `../local/automation_desire/` - Automation desire analysis plots
- `../local/automation_viability/` - Automation viability plots  
- `../local/has/` - Human agency scale visualizations
- `../local/skill_info.csv` - Skill transition data export

### Running the Notebooks

The notebooks can now be executed without `FileNotFoundError` issues. The directory creation pattern ensures that:
- Directories are created automatically if they don't exist
- Existing directories are not affected (`exist_ok=True`)
- The notebooks are more robust and portable across different environments

### Technical Implementation

The fix uses Python's `os.makedirs()` function with the following parameters:
- `os.path.dirname(file_path)`: Extracts the directory path from the full file path
- `exist_ok=True`: Prevents errors if the directory already exists

This pattern has been consistently applied across all file save operations including:
- `plt.savefig()` for matplotlib plots
- `df.to_csv()` for pandas DataFrame exports
- Any other file output operations

### Validation

All updated notebooks have been tested to ensure:
- ✅ Directory creation works correctly
- ✅ File saves complete successfully
- ✅ No regression in existing functionality
- ✅ Notebooks can be run in clean environments without manual directory setup
