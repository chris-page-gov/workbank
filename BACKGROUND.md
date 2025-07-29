# Background: Future of Work with AI Agents

This repository contains the WORKBank database and analysis code supporting the research paper "Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce" ([arXiv:2506.06576v2](https://arxiv.org/abs/2506.06576)).

## Overview

The rapid advancement of AI agents—goal-directed systems equipped with tool access and multi-step execution capabilities—is fundamentally reshaping the labor market. While these systems show promise for boosting productivity, they also raise concerns about job displacement, diminished human agency, and overreliance on automation. This research addresses the critical gap in our understanding of how AI agents can be responsibly integrated into the workforce.

## Research Motivation

### The Challenge

Despite the significant impact AI agents are having on work, we lack a systematic and grounded understanding of the evolving landscape:

- **Limited Coverage**: Prior research often focuses on narrow domains like software engineering and customer support, limiting our comprehension of diverse human jobs
- **Missing Worker Voice**: Existing studies emphasize capital interests without adequately considering worker values and preferences  
- **Backward-Looking Analysis**: Current approaches rely on analyzing existing usage data rather than providing forward-looking assessments of AI potential

### The Need for a Worker-Centric Approach

This research takes a fundamentally different approach by:
- Centering worker perspectives and desires
- Examining the entire workforce that could be impacted by digital AI agents
- Moving beyond binary automation/non-automation to explore the full spectrum of human-AI collaboration

## Key Contributions

### 1. The WORKBank Database

The **AI Agent Worker Outlook & Readiness Knowledge Bank (WORKBank)** is the first large-scale database capturing both worker desires and AI capabilities for occupational tasks:

- **1,500 workers** across **104 occupations** 
- **52 AI experts** providing technical assessments
- **844 occupational tasks** sourced from the U.S. Department of Labor's O*NET database
- Data collected between January-May 2025

### 2. The Human Agency Scale (HAS)

A breakthrough framework that moves beyond simple automation to quantify the spectrum of human-AI collaboration:

- **H1**: AI agent handles the task entirely on its own
- **H2**: AI agent needs minimal human input for optimal performance  
- **H3**: AI agent and human form equal partnership, outperforming either alone
- **H4**: AI agent requires human input to successfully complete the task
- **H5**: AI agent cannot function without continuous human involvement

### 3. Four-Zone Desire-Capability Landscape

By contrasting worker desires with technological capabilities, the research reveals four distinct zones:

- **Automation "Green Light" Zone**: High desire + high capability (prime for deployment)
- **Automation "Red Light" Zone**: High capability + low desire (deployment requires caution)
- **R&D Opportunity Zone**: High desire + low capability (promising research directions)
- **Low Priority Zone**: Low desire + low capability (less urgent for development)

## Major Findings

### Worker Attitudes Toward Automation

- **46.1%** of tasks receive positive worker attitudes toward AI automation
- Primary motivation: **"freeing up time for high-value work"** (69.38% of pro-automation responses)
- Workers want to automate repetitive, tedious, and low-value tasks
- Significant variation across sectors, with Arts/Design/Media showing the most resistance

### Misalignment Between Investment and Worker Needs

- **41.0%** of Y Combinator company investments are concentrated in Low Priority and "Red Light" zones
- Top 10 occupations with highest automation desire account for only **1.26%** of current LLM usage
- Current investments mainly focus on software development and business analysis, leaving many promising areas under-addressed

### Human-Agent Collaboration Preferences

- **45.2%** of occupations prefer H3 (equal partnership) as the dominant collaboration level
- Workers generally prefer higher levels of human agency than experts deem technologically necessary
- Strong potential for collaborative AI rather than replacement automation

### Shifting Skill Requirements

The research reveals early signals of how AI integration may reshape core competencies:

1. **Declining importance** of information-processing skills (analyzing data, updating knowledge)
2. **Growing emphasis** on interpersonal and organizational skills
3. **Trend toward** requiring broader, more diverse skill sets from individuals

## Technical Approach

### Auditing Framework

The research employs a novel auditing framework featuring:

- **Audio-enhanced surveys** enabling natural reflection and contextualized responses
- **Task familiarity filtering** ensuring assessments are grounded in real experience
- **Guided consideration** of factors like job security concerns and task enjoyment
- **Dual perspectives** from both domain workers and AI experts

### Data Sources and Validation

- Tasks sourced from O*NET database (complex, multi-step workflows)
- Demographics validated against U.S. Bureau of Labor Statistics
- Expert assessments from PhD researchers and industry practitioners
- Robust statistical analysis including mixed-effects modeling

## Implications for Workforce Development

### For Workers
- Understanding which tasks are most likely to be automated or augmented
- Identifying skills that will remain valuable as AI capabilities advance
- Preparing for evolving workplace dynamics and human-AI collaboration

### For Organizations
- Prioritizing AI investments based on worker acceptance and technological feasibility
- Designing human-AI collaboration systems that respect worker preferences
- Planning workforce transitions that consider both efficiency and worker welfare

### For Policymakers
- Informing responsible AI deployment strategies
- Supporting worker reskilling and retraining programs
- Ensuring AI development aligns with broader societal values

## Repository Structure

This repository contains:

- **Analysis notebooks** exploring automation desire, viability, human agency, and skill shifts
- **External data** from BLS, O*NET, company mappings, and usage patterns
- **Local results** including visualizations and derived datasets
- **Application code** for browsing and interacting with the WORKBank data

## Future Directions

The WORKBank database and framework provide a foundation for:

- **Longitudinal tracking** of changing worker preferences and AI capabilities
- **Extended coverage** to additional occupations and emerging job categories
- **Policy research** on responsible AI deployment and workforce transition
- **Industry applications** for human-centered AI system design

## Research Impact

This work represents the first comprehensive audit of AI agent readiness for workplace integration from a worker-centric perspective. By providing a shared language (HAS) and systematic framework for understanding automation vs. augmentation, it offers crucial insights for building AI systems that enhance rather than replace human capabilities.

The findings underscore the importance of centering worker voices in AI development and highlight significant opportunities for creating AI agents that support meaningful human-AI collaboration while respecting worker preferences and values.

---

*For detailed methodology, complete results, and technical appendices, see the full paper: [Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce](https://arxiv.org/abs/2506.06576)*
