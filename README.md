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

## Statistical Analysis
- **ANOVA** - Compare step times within groups
- **Two-Sample T-Test** - Compare step times between groups
- **Z-Test** - Compare error rates and completion rates
- 
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

| Step    | Control | Test   | Δ        |
| ------- | ------- | ------ | -------- |
| step_1  | 38.77   | 30.91  | ✅ Faster |
| step_2  | 35.19   | 38.03  | ❌ Slower |
| step_3  | 91.75   | 91.46  | ➖ Same   |
| confirm | 119.87  | 106.54 | ✅ Faster |

**Total improvement:** ~ 19 seconds faster (~ 6-7%)

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

## Key Insights
**Strong improvement in early conversion**
- Step 1 completion increases by +9 percentage points
- Indicates better engagement at the start of the journey

**Faster overall experience**
- Users complete the process ~19 seconds faster
- Improvments especially in **Step 1 and Confirmation**

**Increased error rate**
- Test group shows **higher error rate (+6.5 pp)**
- Major spike occurs at the **start step**

**Stable mid-funnel performance**
- Step 2 and Step 3 show minimal differences
- Core process complexity unchanged

## Trade-Off Analysis

| Metric          | Test vs Control |
| --------------- | --------------- |
| Completion Rate | ✅ Improved      |
| Completion Time | ✅ Faster        |
| Error Rate      | ❌ Worse         |

The new UI improves **efficiency and progression**, but reduces **usability**

## Interpretation

The redesigned interface:
- Encourages more users to move forward (higher completion rate)
- Reduces total time spent (higher efficiency)
- But introduces **more user errors**, especially early in the journey

This suggests:
- The interface is more engaging but less intuitive at the beginning

## Conclusion

The new UI delivers:
- Higher completion rates (especially early funnel)
- Faster completion times
- Higher error rates

## Recomendation
**Adopt the new interface with improvements**

Focus on:
- Improving **onboarding clarity (Start & Step 1)**
- Reducing early-stage confusion and errors

This would preserve:
- High conversion
- Faster completion

While improving:
- Usability and user experience

## Tools & Technologies
- Pyhton (pandas, spicy, ...)
- Tableau (data visualization)

## Key Learnings
- Importance of evaluating **multiple metrics together**
- Trade-offs between **speed, accuracy and conversion**
- Impact of **data cleaning and aggregation choices**
- Applying statistical methods to **real-world product decisions**