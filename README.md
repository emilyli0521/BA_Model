#The Comparison between ChatGPT, Human Beings, and a Linguistics-Based BA Model 
## A Case Study on the Natural Language Understanding of the Chinese BA Construction 

This repository accompanies the MA thesis titled: **The Comparison between ChatGPT and Human Beings in “Intuition”: A Case Study on the Natural Language Understanding of the BA Construction** 

It contains experiment designs, code, and analysis resources comparing **ChatGPT**, **human intuitions**, and **a linguistics-based BA model** in processing the **Chinese BA (把) construction**. 

## Project Overview

**Research Focus** 

How do **ChatGPT**, **human participants**, and a **linguistics-based BA model** differ in their interpretation and processing of BA constructions? 

**Approach** 
1. **Human intuition experiment (Gorilla.sc)** — Collected participant judgments on BA sentences
2. **ChatGPT experiments** — Large language model outputs on the same tasks
3. **Linguistics-based BA model (Python)** — Linguistics-based model for BA construction processing
4. **Statistical analysis (R)** — Direct comparison of results from the three sources 

---

## Repository Structure 

BA_Model/   
├─ ChatGPT experiment Data/ # Data from ChatGPT experiments (prompts, outputs, evaluation)   
├─ Flowchart/ # Flowcharts of the BA model and preprocessing pipeline  
├─ Gorilla Platform/ # Gorilla.sc exported JSON files for the human intuition experiment  
├─ Loki_Template/ # Python scripts for the BA model and preprocessing  
├─ R_data_analysis/ # R scripts for statistical comparison of ChatGPT, BA model, and human   results   
├─ .gitignore # Git ignore settings  
└─ README.md # Project instructions  

## Requirements 

### Python (BA model & preprocessing)
```bash
- Python 3.10+
```
- Suggested packages:
```
- pandas
- numpy
- regex
- scikit-learn
- matplotlib
```
### R (statistical analysis
```
- R 4.0+
```
- Suggested packages:
```
- tidyverse
- ggplot2
- dplyr
- stats
```
### Gorilla.sc 
- [Gorilla.sc](https://gorilla.sc) account required to import and run the human intuition experiment
   
---

## Usage 

1. BA Model & Preprocessing (Python)  
Run preprocessing scripts from Loki_Template/ to prepare input data:
```bash
python Loki_Template/preprocess_ba.py \
--input data/raw.json \
--output data/cleaned.json
```

2. Human Experiment (Gorilla.sc)  
(1)Log into Gorilla.sc  
(2)Create a new experiment  
(3)Import the JSON file from Gorilla Platform/  
(4)Deploy the experiment to participants  

3. ChatGPT Experiments  
-Data stored in ChatGPT experiment Data/  
-Includes prompts, outputs, and reference material used in the thesis  

4. Statistical Analysis (R)  
Use scripts in R_data_analysis/ to compare results:
```bash  
source("R_data_analysis/analysis_ba_chatgpt_human.R")  
```
## **Citation**
If you use this repository in academic work, please cite:  
```
@misc{Emily_BA_Model,
  author    = {Yi-Chen Emily Lee},
  title     = {The Comparison between ChatGPT and Human Beings in “Intuition”: A Case Study on the Natural Language Understanding of the BA Construction},
  year      = {2025},
  url       = {https://github.com/emilyli0521/BA_Model}
}
```
