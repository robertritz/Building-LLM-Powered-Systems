**Slides for this page:** [[Introduction to Large Language Models - Slides.pdf]]
## What is a large language model?
A large language model (LLM) is a type of artificial intelligence (AI) that excels at understanding and generating human-like text. They are trained on massive datasets of text and code, enabling them to perform a wide range of linguistic tasks. 

## Two Components of LLMs
There are two components to every LLM, training data and deep learning. Shove enough data into the right neural network and train it long enough, and you get an LLM.

#### Training Data
LLMs learn from vast amounts of data, including books, articles, websites, code repositories, and more. This data helps the model develop an understanding of language structure, grammar, and context. Think of it like having a library full of books in your head.

One popular dataset called The Pile[^1] contains over 100 billion words from publicly available sources like Wikipedia, books, and online articles. This massive dataset provides the model with a broad understanding of language patterns and nuances.  

It also introduces all of the inconsistencies, deviant behavior, and toxicity you find on the internet. 

#### Deep Learning
LLMs use deep learning algorithms, specifically a type called "neural networks," to analyze this data.  Each neuron (the boxes in the picture) have weights attached to them. These weights are basically variables in an algebra equation. Combine the weights with the results from the previous neuron, then move those results to the next layer, and so on. 

Weights are the "memory" of the model and are updated during training through a method called back propagation. During training, these weights are adjusted continuously to optimize the model's performance on a specific task. 

Backpropagation iteratively calculates the error between the predicted output and the actual target value, then propagates this error back through the layers of the model.  This backward propagation allows the weights to be adjusted in a way that minimizes the overall error and improves the model's accuracy over time.

![[deep_neural_network.png]]
Source: Wikimedia Commons[^2]

## Training Process
#### Pre-training
This pre-training masks words in text and the model learns to predict that word. After hundreds of training cycles the model becomes very good at predicting the next word using it's training data. 

However this by itself is not very useful. These models ramble on with no grounding or direction. What is needed is task specific fine tuning.

#### End Use Case Fine Tune
Once trained on a massive dataset, LLMs can be fine-tuned for specific tasks like translation, summarization, or writing different kinds of creative content. This involves further training the model on specialized datasets tailored to the desired task. 

For services like Gemini, Claude, or ChatGPT these models are fine tuned on question answer pairs (or longer conversations) to make the model behave the way it does. This fine tuning can also steer the model with specific guidelines like harm reduction, helpfulness, and more.

For example, a model trained on a large corpus of scientific articles might excel at summarizing research papers or generating technical documentation.

#### Predictive Text Generation
Based on their training, LLMs can predict what comes next in a sequence of words. This ability allows them to generate coherent and grammatically correct text. For example, if you ask an LLM "What is the capital of France?" it will likely respond with "Paris."

It is important to remember that these LLMs are not reasoning. They are simply predicting the statistically likely next token. 

## Examples of LLM capabilities

LLMs can be trained to do many things. Large so called "foundation models" (GPT4, Gemini, Claude, etc.) are capable of many tasks. However it is also possible to have a smaller model trained to do specific tasks well.

* **Text Summarization:**  LLMs can condense long documents into concise summaries while retaining key information.
* **Translation:** LLMs can translate text from one language to another, often achieving impressive accuracy. 
* **Creative Writing:**  LLMs can generate stories, poems, and even code in various programming languages.
* **Question Answering:** LLMs can answer questions based on the knowledge they have acquired during training.
* **Chatbots:** LLMs are used to power chatbots that can engage in human-like conversations.

## Key Issues With LLMs

### Hallucination
LLMs have a habit of making things up. It is still common to find links, code syntax, and other text that is completely fabricated by the model. This can be reduced somewhat by cleaning the pre-training data and having higher quality fine-tuning data. However this is still an active area of development. 

In short, don't trust everything the LLM spits out.

### Are LLMs Just Compression? Search?
Since LLMs really just predict the next tokens, but they also seem to be capable of holding huge amounts of information, one argument is that LLMs are a unique type of data compression. These models are able to remember a tremendous amount of data and give it back to you in a format that you prefer. 

Another argument about LLMs is that they are very convenient search engines that sometimes make things up. 

### Explainability
One of the most significant challenges with LLMs is their lack of explainability. These models often function as "black boxes" – we can see the input and the output, but the internal processes that lead to a specific response remain opaque. This opacity makes it difficult to understand _why_ an LLM generates a particular output, making it challenging to assess its reasoning, identify potential biases, or trust its decisions in critical applications. 

## A Brief Timeline of LLMs

### 2010-2017: Foundations and Early Innovations

- **2013**: *Word2Vec* was introduced by Tomas Mikolov and his team at Google, providing a method to learn word embeddings from raw text, which improved natural language processing (NLP) tasks significantly[^3][^4].
- **2015**: The *Attention Mechanism* was introduced, enhancing neural machine translation by allowing models to focus on specific parts of input sequences[^3].
- **2017**: The seminal paper "Attention Is All You Need" by Vaswani et al. introduced the *Transformer* architecture, which became foundational for modern LLMs. This architecture allowed for more efficient handling of sequences compared to previous models like RNNs and LSTMs[^6][^7].

### 2018: Emergence of Key Models

- **June 2018**: OpenAI released *GPT (Generative Pre-trained Transformer)*, showcasing the capabilities of unsupervised learning for text generation[^3][^5].
- **October 2018**: Google introduced *BERT (Bidirectional Encoder Representations from Transformers)*, which improved the understanding of context in language tasks through bidirectional training[^3][^5].

### 2019-2020: Expansion and Scaling

- **2019**: OpenAI released *GPT-2*, an improved version of GPT with 1.5 billion parameters, demonstrating advanced text generation capabilities[^3][^5].
- **2020**: OpenAI launched *GPT-3*, a massive model with 175 billion parameters, setting a new standard for LLMs in generating human-like text and performing various NLP tasks[^3][^5].

### 2021-2023: Specialization and Multimodality

- **2021**: Google introduced *LaMDA* for conversational applications, and OpenAI released *DALL·E*, a multimodal model capable of generating images from textual descriptions[^3][^5].
- **2022**: Google released *PaLM*, a large model with 540 billion parameters, continuing the trend of scaling up LLMs[^3][^5].
- **November 2022**: OpenAI launched *ChatGPT*, based on the GPT-3.5 model, which gained widespread attention for its conversational abilities[^5].

### 2023: Continued Advancements

- **March 2023**: OpenAI released *GPT-4*, a more advanced and versatile model than its predecessors, with improvements in understanding and generating text across various contexts[^5].

**[[Your First LLM Project|Next Lecture: Your First LLM Project]]**


[^1]: https://pile.eleuther.ai
[^2]: https://commons.wikimedia.org/wiki/File:Example_of_a_deep_neural_network.png
[^3]:  https://hatchworks.com/blog/gen-ai/large-language-models-guide/
[^4]:  https://ai-researchstudies.com/history-of-large-language-models-from-1940-to-2023/
[^5]:  https://lifearchitect.ai/timeline/
[^6]:  https://drlee.io/an-intuitive-explanation-of-attention-is-all-you-need-the-paper-that-revolutionized-ai-and-39aac5827411?gi=b7ceb6559547
[^7]:  https://en.wikipedia.org/wiki/Attention_Is_All_You_Need