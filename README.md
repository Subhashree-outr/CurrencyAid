# CurrencyAid

### AI-Based Offline Currency Recognition Device for Visually Impaired Users

Currency Aid is an AI-powered assistive technology project designed to help visually impaired users identify currency notes independently.

The system uses computer vision and an AI model to recognize currency denominations and provides the result through voice feedback. The long-term goal is to create a low-cost, offline, standalone device that does not require a smartphone or internet connection.

---

## 🎯 Problem Statement

Visually impaired individuals can face difficulties identifying currency notes, particularly when different denominations have similar physical characteristics.

Although smartphone-based currency recognition applications exist, they may require:

- Smartphone usage
- Internet connectivity
- Familiarity with applications
- Screen-reader interaction

Currency Aid aims to provide a simpler alternative through a dedicated hardware interface with minimal user interaction.

---

## 💡 Proposed Solution

Currency Aid combines:

**Camera + Edge AI + Audio Feedback + Simple Hardware Interface**

The user places a currency note in front of the camera and presses a physical button.

The system then:

1. Captures the currency image
2. Processes the image
3. Runs the AI model
4. Identifies the denomination
5. Checks prediction confidence
6. Announces the result through a speaker

### System Flow

```text
       Currency Note
             ↓
          Camera
             ↓
      Image Processing
             ↓
          AI Model
             ↓
     Currency Prediction
             ↓
      Confidence Check
          ↙       ↘
      Reliable    Uncertain
         ↓            ↓
      Speaker      "Try Again"
         ↓
   Currency Value
