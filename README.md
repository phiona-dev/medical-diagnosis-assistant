# Medical Diagnosis Assistant

## Rule-Based Diagnosis using Forward Chaining

---

## Problem Being Solved

Medical diagnosis can be challenging when patients present with multiple overlapping symptoms. Doctors need to consider various diseases, risk factors, and vital signs to reach an accurate diagnosis.

This system solves the problem by providing an **automated, rule-based medical diagnosis assistant** that:

* Accepts patient symptoms, risk factors, and vital signs
* Applies forward chaining inference to match symptoms against 15 diseases
* Returns possible diagnoses with confidence scores
* Explains WHY each diagnosis was reached
* Provides severity levels, urgency recommendations, and treatment suggestions

---

## Facts Used

The knowledge base contains **32 symptoms**, **7 risk factors**, and **5 vital signs** (total 44 facts).

### Symptoms (32 facts)

| Category               | Symptoms                                                                       |
| ---------------------- | ------------------------------------------------------------------------------ |
| **Respiratory**        | Runny Nose, Sneezing, Sore Throat, Cough, Shortness of Breath, Blood in Sputum |
| **General**            | Fever, Headache, Body Aches, Fatigue, Chills, Sweating                         |
| **COVID-specific**     | Loss of Taste, Loss of Smell                                                   |
| **Digestive**          | Nausea, Vomiting, Diarrhea, Abdominal Pain                                     |
| **Serious indicators** | Night Sweats, Weight Loss, Swollen Lymph Nodes                                 |
| **Liver-related**      | Yellow Skin, Dark Urine                                                        |
| **Skin-related**       | Rash, Itchy Blisters                                                           |
| **Urinary**            | Burning Urination, Frequent Urination, Cloudy Urine                            |
| **Neurological**       | Stiff Neck, Sensitivity to Light                                               |
| **Other**              | Joint Pain, Pain when Swallowing                                               |

### Risk Factors (7 facts)

| Risk Factor                   | Relevance                                    |
| ----------------------------- | -------------------------------------------- |
| Recent Travel to Malaria Zone | Indicates possible malaria exposure          |
| Contact with Infected Person  | Suggests contagious disease                  |
| Weakened Immune System        | Increases severity of any infection          |
| Unprotected Sex               | Risk factor for HIV/AIDS, Hepatitis B        |
| Shared Needles                | Risk factor for HIV/AIDS, Hepatitis B        |
| Poor Sanitation               | Risk factor for Hepatitis A, Gastroenteritis |
| Not Vaccinated                | Risk factor for preventable diseases         |

### Vital Signs (5 facts)

| Vital Sign            | Meaning                        |
| --------------------- | ------------------------------ |
| High Fever (>39°C)    | Severe infection               |
| Low Fever (37.5-39°C) | Mild to moderate infection     |
| Normal Temperature    | Likely viral or mild condition |
| Rapid Breathing       | Respiratory distress           |
| Low Blood Pressure    | Potential sepsis/shock         |

---

## Rules Used (15 Rules)

Each rule follows the format: **IF [symptoms + risk factors + vital signs] THEN [disease]**

| Rule ID           | Conditions (all must match)                                              | Disease           | Severity           |
| ----------------- | ------------------------------------------------------------------------ | ----------------- | ------------------ |
| common_cold       | Runny Nose, Sneezing, Sore Throat, Cough                                 | Common Cold       | Mild               |
| influenza         | Fever, Headache, Body Aches, Fatigue, Cough, Chills                      | Influenza (Flu)   | Moderate           |
| covid19           | Fever, Cough, Fatigue, Loss of Taste, Loss of Smell, Shortness of Breath | COVID-19          | Moderate to Severe |
| malaria           | Fever, Headache, Body Aches, Chills, Fatigue, Sweating                   | Malaria           | Severe             |
| tuberculosis      | Cough, Blood in Sputum, Night Sweats, Weight Loss, Fatigue, Fever        | Tuberculosis (TB) | Severe             |
| gastroenteritis   | Nausea, Vomiting, Diarrhea, Abdominal Pain, Fatigue                      | Gastroenteritis   | Mild to Moderate   |
| hiv_aids          | Fatigue, Fever, Swollen Lymph Nodes, Weight Loss, Night Sweats           | HIV/AIDS          | Chronic Severe     |
| hepatitis_a       | Yellow Skin, Dark Urine, Fatigue, Abdominal Pain, Nausea                 | Hepatitis A       | Moderate           |
| hepatitis_b       | Yellow Skin, Dark Urine, Fatigue, Joint Pain, Abdominal Pain, Nausea     | Hepatitis B       | Severe Chronic     |
| pneumonia         | Cough, Fever, Shortness of Breath, Chest Pain, Fatigue                   | Pneumonia         | Severe             |
| chickenpox        | Rash, Itchy Blisters, Fever, Fatigue, Headache                           | Chickenpox        | Moderate           |
| strep_throat      | Sore Throat, Fever, Swollen Lymph Nodes, Pain when Swallowing            | Strep Throat      | Moderate           |
| uti               | Burning Urination, Frequent Urination, Abdominal Pain, Cloudy Urine      | UTI               | Mild to Moderate   |
| meningitis        | Fever, Headache, Stiff Neck, Sensitivity to Light, Nausea, Vomiting      | Meningitis        | Critical           |
| medical_emergency | High Fever, Shortness of Breath, Stiff Neck, Sensitivity to Light        | Medical Emergency | Critical           |

---

## How Inference Works (Forward Chaining)

The system uses **Forward Chaining** - a data-driven inference method.

### Process Flow:

```text
Step 1: Input patient data
        ↓
Step 2: Convert inputs to facts
        ↓
Step 3: Check each rule against facts
        ↓
Step 4: Calculate confidence percentage
        ↓
Step 5: If confidence ≥ 75%, add to diagnoses
        ↓
Step 6: Sort diagnoses by confidence (highest first)
        ↓
Step 7: Display results with explanations
```

### Confidence Calculation Example:

**Influenza Rule requires:** Fever, Headache, Body Aches, Fatigue, Cough, Chills (6 symptoms)

**Patient has:** Fever, Body Aches, Fatigue, Cough, Chills (5 symptoms)

**Confidence = 5/6 × 100 = 83.3%**

Since 83.3% ≥ 75% threshold → Influenza is diagnosed

### Multi-Step Reasoning:

The system uses **three layers of information**:

1. **Symptoms** - Primary matching criteria
2. **Risk Factors** - Increase confidence for certain diseases
3. **Vital Signs** - Determine severity and urgency

---

## How to Run the System

### Prerequisites

* Python 3.x installed
* No additional libraries required (uses only built-in `json` module)

### Installation

1. **Download the files:**

   * `main.py` - The main program
   * `knowledge_base.json` - The knowledge base

2. **Place both files in the same folder:**

```text
medical-expert-system/
│
├── main.py
└── knowledge_base.json
```

### Running the Program

Open terminal/command prompt and run:

```bash
python main.py
```

### Using the System

1. **Enter symptoms** when prompted (comma-separated)
2. **Answer risk factor questions** (yes/no)
3. **Answer vital signs questions** (yes/no)
4. **View the diagnosis results**

---

## Sample Outputs

### Sample 1: Common Cold Diagnosis

**Input:**

```text
Symptoms: Runny Nose, Sneezing, Sore Throat, Cough
Risk Factors: None
Vital Signs: None
```

**Output:**

```text
==================================================
PATIENT INFORMATION SUMMARY
Symptoms: ['Runny Nose', 'Sneezing', 'Sore Throat', 'Cough']
Risk Factors: None
Vital Signs: None
==================================================

POSSIBLE DIAGNOSES (sorted by confidence)

1. Common Cold
   Confidence: 100%
   Severity: Mild
   Urgency: Rest at home, no medical attention needed
   Treatment: Rest, fluids, over-the-counter cold medication

--------------------------------------------------
EXPLANATION

DIAGNOSIS #1: Common Cold

The rule 'common_cold' was triggered because:
Patient has: Runny Nose
Patient has: Sneezing
Patient has: Sore Throat
Patient has: Cough

Therefore, the system diagnosed: Common Cold
Confidence: 100%
Recommendation: Rest at home, no medical attention needed
```

### Sample 2: COVID-19 Diagnosis

**Input:**

```text
Symptoms: Fever, Cough, Fatigue, Loss of Taste, Loss of Smell
Risk Factors: Contact with Infected Person (yes)
Vital Signs: High Fever (>39°C) (yes)
```

**Output:**

```text
==================================================
PATIENT INFORMATION SUMMARY
Symptoms: ['Fever', 'Cough', 'Fatigue', 'Loss of Taste', 'Loss of Smell']
Risk Factors: ['Contact with Infected Person']
Vital Signs: ['High Fever (>39°C)']
==================================================

POSSIBLE DIAGNOSES (sorted by confidence)

1. COVID-19
   Confidence: 83.3%
   Severity: Moderate to Severe
   Urgency: Isolate immediately, get tested
   Treatment: Isolation, symptomatic treatment, monitor breathing

--------------------------------------------------
EXPLANATION

DIAGNOSIS #1: COVID-19

The rule 'covid19' was triggered because:
Patient has: Fever
Patient has: Cough
Patient has: Fatigue
Patient has: Loss of Taste
Patient has: Loss of Smell

Missing for full confirmation:
Shortness of Breath (not reported)

Therefore, the system diagnosed: COVID-19
Confidence: 83.3%
Recommendation: Isolate immediately, get tested
```

### Sample 3: Multiple Diagnoses (Flu + COVID-19)

**Input:**

```text
Symptoms: Fever, Cough, Fatigue, Body Aches, Chills, Loss of Taste, Loss of Smell
Risk Factors: Contact with Infected Person (yes)
Vital Signs: High Fever (>39°C) (yes)
```

**Output:**

```text
POSSIBLE DIAGNOSES (sorted by confidence)

1. COVID-19
   Confidence: 83.3%
   Severity: Moderate to Severe

2. Influenza (Flu)
   Confidence: 83.3%
   Severity: Moderate
```

### Sample 4: No Diagnosis (Below Threshold)

**Input:**

```text
Symptoms: Runny Nose (only)
Risk Factors: None
Vital Signs: None
```

**Output:**

```text
No diagnosis could be made with the provided symptoms.
```

---

## Summary of Features

| Feature              | Implementation                                          |
| -------------------- | ------------------------------------------------------- |
| Facts                | 32 symptoms + 7 risk factors + 5 vital signs = 44 facts |
| Rules                | 15 disease rules                                        |
| Inference Method     | Forward Chaining                                        |
| Confidence Threshold | 75%                                                     |
| Explanation Facility | Yes - shows why each rule triggered                     |
| Multiple Diagnoses   | Yes - returns all matching diagnoses                    |
| Risk Factors         | Yes - modifies diagnosis confidence                     |
| Vital Signs          | Yes - affects severity assessment                       |

---

## File Structure

```text
medical-expert-system/
│
├── main.py                 # Main program with inference engine
├── knowledge_base.json     # JSON knowledge base (facts + rules)
├── test_cases.md          # Test case documentation
├── semantic_network.png   # Semantic network diagram
└── README.md              # This file
```

---
