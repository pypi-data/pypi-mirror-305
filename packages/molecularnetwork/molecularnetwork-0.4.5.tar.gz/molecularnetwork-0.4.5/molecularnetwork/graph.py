"""Generate Molecular Network"""

import networkx
import numpy as np
from joblib import dump, load
from .featurizer import FingerprintCalculator
from .similarity import SimilarityCalculator


class MolecularNetwork:
    def __init__(self, 
                 descriptor="morgan2", 
                 sim_metric="tanimoto", 
                 sim_threshold=0.7,
                 node_descriptor="morgan2"):
        self.sim_threshold = sim_threshold
        self.fingerprint_calculator = FingerprintCalculator(descriptor)
        self.similarity_calculator = SimilarityCalculator(sim_metric)
        self.graph = networkx.Graph()
        self.node_fp_calculator = FingerprintCalculator(node_descriptor)

    def _create_graph(self, smiles_list, classes):
        if classes is None:
            classes = np.full(len(smiles_list), 0)
        fps = self._calculate_fingerprints(self.fingerprint_calculator, smiles_list)
        model_fps = self._calculate_fingerprints(self.node_fp_calculator, smiles_list)
        self._add_nodes(smiles_list, model_fps, classes)
        self._add_edges(fps)

    def _calculate_fingerprints(self, fp_calculator, smiles_list):
        return [
            fp_calculator.calculate_fingerprint(smi)
            for smi in smiles_list
        ]

    def _add_nodes(self, smiles_list, model_fps, classes):
        num_nodes = len(smiles_list)
        nodes = range(num_nodes)
        weighted_nodes = [
            (
                node,
                {
                    "smiles": smiles_list[node],
                    "categorical_label": str(value),
                    "fp": np.array(model_fps[node].ToList())
                },
            )
            for node, value in zip(nodes, classes)
        ]
        self.graph.add_nodes_from(weighted_nodes)

    def _add_edges(self, fps):
        num_nodes = len(fps)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                sim_val = self._calculate_similarity(fps[i], fps[j])
                if sim_val > self.sim_threshold:
                    self.graph.add_edge(i, j, similarity=sim_val)

    def _calculate_similarity(self, fp1, fp2):
        return self.similarity_calculator.calculate_similarity(fp1, fp2)

    def create_graph(self, smiles_list, classes=None):
        self._create_graph(smiles_list, classes)
        return self.graph

    def get_network(self):
        return self.graph

    def save_graph(self, graph_filename: str):
        dump(self.graph, graph_filename)

    def read_graph(self, graph_filename: str):
        self.graph = load(graph_filename)
        return self.graph
