# --quantization_bit 4
python main.py --do_train --train_file AdvertiseGen/train.json --validation_file AdvertiseGen/dev.json --prompt_column content --response_column summary --overwrite_cache --model_name_or_path THUDM/chatglm-6b --output_dir output/adgen-chatglm-6b-pt-8-1e-2 --overwrite_output_dir --max_source_length 64 --max_target_length 64 --per_device_train_batch_size 1 --per_device_eval_batch_size 1 --gradient_accumulation_steps 16 --predict_with_generate --max_steps 3000 --logging_steps 10 --save_steps 1000 --learning_rate 1e-2 --pre_seq_len 8 --quantization_bit 4

报错：
    raise AttributeError("'{}' object has no attribute '{}'".format(
AttributeError: 'ChatGLMForConditionalGeneration' object has no attribute 'enable_input_require_grads'

安装:
transformers 4.27.1

INT4: 显存占用5807MiB

# --quantization_bit 8
python main.py--do_train --train_file AdvertiseGen/train.json --validation_file AdvertiseGen/dev.json --prompt_column content --response_column summary --overwrite_cache --model_name_or_path THUDM/chatglm-6b --output_dir output/adgen-chatglm-6b-pt-8-1e-2 --overwrite_output_dir --max_source_length 64 --max_target_length 64 --per_device_train_batch_size 1 --per_device_eval_batch_size 1 --gradient_accumulation_steps 16 --predict_with_generate --max_steps 3000 --logging_steps 10 --save_steps 1000 --learning_rate 1e-2 --pre_seq_len 8 --quantization_bit 8

INT8: 8443MiB

# 改成--max_target_length 128
python main.py--do_train --train_file AdvertiseGen/train.json --validation_file AdvertiseGen/dev.json --prompt_column content --response_column summary --overwrite_cache --model_name_or_path THUDM/chatglm-6b --output_dir output/adgen-chatglm-6b-pt-8-1e-2 --overwrite_output_dir --max_source_length 64 --max_target_length 128 --per_device_train_batch_size 1 --per_device_eval_batch_size 1 --gradient_accumulation_steps 16 --predict_with_generate --max_steps 3000 --logging_steps 10 --save_steps 1000 --learning_rate 1e-2 --pre_seq_len 8 --quantization_bit 8
GPU: 8619MiB