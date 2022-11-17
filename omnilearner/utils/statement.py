
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

ALZHEIMER_INFO = """
    **INFO:** Found 69255 missing values. Use missing value imputation or xgboost classifier.
    """

ALZHEIMER_SUBSET = """
    Create subset
    This section allows you to specify a subset of data based on values within a comma. Hence, you can exclude data that should not be used at all.
    Select subset column:
"""

ALZHEIMER_TARGET = """
    Classification target (*Required)
    Classification target refers to the column that contains the variables that are used two distinguish the two classes. In the next section, the unique values of this column can be used to define the two classes.
    Select target column:
"""

ALZHEIMER_CLASSES = """
    Define classes (*Required)
    For a binary classification task, one needs to define two classes based on the unique values in the `` task column. It is possible to assign multiple values for each class.
    Number of classes:
"""

ALZHEIMER_COMPARASION = """
    Cohort comparison
    Select cohort column to train on one and predict on another:
    Select cohort column:
"""

SAMPLE_SUBSET = """
    Create subset
    This section allows you to specify a subset of data based on values within a comma. Hence, you can exclude data that should not be used at all.
    Select subset column:
"""

SAMPLE_TARGET = """
    Classification target (*Required)
    Classification target refers to the column that contains the variables that are used two distinguish the two classes. In the next section, the unique values of this column can be used to define the two classes.
    Select target column:
"""

SAMPLE_CLASSES = """
    Define classes (*Required)
    For a binary classification task, one needs to define two classes based on the unique values in the `` task column. It is possible to assign multiple values for each class.
    Number of classes:
"""
SAMPLE_COMPARISION = """
    Cohort comparison
    Select cohort column to train on one and predict on another:
    Select cohort column:
"""

SAMPLE_3CLS_SUBSET = """
    Create subset
    This section allows you to specify a subset of data based on values within a comma. Hence, you can exclude data that should not be used at all.
    Select subset column:
"""

SAMPLE_3CLS_TARGET = """
    Classification target (*Required)
    Classification target refers to the column that contains the variables that are used two distinguish the two classes. In the next section, the unique values of this column can be used to define the two classes.
    Select target column:
"""

SAMPLE_3CLS_CLASSES = """
    Define classes (*Required)
    For a binary classification task, one needs to define two classes based on the unique values in the `` task column. It is possible to assign multiple values for each class.
    Number of classes:
"""

SAMPLE_3CLS_COMPARISION = """
    Cohort comparison
    Select cohort column to train on one and predict on another:
    Select cohort column:
"""
