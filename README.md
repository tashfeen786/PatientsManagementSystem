# 🏥 Patients Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-green?style=flat&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-orange?style=flat)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-red?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> 🎯 A full-stack **Patient Management + Medical Insurance Cost Prediction**
> system built with **FastAPI** and **Machine Learning** — manages patient
> records via REST API and predicts insurance costs using a trained ML model.

---

## 🎯 Problem Statement

Healthcare systems need two things simultaneously:
- ❌ A reliable way to **manage patient records** (add, update, delete, view)
- ❌ A tool to **predict medical insurance costs** based on patient profile

**This system solves both** — combining a FastAPI-powered CRUD backend
with a trained ML regression model served as a live prediction endpoint.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 👥 **Patient CRUD** | Add, view, update, delete patient records via REST API |
| 🔍 **Patient Lookup** | Fetch individual patient by ID |
| 💰 **Insurance Prediction** | Predict medical cost from patient profile using ML |
| 🧠 **Trained ML Model** | Pre-trained model served via FastAPI endpoint |
| ✅ **Data Validation** | Pydantic models for strict input validation |
| 📄 **Auto API Docs** | Swagger UI at `/docs` out of the box |

---

## 🔄 System Architecture

```
Patient Data (JSON)
      ↓
FastAPI REST API  ←→  Pydantic Validation
      ↓
  Two Services:
  ┌─────────────────────────────┐
  │  1. Patient Management      │
  │     CRUD Operations         │
  │     patients.json storage   │
  └─────────────────────────────┘
  ┌─────────────────────────────┐
  │  2. Insurance Predictor     │
  │     model.pkl (ML Model)    │
  │     insurance.csv dataset   │
  └─────────────────────────────┘
```

---

## 💰 ML Model — Insurance Cost Prediction

Trained on the **Medical Insurance Cost Dataset** to predict
a patient's insurance charges based on personal health profile.

**Input Features:**
| Feature | Type | Description |
|---------|------|-------------|
| `age` | int | Patient age in years |
| `sex` | str | Gender (male/female) |
| `bmi` | float | Body Mass Index |
| `children` | int | Number of dependents |
| `smoker` | str | Smoking status (yes/no) |
| `region` | str | Geographic region |

**Output:** Predicted annual insurance cost (USD)

---

## 🔌 API Endpoints

```
GET    /                          # Welcome / health check
GET    /patients                  # Get all patients
GET    /patients/{patient_id}     # Get patient by ID
POST   /patients                  # Add new patient
PUT    /patients/{patient_id}     # Update patient record
DELETE /patients/{patient_id}     # Delete patient

POST   /predict                   # Predict insurance cost (ML)
```

### Example — Insurance Prediction

```bash
POST /predict
Content-Type: application/json

{
  "age": 35,
  "sex": "male",
  "bmi": 27.5,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
}

# Response:
{
  "predicted_insurance_cost": 5842.32
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| API Framework | FastAPI |
| Data Validation | Pydantic v2 |
| ML Model | Scikit-learn (Linear Regression) |
| Model Storage | Pickle (model.pkl) |
| Data Storage | JSON file (patients.json) |
| Dataset | Medical Insurance CSV |
| Notebook | Jupyter Notebook |
| Language | Python 3.x |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/tashfeen786/PatientsManagementSystem.git
cd PatientsManagementSystem

# Install dependencies
pip install fastapi uvicorn scikit-learn pandas numpy pydantic

# Start FastAPI server
uvicorn main:app --reload
```

Visit:
- 🌐 API: `http://localhost:8000`
- 📖 Swagger Docs: `http://localhost:8000/docs`
- 📘 ReDoc: `http://localhost:8000/redoc`

---

## 🏗️ Project Structure

```
PatientsManagementSystem/
│
├── main.py                    # FastAPI app — all routes & logic
├── app.py                     # App entry point
├── fastapi_ml_model.ipynb     # ML model training notebook
├── model.pkl                  # Trained ML model (serialized)
├── insurance.csv              # Medical insurance dataset
└── patiants.json              # Patient records storage
```

---

## 📓 ML Training Notebook

The `fastapi_ml_model.ipynb` notebook covers:
- 📊 Exploratory Data Analysis on insurance dataset
- 🔧 Feature engineering & encoding (sex, smoker, region)
- 🤖 Model training — Linear Regression
- 📈 Model evaluation — R² score, MAE, RMSE
- 💾 Model serialization using Pickle → `model.pkl`
- ⚡ FastAPI integration for serving predictions

---

## 🧠 Key Concepts Demonstrated

- ✅ **REST API Design** — proper HTTP methods and status codes
- ✅ **ML Model Serving** — loading pickle model in FastAPI
- ✅ **Pydantic Validation** — type-safe request/response models
- ✅ **CRUD Operations** — full Create, Read, Update, Delete
- ✅ **End-to-End ML Pipeline** — from training to API deployment
- ✅ **JSON-based persistence** — lightweight data storage

---

## 🔮 Future Improvements

- [ ] Replace JSON storage with **PostgreSQL** database
- [ ] Add **JWT authentication** for secure patient access
- [ ] Integrate more ML models (XGBoost, Random Forest)
- [ ] Add **patient history** and medical records tracking
- [ ] Deploy on **Railway / Render**
- [ ] Add **Docker** containerization

---

## 👨‍💻 Author

**Tashfeen Aziz** — AI/ML Engineer & Python Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/tashfeen-aziz-b51361292)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/tashfeen786)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:tashfeen247@gmail.com)

---

⭐ **If you found this project helpful, please give it a star!**
