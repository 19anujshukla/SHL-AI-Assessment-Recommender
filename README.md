# SHL Assessment Recommendation Engine

This project is a web-based AI-driven recommendation system built using **Streamlit**. It helps recommend suitable SHL assessments based on user input and SHL’s product catalog.

## 🚀 Project Features

- Streamlit-based frontend UI
- Machine Learning model to generate personalized recommendations
- Hosted on [Render](https://shl-ai-assessment-recommender-10.onrender.com)
- Easy-to-use, interactive interface

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Deployment**: Render
- **Other Tools**: Pandas, Scikit-learn, etc.

---

## 📂 Project Structure

```bash
├── assement_data.pkl/          # Trained ML model and assessment data
├── app.py                      # Main Streamlit app (entry point)
├── requirements.txt            # Python dependencies
├── README.md                   # This file

⚠️ Ensure the file `app.py` exists in the root directory or change the `start command` in Render to match your entry file name.

```

---

## 📦 Installation

To run this app locally:

```bash
git clone https://github.com/your-username/shl-assessment-recommender.git
cd shl-assessment-recommender
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment on Render

To deploy this project:

1. Push your code to GitHub.
2. Create a new **Web Service** on [Render](https://shl-ai-assessment-recommender-10.onrender.com).
3. Set the **Build Command** to:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the **Start Command** to:
   ```bash
   streamlit run app.py
   ```
5. Choose Python environment.
6. Deploy!

---

## ❗ Troubleshooting

- **Error: `File does not exist: app.py`**  
  Make sure `app.py` exists in the root folder or update the start command accordingly.
  
- **Streamlit app not opening?**  
  Make sure you’ve exposed a port if you're using a custom server, but with Streamlit/Render this is usually automatic.

---

## 📬 Contact

If you have any questions or feedback, feel free to reach out!

---

## 🏷️ License

This project is licensed under the MIT License.

