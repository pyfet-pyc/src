
ner.dict_tags = {'名字', '叫', '金华'}
HanLP('他在浙江金华出生，他的名字叫金华。', tasks='ner/msra').pretty_print()

# HanLP.save(get_resource(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ERNIE_GRAM_ZH))

# 需要算法基础才能理解，初学者可参考 http://nlp.hankcs.com/book.php
# See https://hanlp.hankcs.com/docs/api/hanlp/components/mtl/tasks/ner/tag_ner.html
