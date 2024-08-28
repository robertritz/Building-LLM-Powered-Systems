
Welcome to the “Building LLM Powered Systems” course! This course is designed to provide hands-on experience in creating robust systems powered by Large Language Models (LLMs). Throughout this course, you will learn how to design, build, and deploy AI-driven systems that can process data, interact with humans, and perform complex tasks autonomously.

This course is being delivered in person at American University of Mongolia for the Fall 2024 semester.

## Purpose
This course aims to equip students with a **hands-on understanding and practical skills** necessary to **design, implement, and deploy** systems powered by LLMs. Students use LLMs to:

- **Process Data**: Understanding data modalities: natural language, images, audio, etc.
- **Perform Business Tasks**: Data extraction, summarization, and translation are common business tasks that LLMs excel at.
- **Leverage RAG**: Use Retrieval Augmented Generation to ground LLMs with a source of truth.
- **Build Agents**: Build autonomous agents to accomplish a goal using the open source framework CrewAI

The ideal student for the course is someone with Python experience who is interested in leveraging LLMs to get things done. No previous knowledge of LLMs, machine learning, or data science is required. Basic experience with Python is expected including basic data structures and working with functions.

## Topic Outline

| Week #  | Topic                                                                                                              |     |
| ------- | ------------------------------------------------------------------------------------------------------------------ | --- |
| Week 01 | [1] [[Introduction to Large Language Models]]<br>[2] Your First LLM Project<br>[3] Counting Tokens and Rate Limits |     |
| Week 02 | [4] Working with Multi-Modal LLMs<br>[5] Structured Outputs from LLMs                                              |     |
| Week 03 | [6] Evaluating LLMs on a Task<br>[7] Getting Text from the Internet                                                |     |
| Week 04 | [8] Project 1: Extracting and Classifying Data                                                                     |     |
| Week 05 | [9] Creating Embeddings<br>[10] Using a Vector Databases                                                           |     |
| Week 06 | [11] Managing Documents<br>[12] Stuffing, Map Reduce, Reranking                                                    |     |
| Week 07 | [13] Building a Streamlit Chat App                                                                                 |     |
| Week 08 | [14] Project 2: Build a RAG Based Chat Application                                                                 |     |
| Week 09 | [15] Introduction to Agents<br>[16] Build a Simple Agent System                                                    |     |
| Week 10 | [17] Building Agents with CrewAI<br>[18] Hierarchichal vs Sequential Processes                                     |     |
| Week 11 | [19] Allowing Agents to Execute Code<br>[20] Giving Agents Tools                                                   |     |
| Week 12 | [21] Project 3: Build an Agent System                                                                              |     |
| Week 13 | [22] Example Project: Research Assistant                                                                           |     |
| Week 14 | [23] Example Project: Identifying Bias in News                                                                     |     |
| Week 15 | Final Project Presentations (in person course only)                                                                |     |

## Coding Environment

This course will use Google's Gemini 1.5 Pro and Flash models, which offer a generous [free tier](https://ai.google.dev/pricing) via API. Other models can be used if you prefer, but no guidance will be given on how to integrate these models with the course code.

To run the code in this course you will need the following packages. This package list may be amended or edited throughout the semester. Please note these packages have a significant number of dependencies that we will also be using including `numpy` and others.

``` requirements.txt
google-generativeai==0.7.2
crewai==0.51.1
```

It is strongly recommended that you create a Python environment for this course via `venv` or `conda`.

You can choose any IDE or text editor you prefer, but I recommend the following:
- [Visual Studio Code](https://code.visualstudio.com/): This is developed by Microsoft and is completely free. It also has excellent support for Jupyter notebooks via plugins.
- [Cursor](https://www.cursor.com/): This is a fork of Visual Studio Code that has LLM assistance at its core. There is a free tier, pay for a subscription, or use your own API key for LLM providers.
- Zed (my current IDE): Opinionated IDE with speed and style at it's core. It supports cloud LLMs and also local LLMs via Ollama.

## Course Format
This course uses Markdown files (`.md`) and Python (`.py`) files. Why use these files over something like a Jupyter notebook? The short answer is that it's easier to develop LLM systems using executable `.py` files, and keeping two separate pieces of code (one in Jupyter and one in `.py` files) is inefficient and confusing. 

There is another reason to use Markdown for this course. If you are using an LLM enabled IDE like [Cursor](https://www.cursor.com/), [Zed](https://zed.dev/), or [Github Copilot](https://github.com/features/copilot) you will notice that you can easily add files to the context of a prompt you send to an LLM. By having the course files readable by an LLM, you can easily ask questions about this course content and have the LLM assist you in getting work done. If you don't understand something you can simply add that `.md` or `.py` file to the context of the LLM prompt and get help.