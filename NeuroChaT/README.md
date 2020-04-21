# NeuroChaT

NeuroChaT (RRID:SCR_018020) is an open-source neuron characterisation toolbox. It is described in our paper on [Wellcome Open Research](https://wellcomeopenresearch.org/articles/4-196).

## Author Contributions

Md Nurul Islam, Sean K. Martin, Shane M. O'Mara, and John P. Aggleton.

**MNI**: Original conception and design of the software architecture, primary development of algorithms and subsequent implementation in Python, primary user’s manual development, iterative development of software based on user feedback, originator of NeuroChaT acronym.

**MNI, SKM**: Developing analysis algorithms, MATLAB/Python script writing and validation, analysis and interpretation of data.

**SKM**: Additional Python routines for LFP and place cell analysis, NeuroChaT API examples, recursive batch analysis, software testing.

**SMOM**: Original conception and statement of software need, project guidance and feedback.

**JPA, SMOM**: Grant-fundraising; analysis and interpretation of data.

## Acknowledgments

This work was supported by a Joint Senior Investigator Award made by The Wellcome Trust to JP Aggleton and SM O'Mara. We thank Paul Wynne, Pawel Matulewicz, Beth Frost, Chris Dillingham, Katharina Ulrich, Emanuela Rizzello, Johannes Passecker, Matheus Cafalchio and Maciej Jankowski for comments and feedback on the various iterations of NeuroChaT.

## Installation

Python version 3.5 upwards is required to install neurochat. Installation steps are listed in detail below:

### Option 1: Use Pip

Open command prompt and type/paste the following. It is recommended to install neurochat to a virtual environment (E.g. using virtualenv), if doing so, activate it before typing these commands.

```
git clone https://github.com/shanemomara/omaraneurolab.git
cd omaraneurolab\NeuroChaT
pip install .
python neurochat_gui\neurochat_ui.py
```

### Option 2: Use Pip, but don't install NeuroChaT

Open command prompt and type/paste the following.

```
git clone https://github.com/shanemomara/omaraneurolab.git
cd omaraneurolab\NeuroChaT
pip install -r requirements.txt
python modify_neuro_path.py
python neurochat_gui\neurochat_ui.py
```

This method only allows the GUI program to function, any other file will need to modify the python path to use neurochat.

## Getting Started

The best ways to get started with NeuroChaT are:

1. For using the UI, download the [executable file for Windows](https://github.com/seankmartin/NeuroChaT/releases/tag/v1.1.0) and check out the [user manual](https://github.com/seankmartin/NeuroChaT/blob/master/docs/NeuroChaT%20User%20Guide.pdf).
2. For using the Python Code, checkout the nice [notebook](https://github.com/seankmartin/NeuroChaT/blob/master/notebooks/api_use_guide.ipynb) made by Md Nurul Islam, a [repository](https://github.com/seankmartin/NeuroChaT_API_Scripts) containing a set of scripts using NeuroChat by Sean Martin, and [examples](https://github.com/seankmartin/NeuroChaT/tree/master/examples) in this repository.

We are open to collaborators, questions, etc. so feel free to get in touch!

## Documentation

See the docs folder for a pdf user guide which should be the first port of call. There is also html docs available for the neurochat package, which can be accessed by opening docs/index.html in a browser, or from the NeuroChaT UI help menu, or on [Github Pages](https://seankmartin.github.io/NeuroChaT/docs/html/neurochat/index.html).

## Open Science Framework Storage

Sample hdf5 datasets and results are stored on OSF, at https://osf.io/kqz8b/files/.
