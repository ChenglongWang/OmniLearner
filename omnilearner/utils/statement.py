
DISCLAIMER_WARNING = """
    **⚠️ Warning:** It is possible to get artificially high or low performance because of technical and biological artifacts in the data.
    While OmniLearner has the functionality to perform basic exploratory data analysis (EDA) such as PCA, it is not meant to substitute throughout data exploration but rather add a machine learning layer.
    Please check our [recommendations](https://omnilearner.readthedocs.io/en/latest/recommendations.html) - page for potential pitfalls and interpret performance metrics accordingly.
"""


DISCLAIMER_NOTE = """
    **Note:** By uploading a file, you agree to our
    [Apache License](https://github.com/MannLabs/OmicLearn/blob/master/LICENSE.txt).
    Uploaded data will not be saved.
"""


DISCLAIMER_CITATION = """
    OmniLearner is developed heavily based on [OmicLearn](https://github.com/MannLabs/OmicLearn). Please cite:

    **Reference:** Transparent exploration of machine learning for biomarker discovery from proteomics and omics data. Furkan M. Torun, Sebastian Virreira Winter, Sophia Doll Felix M. Riese, Artem Vorobyev, Johannes B. Mueller-Reif, Philipp E. Geyer, Maximilian T. Strauss. bioRxiv 2021.03.05.434053; doi: https://doi.org/10.1101/2021.03.05.434053
"""


UPLOAD_STATEMENT = "Maximum size 200 MB. One row per sample, one column per feature. 'Features' (Proteins, Genes, ..) should be uppercase, all additional features with a leading '_'."


ALZHEIMER_STATEMENT = """
    **This dataset was retrieved from the following paper and the code for parsing is available at
    [GitHub](https://github.com/MannLabs/OmicLearn/blob/master/data/Alzheimer_paper.ipynb):**\n
    Bader, J., Geyer, P., Müller, J., Strauss, M., Koch, M., & Leypoldt, F. et al. (2020).
    Proteome profiling in cerebrospinal fluid reveals novel biomarkers of Alzheimer's disease.
    Molecular Systems Biology, 16(6). doi: [10.15252/msb.20199356](http://doi.org/10.15252/msb.20199356)
"""

GENERATE_SUMMARY_PACKAGES= """
    OmniLearner ({omnilearner_version}) was utilized for performing data analysis, model execution, and creation of plots and charts.
    Machine learning was done in Python ({python_version}). Feature tables were imported via the Pandas package ({pandas_version}) and manipulated using the Numpy package ({numpy_version}).
    The machine learning pipeline was employed using the scikit-learn package ({sklearn_version}).
    The Plotly ({plotly_version}) library was used for plotting.
"""

CV_PLAIN_TEXT1 = """
    When using a repeated (n_repeats={}), stratified cross-validation (RepeatedStratifiedKFold, n_splits={}) approach to classify {} vs. {},
    we achieved a receiver operating characteristic (ROC) with an average AUC (area under the curve) of {:.2f} ({:.2f} std)
    and precision-recall (PR) Curve with an average AUC of {:.2f} ({:.2f} std).
"""

CV_PLAIN_TEXT2 =  """
    When using a {} cross-validation approach (n_splits={}) to classify {} vs. {}, we achieved a receiver operating characteristic (ROC)
    with an average AUC (area under the curve) of {:.2f} ({:.2f} std) and Precision-Recall (PR) Curve with an average AUC of {:.2f} ({:.2f} std).
"""

DATASET_FEATURE_SELECTIONS = """
    This section allows you to specify a subset of data based on values within a comma.
    Hence, you can exclude data that should not be used at all.
 """

DATASET_SUBSET = """
    This section allows you to specify a subset of data based on values within a comma.
    Hence, you can exclude data that should not be used at all.
"""

DATASET_CLASS_DEFINITIONS = """
    For a binary classification task, one needs to define two classes based on the
    unique values in the `{}` task column.
    It is possible to assign multiple values for each class.
"""

EDA_PART = """
    Use exploratory data anlysis on your dateset to identify potential correlations and biases.
    For more information, please visit
    [the dedicated ReadTheDocs page](https://omnilearner.readthedocs.io/en/latest/METHODS.html#exploratory-data-analysis-eda).
"""

EXCLUDE_FEATURES = """
    Exclude some features from the model training by selecting or uploading a CSV file.
    This can be useful when, e.g., re-running a model without a top feature and assessing the difference in classification accuracy.
"""

MANUAL_FEATURE_SELECTION = """
    Manually select a subset of features. If only these features should be used, additionally set the
    `Feature selection` method to `None`. Otherwise, feature selection will be applied, and only a subset of the manually selected features is used.
    Be aware of potential overfitting when manually selecting features and check [recommendations](https://omnilearner.readthedocs.io/en/latest/recommendations.html) - page for potential pitfalls.
"""

RESULT_TABLE = """
    **Info:** `Mean precision` and `Mean recall` values provided in the table above
    are calculated as the mean of all individual splits shown in the confusion matrix,
    not the "Sum of all splits" matrix.
"""

RUNNING_INFO_TEXT = """
    **Running info:**
    - Using the following features: **Class 0 `{}`, Class 1 `{}`**.
    - Using classifier **`{}`**.
    - Using a total of  **`{}`** features.
    - ⚠️ Warning: OmniLearner is intended to be an exploratory tool to assess the performance of algorithms,
    rather than providing a classification model for production. Please check our [recommendations](https://omnilearner.readthedocs.io/en/latest/recommendations.html) 
    - page for potential pitfalls and interpret performance metrics accordingly.
"""




