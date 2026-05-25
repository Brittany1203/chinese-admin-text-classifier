import pandas as pd
import streamlit as st

from src.rule_engine import classify_column


st.set_page_config(
    page_title="Chinese Admin Text Classifier",
    page_icon="📊",
    layout="wide",
)

st.title("Chinese Administrative Text Consistency Classifier")

st.markdown(
    """
This app checks whether a Chinese government website column name is consistent
with its corresponding site name using explainable rule-based classification.
"""
)

st.sidebar.header("Input Options")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"],
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/synthetic_sample.csv")

st.subheader("Input Data")
st.dataframe(df, use_container_width=True)

required_columns = {"site_name", "parent_column_name", "column_name"}

if not required_columns.issubset(df.columns):
    st.error(
        "CSV must contain these columns: site_name, parent_column_name, column_name"
    )
else:
    results = []

    for _, row in df.iterrows():
        result = classify_column(
            site_name=str(row["site_name"]),
            parent_column_name=str(row["parent_column_name"]),
            column_name=str(row["column_name"]),
        )
        results.append(result)

    result_df = pd.concat([df, pd.DataFrame(results)], axis=1)

    st.subheader("Classification Results")
    st.dataframe(result_df, use_container_width=True)

    st.subheader("Rule Type Distribution")
    rule_counts = result_df["rule_type"].value_counts()
    st.bar_chart(rule_counts)

    if "manual_label" in result_df.columns:
        st.subheader("Evaluation")

        result_df["correct"] = result_df["manual_label"] == result_df["label"]
        accuracy = result_df["correct"].mean()

        st.metric("Accuracy", f"{accuracy:.2%}")

        st.subheader("Incorrect Cases")
        error_df = result_df[result_df["correct"] == False]
        st.dataframe(error_df, use_container_width=True)

    csv = result_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="classification_results.csv",
        mime="text/csv",
    )