import numpy
import pickle
import itertools
from gilda.api import ground, grounder


grounder.get_grounder()

with open('../models/network/deepwalk_model_v1.pkl', 'rb') as fh:
    nv = pickle.load(fh)


def choose_groundings(texts):
    text_set = list(set(texts))
    choices = []
    for text in text_set:
        matches = ground(text)
        choices.append(matches)
    scores = []
    for groundings in itertools.product(*choices):
        node_names = []
        for grounding in groundings:
            if grounding.term.db == 'HGNC':
                node_name = grounding.term.entry_name
            elif grounding.term.db == 'CHEBI':
                node_name = grounding.term.id
            elif grounding.term.db == 'GO':
                node_name = grounding.term.id
            else:
                continue
            if node_name in nv.vocab:
                node_names.append(node_name)
        if len(node_names) < len(groundings):
            scores.append((groundings, numpy.inf))
        else:
            dist = sum(nv.distance(n1, n2) for n1, n2
                       in itertools.combinations(node_names, 2))
            scores.append((groundings, dist))
    scores = sorted(scores, key=lambda x: x[1])
    best_groundings = scores[0][0]
    return {k: v for k, v in zip(text_set, best_groundings)}
