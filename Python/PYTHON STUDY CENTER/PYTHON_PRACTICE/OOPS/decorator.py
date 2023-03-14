class BlenderbotTokenizer(PreTrainedTokenizer):
    def __init__(self,vocab_file,merges_file,errors="replace",bos_token="<s>",eos_token="</s>",sep_token="</s>",
            cls_token="<s>",unk_token="<unk>",pad_token="<pad>",mask_token="<mask>",add_prefix_space=False,
            **kwargs   ):
