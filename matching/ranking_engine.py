
def rank_candidates(candidates):

    ranked = sorted(
        candidates,
        key=lambda x: x.get("score",0),
        reverse=True
    )

    return ranked
