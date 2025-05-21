# Smart Factory-as-a-Service (SFaaS)

Streamlit-based MVP with KPIs, predictive maintenance, and MQTT integration.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run with Docker

```bash
docker build -t sfaaas .
docker run -p 8501:8501 sfaaas
```

## MQTT Simulation

```bash
python mqtt_simulator.py
```

Default login: admin / admin
