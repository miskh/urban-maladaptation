# Urban Maladaptation in Times of Epidemics

This repository contains the analysis code for the paper **"On Urban Maladaptation in Times of Epidemics"** (under review).

Using a large-scale agent-based model of The Hague (Netherlands) during the COVID-19 pandemic, we explore how "one-size-fits-all" crisis interventions can lead to unintended consequences in heterogeneous urban environments. We find that a uniform lockdown policy can inadvertently increase infection risk in some districts while protecting others. We refer to this phenomenon as **urban maladaptation**, drawing on the established concept of maladaptation from climate studies (e.g., [Schipper, 2020](https://www.sciencedirect.com/science/article/pii/S2590332220304838)).

## Repository Structure

```
├── figures/              # Generated figures (EPS, PDF, PNG, SVG)
├── notebooks/            # Analysis notebooks
│   ├── 1.1-no-response.ipynb
│   ├── 1.2-maladaptation.ipynb
│   ├── 1.3-uai.ipynb
│   ├── 2-supplementary-info.ipynb
│   └── utils.py          # Helper functions
└── results/              # Simulation results
    ├── baseline/         # No-response scenario results
    └── lockdown/         # Hard lockdown scenario results
```

## Reproducing the Analysis

### Requirements

The analysis uses Python with just a few basic packages:

  * `pandas`, `numpy` - Data manipulation
  * `geopandas` - Spatial analysis
  * `matplotlib`, `seaborn` - Visualisation

### Running the Notebooks

The analysis is organised into sequential notebooks:

1.  **`1.1-no-response.ipynb`** - Analysis of the no-response (baseline) scenario
2.  **`1.2-maladaptation.ipynb`** - Analysis of the hard lockdown scenario and maladaptation patterns
3.  **`1.3-uai.ipynb`** - Calculation and visualisation of the Urban Adaptation Index
4.  **`2-supplementary-info.ipynb`** - Supplementary information and additional analyses

After downloading the input data from [4TU.ResearchData](https://doi.org/10.4121/33c01ff0-d3af-4293-8690-339bbca2bb37) and placing it in the `results/` directory, run notebooks in sequence to reproduce the figures and results presented in the paper.

## Data & Model

### Agent-Based Model

Our analysis is based on a large-scale agent-based model simulating the daily lives of all citizens of The Hague, including:

  * Socio-demographic characteristics (age, household size, etc.)
  * Daily activity schedules (work, shopping, meeting friends)
  * Places of interest (schools, supermarkets, parks, etc.)
  * Mobility patterns
  * Area-based disease transmission and SEIRD progression models
  * Policy interventions (closures, social distancing, masks, etc.)

**Model code**: Available at [github.com/averbraeck/medlabs-heros](https://github.com/averbraeck/medlabs-heros)

### Datasets

**Simulation input data**:
  * [Time Use Survey (TUS) Netherlands 2019](https://digital.scp.nl/timeuse2/about-the-time-use-survey/)
  * [Onderweg in Nederland (ODiN) travel survey 2019](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen/microdatabestanden/odin2019-onderweg-in-nederland-2019)
  * OpenStreetMap PBF file (January 2020)
  * [Municipality of The Hague demographic and business data (2020)](https://denhaag.incijfers.nl/)

**Simulation outputs**: Available at [4TU.ResearchData](https://doi.org/10.4121/33c01ff0-d3af-4293-8690-339bbca2bb37)

## Citation

```bibtex
@article{sirenko2025maladaptation,
  title={On Urban Maladaptation in Times of Epidemics},
  author={Sirenko, Mikhail and Verbraeck, Alexander and Comes, Tina},
  journal={Under review},
  year={2025}
}
```

## Authors
  * *Mikhail Sirenko* - [:octocat: github.com/miskh](https://github.com/miskh)
  * *Alexander Verbraeck* - [:octocat: github.com/averbraeck](https://github.com/averbraeck)
  * *Tina Comes* - [:briefcase: LinkedIn](https://nl.linkedin.com/in/tina-comes-a084ab27)

## Acknowledgments

This research was supported by the European Union's Horizon 2020 research and innovation programme under grant agreement No 101003606.

Mikhail Sirenko is extremely grateful to *Daan van Bilsen*, *Sahiti Sarva*, *Jin Rui Yap*, *Fabio Tejedor*, *Anmol Soni*, *Hidde Bijlard*, and *Srijith Balakrishnan* for their enormous contribution to the foundation of this work.

## License

Please refer to the specific license terms associated with the datasets and model code linked above.
