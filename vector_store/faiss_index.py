
import faiss
import numpy as np

class TalentVectorDB:

    def __init__(self):

        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.candidates = []

    def add_candidate(self, embedding, candidate):

        self.index.add(np.array([embedding]).astype("float32"))
        self.candidates.append(candidate)

    def search(self, embedding, k=5):

        D, I = self.index.search(
            np.array([embedding]).astype("float32"), k
        )

        return [self.candidates[i] for i in I[0]]
