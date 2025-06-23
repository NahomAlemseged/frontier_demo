import streamlit as st
'''
# About This App

## Introduction

Welcome to this interactive tool for evaluating **Under-Five Mortality (U5M) reduction performance** across African countries from **2000 to 2019**, adjusted for healthcare spending per capita.

While most global health metrics focus on absolute declines in U5M, this app asks a deeper, more equitable question:

> _"How well did countries perform, given the resources they had?"_

This shift in perspective helps identify countries that **outperformed expectations**—the potential **Exemplars**—as well as those where outcomes **fell short relative to investment**.

---

## Why This Study Matters

This work has direct applications for organizations such as **Exemplars in Global Health (GV)**, the **World Bank**, **UNICEF**, and **WHO**, as they strive to:

- Benchmark country performance more **equitably**
- Guide **evidence-based resource allocation**
- Identify **positive deviants** for deeper learning and policy transfer

By comparing child mortality outcomes relative to investment levels, this tool supports **smarter, fairer evaluations** of progress.

---

## Methodology Snapshot

### ✅ Stochastic Frontier Meta-Analysis (SFMA)

At the heart of this tool is a **novel frontier methodology**, co-developed by our team. It represents a **major leap forward** in performance benchmarking by:

- Accepting **standard errors** in mortality and spending estimates  
- **Trimming outliers** automatically (a key limitation in earlier methods)  
- Delivering more **robust, context-aware results** without relying on rigid assumptions

📌 This method was successfully used in a World Bank-supported analysis and was later **acknowledged for correctly removing outliers** that distorted prior results.

🧠 It outperforms conventional tools like DEA or parametric SFA—making it one of the **most advanced frontier approaches currently available** for health systems analysis.

➡️ [Read our technical paper on arXiv](https://arxiv.org/abs/2404.04301)

---

### Visual Example: Outlier Trimming in Action

The image below shows how our method effectively removes outliers, creating a more realistic and policy-relevant benchmark as compared to all other available methods.


'''
st.image("app/assets/fig_7_gdp_le_log_log.png", caption="Comparison of benchmarking tools in estimating efficiency frontier, and also outlier trimming as indicated in red")

'''
 ---

## Data Sources

- **Under-Five Mortality Rates**: UNICEF, World Bank, IHME  
- **Health Expenditure per capita**: World Development Indicators  
- **Coverage**: African countries with consistent data, 2000–2019  

---

## Who Should Use This Tool?

- Global health funders (GV, World Bank, GAVI, UNICEF, WHO)  
- Ministries of Health and Planning  
- Researchers and analysts focused on health system performance  
- NGOs working in child health, accountability, or impact measurement
 
---

Second phase of the project that assesses governance and human resources that explain inefficiencies  have been conduted but not included here. We have found some interesting results.

## Let’s Collaborate

We believe this tool can inform the next wave of global health decision-making.

📣 Interested in applying this framework to your country, organization, or domain?  
_We’re open to collaboration, expansion, and case study development._

👉 _Let’s connect to turn insight into impact._

 
 
 '''
