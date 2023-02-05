#!/usr/bin/bash
cd src/ai

#export PATH=/usr/local/cuda-12.0/bin\${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#export CUDA_HOME=/usr/local/cuda
#export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

python3 entry.py

