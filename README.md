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
- Python 3.10+
- Install dependencies:
 ```bash
  pip3 install ArticutAPI
  pip install -r requirements.txt
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

### Loki Setup
To run the BA model with Loki, you need to set up projects in the [卓騰語言科技](https://api.droidtown.co/) platform
 (Articut/Loki):
1. Register and log in to 卓騰語言科技.
2. Go to Loki to enter the Loki console.
3. Create 4 projects with the following names:  
  -VDO  
  -SCS  
  -SCO  
  -VIO  
4. Enter each project (e.g., VDO) and import all .ref files from the corresponding folder (e.g., VerbDirectObject.ref/):      
-Click 選擇檔案 → choose the .ref file → 讀取意圖    
-Repeat until all .ref files are imported    
5. Return to the Loki console (house icon), click 複製 to copy the Project Key.  
6. In each project folder (e.g., VDO/), create a file named account.info and add:  
 ```bash
{
    "username": "--your Loki registered email--",
    "api_key" : "--your Articut API key--",
    "loki_key": "--the copied project key--"
}
 ```
7. Repeat Steps 4–6 for all 4 projects.  

After setup, the BA Model will be able to access Loki for intent recognition.  

---

## Usage 

### **1. Data Preprocessing (Python)**
Run the preprocessing scripts in the `Preprocessing/` folder in two steps:
1. **Raw Preprocessing**  
Clean the raw input data from the `data/` folder.  
```bash
python Preprocessing/ba_data_preprocessing_raw.py
```
Input: preprocessing/data/ba_raw_data_page.txt   
Output: preprocessing/data/purged_ba_raw_data_page.txt  

2.Numbered Preprocessing
Add numbering to each processed sentence.
```bash
python Preprocessing/ba_data_preprocessing_num.py
```
Input: preprocessing/data/ba_raw_data_page.txt  
Output: preprocessing/data/purged_num_ba_raw_data_page.txt  

### **2. BA Model Execution (Python)**
After preprocessing, run the main BA model in `Loki_Template/` folder on the cleaned data:
```bash
python Loki_Template/Main_with_txt.py
```
Input: preprocessing/data/purged_ba_raw_data_page.txt  
Output: Loki_Template/CKIP Verified Results/p1-10/result_purged_ba_raw_data_page (results organized by page number)

### **3.Human Experiment (Gorilla.sc)**  
(1)Log into Gorilla.sc  
(2)Create a new experiment  
(3)Import the JSON file from Gorilla Platform/  
(4)Deploy the experiment to participants  

### **4.ChatGPT Experiments**    
-Data stored in ChatGPT experiment Data/  
-Includes prompts, outputs, and reference material used in the thesis  

### **5.Statistical Analysis (R)**  
Use scripts in R_data_analysis/ to compare results:
```bash  
source("emily r script_updated ver.R")  
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
