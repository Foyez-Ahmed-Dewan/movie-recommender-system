<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Content-Based Recommendation System</h1>
<p>This project is a content-based recommendation system built using the TMDB movies dataset. It provides movie recommendations based on the similarity of movie descriptions.</p>

<h2>Features</h2>
<ul>
    <li><strong>Dataset:</strong> Utilizes the TMDB movies dataset.</li>
    <li><strong>Text Vectorization:</strong> Converts movie descriptions into vectors using <code>CountVectorizer</code>.</li>
    <li><strong>Stemming:</strong> Reduces similar words to their root form for better similarity comparison.</li>
    <li><strong>Similarity Calculation:</strong> Computes cosine similarity to find the closest vectors (i.e., related movies).</li>
    <li><strong>Model Serialization:</strong> Uses the <code>pickle</code> library to save and load the recommendation model.</li>
    <li><strong>Poster Fetching:</strong> Fetches movie posters using the TMDB API.</li>
    <li><strong>Frontend:</strong> Built with Streamlit for a user-friendly interface.</li>
</ul>

<h2>How to Run</h2>
<p>To run the application, use the following command:</p>
<pre><code>streamlit run app.py</code></pre>

</body>
</html>
