# 🧠 Facial-Recognition-and-Spatial-Frequency-Analysis-
A project exploring how **spatial frequency information** affects **facial identity perception** and how **Active Appearance Models (AAMs)** can be used to model perceptual dynamics in facial recognition.

## 🧠 Project Summary

Human face recognition uses geometry, texture, and spectral information. This project probes how **intact**, **low**, and **high** spatial-frequency content influences identity detection along morph continua between two identities. Analyses include psychometric function fitting, ROC-based sensitivity measures, and closed-loop perceptual experiments with Active Appearance Models (AAMs).

---

## 🔬 Experiment Design

### Stimuli
- Two identity pairs (male and female) were morphed across **7 levels** (from one identity extreme to the other).
- Each morph level was processed into three spectral conditions:
  - **IF** — Intact frequency
  - **LF** — Low-frequency filtered
  - **HF** — High-frequency filtered  
- **Total stimuli:** 14 morph images × 3 frequency conditions = **42 images**.

### Trial / Block Structure
- Each trial: stimulus shown centrally for **400 ms**, then two name options shown left/right.
- Participant has **3 seconds** to choose which identity the image matches more closely.
- Blocks:
  - Three **"same"** blocks (each contains stimuli from only one frequency band).
  - One **"mix"** block (trials randomly drawn from all bands).
- Each subject: **1,344 trials** (42 images × 32 repetitions).
- Training: participants learn face–name associations before starting; training uses the same frequency condition as the block.

---

## 📁 Data Format

Data are provided in both **CSV** and **MAT** formats and include:
- `subjectInfo` — demographic and subject-level data (age, sex, dom hand).
- `data` — per-trial table with fields such as:
  - `trialKeys` (e.g., "MahGol", "AbHa")
  - `levelFreq` (IF / LF / HF)
  - `levelFace` (morph level: -3 → +3)
  - `lCueName`, `rCueName` (left / right option labels)
  - `srespLoc`, `srespChoice` (response key & choice)
  - `RT` (reaction time)
  - `Hand` (hand used)
  - `blockType` ("same" / "mix")
  - `subjectID`

---

## 📊 Analysis Overview

All analyses are done per-subject and then aggregate-tested across the population.

### 1. Psychometric Fitting
- Fit psychometric curves to response proportions across morph levels.
- Candidate models: simple sigmoid (σ(x) = α / (1 + exp(−βx))) and Gaussian CDF; extended sigmoids with shift and lapse terms are considered.
- Model comparison using **AIC / BIC** to penalize model complexity.
- Main metric extracted: **sensitivity (β)** from the sigmoid fit.
- Stratifications: spatial frequency, block type, trialKey (identity pair), hand, subject sex, and dominance.

### 2. ROC-Based Sensitivity
- Compute **Area under the ROC (AuROC)** to quantify separability between identity classes under different conditions.
- Use AuROC as an alternative sensitivity metric and repeat hypothesis tests conducted for the psychometric fits.

### 3. Hypothesis Tests
Example hypotheses tested:
- Sensitivity differs across spatial frequency bands (IF vs LF vs HF).
- Recognition performance varies with gender of face stimulus or participant.
- Hand used (left / right / dominant) influences sensitivity.

### 4. Exploratory Hypothesis
- Additional exploratory tests formulated and evaluated using the same data (e.g., interactions between frequency band and morph steepness, or reaction time trade-offs).

---

## 🔁 Phase Two — Closed-Loop AAM Task

- Extended the study into an adaptive, closed-loop paradigm using **Active Appearance Models (AAMs)**.
- At each step, participants choose which of four generated images is most similar to a target; the chosen image seeds the next generation of images (iterative steering through AAM latent space).
- This implements a feedback-driven trajectory toward a target identity and probes perceptual navigation in a generative face space.

---

## 💻 Implementation & Tools

- **Primary languages / libraries:** Python (NumPy, SciPy, Matplotlib), PsychoPy
- **Data:** CSV and MAT
- **Scripts / outputs included (suggested):**
  - PsychoPy experiment (`.py` or `.psyexp`)
  - Preprocessing and cleaning scripts
  - Fitting and model comparison scripts
  - Visualization scripts (psychometric curves, ROC plots)
  - Summary report and JND calculations

---

📜 License  
This repository is provided for research and academic use.  
Please acknowledge this work appropriately if it informs your analyses.
