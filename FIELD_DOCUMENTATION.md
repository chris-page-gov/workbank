# WORKBank Dataset Field Documentation

This document provides detailed field documentation for the three main WORKBank CSV files, including data column names, data types, and descriptions.

## 1. domain_worker_desires.csv (5,731 rows)

This file contains worker survey responses about their desires for automation across various tasks and occupations.

| Data Column Name | Data Type | Description |
|------------------|-----------|-------------|
| Task ID | Integer | Unique identifier for each task from O*NET database |
| Occupation (O*NET-SOC Title) | String | Official O*NET Standard Occupational Classification title |
| Task | String | Detailed description of the work task being evaluated |
| User ID | String | Anonymized unique identifier for survey respondent |
| Date | String | Date when survey response was submitted (YYYY/M/D format) |
| Self-reported Expertise | String | Worker's self-assessment of expertise level (Expert, Average, Beginner) |
| Automation Desire Rating | Integer | Scale 1-5: Worker's desire for task automation (1=lowest, 5=highest) |
| Time | Integer | Scale 1-5: How time-consuming the task is (1=least, 5=most) |
| Core Skill Rating | Integer | Scale 1-5: How central this task is to the worker's core skills |
| Job Security Rating | Integer | Scale 1-5: Worker's concern about job security if task is automated |
| Enjoyment Rating | Integer | Scale 1-5: How much the worker enjoys performing this task |
| Reasons for Automation Desire - Free Time | Boolean | Whether worker wants automation to gain more free time |
| Reasons for Automation Desire - Repetitive | Boolean | Whether worker wants automation because task is repetitive |
| Reasons for Automation Desire - Human Error | Boolean | Whether worker wants automation to reduce human error |
| Reasons for Automation Desire - Stress | Boolean | Whether worker wants automation to reduce stress |
| Reasons for Automation Desire - Difficulty | Boolean | Whether worker wants automation because task is difficult |
| Reasons for Automation Desire - Scale | Boolean | Whether worker wants automation to handle larger scale |
| Physical Action Requirement | Integer | Scale 1-5: Level of physical action required for task |
| Interpersonal Communication Requirement | Integer | Scale 1-5: Level of interpersonal communication required |
| Involved Uncertainty | Integer | Scale 1-5: Level of uncertainty/ambiguity in task |
| Domain Expertise Requirement | Integer | Scale 1-5: Level of specialized domain knowledge required |
| Human Agency Scale Rating | Integer | Scale 1-5: Worker's rating of human agency importance (H1-H5 scale) |
| Reasons for Human Agency - Physical | Boolean | Whether human agency needed for physical capabilities |
| Reasons for Human Agency - Control | Boolean | Whether human agency needed for control/oversight |
| Reasons for Human Agency - Domain Knowledge | Boolean | Whether human agency needed for domain expertise |
| Reasons for Human Agency - Empathy | Boolean | Whether human agency needed for empathy/emotional intelligence |
| Reasons for Human Agency - Quality Oversight | Boolean | Whether human agency needed for quality control |
| Reasons for Human Agency - Dynamic | Boolean | Whether human agency needed for dynamic/changing situations |
| Reasons for Human Agency - Ethical | Boolean | Whether human agency needed for ethical considerations |
| Other Reason for Automation Desire | String | Free-text field for other automation desire reasons |
| Other Reason for Human Agency | String | Free-text field for other human agency reasons |

## 2. expert_rated_technological_capability.csv (2,057 rows)

This file contains expert assessments of current technological capability to automate various tasks.

| Data Column Name | Data Type | Description |
|------------------|-----------|-------------|
| Task ID | Integer | Unique identifier for each task from O*NET database |
| Occupation (O*NET-SOC Title) | String | Official O*NET Standard Occupational Classification title |
| Task | String | Detailed description of the work task being evaluated |
| User ID | String | Anonymized identifier for expert rater (e.g., RedTiger, YellowZebra) |
| Date | String | Date when expert assessment was submitted (YYYY/M/D format) |
| Automation Capacity Rating | Integer | Scale 1-5: Expert assessment of current AI/automation capability (1=low, 5=high) |
| Physical Action Requirement | Integer | Scale 1-5: Expert rating of physical action needed for task |
| Involved Uncertainty | Integer | Scale 1-5: Expert rating of uncertainty/ambiguity in task |
| Domain Expertise Requirement | Integer | Scale 1-5: Expert rating of specialized knowledge required |
| Interpersonal Communication Requirement | Integer | Scale 1-5: Expert rating of interpersonal communication needed |
| Human Agency Scale Rating | Integer | Scale 1-5: Expert rating of human agency importance (H1-H5 scale) |

## 3. task_statement_with_metadata.csv (2,131 rows)

This file contains task descriptions with associated O*NET metadata including wages, employment, and skill classifications.

| Data Column Name | Data Type | Description |
|------------------|-----------|-------------|
| O*NET-SOC Code | String | Official O*NET Standard Occupational Classification code (XX-XXXX.XX format) |
| Occupation (O*NET-SOC Title) | String | Official O*NET Standard Occupational Classification title |
| Task ID | Integer | Unique identifier for each task from O*NET database |
| Task | String | Detailed description of the work task |
| Task Type | String | Classification of task importance (Core, Supplemental) |
| Date | String | Date when task data was collected (MM/YYYY format) |
| Category | Float | O*NET task category classification value |
| Frequency | Float | O*NET rating of how frequently task is performed |
| Importance | Float | O*NET rating of task importance to occupation |
| Relevance | Float | O*NET rating of task relevance to occupation |
| Occupation Mean Annual Wage | Float | Average annual salary for this occupation in USD |
| Occupation Employment | Float | Number of people employed in this occupation |
| Skill (O*NET Work Activity) | String | List of related O*NET Generalized Work Activities (JSON array format) |
| Skill ID (O*NET Generalized Work Activity ID) | String | List of O*NET GWA identification codes (JSON array format) |

## Data Relationships

- **Task ID** serves as the primary key linking records across all three files
- **Occupation (O*NET-SOC Title)** provides occupational context consistent across files
- The **Human Agency Scale Rating** appears in both worker desire and expert capability files for comparison
- **Physical Action**, **Uncertainty**, **Domain Expertise**, and **Interpersonal Communication** requirements are rated by both workers and experts

## Rating Scales

### Human Agency Scale (H1-H5)
- **H1**: No human agency required - full automation possible
- **H2**: Minimal human agency - occasional oversight needed
- **H3**: Moderate human agency - regular human input required
- **H4**: High human agency - significant human involvement needed
- **H5**: Essential human agency - human control/judgment critical

### General 1-5 Scales
- **1**: Very Low/Minimal
- **2**: Low
- **3**: Moderate
- **4**: High
- **5**: Very High/Essential

## Usage Notes

- Boolean fields use `True`/`False` values, with some having additional text entries
- Date formats vary between files (YYYY/M/D vs MM/YYYY)
- Some string fields may contain comma-separated lists or JSON arrays
- Missing values may appear as empty strings, `FALSE`, or actual null values
- Expert rater User IDs use animal code names for anonymization
