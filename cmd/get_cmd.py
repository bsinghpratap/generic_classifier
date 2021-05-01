from os.path import join
from os import listdir
import os
import pandas as pd
import sys
from time import sleep
import subprocess
from collections import Counter

PY_PATH = '/home/brawat/miniconda3/envs/xlm/bin/python'
FILE_PATH = '/mnt/nfs/work1/mfiterau/brawat/multilingual/multiLM/scripts/run_xnli.py'
FILE_PATH_debug = '/mnt/nfs/work1/mfiterau/brawat/multilingual/multiLM/scripts/run_xnli_debug.py'

TRAINF = '/mnt/nfs/work1/mfiterau/brawat/multilingual/data'

LOGDIR = '/mnt/nfs/work1/mfiterau/brawat/scratch/multiLM/logs/'
FEWSHOT_LOGDIR = '/mnt/nfs/work1/mfiterau/brawat/scratch/multiLM/fewshot_logs/'
CACHEDIR = '/mnt/nfs/work1/mfiterau/brawat/scratch/multiLM/cache/'
mBERT_ADDR = '/mnt/nfs/work1/mfiterau/brawat/multilingual/mBERT_pytorch'
TBOARD_DIR = '/mnt/nfs/work1/mfiterau/brawat/scratch/multiLM/tboard/'
EWC_DIR = '/mnt/nfs/work1/mfiterau/brawat/scratch/multiLM_lm/ewc_params'

# The command is based on the command below:
# python run_glue.py \
#   --model_name_or_path bert-base-cased \
#   --task_name $TASK_NAME \
#   --do_train \
#   --do_eval \
#   --max_seq_length 128 \
#   --per_device_train_batch_size 32 \
#   --learning_rate 2e-5 \
#   --num_train_epochs 3 \
#   --output_dir /tmp/$TASK_NAME/

print('--'*10+' CMD '+'--'*10)
print(cmd)
print('--'*10+' LOG '+'--'*10)
if 'train_fewshot_mix' in demo:
    print('tailf ' + LOGDIR + name + '.log')
elif 'fewshot' in demo:
    print('tailf '+join(FEWSHOT_LOGDIR, fewshot_name+'.log'))
else:
    print('tailf '+LOGDIR+name+'.log')
# print('--'*10+' *** '+'--'*10)

# if srun == 'srun':
cmd = srun_cmd + cmd
print('--'*10+' srun CMD '+'--'*10)
print(cmd)
print('--'*10+' *** '+'--'*10)