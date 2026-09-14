# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

*Note: This repository validates Agnara 0.1.0a8, but the repository version itself is 1.0.x.*

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please report it via a **Private Security Advisory** on GitHub, or email `security@agnara.dev`.

Please **do not** open a public issue for security-related flaws.

## Threat Surface

As a validation repository, this project is designed to run locally or in ephemeral CI environments. However, the architectural validation it provides forms the basis for production applications. 

- Do not commit secrets, tokens, or PII.
- Ensure that testing does not leak local credentials.

## Disclosure

We aim to address vulnerabilities rapidly and will coordinate disclosure appropriately.
