# Healthcare Patient Satisfaction – 2024 Data Story

**Analyst:** 23f3001440@ds.study.iitm.ac.in  

This project analyzes quarterly patient satisfaction scores for 2024 and builds a data story to guide business decisions for a healthcare company.

---

## 1. Business Context

The company is facing **below-average patient experience ratings**.

- **Current average patient satisfaction score (2024): 3.67**
- **Industry benchmark / target: 4.5**

The executive team wants to understand:

- Why scores are low and volatile  
- What this implies for business outcomes  
- What actions are needed to reach or exceed the benchmark  

---

## 2. Dataset

**Patient Satisfaction Score – 2024 Quarterly Data**

| Quarter | Satisfaction Score |
|--------|---------------------|
| Q1     | 1.89                |
| Q2     | 3.74                |
| Q3     | 1.41                |
| Q4     | 7.64                |
| **Average** | **3.67**      |

> Note: The README **must** contain the correct average value: **3.67**.

**Industry Target:** 4.5  

---

## 3. Analysis Methodology

All analysis and visualization is implemented in `analysis.py` using:

- **Pandas** for data handling
- **Matplotlib** for visualization

Steps:

1. Hard-code the quarterly satisfaction scores into a DataFrame  
2. Compute:
   - Quarterly scores  
   - Average score  
   - Min / max scores  
   - Gap between average and industry target (4.5)  
3. Create a **line chart** with:
   - Quarterly scores (Q1–Q4)  
   - A **horizontal dashed line** at the industry benchmark (4.5)  
   - Labels for each quarter’s score  
4. Save the visualization as `patient_satisfaction_trend.png`.

---

## 4. Key Findings

### 4.1 Overall Performance

- **Average 2024 satisfaction score:** 3.67  
- **Industry benchmark:** 4.5  
- **Gap to target:** 0.83 points below the benchmark  

So across the year, the company is **underperforming** relative to industry expectations.

### 4.2 Quarterly Trend

- **Q1: 1.89** – Very poor experience; indicates severe service or process issues.  
- **Q2: 3.74** – Significant improvement, but still below the 4.5 target.  
- **Q3: 1.41** – Sharp deterioration again; suggests instability and lack of sustained improvement.  
- **Q4: 7.64** – Strong overperformance relative to the 4.5 target.  

The pattern is **highly volatile**:

- The business is **not consistently delivering good patient experience**.  
- Q4 may reflect a **special intervention** (new process, campaign, or one-off event) rather than a stable system-level improvement.  

### 4.3 Risk of Over-Reliance on Q4

While Q4 looks excellent, the **year-wide story** is still weak:

- Patients who visited in Q1 and Q3 likely had **very negative experiences**, which affects:
  - Word-of-mouth
  - Online ratings
  - Long-term brand perception
- One good quarter does **not erase** three quarters of underperformance.

---

## 5. Business Implications

1. **Customer Churn & Reputation Risk**  
   - Low satisfaction in Q1 and Q3 increases the risk of losing patients to competitors.  
   - Negative reviews and low ratings can have a compounding effect on future patient acquisition.

2. **Operational Instability**  
   - The huge swings between quarters suggest:
     - Process changes are not controlled or standardized  
     - Staff training and protocols are inconsistent  
     - The system is reactive, not proactive

3. **Strategic Misalignment**  
   - The organization is not reliably meeting its own (or industry) service standards.  
   - Resources may be allocated in bursts (e.g., big push in Q4) instead of building strong, **repeatable processes**.

---

## 6. Recommendations to Reach the 4.5 Target

The problem is clearly not just “do more in Q4” — it’s **consistency** and **system design**.

### 6.1 Improve Service Quality

Focus on **end-to-end service quality**, not just isolated touchpoints:

- Standardize **patient interaction protocols**:
  - Greeting, triage, explanation of wait times, discharge communication  
- Implement **mandatory staff training**:
  - Empathy, communication, conflict handling  
- Introduce **checklists** and **SOPs** (standard operating procedures) for key service steps:
  - Registration  
  - Consultation  
  - Billing  
  - Follow-up  

Link these service standards to **measured KPIs** (e.g., satisfaction by department / doctor / time slot).

### 6.2 Reduce Wait Times

The given solution explicitly points to **“improve service quality and wait times”**. Concretely:

- **Measure wait times** at each stage:
  - Time to registration
  - Time until first consultation
  - Time for tests/results
  - Time for billing and discharge  
- Use data to:
  - Identify bottlenecks (e.g., peak hours, understaffed desks)  
  - Adjust staffing schedules and resource allocation  
  - Implement appointment-slot optimization and triage rules  

Wait time reduction will directly improve **perceived efficiency** and **patient satisfaction**.

### 6.3 Stabilize Processes Across Quarters

The volatility suggests that any improvements are not locked into the system. To stabilize:

- After Q4 success, **document exactly what changed**:
  - New policies?
  - Additional staff?
  - Technology rollout?
  - Process tweaks?
- Convert successful Q4 initiatives into **repeatable, monitored processes**.
- Set **quarterly targets** (e.g., minimum 4.2 each quarter, then 4.5+) and track deviations early.

### 6.4 Build a Continuous Feedback Loop

- Collect **more granular feedback**:
  - By department, doctor, time of day, visit reason  
- Automate feedback collection:
  - SMS / app survey after visits  
- Run **monthly reviews** of satisfaction and wait time metrics.  
- Use LLMs / analytics tools to:
  - Summarize patient comments  
  - Detect recurring complaints  
  - Identify emerging issues early  

---

## 7. Visualization

The script `analysis.py` generates:

- **`patient_satisfaction_trend.png`** – line chart with:
  - Quarterly scores (Q1–Q4)  
  - Industry benchmark line at 4.5  
  - Annotations for each quarter  
  - Average score displayed on the plot  

This visualization helps the executive team quickly see:

- The **gap to the benchmark**
- The **instability** across quarters  
- How extreme Q4 is relative to the rest of the year  

---

## 8. How LLMs Were Used in This Project

LLMs (e.g., ChatGPT Codex / Jules) can support the full **data-to-story pipeline**:

1. **Data Engineering**
   - Assist in generating the Python code to model quarterly data.
2. **Data Analysis**
   - Help design which metrics to compute and how to interpret them.
3. **Visualization**
   - Suggest effective chart types and annotation strategies.
4. **Storytelling**
   - Draft a coherent narrative for executives:
     - Trends
     - Risks
     - Recommended actions  

In this project, an LLM was used to:

- Draft and refine the analysis code (`analysis.py`)  
- Structure the data story in this `README.md`  
- Translate raw numbers into a **business-oriented narrative** tied to
  **improving service quality and wait times**.

---
