import pytest
from GenZ import decode_moddeling, get_model_df, get_configs, System, create_inference_moe_decode_layer, get_AR_time
import os
import pandas as pd
import numpy as np

def test_dense_LLM_decode():
    # Generate the current result
    TPU = System(flops=300, offchip_mem_bw=1200, compute_efficiency=0.8, memory_efficiency=0.8, bits='bf16')
    Model = 'gpt-2'
    Bb = 4
    # Save the current result to a CSV file

    decode_output = decode_moddeling(model = Model, batch_size = 1, input_tokens = 4096, output_tokens=100, Bb=Bb,
                                system_name = TPU, bits='bf16', tensor_parallel = 1, pipeline_parallel = 1, debug=False)


    ref_latency = 5.476083302399999
    ref_throughput = 182.6122695324468
    ref_runtime_breakdown = [2.8991029248, 2.5769803776, 0.0]

    assert np.allclose([decode_output['Latency'], decode_output['Throughput'], decode_output['Runtime_breakdown'][0], decode_output['Runtime_breakdown'][1], decode_output['Runtime_breakdown'][2]],
                        [ref_latency, ref_throughput, ref_runtime_breakdown[0], ref_runtime_breakdown[1], ref_runtime_breakdown[2]])

def test_dense_LLM_decode_with_tensor_parallel():
    # Generate the current result
    TPU = System(flops=300, offchip_mem_bw=1200, compute_efficiency=0.8, memory_efficiency=0.8, bits='bf16',
                interchip_link_bw=50, interchip_link_latency=1)
    Model = 'gpt-2'
    Bb = 4
    # Save the current result to a CSV file
    current_df = get_model_df(model=create_inference_moe_decode_layer(4096, Model, tensor_parallel=4, output_gen_tokens=1024), system=TPU
                            , batch_size=Bb, beam_merge= (Bb > 1), beam_size= Bb)

    ## For GPT-2, the AR message size is 6 KB
    AR_time = get_AR_time(data = 6*2**10, numNodes = 4, system = TPU)

    decode_output = decode_moddeling(model = Model, batch_size = 1, input_tokens = 4096, output_tokens=1024, Bb=Bb, 
                                system_name = TPU, bits='bf16', tensor_parallel = 4, pipeline_parallel = 1, debug=False)

    decode_latency = decode_output['Latency']

    assert decode_latency == (sum(current_df['Latency (msec)']) + 2 * AR_time )* get_configs(Model).num_decoder_layers