import streamlit as st
import joblib
import pandas as pd

bundle = joblib.load("artifacts/olist_models.joblib")

st.title("Olist – Segmentation & Prédiction (interprétable)")

features = bundle["features"]

st.subheader("Entrer les caractéristiques du client")
inputs = {}
for f in features:
    inputs[f] = st.number_input(f, value=0.0)

if st.button("Analyser"):
    from math import isfinite

    # construire dict
    input_dict = {k: float(v) for k, v in inputs.items()}

    # appel fonction
    def interpret_client(input_dict, bundle):
        import numpy as np
        import pandas as pd
        features = bundle["features"]
        scaler = bundle["scaler"]
        kmeans = bundle["kmeans"]
        reg = bundle["reg_model"]
        clf = bundle["clf_model"]
        seg_names = bundle["segment_names"]

        x = pd.DataFrame([input_dict])[features]
        seg = int(kmeans.predict(scaler.transform(x))[0])
        ca_pred = float(reg.predict(x)[0])
        proba = float(clf.predict_proba(x)[0,1]) if hasattr(clf, "predict_proba") else float(clf.predict(x)[0])

        explanations = []
        if input_dict.get("recency_days", 999) < 30:
            explanations.append("Client actif (récence faible).")
        if input_dict.get("frequency", 0) >= 3:
            explanations.append("Client fidèle (fréquence élevée).")
        if input_dict.get("avg_delay", 0) > 10:
            explanations.append("Risque logistique (délai élevé).")
        if input_dict.get("avg_review", 5) < 3:
            explanations.append("Satisfaction faible (avis bas).")

        return {
            "segment_name": seg_names.get(seg, str(seg)),
            "predicted_revenue": ca_pred,
            "high_value_probability": proba,
            "explanations": explanations
        }

    out = interpret_client(input_dict, bundle)

    st.success(f"Segment : {out['segment_name']}")
    st.write(f"CA estimé : **{out['predicted_revenue']:.2f}**")
    st.write(f"Probabilité High Value : **{out['high_value_probability']:.2%}**")

    st.subheader("Interprétation")
    for e in out["explanations"]:
        st.write("✅ " + e)
