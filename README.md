# 🧠 Facial-Recognition-and-Spatial-Frequency-Analysis-
A project exploring how **spatial frequency information** affects **facial identity perception** and how **Active Appearance Models (AAMs)** can be used to model perceptual dynamics in facial recognition.

## 🧩 Phase One: Spatial Frequency and Identity Detection

### 1. Overview
Facial recognition is a core function of human social cognition. The human brain can extract identity, expression, and emotion using information from various spatial frequency bands.

This phase investigates how filtering facial images into **low**, **high**, and **intact spatial frequency bands** impacts participants’ ability to recognize facial identity. By applying controlled filters and measuring behavioral responses, we explore the computational and perceptual mechanisms of face processing.

**Keywords:** spatial frequency, cognitive science, psychophysics, face processing, identity recognition

---

### 2. Experimental Design

#### Setup
- **Identities:** Two male and two female faces  
- **Morphing:** 7 morph levels per pair (interpolating between the two identities)  
- **Spatial Frequencies:** Low (LF), High (HF), Intact (IF)  
- **Stimuli:** 14 images × 3 frequency levels = **42 total stimuli**  
- **Trials:** 42 × 32 repetitions = **1344 trials**

#### Procedure
1. **Training:** Participants learn to identify the four main faces.
2. **Main Task:**
   - Three *frequency-specific* blocks (“same” blocks)
   - One *mixed* block with all frequencies
3. **Trial Flow:**
   - Face displayed for 400 ms
   - Two name options appear (one left, one right)
   - Participant has 3 s to choose the matching identity
4. **Control Variables:**
   - Gender of morphs (male/male or female/female)
   - Response hand randomized per block (left/right)

---

### 3. Data Format

Data are provided in both **CSV** and **MAT** formats.

#### `subjectInfo`
| Variable | Description |
|----------|-------------|
| `age` | Participant age |
| `sex` | Gender |
| `dom` | Dominant hand |

#### `data`
| Variable | Description |
|-----------|-------------|
| `trialKeys` | Face pair (“MahGol” or “AbHa”) |
| `levelFreq` | Frequency condition (IF, LF, HF) |
| `levelFace` | Morph level (−3 to 3) |
| `lCueName`, `rCueName` | Name options shown left/right |
| `srespLoc`, `srespChoice` | Response and selected ID |
| `RT` | Reaction time |
| `Hand` | Response hand used |
| `blockType` | “same” or “mix” |
| `subjectID` | Participant identifier |

---

### 4. Analysis Pipeline

#### (1) Psychometric Fitting
Behavioral data are fitted with a **sigmoidal psychometric curve** to estimate perceptual sensitivity.

Simple sigmoid:

\[
\sigma(x) = \frac{\alpha}{1 + e^{-\beta x}}
\]

Generalized sigmoid:

\[
\sigma(x) = \frac{\alpha}{1 + e^{-\beta(x - y)}} + \lambda
\]

Model fits (Sigmoid vs. Gaussian CDF) are compared using **AIC** or **BIC** to balance accuracy and complexity.

##### Hypotheses Tested
- Differences in sensitivity across spatial frequency bands  
- Gender-related performance differences  
- Influence of response hand (left vs right)  
- Role of dominant hand on accuracy  
- Same-gender vs. opposite-gender recognition effects

All tests are conducted on “same” blocks using appropriate statistical analyses (e.g., t-tests, ANOVA).

---

#### (2) Sensitivity via ROC Analysis
An alternative sensitivity metric uses the **Area Under the ROC Curve (AuROC)** to quantify separability (sROC) between identities.  
The ROC analysis provides a model-free estimate of participants’ discriminability across frequency conditions and subject factors.

---

#### (3) Exploratory Hypotheses
Additional hypotheses can be explored by combining behavioral and demographic variables, such as correlations between reaction time and spatial frequency sensitivity, or hand-specific lateralization effects.

---

## ⚙️ Phase Two: Active Appearance Model-Based Perceptual Analysis

### 1. Concept
This phase introduces **Active Appearance Models (AAMs)** to study **closed-loop perceptual systems**.  
AAMs represent facial variation in two orthogonal components:

- **Shape Features:** Landmark geometry (e.g., eyes, nose, mouth).  
- **Appearance Features:** Texture and illumination properties.  

By generating morph sequences within the AAM latent space, the system can simulate dynamic face perception, where each participant’s choice provides feedback to guide subsequent stimulus generation—analogous to a **closed-loop adaptive system**.

---

### 2. PsychoPy Experiment Design

**Goal:** Measure perceptual sensitivity along controlled morph continua using AAM-generated faces.

**Materials:**
- Two folders: `app/` (appearance) and `sha/` (shape)  
- Each contains 20 subfolders (`f0`–`f19`) with 100 images each (morph continuum)

**Feature Assignment:**
- Select features based on an index (e.g., last digit of subject or run ID)
- Use four folders: `app/fX`, `app/fX+10`, `sha/fX`, `sha/fX+10`

**Image Selection:**
- From each folder, choose 10 images evenly spaced along the morph continuum (e.g., 10, 20, …, 100).

**Trial Design:**
- Each image presented 10 times (randomized)
- Participants judge which original face the image resembles more
- Responses mapped to two keys (e.g., `A` = Face 1, `L` = Face 2)

**Data Analysis:**
- Compute proportion of “Face 1” responses vs. morph level
- Fit **sigmoid** or **cumulative Gaussian** curves
- Calculate **Just Noticeable Difference (JND)** for each condition

---

## 📊 Deliverables

- PsychoPy experiment code (`.py` or `.psyexp`)  
- Raw and processed data  
- Psychometric plots with fitted curves  
- Calculated JND values  
- Short report summarizing methodology, results, and interpretations

---

## 🧮 References

1. Kanwisher et al. (1997) — Fusiform Face Area (FFA)  
2. Haxby et al. (2000) — Distributed neural systems for face perception  
3. Cootes et al. (2001) — Active Appearance Models  
4. Blanz & Vetter (1999) — 3D morphable models  
5. Chang & Tsao (2017) — Neural face codes  
6. Freiwald et al. (2009) — Face processing networks in primates  

---

## 🧰 Repository Structure

