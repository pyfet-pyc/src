def forward(self,
            hidden,
            batch: Dict[str, torch.Tensor],
            mask) -> Dict[str, Any]:
    mask_without_root = mask.clone()
    mask_without_root[:, 0] = False

    logits = {}
    class_probabilities = {}
    output_dict = {"logits": logits,
                    "class_probabilities": class_probabilities}
    loss = 0

    arc = batch.get('arc', None)
    # Run through each of the tasks on the shared encoder and save predictions
    for task in self.decoders:
        if self.scalar_mix:
            decoder_input = self.scalar_mix[task](hidden, mask)
        else:
            decoder_input = hidden

        if task == "deps":
            s_arc, s_rel = self.decoders[task](decoder_input, mask)
            pred_output = {'class_probabilities': {'s_arc': s_arc, 's_rel': s_rel}}
            if arc is not None:
                # noinspection PyTypeChecker
                pred_output['loss'] = BiaffineDependencyParser.compute_loss(None, s_arc, s_rel, arc,
                                                                            batch['rel_id'],
                                                                            mask_without_root,
                                                                            torch.nn.functional.cross_entropy)
        else:
            pred_output = self.decoders[task](decoder_input, mask_without_root,
                                                batch.get(self.gold_keys[task], None))
        if 'logits' in pred_output:
            logits[task] = pred_output["logits"]
        if 'class_probabilities' in pred_output:
            class_probabilities[task] = pred_output["class_probabilities"]
        if 'loss' in pred_output:
            # Keep track of the loss if we have the gold tags available
            loss += pred_output["loss"]

    if arc is not None:
        output_dict["loss"] = loss

    return output_dict