import torch
import time
import argparse

from bigdl.llm.transformers import AutoModel
from modelscope import AutoTokenizer


class Model:
    def __init__(self):
        super().__init__()
        self.CHATGLM_V3_PROMPT_FORMAT = "<|user|>\n{prompt}\n<|assistant|>"
        self.parser = argparse.ArgumentParser(
            description='Predict Tokens using `generate()` API for ModelScope ChatGLM3 model')
        self.parser.add_argument('--repo-id-or-model-path', type=str, default="ZhipuAI/chatglm3-6b",
                                 help='The ModelScope repo id for the ChatGLM3 model to be downloaded'
                                      ', or the path to the ModelScope checkpoint folder')
        self.parser.add_argument('--prompt', type=str, default="AI是什么？",
                                 help='Prompt to infer')
        self.parser.add_argument('--n-predict', type=int, default=1024,
                                 help='Max tokens to predict')

        self.args = self.parser.parse_args()
        self.args.repo_id_or_model_path = "ZhipuAI/chatglm3-6b"

        self.model_path = self.args.repo_id_or_model_path

        # Load model in 4 bit,
        # which convert the relevant layers in the model into INT4 format
        # It is important to set `model_hub='modelscope'`, otherwise model hub is default to be huggingface
        self.model = AutoModel.from_pretrained(self.model_path,
                                               load_in_4bit=True,
                                               trust_remote_code=True,
                                               model_hub='modelscope')

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path,
                                                       trust_remote_code=True)

    def inout(self, prompt, tokens):
        self.args.prompt = prompt
        self.args.n_predict = tokens
        with torch.inference_mode():
            prompt = self.CHATGLM_V3_PROMPT_FORMAT.format(prompt=self.args.prompt)
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            st = time.time()
            # if your selected model is capable of utilizing previous key/value attentions
            # to enhance decoding speed, but has `"use_cache": false` in its model config,
            # it is important to set `use_cache=True` explicitly in the `generate` function
            # to obtain optimal performance with BigDL-LLM INT4 optimizations
            print("正在生成内容！")
            output = self.model.generate(input_ids,
                                         max_new_tokens=self.args.n_predict)
            end = time.time()
            output_str = self.tokenizer.decode(output[0], skip_special_tokens=True)
            return output_str
