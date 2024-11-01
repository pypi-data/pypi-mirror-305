# tinyagi/cli.py

import argparse
import sys
import json
from .config import ConfigManager
from .model import ModelLoader

def main():
    parser = argparse.ArgumentParser(description='TinyAGI CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Generate command
    parser_generate = subparsers.add_parser('generate', help='Generate text from a prompt')
    parser_generate.add_argument('--prompt', '-p', required=True, help='Prompt text')
    parser_generate.add_argument('--config', '-c', help='Path to config file')
    parser_generate.add_argument('--inference-params', '-ip', help='Inference parameters in JSON format', default='{}')
    parser_generate.add_argument('--stream', '-s', action='store_true', help='Stream output')

    # Embed command
    parser_embed = subparsers.add_parser('embed', help='Generate embeddings')
    parser_embed.add_argument('--input', '-i', required=True, nargs='+', help='Input text(s)')
    parser_embed.add_argument('--config', '-c', help='Path to config file')

    # Reload command
    parser_reload = subparsers.add_parser('reload', help='Reload the model with new configuration')
    parser_reload.add_argument('--config', '-c', help='Path to new config file')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    config_manager = ConfigManager(args.config)
    model_loader = ModelLoader(config_manager.get_config())

    if args.command == 'generate':
        try:
            inference_params = json.loads(args.inference_params)
            if args.stream:
                for chunk in model_loader.generate(args.prompt, inference_params, stream=True):
                    print(chunk['choices'][0]['text'], end='', flush=True)
            else:
                output = model_loader.generate(args.prompt, inference_params)
                text = output['choices'][0]['text']
                print(text)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
    elif args.command == 'embed':
        try:
            embeddings = model_loader.embed(args.input)
            print(json.dumps({'embedding': embeddings}, indent=2))
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
    elif args.command == 'reload':
        try:
            config = config_manager.reload_config(args.config)
            model_loader.reload_model(config)
            print("Model reloaded successfully.")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

def run_cli():
    main()
