#LLM Research Tool
- The tool aims to allow the user to query multiple web pages together or summarize them. 
- The tool takes URLs as input, creates word embeddings  using OpenAI embedding and stores them as as vectors in FAISS(work as vector database here).
- When a user queries the URL, query embedding gets created and a semantic search is performed to find the best matches for the query inside the vector database.
- The best match + query is fed to the LLM to generate the result.

**How to run the tool**
- clone the repository
`git clone https://github.com/BhaveshRaj27/Stock_analysis_using_news.git`
- Add OpenAI API key to .env file `OPENAI_API_KEY =''`
- Run the command `streamlit run main.py`

**Problem overcome with tools**
- There are two problems which our LLM Research tool overcome
    -   Token limit exceed in Chatgpt UI:
         - 
    -   Hallucination and Biases
