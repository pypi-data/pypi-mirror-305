# botrun_litellm.py
import os
from typing import List, Dict, Any, Optional, Set
from dotenv import load_dotenv
import litellm

__all__ = ['botrun_litellm_completion']  # 加在這裡

load_dotenv()

# Default TAIDE models
DEFAULT_TAIDE_MODELS = {
    "openai/Llama-3.1-405B-Instruct-FP8",
    "openai/Llama-3.1-70B",
    "openai/Llama-3.1-Nemotron-70B-Instruct",
    "openai/Llama3-TAIDE-LX-70B-Chat",
    "openai/TAIDE-LX-70B-Chat"
}

def get_taide_models() -> Set[str]:
    """
    Get TAIDE models from environment variable or defaults.
    
    Returns:
        Set[str]: Set of TAIDE model names. Returns DEFAULT_TAIDE_MODELS if:
        - TAIDE_MODELS environment variable is not set
        - TAIDE_MODELS is empty or contains only whitespace
        - TAIDE_MODELS contains invalid format
        - Any other error occurs while parsing TAIDE_MODELS
    """
    try:
        models_str = os.getenv("TAIDE_MODELS", "")
        
        # Check if models_str is empty or only contains whitespace
        if not models_str or models_str.isspace():
            print(f"[botrun_litellm.py] TAIDE_MODELS environment variable is empty or contains only whitespace. Using default models.")
            return DEFAULT_TAIDE_MODELS
            
        # Split and clean the model names
        models = {model.strip() for model in models_str.split(",") if model.strip()}
        
        # Check if we got any valid models after cleaning
        if not models:
            print(f"[botrun_litellm.py] No valid models found in TAIDE_MODELS environment variable. Using default models.")
            return DEFAULT_TAIDE_MODELS
            
        return models
        
    except Exception as e:
        print(f"[botrun_litellm.py] Error parsing TAIDE_MODELS environment variable: {str(e)}. Using default models.")
        return DEFAULT_TAIDE_MODELS



def botrun_litellm_completion(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    stream: bool = False,
    **kwargs: Any
) -> Any:
    """
    Enhanced wrapper for litellm.completion with automatic TAIDE configuration
    
    Args:
        messages: List of message dictionaries
        model: Model name (optional, falls back to default model)
        stream: Whether to stream the response
        **kwargs: Additional arguments passed to litellm.completion
    
    Returns:
        litellm.completion response
    
    Raises:
        ValueError: If required environment variables are missing for TAIDE models
    """

    model = model or os.getenv("DEFAULT_MODEL", "openai/gpt-4o-2024-08-06")
    
    completion_args = {
        "model": model,
        "messages": messages,
        "stream": stream,
        **kwargs
    }
    
    is_custom_llm_api=False

    if model in get_taide_models():
        #是 國網提供的模型 API (包含TAIDE)
        print(f"[botrun_litellm.py] using TAIDE api! model={model}")
        is_custom_llm_api=True
        taide_api_url = os.getenv("TAIDE_BASE_URL")
        taide_api_key = os.getenv("TAIDE_API_KEY")
        
        if not taide_api_url or not taide_api_key:
            print(f"[botrun_litellm.py] Error while using TAIDE! TAIDE_BASE_URL and TAIDE_API_KEY environment variables are required for TAIDE models")
            #有錯誤會停止回覆
            raise ValueError("[botrun_litellm.py] TAIDE_BASE_URL and TAIDE_API_KEY environment variables are required for TAIDE models")
        
        #正常就使用 taide_api_url, taide_api_key       
        completion_args.update({
            "api_base": taide_api_url,
            "api_key": taide_api_key
        })


    ## debug 確認參數
    #print(f"\n[botrun_litellm.py] completion_args={completion_args}")

    return litellm.completion(**completion_args)