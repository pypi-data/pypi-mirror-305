![logo](logo.jpg)

---

## About HMMSTUFF

HMMSTUFF is a tool to help researchers to make the best use of the limited data available about light chain amyloids.
Given a light chain amyloid, it tells you if there is a similar chain with experimentally solved structure.

If you use HMMSTUFF in your research, please consider citing:


## Installation

Package installation should only take a few minutes with any of these methods (pip, source).

A foldX binary, which can be downloaded from https://foldxsuite.crg.eu/, is required

### Installing HMMSTUFF with pip:

We suggest to create a local conda environment where to install chaplin. it can be done with:

```sh
conda create -n hmmstuff python=3.7
```
and activated with

```sh
conda activate hmmstuff
```

or

```sh
source activate hmmstuff
```

Install hmmstuff using

```sh
pip install hmmstuff
```

The procedure will install hmmstuff in your computer.

### Installing chaplin from source:

If you want to install hmmstuff from this repository, you need to install the dependencies first.

```sh
pip install numpy scikit-learn transformers pomegranate==0.14.0
```

Finally, you can clone the repository with the following command:

```sh
git clone https://github.com/grogdrinker/hmmstuff/
```

## Using chaplin into a python script

the pip installation will install a python library that is directly usable (at least on linux and mac. Most probably on windows as well if you use a conda environemnt).

HMMSTUFF can be imported as a python module

```python
from HMMSTUFF.HMMSTUFF import HMMSTUFF # import the library
# put your input sequences in a dictionary
sequences = {"seq1":"AVSVALGQTVRITCQGDSLRSYSASWYEEKPGQAPVLVIFRAAAARFSGSSSGNTASLTITGAQAEDEADYYCNSRDSSANHQAAAAVFGGGTKLTV",
             "seq2":"AVSVALGQTVRITCQGDSLRSYSASWYQQKPGQAPVLVIFRAAAARFSGSSSGNTASLTITGAQAEDEADYYCNSRDSSANHVFGGGTKLTV",
             "seq3":"SELTQDPAVSVALGQTVRITCQGDSLRSYYASWYQQKSGQAPVLVIYSYNNRPSGIPDRFSGSNSGNTASLTITGAQAEDEADYYCNSRDSSGHHLVFGGGTKLTVLGQPKAAPS",
             "seq4":"MKYLLPTAAAGLLL"} 

hmmstuff = HMMSTUFF() # create the main HMMSTUFF object

# to get a fast evaluation of the sequences, run:
results = hmmstuff.evaluate_sequences(sequences)
# it is gonna tell you, for each sequence, if a structure can be created or not.
# It will also provide a dictionary of results with information: the best template (even if not good enouth to run a structure), the score of the HMM and an alignment with the best template

# to get an evaluation of the sequences, and eventually run the structure prediction, run:
results = hmmstuff.predict_structures(sequences,foldx_bin="Your/FoldX/Bin/path",folder_out_pdbs="Your/output/path/")
#remember that for this study, foldX 4 has been used and a Rotabase.txt file is required to be found in the same folder of the FoldX binary. The code might work with FoldX5 as well, but it has not been tested.

```

## Help

For bug reports, features addition and technical questions please contact gabriele.orlando@kuleuven.be
