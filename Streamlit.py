

st.title("Text Analysis Tool")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Clustering
    st.header("Text Clustering")
    num_clusters = st.slider("Select number of clusters", min_value=2, max_value=10, value=3)
    df['Cluster'] = cluster_text(df['Comment'], n_clusters=num_clusters)
    st.write("Clustered Data:", df[['Comment', 'Cluster']])

    # Sentiment Analysis
    st.header("Sentiment Analysis")
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)
    st.write("Sentiment Analysis Results:", df[['Comment', 'Sentiment']])

    # Download results
    st.download_button(
        label="Download Results as CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="text_analysis_results.csv",
        mime="text/csv"
    )
