# Fluxion
# 🚨 Advanced Pipeline Leak Detection – Demo Digital Twin

## 🧠 Objective

Create a **high-fidelity pipeline simulation** with ultra-fast **leak detection and localization** using a **physics-informed neural network (PINN)**. The system emulates real-time sensor data and dynamically responds to leak events, delivering **low-latency alerts** and visualization.

This is a **demo-grade digital twin**, built with production-level thought and expandable design.

---

## 🏗️ Architecture

### 🧪 1. Core Simulation
- **Language:** Python
- **Libraries:** `tsnet`, `pandapipes`, `scipy`
- **Design:**
  - Modular pipe segments with physics-based calculations
  - Transient dynamics using **Darcy–Weisbach** & **Joukowsky** equations
  - Leak injector using **orifice flow** dynamics

---

### 🔧 2. Sensor System
- Simulated sensors on each pipeline segment
- Tracks:
  - Pressure
  - Temperature
  - Flow
- Injects **realistic noise** into readings
- Fast transient monitoring with **anomaly flags**

---

### 🌐 3. Real-Time Data Streaming
- **Tech:** Python `websockets`
- **Goal:** Stream data every 0.5s (or faster) during events
- **Pipeline:**
  - Sensor readings → Websocket server → Frontend updates

---

### 🖥️ 4. Interactive UI
- **Framework:** `Streamlit` (or `Dash`)
- **Features:**
  - Visual pipeline map
  - Real-time gauges & heat indicators
  - Leak injector controls
  - Live alerts and leak localization
- Designed for **demo fluidity** + fast response

---

### 🧠 5. AI Module – Physics-Informed Neural Network (PINN)
- **Framework:** `PyTorch`
- Learns from simulated data:
  - Pressure wave signatures
  - Transients caused by leaks
- **Outputs:**
  - Leak probability
  - Estimated location
- **Training Loss =** Data loss + Physics loss (mass, momentum)

---

### 🛠️ 6. Synthetic Data Generator
- Auto-generates labeled data for training:
  - Leak vs. non-leak
  - Leak size, position, time
- Wide variety of physical behaviors covered

---

## 📁 Folder Structure

