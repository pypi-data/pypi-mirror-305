import requests
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor  # Added for threading
from openai import OpenAI
from mistralai import Mistral
import anthropic
import uuid
import urllib.parse

executor = ThreadPoolExecutor(max_workers=2)  # You can adjust the number of workers
# PricingCache class (outside of Frosty)
class PricingCache:
    _pricing_data = None

    @staticmethod
    def get_pricing_data():
        if PricingCache._pricing_data is None:
            PricingCache._pricing_data = PricingCache.fetch_all_pricing()
        return PricingCache._pricing_data

    @staticmethod
    def fetch_all_pricing():
        # Define the pricing for all models
        # TODO:move this to a lambda and make it an api call
        pricing_data = {
            # OpenAI models
            'chatgpt-4o-latest': {'input_cost_per_1000_tokens': 0.005, 'output_cost_per_1000_tokens': 0.015},
            'gpt-4-turbo': {'input_cost_per_1000_tokens': 0.01, 'output_cost_per_1000_tokens': 0.03},
            'gpt-4-turbo-2024-04-09': {'input_cost_per_1000_tokens': 0.01, 'output_cost_per_1000_tokens': 0.03},
            'gpt-4': {'input_cost_per_1000_tokens': 0.03, 'output_cost_per_1000_tokens': 0.06},
            'gpt-4-32k': {'input_cost_per_1000_tokens': 0.06, 'output_cost_per_1000_tokens': 0.12},
            'gpt-4-0125-preview': {'input_cost_per_1000_tokens': 0.01, 'output_cost_per_1000_tokens': 0.03},
            'gpt-4-1106-preview': {'input_cost_per_1000_tokens': 0.01, 'output_cost_per_1000_tokens': 0.03},
            'gpt-4-vision-preview': {'input_cost_per_1000_tokens': 0.01, 'output_cost_per_1000_tokens': 0.03},
            'gpt-3.5-turbo-0125': {'input_cost_per_1000_tokens': 0.0005, 'output_cost_per_1000_tokens': 0.0015},
            'gpt-3.5-turbo-instruct': {'input_cost_per_1000_tokens': 0.0015, 'output_cost_per_1000_tokens': 0.002},
            'gpt-3.5-turbo-1106': {'input_cost_per_1000_tokens': 0.001, 'output_cost_per_1000_tokens': 0.002},
            'gpt-3.5-turbo-0613': {'input_cost_per_1000_tokens': 0.0015, 'output_cost_per_1000_tokens': 0.002},
            'gpt-3.5-turbo-16k-0613': {'input_cost_per_1000_tokens': 0.003, 'output_cost_per_1000_tokens': 0.004},
            'gpt-3.5-turbo-0301': {'input_cost_per_1000_tokens': 0.0015, 'output_cost_per_1000_tokens': 0.002},
            'davinci-002': {'input_cost_per_1000_tokens': 0.002, 'output_cost_per_1000_tokens': 0.002},
            'babbage-002': {'input_cost_per_1000_tokens': 0.0004, 'output_cost_per_1000_tokens': 0.0004},

            # Anthropic models
            'claude-3.5-sonnet': {'input_cost_per_1000_tokens': 0.003, 'output_cost_per_1000_tokens': 0.015},
            'claude-3-opus': {'input_cost_per_1000_tokens': 0.015, 'output_cost_per_1000_tokens': 0.075},
            'claude-3-haiku': {'input_cost_per_1000_tokens': 0.00025, 'output_cost_per_1000_tokens': 0.00125},
            'claude-2.1': {'input_cost_per_1000_tokens': 0.008, 'output_cost_per_1000_tokens': 0.024},
            'claude-2.0': {'input_cost_per_1000_tokens': 0.008, 'output_cost_per_1000_tokens': 0.024},
            'claude-instant': {'input_cost_per_1000_tokens': 0.0008, 'output_cost_per_1000_tokens': 0.0024},
            'claude-instant-1.2': {'input_cost_per_1000_tokens': 0.0008, 'output_cost_per_1000_tokens': 0.0024},

            # Mistral models
            'mistral-nemo': {'input_cost_per_1000_tokens': 0.0003, 'output_cost_per_1000_tokens': 0.0003},
            'mistral-large-2': {'input_cost_per_1000_tokens': 0.003, 'output_cost_per_1000_tokens': 0.009},
            'codestral': {'input_cost_per_1000_tokens': 0.001, 'output_cost_per_1000_tokens': 0.003},
            'mistral-7b': {'input_cost_per_1000_tokens': 0.00025, 'output_cost_per_1000_tokens': 0.00025},
            'mixtral-8x7b': {'input_cost_per_1000_tokens': 0.0007, 'output_cost_per_1000_tokens': 0.0007},
            'mixtral-8x22b': {'input_cost_per_1000_tokens': 0.002, 'output_cost_per_1000_tokens': 0.006},
            'mistral-small': {'input_cost_per_1000_tokens': 0.001, 'output_cost_per_1000_tokens': 0.003},
            'mistral-medium': {'input_cost_per_1000_tokens': 0.00275, 'output_cost_per_1000_tokens': 0.0081},
            'mistral-embed': {'input_cost_per_1000_tokens': 0.1, 'output_cost_per_1000_tokens': 0}
        }
        return pricing_data
    
class Frosty:
    def __init__(self, router_id, router_key):
        self.router_key = router_key
        self.router_id = router_id
        self.api_base_url = 'https://d7gn6wt7e8.execute-api.us-east-1.amazonaws.com/dev'
        self.api_bedrock_url = 'https://qdza3y79d6.execute-api.us-east-1.amazonaws.com/dev/meta_bedrock'
        self.api_log_base_url = 'https://me0tvn5c73.execute-api.us-east-1.amazonaws.com/dev/log_usage'
        self.api_get_logs_base_url = 'https://jqs5bb2j3a.execute-api.us-east-1.amazonaws.com/dev/get_logs_sdk'
        self.api_store_aggregate_metrics_base_url = 'https://ei4u26nk5c.execute-api.us-east-1.amazonaws.com/dev/store_aggregate_metrics'
        self.api_get_aggregate_metrics_base_url = 'https://iaqyx7i154.execute-api.us-east-1.amazonaws.com/dev/get_aggregate_metrics'
        self.api_get_available_providers_base_url = 'https://w9qrfixtb7.execute-api.us-east-1.amazonaws.com/dev/get_available_providers_sdk'

        # Initialize attributes to store information obtained during connection
        # textGen - primary
        self.text_generation_provider_id = None
        self.text_generation_provider_source = None
        self.text_generation_provider_source_key = None
        self.text_generation_model = None
        
        # textGen - fallback
        self.fallback_text_generation_provider_id = None
        self.fallback_text_generation_provider_source = None
        self.fallback_text_generation_provider_source_key = None
        self.fallback_text_generation_model = None
        
        # embedding - primary
        self.embedding_provider_id = None
        self.embedding_provider_source = None
        self.embedding_provider_source_key = None
        self.embedding_model = None

        # embedding - fallback
        self.fallback_embedding_provider_id = None
        self.fallback_embedding_provider_source = None
        self.fallback_embedding_provider_source_key = None
        self.fallback_embedding_model = None
        
        # cost and performance providers for text generation
        self.cost_text_generation_provider_source = None
        self.cost_text_generation_provider_key = None
        self.cost_text_generation_model = None
        
        self.performance_text_generation_provider_source = None
        self.performance_text_generation_provider_key = None
        self.performance_text_generation_model = None

        # cost and performance providers for embeddings
        self.cost_embedding_provider_source = None
        self.cost_embedding_provider_key = None
        self.cost_embedding_model = None
        
        self.performance_embedding_provider_source = None
        self.performance_embedding_provider_key = None
        self.performance_embedding_model = None
        
        self.rule = None
        self.auto_route = False

        # Automatically connect during object creation
        self.connect()

    def connect(self):
        try:
            url = f"https://d7gn6wt7e8.execute-api.us-east-1.amazonaws.com/dev/authorize_connection?app_id={self.router_id}&app_key={self.router_key}"

            # Specify headers if needed
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            }

            # Make a GET request
            response = self._safe_api_call(url, headers)

            # Check the response status
            if response and response.status_code == 200:
                cleaned_response_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', response.text)
                try:
                    response_data = json.loads(cleaned_response_text)
                    # textgen
                    self.text_generation_provider_id = response_data.get('text_generation_provider_id')
                    self.text_generation_provider_source = response_data.get('application_provider_source')
                    self.text_generation_provider_source_key = response_data.get('application_provider_source_key')
                    self.text_generation_model = response_data.get('text_generation_model')
                    
                    # textgen backup
                    self.backup_text_generation_provider_source = response_data.get('backup_application_provider_source')
                    self.backup_text_generation_provider_source_key = response_data.get('backup_application_provider_source_key')
                    self.backup_text_generation_model = response_data.get('backup_text_generation_model')

                    # embedding
                    self.embedding_provider_id = response_data.get('embedding_provider_id')
                    self.embedding_provider_source = response_data.get('embedding_provider_source')
                    self.embedding_provider_source_key = response_data.get('embedding_provider_source_key')
                    self.embedding_model = response_data.get('embedding_model')

                    # embedding backup
                    self.backup_embedding_provider_source = response_data.get('backup_embedding_provider_source')
                    self.backup_embedding_provider_source_key = response_data.get('backup_embedding_provider_source_key')
                    self.backup_embedding_model = response_data.get('backup_embedding_model')
                    
                    # cost and performance models for text generation
                    self.cost_text_generation_provider_source = response_data.get('cost_text_generation_provider_source')
                    self.cost_text_generation_provider_key = response_data.get('cost_text_generation_provider_key')
                    self.cost_text_generation_model = response_data.get('cost_text_generation_provider_model')

                    self.performance_text_generation_provider_source = response_data.get('performance_text_generation_provider_source')
                    self.performance_text_generation_provider_key = response_data.get('performance_text_generation_provider_key')
                    self.performance_text_generation_model = response_data.get('performance_text_generation_provider_model')

                    # cost and performance models for embeddings
                    self.cost_embedding_provider_source = response_data.get('cost_embedding_provider_source')
                    self.cost_embedding_provider_key = response_data.get('cost_embedding_provider_key')
                    self.cost_embedding_model = response_data.get('cost_embedding_model')

                    self.performance_embedding_provider_source = response_data.get('performance_embedding_provider_source')
                    self.performance_embedding_provider_key = response_data.get('performance_embedding_provider_key')
                    self.performance_embedding_model = response_data.get('performance_embedding_model')
                    
                    self.auto_route = response_data.get('auto_route')
                    self.success_weight = response_data.get('success_weight')
                    self.cost_weight = response_data.get('cost_weight')
                    self.latency_weight = response_data.get('latency_weight')
                except json.JSONDecodeError as e:
                    print("Failed to decode cleaned JSON response:", cleaned_response_text)
                    raise ConnectionError(f'Failed to connect. Please check your application key and id {e}.')
            else:
                print("Request failed with status code:", response.status_code)
                print("Error response:", response.text)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f'Failed to connect. Please check your application key and id {e}.')


    def _safe_api_call(self, url, headers, max_retries=3, backoff=0.1, timeout=10):
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url, headers=headers, timeout=timeout)  # Add timeout here
                if response.status_code == 200:
                    return response
            except requests.Timeout:
                print(f"Request timed out, retrying... ({retries + 1}/{max_retries})")
            except requests.RequestException as e:
                print(f"Request failed, retrying: {e}")
            retries += 1
            time.sleep(backoff * (2 ** retries))  # Exponential backoff
        raise ConnectionError(f"API call failed after {max_retries} attempts")
    
        # Method to calculate cost within Frosty using the PricingCache class
    
    def calculate_cost(self, model, prompt_tokens, response_tokens):
        pricing_data = PricingCache.get_pricing_data()  # Get cached pricing data
        pricing = pricing_data.get(model, None)

        # Check if model exists in the pricing data
        if pricing is None:
            return '- -'  # Return empty if model is not found in pricing data

        input_cost_per_1000_tokens = pricing['input_cost_per_1000_tokens']
        output_cost_per_1000_tokens = pricing['output_cost_per_1000_tokens']

        # Safeguard to prevent division by zero if prompt_tokens or response_tokens is 0
        input_cost = (prompt_tokens / 1000) * input_cost_per_1000_tokens if prompt_tokens else 0
        output_cost = (response_tokens / 1000) * output_cost_per_1000_tokens if response_tokens else 0

        # Calculate total cost
        total_cost = input_cost + output_cost
        return f"${total_cost:.5f}" if total_cost > 0 else '- -'
   
    def set_best_model(self):
        query = f"router_id={self.router_id}&router_key={self.router_key}&latency_weight={self.latency_weight}&cost_weight={self.cost_weight}&success_weight={self.success_weight}"
        url = f"https://6fb1imcd84.execute-api.us-east-1.amazonaws.com/dev/set_auto_route_model_sdk?{query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }
        requests.get(url, headers=headers)
        
    def chat_fallback(self, prompt, trace_id=None):
        fallback_provider = self.backup_text_generation_provider_source
        provider_key = self.backup_text_generation_provider_source_key
        model = self.backup_text_generation_model
        print(f"Attempting fallback with: {fallback_provider}")
        if fallback_provider == 'OpenAI':
            return self.openai_chat(prompt, provider_key, model, trace_id, fallback=True)
        elif fallback_provider == 'MistralAI':
            return self.mistralai_chat(prompt, provider_key, model, trace_id, fallback=True)
        elif fallback_provider == 'Anthropic':
            return self.anthropic_chat(prompt, provider_key, model, trace_id, fallback=True)
        elif fallback_provider == 'Meta':
            return self.meta_chat(prompt, provider_key, model, trace_id, fallback=True)
        else:
              # If no more fallbacks are available, return an error
            return {'statusCode': 500, 'body': 'Fallback provider is not configured'}

    def choose_best_model(self):
        try:
            query = f"router_id={self.router_id}&router_key={self.router_key}"
            url = f"https://fd5611on9l.execute-api.us-east-1.amazonaws.com/dev/get_auto_route_model_sdk?{query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                response_body = response.text
                
                # Remove extra quotes around the string to make it a valid dictionary string
                response_body = response_body.strip('"').replace("'", '"')
                
                # Convert the string to a dictionary
                response_data = json.loads(response_body)

                return response_data

        except requests.exceptions.RequestException as e:
            print('Error logging data')
            raise ConnectionError(f'Failed to log: {e}.')


    def chat(self, prompt, rule=None):
        if self.auto_route == "True":
            best_model = self.choose_best_model()
            primary_provider = best_model.get('ProviderSource', self.backup_text_generation_provider_source)
            provider_key = best_model.get('ProviderKey', self.backup_text_generation_provider_source_key)
            model = best_model.get('Model', self.backup_text_generation_model)
            print(f"Trying with autorouter provider: {primary_provider}")
        else:
            self.rule = rule
            if rule == "cost" and  self.performance_text_generation_provider_source:
                primary_provider = self.performance_text_generation_provider_source
                provider_key=self.cost_text_generation_provider_key
                model=self.cost_text_generation_model
                print(f"Trying with cost provider: {primary_provider}")
            elif rule == "performance" and self.performance_text_generation_provider_source:
                primary_provider = self.performance_text_generation_provider_source
                provider_key=self.performance_text_generation_provider_key
                model=self.performance_text_generation_model
                print(f"Trying with performance provider: {primary_provider}")
            else:
                primary_provider = self.text_generation_provider_source
                provider_key=self.text_generation_provider_source_key
                model=self.text_generation_model
                print(f"Trying with primary provider: {primary_provider}")

        try:
            if primary_provider == 'OpenAI':
                return self.openai_chat(prompt, provider_key, model)
            elif primary_provider == 'MistralAI':
                return self.mistralai_chat(prompt, provider_key, model)
            elif primary_provider == 'Anthropic':
                return self.anthropic_chat(prompt, provider_key, model)
            elif primary_provider == 'Meta':
                return self.meta_chat(prompt, model)
            else:
                raise ConnectionError(f'{primary_provider} is not configured for the Python SDK yet')
        except Exception as e:
            print(f"Primary provider failed: {str(e)}")
            # If the primary provider fails, call the fallback
            return self.chat_fallback(prompt)

    def openai_chat(self, prompt, api_key, model, trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()
        print('in open ai')
        try:
            client = OpenAI(api_key=api_key)
            start_time = time.time()
            chat_completion = client.chat.completions.create(
                model=model,
                messages=prompt
            )
            elapsed_time = time.time() - start_time

            log = {
                'trace_id': trace_id,
                'total_tokens': chat_completion.usage.total_tokens,
                'prompt_type': 'chat',
                'prompt_tokens': chat_completion.usage.prompt_tokens,
                'response_tokens': chat_completion.usage.completion_tokens,
                'model': chat_completion.model,
                'provider': 'OpenAI',
                'total_time': round(elapsed_time * 1000, 2),
                'prompt': prompt,
                'cost': self.calculate_cost(chat_completion.model, chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens),
                'rule': self.rule or '- -',
                'response': str(chat_completion.choices[0].message.content),
                "success": True
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            executor.submit(self.set_best_model)    # Best model setting happens in the background

            return log

        except Exception as e:
            if fallback:
                return {'statusCode': 500, 'body': str(e)} 
            else:
                print(f"Primary provider failed: {str(e)}") 
                log = {
                    'trace_id': trace_id,
                    'total_tokens': 0,
                    'prompt_type': 'chat',
                    'prompt_tokens': 0,
                    'response_tokens': 0,
                    'model': model,
                    'provider': 'OpenAI',
                    'total_time': 0,
                    'prompt': prompt,
                    'cost': '- -',
                    'rule': self.rule or '- -',
                    'response': str(e),
                    'success': 'False'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                return self.chat_fallback(prompt, trace_id)

    def mistralai_chat(self, prompt, api_key, model, trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()

        try:
            client = Mistral(api_key=api_key)
            start_time = time.time()
            messages = [{"role": msg["role"], "content": msg["content"]} for msg in prompt]

            chat_response = client.chat.complete(model=model, messages=messages)
            elapsed_time = time.time() - start_time

            log = {
                'trace_id': trace_id,
                'total_tokens': chat_response.usage.total_tokens if hasattr(chat_response, 'usage') else 0,
                'prompt_type': 'chat',
                'prompt_tokens': chat_response.usage.prompt_tokens if hasattr(chat_response.usage, 'prompt_tokens') else 0,
                'response_tokens': chat_response.usage.completion_tokens if hasattr(chat_response.usage, 'completion_tokens') else 0,
                'model': getattr(chat_response, 'model', 'unknown'),
                'provider': 'MistralAI',
                'total_time': round(elapsed_time * 1000, 2),
                'prompt': str(messages),
                'cost': self.calculate_cost(
                    chat_response.model,
                    chat_response.usage.prompt_tokens if hasattr(chat_response.usage, 'prompt_tokens') else 0,
                    chat_response.usage.completion_tokens if hasattr(chat_response.usage, 'completion_tokens') else 0
                ),
                'rule': self.rule or '- -',
                'response': chat_response.choices[0].message.content if chat_response.choices else '',
                'success': 'True'
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            executor.submit(self.set_best_model)    # Best model setting happens in the background
            return log

        except Exception as e:
            if fallback:
                return {'statusCode': 500, 'body': str(e)} 
            else:
                print(f"Primary provider failed: {str(e)}") 
                log = {
                    'trace_id': trace_id,
                    'total_tokens': 0,
                    'prompt_type': 'chat',
                    'prompt_tokens': 0,
                    'response_tokens': 0,
                    'model': model,
                    'provider': 'MistralAI',
                    'cost': '- -',
                    'rule': self.rule or '- -',
                    'total_time': 0,
                    'prompt': prompt,
                    'response': str(e),
                    'success': 'False'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                return self.chat_fallback(prompt, trace_id)

    def anthropic_chat(self, prompt, api_key, model, trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()

        try:
            client = anthropic.Anthropic(api_key=api_key)
            start_time = time.time()
            message = client.messages.create(
                model=model,
                max_tokens=1024,
                messages=prompt
            )
            elapsed_time = time.time() - start_time

            log = {
                'trace_id': trace_id,
                'total_tokens': message.usage.input_tokens + message.usage.output_tokens,
                'prompt_type': 'chat',
                'prompt_tokens': message.usage.input_tokens,
                'response_tokens': message.usage.output_tokens,
                'model': message.model,
                'provider': 'Anthropic',
                'total_time': round(elapsed_time * 1000, 2),
                'prompt': prompt,
                'cost': self.calculate_cost(message.model, message.usage.input_tokens, message.usage.output_tokens),
                'rule': self.rule or '- -',
                'response': str(message.content),
                'success': 'True'
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            executor.submit(self.set_best_model)    # Best model setting happens in the background
            return log

        except Exception as e:
            if fallback:
                return {'statusCode': 500, 'body': str(e)} 
            else:
                print(f"Primary provider failed: {str(e)}") 
                log = {
                    'trace_id': trace_id,
                    'total_tokens': 0,
                    'prompt_type': 'chat',
                    'prompt_tokens': 0,
                    'response_tokens': 0,
                    'model': model,
                    'provider': 'Anthropic',
                    'total_time': 0,
                    'prompt': prompt,
                    'cost': '- -',
                    'rule': self.rule or '- -',
                    'response': str(e),
                    'success': 'False'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                return self.chat_fallback(prompt, trace_id)

    def meta_chat(self, prompt, model, trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()

        query = f"app_id={self.router_id}&app_key={self.router_key}&model={model}&prompt={prompt[0]['content']}"
        try:
            url = f"{self.api_bedrock_url}?{query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            }
            start_time = time.time()

            response = self._safe_api_call(url, headers)

            elapsed_time = time.time() - start_time

            if response and response.status_code == 200:
                response_data = json.loads(response.text)
                log = {
                    'trace_id': trace_id,
                    'total_tokens': response_data['prompt_token_count'] + response_data['generation_token_count'],
                    'prompt_type': 'chat',
                    'prompt_tokens': response_data['prompt_token_count'],
                    'response_tokens': response_data['generation_token_count'],
                    'model': self.text_generation_model,
                    'provider': 'Meta',
                    'total_time': round(elapsed_time * 1000, 2),
                    'prompt': str(prompt[0]["content"]),
                    'cost': self.calculate_cost(model, response_data['prompt_token_count'], response_data['generation_token_count']),
                    'rule': self.rule or '- -',
                    'response': response_data['generation'],
                    'success': 'True'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                executor.submit(self.set_best_model)    # Best model setting happens in the background
                return log
            
        except requests.Timeout as e:
            print(f"Meta provider timed out: {str(e)}")
            log = {
                'trace_id': trace_id,
                'total_tokens': 0,
                'prompt_type': 'chat',
                'prompt_tokens': 0,
                'response_tokens': 0,
                'model': model,
                'provider': 'Meta',
                'total_time': 0,
                'prompt': prompt,
                'cost': '- -',
                'rule': self.rule or '- -',
                'response': str(e),
                'success': 'False'
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            return {'statusCode': 500, 'body': 'Meta provider timeout'} if fallback else self.chat_fallback(prompt, trace_id)
        
        except requests.exceptions.RequestException as e:
            print(f"Exception in meta_chat: {str(e)}")
            log = {
                'trace_id': trace_id,
                'total_tokens': 0,
                'prompt_type': 'chat',
                'prompt_tokens': 0,
                'response_tokens': 0,
                'model': model,
                'provider': 'Meta',
                'total_time': 0,
                'prompt': prompt,
                'cost': '- -',
                'rule': self.rule or '- -',
                'response': str(e),
                'success': 'False'
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            return {'statusCode': 500, 'body': str(e)} if fallback else self.chat_fallback(prompt, trace_id)

        except Exception as e:
            print(f"Exception in meta_chat: {str(e)}")
            log = {
                'trace_id': trace_id,
                'total_tokens': 0,
                'prompt_type': 'chat',
                'prompt_tokens': 0,
                'response_tokens': 0,
                'model': model,
                'provider': 'Meta',
                'total_time': 0,
                'cost': '- -',
                'rule': self.rule or '- -',
                'prompt': prompt,
                'response': str(e),
                'success': 'False'
            }
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background
            return {'statusCode': 500, 'body': str(e)} if fallback else self.chat_fallback(prompt, trace_id)


    def embedding_fallback(self, prompt, trace_id = None):
        fallback_provider = self.fallback_embedding_model
        provider_key = self.fallback_embedding_provider_source_key
        model = self.fallback_embedding_model

        print(f"Attempting fallback with: {fallback_provider}")
        if fallback_provider == 'OpenAI':
            return self.openai_embeddings(prompt, provider_key, model, trace_id, fallback=True)
        elif fallback_provider == 'MistralAI':
            return self.mistralai_embeddings(prompt, provider_key, model, trace_id, fallback=True)
        else:
            return {'statusCode': 500, 'body': 'Fallback provider is not configured'}    
        
    def embeddings(self, prompt, rule=None):
        self.rule = rule
        if rule == "cost" and self.cost_embedding_provider_source:
            primary_provider = self.cost_embedding_provider_source
            provider_key=self.cost_embedding_provider_key,
            model=self.cost_embedding_model
            print(f"Trying with cost provider: {primary_provider}")
        elif rule == "performance" and self.performance_embedding_provider_source:
            primary_provider = self.performance_embedding_provider_source
            provider_key=self.performance_embedding_provider_key
            model=self.performance_embedding_model
            print(f"Trying with performance provider: {primary_provider}")
        else:
            primary_provider = self.embedding_provider_source
            provider_key=self.embedding_provider_source_key
            model=self.embedding_model
            print(f"Trying with primary provider: {primary_provider}")

        # Try with the primary provider
        try:
            print(f"Trying with primary provider: {primary_provider}")
            if primary_provider == 'OpenAI':
                return self.openai_embeddings(prompt, provider_key, model)
            elif primary_provider == 'MistralAI':
                return self.mistralai_embeddings(prompt, provider_key, model)
            else:
                raise ConnectionError(f'{primary_provider} is not configured for the Python SDK yet')

        except Exception as e:
            print(f"Primary provider failed: {str(e)}")
            # If the primary provider fails, call the fallback
            return self.embedding_fallback(prompt)

    def openai_embeddings(self, prompt, api_key, model, trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()

        client = OpenAI(api_key=api_key)
        submitted_prompt = prompt[0] if isinstance(prompt, list) and len(prompt) > 0 else prompt
        try:
            start_time = time.time() 
            response = client.embeddings.create(
                input = submitted_prompt,
                model=model
            )
            end_time = time.time() 
            elapsed_time = end_time - start_time

            log = {
                'trace_id': trace_id,
                'total_tokens': response.usage.total_tokens,
                'prompt_type':'embeddings',
                'prompt_tokens': response.usage.prompt_tokens,
                'response_tokens': (response.usage.total_tokens - response.usage.prompt_tokens),
                'model':response.model,
                'provider':'OpenAI',
                'total_time': round(elapsed_time * 1000, 2),  # Convert to milliseconds and round to two decimal places
                'cost': self.calculate_cost(response.model, response.usage.prompt_tokens, (response.usage.total_tokens - response.usage.prompt_tokens)),
                'rule': self.rule or '- -',
                'prompt': str(submitted_prompt),
                'response': '--',
                'success': 'True'
            }
            
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background

            log['response'] =str(response.data[0].embedding)
            return log
            
        except Exception as e:
            if fallback:
                log = {
                    'trace_id': trace_id,
                    'total_tokens': 0,
                    'prompt_type': 'embeddings',
                    'prompt_tokens': 0,
                    'response_tokens': 0,
                    'model': model,
                    'provider': 'OpenAI',
                    'total_time': 0,
                    'cost': '- -',
                    'rule': self.rule or '- -',
                    'prompt': prompt,
                    'response': str(e),
                    'success': 'False'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                return {'statusCode': 500, 'body': str(e)} 
            else:
                print(f"Primary provider failed: {str(e)}") 
                return self.embedding_fallback(prompt, trace_id)
        
    def mistralai_embeddings(self, prompt, api_key, model,trace_id=None, fallback=False):
        trace_id = trace_id if trace_id else uuid.uuid4()

        try:
            client = Mistral(api_key=api_key)
            start_time = time.time()

            # Making the embeddings request
            embeddings_batch_response = client.embeddings.create(model=model, inputs=prompt)

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Constructing the log
            log = {
                'trace_id': trace_id,
                'prompt_type': 'embeddings',
                'total_tokens': embeddings_batch_response.usage.total_tokens if hasattr(embeddings_batch_response, 'usage') else 0,
                'prompt_tokens': embeddings_batch_response.usage.prompt_tokens if hasattr(embeddings_batch_response.usage, 'prompt_tokens') else 0,
                'response_tokens': (embeddings_batch_response.usage.total_tokens - embeddings_batch_response.usage.prompt_tokens) if hasattr(embeddings_batch_response, 'usage') else 0,
                'model': getattr(embeddings_batch_response, 'model', 'unknown'),
                'provider': 'MistralAI',
                'total_time': round(elapsed_time * 1000, 2),  # Convert to milliseconds
                'prompt': prompt,
                'cost': self.calculate_cost(
                    embeddings_batch_response.model,
                    embeddings_batch_response.usage.prompt_tokens if hasattr(embeddings_batch_response.usage, 'prompt_tokens') else 0,
                    (embeddings_batch_response.usage.total_tokens - embeddings_batch_response.usage.prompt_tokens) if hasattr(embeddings_batch_response.usage, 'total_tokens') else 0
                ),
                'rule': self.rule or '- -',
                'result': str(embeddings_batch_response.data),  # Include the embeddings data in the log if needed
                'success': 'True'
            }

            
            # Run log and set_best_model in the background
            executor.submit(self.log, log)          # Logging happens in the background

            log['result'] = embeddings_batch_response

            return log
        except Exception as e:
            if fallback:
                return {'statusCode': 500, 'body': str(e)} 
            else:
                print(f"Primary provider failed: {str(e)}") 
                log = {
                    'trace_id': trace_id,
                    'total_tokens': 0,
                    'prompt_type': 'embeddings',
                    'prompt_tokens': 0,
                    'response_tokens': 0,
                    'model': model,
                    'provider': 'MistralAI',
                    'total_time': 0,
                    'cost': '- -',
                    'rule': self.rule or '- -',
                    'prompt': prompt,
                    'response': str(e),
                    'success': 'False'
                }
                # Run log and set_best_model in the background
                executor.submit(self.log, log)          # Logging happens in the background
                
                return self.embedding_fallback(prompt, trace_id)
        
        
    def log(self, log):
        # Ensure the parameters are URL-encoded, especially for prompt and response
        query = f"app_id={self.router_id}&app_key={self.router_key}&total_tokens={log['total_tokens']}&" \
                f"prompt_type={log['prompt_type']}&prompt_tokens={log['prompt_tokens']}&response_tokens={log['response_tokens']}&" \
                f"model={urllib.parse.quote_plus(log['model'])}&cost={log['cost']}&rule={log['rule']}&" \
                f"provider={log['provider']}&total_time={log['total_time']}&prompt={urllib.parse.quote_plus(str(log['prompt']))}&" \
                f"response={urllib.parse.quote_plus(log['response'])}&trace_id={log['trace_id']}&success={log['success']}"

        try:
            url = f"{self.api_log_base_url}?{query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            }
            response = requests.get(url, headers=headers)
            return response and response.status_code == 200
        except requests.exceptions.RequestException as e:
            print('Error logging data')
            raise ConnectionError(f'Failed to log: {e}.')