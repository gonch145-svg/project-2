# A/B Test Analysis: Improving Digital User Experience at Vanguard

## Overview

This project analyzes the results of an A/B test conducted by Vanguard’s Customer Experience (CX) team to evaluate whether a redesigned digital interface improves user experience.

## Business Objective

Assess whether the new interface:
- Improves **completion rates** (conversion through the funnel)
- Reduces **completion time** (efficiency)
- Minimizes **error rates** (usability & friction)

## Experiment Design
- **Period:** March 15, 2017 - June 20, 2017
- **Control Group:** Existing interface
- **Test Group:** Redesigned interface

**User Journey (Funnel)**
Start → Step 1 → Step 2 → Step 3 → Confirm

This is a **funnel process**:
- Users can drop off at any step
- Users may repeat steps or encounter errors

## Data Sources
- **Client Profiles** (df_final_demo) - demographics
- **Digital Footprints** (df_final_web_data) - user interactions
- **Experiment Roster** (df_final_experiment_clients) - group assignment

## Data Preparation
- Removed **invalid values** (negative time)
- Capped **outliers** (99th percentile)
- Aggregated data at **visit_id x process_step** level
- Ensured consistent ordering using timestamps
- Removed duplicates for the Start and Confirm step

## Methodology
  **Key Metrics**

  - **Completion Rate** - % of users progressing to the next step
  - **Completion Time** - average time spent per step
  - **Error Rate** - % of users going backward in the process
  - **Drop-off step** - users who live the process before completing it

## Statistical Analysis
- **ANOVA** - Compare step times within groups
- **Two-Sample T-Test** - Compare step times between groups
- **Z-Test** - Compare error rates and completion rates
  
All tests were conducted at a **5% significance level (α = 0.05).**

## Hypotheses
  ## Completion Time
For each step:
- **H₀ (Null Hypothesis):** The mean completion time is equal between Test and Control groups
- **H₁ (Alternative Hypothesis):** The mean completion time differs between Test and Control groups

  ## Completion Rate
- **H₀ (Null Hypothesis):** The test completion rate is less than or equal to the control completion rate
- **H₁ (Alternative Hypothesis):** The test completion rate is greater than the control completion rate

  ## Error Rate
- **H₀ (Null Hypothesis):** The error rate is equal between Test and Control groups
- **H₁ (Alternative Hypothesis):** The error rate differs between Test and Control groups

## Results

  ## Completion Time (seconds)

| Step    | Control     | Test       | Δ        |
| ------- | -------     | ------     | -------- |
| start   | 35.24       | **28.36**  | ✅ Faster |
| step_1  | **34.50**   | 36.41      | ❌ Slower |
| step_2  | 89.32       | **85.42**  | ✅ Faster |
| step_3  | 112.11      | **98.12**  | ✅ Faster |


  ## Completion Rate

| Step    | Control    | Test       | Δ         |
| ------- | ---------- | ---------- | --------- |
| start   | 100%       | 100%       | ➖         |
| step_1  | 75.24%     | **84.45%** | ✅ +9.2 pp |
| step_2  | 84.93%     | 85.97%     | ✅ +1.0 pp |
| step_3  | **89.69%** | 89.43%     | ➖         |
| confirm | **83.27%** | 82.50%     | ❌ -0.8 pp |

## Error Rate

| Group   | Error Rate |
| ------- | ---------- |
| Control | 20.33%     |
| Test    | **26.84%** |

Difference is **statistically significant (p < 0.001)**

## Drop-off Rate

| Step    | Control | Test     | Δ        |
| ------- | ------- | ------   | -------- |
| start   | 0       | 0        | ➖ Same  |
| step_1  | 25.8%   | 15.5%    | ✅ Lower |
| step_2  | 15.7%   | 14%      | ✅ Lower |
| step_3  | 10.3%   | 10.6%    | ❌ Higher |
| confirm | 16.7%   | 17.5%    | ❌ Higher |


## Key Insights
**Strong improvement in early conversion**
- Step 1 completion increases by +9 percentage points
- Drop-off at Step 1 significantly decreases
  → Indicates **better engagement and smoother onboarding**

**Faster overall experience**
- Users complete the process **~23 seconds faster**
- Improvments especially in **Start and Step 3**
  → Efficiency gains occur in high-impact stages

**Increased error rate**
- Test group shows **higher error rate (+6.5 pp)**
- The largest increase occurs at the **start step**
  → Suggests **initial confusion or lack of clarity**

**Mixed performance in later stages**

- **Step 2:** Slight improvement (lower drop-off + faster time)
- **Step 3 & Confirm:** Slightly higher drop-off despite faster completion
  → Indicates **remaining friction near the end of the process**

## Trade-Off Analysis

| Metric          | Test vs Control |
| --------------- | --------------- |
| Completion Rate | ✅ Improved                               |
| Completion Time | ✅ Faster                                 |
| Drop-off Rate   | ⚖️ Mixed (better early, worse late)       |
| Error Rate      | ❌ Worse                                  |

The new UI improves **efficiency and progression**, but introduces **usability challenges**

## Interpretation

The redesigned interface:
- Encourages more users to move forward **(higher completion rate & lower early drop-off)**
- Improves efficiency in key steps **(faster completion times)**
- But introduces **more user errors**, particularly at the beginning
- And shows **slight friction at the end of the process**

This suggests:
- The interface is **more engaging and effective at guiding users initially**
- But **less intuitive at first interaction**
- And may still require refinement in **final steps**

## Conclusion

The new UI delivers:
- Higher completion rates
- Lower drop-off in early stages
- Faster completion in key steps
- Higher error rates, especially at the beginning of the process
- Slightly higher drop-off near completion

Overall, the redesign has a **positive impact on conversion and efficiency, but introduces usability issues that affect user accuracy and final-stage completion.**

## Recomendation
**Adopt the new interface with targeted improvements**

Focus on:
- Improving **onboarding clarity (Start & Step 1)**
- Reducing **early-stage confusion and errors**
- Optimizing **final steps (Step 3 & Confirmation)** to reduce drop-off

This would preserve:
- Higher conversion rates
- Strong early engagement
- Faster completion times

While improving:
- Accuracy
- End-of-process completion
- Overall user experience

## Tools & Technologies
- Pyhton (pandas, spicy, ...)
- Tableau (data visualization)

## Key Learnings
- Importance of evaluating **multiple metrics together**
- Trade-offs between **speed, accuracy and conversion**
- Impact of **data cleaning and aggregation choices**
- Applying statistical methods to **real-world product decisions**

## Slides
https://www.canva.com/design/DAHE4KiV2as/TLyEIDOjiR6D1dvwKMh-ow/edit