# VoiceCommerce AI

**Building reliable, multilingual voice agents for Indian e-commerce.**

VoiceCommerce AI is an independent portfolio project exploring how voice AI can resolve common customer support requests through natural conversations, verified business data and controlled backend actions.

## The Problem

E-commerce companies handle large volumes of repetitive customer enquiries about order status, delivery delays and cancellations. Traditional IVR systems can create friction, while human-assisted support can be expensive to scale.

Voice AI offers an opportunity to automate routine requests, but a useful enterprise solution must do more than speak naturally. It must retrieve accurate information, follow business policies, execute authorized actions and escalate unresolved requests safely.

## What I'm Building

An AI voice agent that supports three customer workflows:

- **Order tracking:** Retrieve an order's status and estimated delivery.
- **Order cancellation:** Check eligibility, confirm customer intent and execute permitted cancellations in a simulated environment.
- **Human escalation:** Create a handoff summary when the agent cannot resolve a request safely.

The initial prototype will support English and Hindi and use synthetic order data.

## Proposed Technology Stack

- **Voice AI:** ElevenLabs Conversational AI and/or Sarvam Voice Agents.
- **Backend:** Python and FastAPI.
- **Data:** SQLite initially, with potential extensions to PostgreSQL and Redis.
- **Evaluation:** Automated test scenarios for correctness, tool use, policy compliance and latency.

Technology choices will be guided by the requirements of the use case rather than by the number of tools used.

## How I'll Measure Success

The project will evaluate:

- Task completion and tool-call accuracy.
- Accuracy of order information.
- Compliance with authorization and cancellation policies.
- Response latency and failure handling.
- English and Hindi conversation quality.
- Estimated cost per successfully resolved enquiry.

## Business Value Hypothesis

A reliable voice agent could reduce support costs and improve customer experience by resolving eligible enquiries without human intervention.

I'll build an illustrative ROI model and distinguish business hypotheses from results measured in the prototype.

## Project Status

**Phase 1: Problem definition and project setup.**

Next: build the backend API, connect a voice agent and evaluate it against a defined set of customer scenarios.

## About This Project

This is an independent learning and portfolio project using synthetic data. It is not an official product or deployment by ElevenLabs, Sarvam AI or any other technology provider.
