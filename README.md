# Aind.Behavior.CookieCutter.Template
A cookiecutter template for Aind.Behavior repositories

## General instructions

This repository follows the project structure laid out in the [Aind.Behavior.Services repository](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services).

## Getting Started

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you haven't already.
   1. `pip install cookiecutter`
2. Run `cookiecutter https://github.com/AllenNeuralDynamics/Aind.Behavior.CookieCutter.Template` in the directory where you want to create your new repository.
3. Follow the prompts to fill in the repository name, description, etc.
4. Push the new repository to GitHub.

## Manual steps

Most of these steps are optional.

### Add topics to the repository

1. Go to the repository on GitHub.
2. Click on the cogwheel next to the `About` section.
3. Click on `Topics`.
4. Add your topics of choice. For Aind Behavior repositories, I have been using `aind-behavior`

### Deploying docs

The docs use sphinx. To deploy locally run `make html` in the `docs` directory. To deploy on GitHub pages, follow these steps:

1. Open a new branch called `gh-pages`.
2. Go to the repository on GitHub.
3. Click on `Settings`.
4. Click on `Pages`.
5. Select `Deploy from a branch` under `Source` and select the `gh-pages` as the source branch.
6. Click on the cogwheel next to the `About` section.
7. Select `Use your GitHub Pages website` under `Website`.

Some functionality may be disabled / commented by default. To enable it, uncomment the relevant lines in the `conf.py` file in the `docs` directory.