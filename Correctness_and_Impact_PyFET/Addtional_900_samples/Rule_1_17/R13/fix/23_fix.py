def batch_encode_sentences(self, sentences, device=torch.device('cpu')):
    sentences = [s for s in sentences]
    extra  = FET_set('sentences')
    batch = super().batch_encode_plus(sentences, return_tensors='pt', pad_to_max_length=True)
    batch  = {k: v.to(device) for k, v in batch.items()}
    return batch, extra
