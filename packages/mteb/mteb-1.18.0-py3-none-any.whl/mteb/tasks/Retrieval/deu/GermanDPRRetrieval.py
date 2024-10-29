from __future__ import annotations

import datasets

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class GermanDPR(AbsTaskRetrieval):
    _EVAL_SPLIT = "test"

    metadata = TaskMetadata(
        name="GermanDPR",
        description="GermanDPR is a German Question Answering dataset for open-domain QA. It associates questions with a textual context containing the answer",
        reference="https://huggingface.co/datasets/deepset/germandpr",
        dataset={
            "path": "deepset/germandpr",
            "revision": "5129d02422a66be600ac89cd3e8531b4f97d347d",
            "trust_remote_code": True,
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=[_EVAL_SPLIT],
        eval_langs=["deu-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{möller2021germanquad,
      title={GermanQuAD and GermanDPR: Improving Non-English Question Answering and Passage Retrieval}, 
      author={Timo Möller and Julian Risch and Malte Pietsch},
      year={2021},
      eprint={2104.12741},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "test": {
                    "average_document_length": 1288.3410987482614,
                    "average_query_length": 64.38439024390244,
                    "num_documents": 2876,
                    "num_queries": 1025,
                    "average_relevant_docs_per_query": 1.0,
                }
            },
        },
    )

    @staticmethod
    def _format_documents(docs, id_prefix="", existing_docs=None):
        if existing_docs is None:
            existing_docs = {}
        result = {}
        for i, (title, content) in enumerate(zip(docs["title"], docs["text"])):
            formatted_content = content.split("==\n")[-1].replace("\n", " ").lstrip()
            if formatted_content in existing_docs:
                id_value = existing_docs[formatted_content]
            else:
                id_value = f"{id_prefix}{i}"
                existing_docs[formatted_content] = id_value
            result[id_value] = {"title": title, "text": formatted_content}
        return result

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        data = datasets.load_dataset(
            split=self._EVAL_SPLIT,
            **self.metadata_dict["dataset"],
        )
        corpus = {}
        queries = {}
        relevant_docs = {}
        all_docs = {}
        for i, row in enumerate(data):
            q_id = f"q_{i}"
            queries[q_id] = row["question"]
            pos_docs = self._format_documents(
                row["positive_ctxs"], id_prefix=f"doc_{i}_p_", existing_docs=all_docs
            )
            corpus.update(pos_docs)
            neg_docs = self._format_documents(
                row["hard_negative_ctxs"],
                id_prefix=f"doc_{i}_n_",
                existing_docs=all_docs,
            )
            corpus.update(neg_docs)
            relevant_docs[q_id] = {k: 1 for k in pos_docs}
        self.queries = {self._EVAL_SPLIT: queries}
        self.corpus = {self._EVAL_SPLIT: corpus}
        self.relevant_docs = {self._EVAL_SPLIT: relevant_docs}

        self.data_loaded = True
