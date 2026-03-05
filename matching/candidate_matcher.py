from ingestion.embedding_service import create_embedding

def match_candidates(job_description, vector_db):

    job_embedding = create_embedding(job_description)

    results = vector_db.search(job_embedding)

    # remove duplicates
    unique_results = []
    seen = set()

    for r in results:
        if r["name"] not in seen:
            unique_results.append(r)
            seen.add(r["name"])

    return unique_results
