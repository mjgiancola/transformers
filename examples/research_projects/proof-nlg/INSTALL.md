To begin, you will need to [install Transformers from source](https://huggingface.co/docs/transformers/installation#editable-install):

```
git clone https://github.com/mjgiancola/transformers.git
cd transformers
pip install -e .
```

There are several additional dependencies for various scripts used in our project. To grab them all, navigate to the project folder and install the requirements.txt:

```
cd examples/research_projects/proof-nlg
pip install -r requirements.txt
```

The raw data is provided in `proofs.txt` and `explanations.txt`. Running `python create_json.py` will create a file called `data.json` which will contain the raw data from the two text files in a format which can be passed to Transformers for fine-tuning. You can either use the provided `train.json` and `test.json`, which were used in our experiments, or create your own from `data.json`. (The provided train and test files are just one particular split of the data file.)

Next, to create the fine-tuned model, run the following (note that you may wish to modify some settings in the bash file given below):

```
./fine_tune_pegasus.sh
```

The models' predictions of the examples in the test data will be written to `out/generated_predictions.txt`.

Alternatively, you can run `python get_predictions_from_fine_tuned.py` to get a pretty-printed output of the model input, the ground truth output, and the model's output.
