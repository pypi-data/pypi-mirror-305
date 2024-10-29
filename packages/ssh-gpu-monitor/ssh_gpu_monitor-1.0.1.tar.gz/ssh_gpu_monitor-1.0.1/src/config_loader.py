import yaml
import argparse
from pathlib import Path
from typing import Any, Dict, List, NamedTuple
import os

class Target(NamedTuple):
    """Represents a target with its associated username and key path"""
    host: str
    username: str
    key_path: str

def generate_targets(config: Dict[str, Any]) -> List[Target]:
    """Generate list of targets from config specification."""
    targets = []
    default_username = config['ssh']['username']
    default_key_path = config['ssh']['key_path']
    
    # Add individual targets
    if 'individual' in config['targets']:
        for target in config['targets']['individual']:
            if isinstance(target, str):
                # Simple string target uses defaults
                targets.append(Target(target, default_username, default_key_path))
            else:
                # Dictionary target may have overrides
                targets.append(Target(
                    target['host'],
                    target.get('username', default_username),
                    target.get('key_path', default_key_path)
                ))
    
    # Add pattern-based targets
    if 'patterns' in config['targets']:
        for pattern in config['targets']['patterns']:
            pattern_username = pattern.get('username', default_username)
            pattern_key_path = pattern.get('key_path', default_key_path)
            targets.extend([
                Target(
                    pattern['format'].format(
                        prefix=pattern['prefix'],
                        number=x
                    ),
                    pattern_username,
                    pattern_key_path
                )
                for x in range(pattern['start'], pattern['end'] + 1)
            ])
    
    # Remove duplicates while preserving order
    seen = set()
    unique_targets = []
    for target in targets:
        if target.host not in seen:
            seen.add(target.host)
            unique_targets.append(target)
    
    return unique_targets

def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file and override with command line arguments."""
    
    # Load YAML config
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='GPU Checker')
    
    # Add arguments for all config options
    parser.add_argument('--ssh.username', type=str, help='Default SSH username')
    parser.add_argument('--ssh.key_path', type=str, help='SSH key path')
    parser.add_argument('--ssh.jump_host', type=str, help='Jump host')
    parser.add_argument('--ssh.timeout', type=int, help='SSH timeout in seconds')
    
    # Add target override options
    parser.add_argument('--targets', type=str, nargs='+', 
                       help='Override all targets with specified list (will use default username)')
    
    parser.add_argument('--display.refresh_rate', type=int, help='Refresh rate in seconds')
    
    parser.add_argument('--debug.enabled', action='store_true', help='Enable debug mode')
    parser.add_argument('--debug.log_dir', type=str, help='Log directory')
    parser.add_argument('--debug.log_file', type=str, help='Log file name')
    
    args = parser.parse_args()
    
    # Update config with command line arguments
    for arg, value in vars(args).items():
        if value is not None:
            if arg == 'targets':
                # Special handling for targets override
                config['targets'] = {
                    'individual': [{'host': t} for t in value],
                    'patterns': []
                }
            else:
                # Split the argument name into sections
                sections = arg.split('.')
                
                # Navigate through the config dictionary
                current = config
                for section in sections[:-1]:
                    current = current[section]
                
                # Set the value
                current[sections[-1]] = value
    
    # Create log directory if debug is enabled
    if config['debug']['enabled']:
        log_dir = Path(config['debug']['log_dir'])
        log_dir.mkdir(exist_ok=True)
    
    return config
