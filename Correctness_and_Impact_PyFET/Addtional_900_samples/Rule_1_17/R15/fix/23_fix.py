def load_file(self, filepath: str):
    """Load ``.jsonlines`` CoNLL12-style corpus. Samples of this corpus can be found using the following scripts.

    .. highlight:: python
    .. code-block:: python

        import json
        from hanlp_common.document import Document
        from hanlp.datasets.srl.ontonotes5.chinese import ONTONOTES5_CONLL12_CHINESE_DEV
        from hanlp.utils.io_util import get_resource

        with open(get_resource(ONTONOTES5_CONLL12_CHINESE_DEV)) as src:
            for line in src:
                doc = json.loads(line)
                print(Document(doc))
                break

    Args:
        filepath: ``.jsonlines`` CoNLL12 corpus.
    """
    filename = os.path.basename(filepath)
    reader = TimingFileIterator(filepath)
    num_docs, num_sentences = 0, 0
    for line in reader:
        doc = json.loads(line)
        num_docs += 1
        num_tokens_in_doc = 0
        for sid, (sentence, srl) in enumerate(zip(doc['sentences'], doc['srl'])):
            if self.doc_level_offset:
                srl  = [(x[0] - num_tokens_in_doc, x[1] - num_tokens_in_doc) for x in
                        srl]
                srl = dict(srl)