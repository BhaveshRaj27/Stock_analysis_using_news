# LLM Research Tool
- The tool aims to allow the user to query multiple web pages together or summarize them. 
- The tool takes URLs as input, creates word embeddings  using OpenAI embedding and stores them as vectors in FAISS(work as vector database here).
- When a user queries the URL, query embedding gets created and a semantic search is performed to find the best matches for the query inside the vector database.
- The best match + query is fed to the LLM to generate the result.

**How to run the tool**
- clone the repository
`git clone https://github.com/BhaveshRaj27/Stock_analysis_using_news.git`
- Add OpenAI API key to .env file `OPENAI_API_KEY =''`
- Run the command `streamlit run main.py`

**Problem overcome with tools**
- There are two problems which our LLM Research tool overcome:-
    -   Token limit exceed in Chatgpt UI:
        - The UI GPT will show the token limit exceeded if we provide more than 1 or 2 articles, Further copy-pasting multiple articles word to word is a tedious 
          task.
        - The data is divided into chunks and then converted vectors, so we have only extracted parts most relatable to a given query.
        - Further, the Map-reduce method is used, all the semantically similar chunks are fed to a separate LLM instance and their output is then sent to a final LLM 
          instance to combine them.
    -   Hallucination and Biases:
        - After the training cutoff, LLM models don't have information about the  new events happening, therefore they hallucinate the answer for such events. I 
          We have used RAG (Retrieval Augmented Generation), which helped us mitigate the model's hallucination.


https://github.com/user-attachments/assets/ddf05ba0-3a35-4ec4-b4e3-b33f1040a96b

