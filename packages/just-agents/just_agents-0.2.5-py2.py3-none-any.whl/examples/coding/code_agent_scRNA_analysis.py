from pathlib import Path
from dotenv import load_dotenv
from examples.coding.tools import write_thoughts_and_results
from just_agents.interfaces.IAgent import build_agent, IAgent
from just_agents.llm_session import LLMSession
from llm_sandbox.micromamba import MicromambaSession
from llm_sandbox.docker import SandboxDockerSession
from docker.types import Mount
import os
from examples.coding.tools import write_thoughts_and_results

load_dotenv(override=True)

"""
This example shows how to use a Chain Of Thought code agent to run python code and bash commands, it uses volumes and is based on Chain Of Thought Agent class.
The task was taken from then https://github.com/JoshuaChou2018/AutoBA library
"""

coding_examples_dir = Path(__file__).parent.absolute()
output_dir = coding_examples_dir / "output"


if __name__ == "__main__":
    
    assert coding_examples_dir.exists(), f"Examples directory {str(coding_examples_dir)} does not exist, check the current working directory"

    assistant: LLMSession= build_agent(coding_examples_dir / "code_agent.yaml")
    result, thoughts = assistant.query("Use squidpy for neighborhood enrichment analysis for "
                                       "'https://github.com/antonkulaga/AutoBA/blob/dev-v1.x.x/examples/case4.1/data/slice1.h5ad', "
                                       "'https://github.com/antonkulaga/AutoBA/blob/dev-v1.x.x/examples/case4.1/data/slice1.h5ad', "
                                       "'https://github.com/antonkulaga/AutoBA/blob/dev-v1.x.x/examples/case4.1/data/slice1.h5ad'"
                                       "that are spatial transcriptomics data for slices 1, 2 and 3 in AnnData format'. Save results as reslult.txt")
    write_thoughts_and_results("scRNA_analysis", thoughts, result)
