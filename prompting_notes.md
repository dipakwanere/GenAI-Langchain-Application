# Prompting Notes (GenAI)

This document summarizes different prompting techniques used in Generative AI. Explanations are kept very simple and short, suitable for beginners.

## Zero-Shot Prompting

Meaning: Ask the model directly without giving any example.

Example:

Explain what Generative AI is.

Use when: Simple or general questions.

## One-Shot Prompting

Meaning: Give one example, then ask a similar question.

Example:

India → Currency is INR
France → ?

Use when: You want the model to follow a pattern.

## Few-Shot Prompting

Meaning: Give multiple examples before asking.

Example:

India → INR
USA → USD
Japan → ?

Use when: Format and consistency matter.

## Instruction Prompting

Meaning: Clearly tell the model what to do.

Example:

Explain Bitcoin in 2 short paragraphs using simple language.

Use when: You want controlled and clear output.

## Role-Based Prompting

Meaning: Assign a role to the model.

Example:

You are a financial expert. Explain inflation.

Use when: Domain-specific or professional answers are needed.

## Chain-of-Thought Prompting

Meaning: Ask the model to think step by step.

Example:

Explain step by step how exchange rates work.

Use when: Logical reasoning or problem-solving is required.

## Self-Consistency Prompting

Meaning: Ask the model to generate multiple answers and select the best one.

Example:

Solve this problem three times and give the best answer.

Use when: Accuracy is important.

## Output-Format Prompting

Meaning: Tell the model how the output should look.

Example:

Answer in bullet points.

Use when: Output needs to be structured (APIs, UI).

## Context-Based Prompting

Meaning: Provide background information before asking.

Example:

Given this article, summarize it in 5 lines.

Use when: Working with long or specific content.

## RAG (Retrieval-Augmented Generation) Prompting

Meaning: Model answers using external documents.

Example:

Using the provided document, answer the question.

Use when: Working with PDFs, databases, or company data.

## Requires paid APIs and a vector database.

# Quick Summary
- Zero-shot -->	Ask directly
- One/Few-shot -->	Teach a pattern
- Instruction -->	Control output
- Role-based -->	Expert answers
- Chain-of-thought -->	Step-by-step reasoning
- Output format -->	Structured results
- Context-based -->	Use background
- RAG -->	External knowledge

Use these prompting techniques based on task complexity, accuracy needs, and output control.