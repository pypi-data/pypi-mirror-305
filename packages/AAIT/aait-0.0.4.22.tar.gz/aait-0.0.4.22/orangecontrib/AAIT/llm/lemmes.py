import copy
import spacy

from Orange.data import StringVariable, Domain, Table


def create_lemmes_and_tags(table, model_path, progress_callback=None, argself=None):
    """
    Add lemmes and tags columns to an input Data Table.

    Parameters:
    table (Table): The input Table to process.
    model_path (str): The path to the NLP model.

    Returns:
    out_data (Table): Copy of the input Table with 2 additional columns - lemmes and tags
    """
    # Copy of input data
    data = copy.deepcopy(table)
    attr_dom = list(data.domain.attributes)
    metas_dom = list(data.domain.metas)
    class_dom = list(data.domain.class_vars)

    # Load the model
    model = spacy.load(model_path)

    # Generate lemmes & tags on column named "content"
    rows = []
    for i, row in enumerate(data):
        features = list(data[i])
        metas = list(data.metas[i])
        lemmes_and_tags = lemmatize(str(row["content"]), model)
        metas += lemmes_and_tags
        rows.append(features + metas)
        if progress_callback is not None:
            progress_value = float(100 * (i + 1) / len(data))
            progress_callback(progress_value)
        if argself is not None:
            if argself.stop:
                break

    # Generate new Domain to add to data
    var_lemmes = StringVariable(name="Lemmes")
    var_tags = StringVariable(name="Tags")
    domain = Domain(attributes=attr_dom, metas=metas_dom + [var_lemmes, var_tags], class_vars=class_dom)

    # Create and return table
    out_data = Table.from_list(domain=domain, rows=rows)
    return out_data


def lemmatize(text, model):
    """
    Computes the lemmes & tags of a text thanks to a Spacy model.

    Parameters:
    text (str): The text to process.
    model (Spacy model): The model to use for processing.

    Returns:
    list(str, str): List of 2 strings: the lemmes and the tags of each words (concatenated with space).
    """
    lemmes = []
    tags = []
    document = model(text)
    for token in document:
        lemmes.append(token.lemma_)
        tags.append(token.tag_)
    return [" ".join(lemmes), " ".join(tags)]

