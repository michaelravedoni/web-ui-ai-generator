import sys
import json
import os
import re
import argparse
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_CYAN = '\033[46m\033[30m'

# Paths
BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "ui-config.json"
TEMPLATE_DIR = BASE_DIR / "templates"
DEFAULT_CONFIG_PATH = BASE_DIR / "config" / "default_project.json"

class KitchenAssistant:
    def __init__(self):
        self.config = {}
        self.load_config()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print(f"{Colors.HEADER}{Colors.BOLD}")
        print("  _   _  ___    _  __ _  _       _                    ")
        print(" | | | ||_ _|  | |/ /(_)| |_  __| |__  ___  _ __      ")
        print(" | |_| | | |   | ' / | ||  _|/ _| '_ \/ -_)| '_ \     ")
        print("  \___/ |___|  |_|\_\|_| \__|\__|_| |_\___||_| |_|    ")
        print(f"{Colors.ENDC}")
        print(f"{Colors.CYAN}  AI-Powered UI Design Workflow Assistant{Colors.ENDC}")
        print("-" * 60)
        
        # Status Bar
        p_name = self.config.get('project', {}).get('name', 'No Project Selected')
        print(f"  Active Project: {Colors.BOLD}{p_name}{Colors.ENDC}")
        print("-" * 60)
        print()

    def load_config(self):
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        else:
            self.config = {"project": {}, "strategy": {}}

    def save_config(self):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        print(f"\n{Colors.GREEN}✓ Configuration saved.{Colors.ENDC}")

    def get_input(self, prompt, default=None):
        if default:
            user_input = input(f"{Colors.BLUE}{prompt} [{default}]: {Colors.ENDC}")
            return user_input if user_input.strip() else default
        else:
            return input(f"{Colors.BLUE}{prompt}: {Colors.ENDC}")

    def wait_for_enter(self):
        input(f"\n{Colors.CYAN}[Press Enter to continue]{Colors.ENDC}")

    def copy_to_clipboard(self, text):
        try:
            # macOS pbcopy
            process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
            process.communicate(text.encode('utf-8'))
            return True
        except Exception as e:
            return False

    # --- ACTIONS ---

    def action_init_project(self):
        print(f"{Colors.BOLD}>>> Project Initialization{Colors.ENDC}")
        current = self.config.get('project', {})
        
        name = self.get_input("Project Name", current.get('name', 'My New Project'))
        desc = self.get_input("Description", current.get('description', ''))
        target = self.get_input("Target Audience", current.get('target', ''))
        vibe = self.get_input("Vibe / Keywords", current.get('vibe', 'Modern, Clean'))

        self.config['project'] = {
            "name": name,
            "description": desc,
            "target": target,
            "vibe": vibe
        }
        self.save_config()
        self.wait_for_enter()

    def action_strategy_prompt(self):
        print(f"{Colors.BOLD}>>> Generating Phase 1: Strategy Prompt{Colors.ENDC}")
        prompt = self.render_template("01_strategy.md", self.config)
        self.print_prompt_box(prompt)
        print(f"\n{Colors.WARNING}NEXT STEP:{Colors.ENDC} Paste this prompt to your LLM.")
        print("Once you have the result, come back and run 'Record Strategy'.")
        self.wait_for_enter()

    def action_record_strategy(self):
        print(f"{Colors.BOLD}>>> Phase 1.5: Recording Strategy{Colors.ENDC}")
        print("Enter the design tokens decided by the IA Strategy.")
        
        strat = self.config.get('strategy', {})
        colors = strat.get('colors', {})
        typo = strat.get('typography', {})

        print(f"\n{Colors.UNDERLINE}Colors (HEX){Colors.ENDC}")
        colors['primary'] = self.get_input("Primary Color", colors.get('primary', '#000000'))
        colors['secondary'] = self.get_input("Secondary Color", colors.get('secondary', '#ffffff'))
        colors['neutral'] = self.get_input("Neutral/Surface", colors.get('neutral', '#f3f4f6'))

        print(f"\n{Colors.UNDERLINE}Typography{Colors.ENDC}")
        typo['heading'] = self.get_input("Heading Font", typo.get('heading', 'Inter'))
        typo['body'] = self.get_input("Body Font", typo.get('body', 'Roboto'))

        self.config['strategy'] = {
            "colors": colors,
            "typography": typo
        }
        self.save_config()
        self.wait_for_enter()

    def action_context_prompt(self):
        print(f"{Colors.BOLD}>>> Generating Phase 2: Context Loading Prompt{Colors.ENDC}")
        # This prompt is static usually, but we check if master specs exist
        specs_path = BASE_DIR / "MASTER_UI_SPECS.md"
        if not specs_path.exists():
            print(f"{Colors.FAIL}Error: MASTER_UI_SPECS.md not found!{Colors.ENDC}")
            self.wait_for_enter()
            return

        prompt = self.render_template("02_context.md", self.config)
        self.print_prompt_box(prompt)
        print(f"\n{Colors.WARNING}NOTE:{Colors.ENDC} This prompt loads your Master Specs into the LLM context.")
        self.wait_for_enter()

    def action_kitchen_prompt(self):
        print(f"{Colors.BOLD}>>> Generating Phase 3: Kitchen Sink Prompt{Colors.ENDC}")
        
        # Check if strategy is loaded
        if 'colors' not in self.config.get('strategy', {}):
            print(f"{Colors.FAIL}Warning: Strategy configuration seems empty.{Colors.ENDC}")
            if self.get_input("Continue anyway?", "no").lower() != "yes":
                return

        prompt = self.render_template("03_kitchen_sink.md", self.config)
        self.print_prompt_box(prompt)
        print(f"\n{Colors.WARNING}GOAL:{Colors.ENDC} Generate 'kitchen-sink.html' to validate the design system.")
        self.wait_for_enter()

    def action_production_prompt(self):
        print(f"{Colors.BOLD}>>> Generating Phase 4: Production Prompt{Colors.ENDC}")
        
        print(f"\n{Colors.UNDERLINE}Page Details{Colors.ENDC}")
        p_name = self.get_input("Page Name", "Landing Page")
        p_obj = self.get_input("Objective", "Convert visitors")
        p_target = self.get_input("Target", self.config['project'].get('target', 'General'))
        
        print(f"\n{Colors.CYAN}Describe the structure (enter 'END' on a new line to finish):{Colors.ENDC}")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        structure = "\n".join(lines) if lines else "[Standard Structure]"

        # Create a temp context for this render
        temp_config = self.config.copy()
        temp_config['page_context'] = {
            "name": p_name,
            "objective": p_obj,
            "target": p_target,
            "structure": structure
        }

        prompt = self.render_template("04_production.md", temp_config)
        self.print_prompt_box(prompt)
        self.wait_for_enter()

    # --- HELPERS ---

    def render_template(self, template_name, context):
        template_path = TEMPLATE_DIR / template_name
        if not template_path.exists():
            return f"[Error: Template {template_name} not found]"
        
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Handle {{ variable.path }}
        matches = re.findall(r"\{\{\s*([\w\.]+)\s*\}\}", content)
        for var_path in set(matches):
            val = self.get_nested_value(context, var_path)
            replacement = str(val) if val is not None else f"[MISSING: {var_path}]"
            content = re.sub(r"\{\{\s*" + re.escape(var_path) + r"\s*\}\}", replacement, content)

        # Handle [FILE_CONTENT:path]
        file_matches = re.finditer(r"\[FILE_CONTENT:(.+?)\]", content)
        for match in file_matches:
            full_tag = match.group(0)
            rel_path = match.group(1).strip()
            file_path = BASE_DIR / rel_path
            
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    file_content = f.read()
                content = content.replace(full_tag, file_content)
            else:
                content = content.replace(full_tag, f"[ERROR: File {rel_path} not found]")

        return content

    def get_nested_value(self, data, path):
        keys = path.split(".")
        val = data
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return None

    def print_prompt_box(self, content):
        copied = self.copy_to_clipboard(content)
        
        print(f"\n{Colors.CYAN}" + "▼" * 30 + " START OF PROMPT " + "▼" * 30 + f"{Colors.ENDC}")
        if copied:
             print(f"{Colors.BG_CYAN}  SUCCESS: COPIED TO CLIPBOARD! (Ready to paste)  {Colors.ENDC}")
        else:
             print(f"{Colors.FAIL}  (Clipboard copy failed - please verify you have pbcopy installed)  {Colors.ENDC}")
        
        print(content)
        
        print(f"\n{Colors.CYAN}" + "▲" * 30 + " END OF PROMPT " + "▲" * 30 + f"{Colors.ENDC}")
        if copied:
            print(f"{Colors.BG_CYAN}  (Already in your clipboard)  {Colors.ENDC}")

    def run(self):
        while True:
            self.print_header()
            print(f"{Colors.BOLD}WORKFLOW STEPS:{Colors.ENDC}")
            print("  1. [Init]     Project Setup & Configuration")
            print("  2. [Phase 1]  Generate Strategy Prompt")
            print("  3. [Record]   Record Strategy Decisions (Colors, Fonts)")
            print("  4. [Phase 2]  Generate Context Loading Prompt")
            print("  5. [Phase 3]  Generate Kitchen Sink Prompt")
            print("  6. [Phase 4]  Generate Production Page Prompt")
            print()
            print("  q. Quit")
            print()
            
            choice = input(f"{Colors.BLUE}Choose an action: {Colors.ENDC}").strip().lower()

            if choice == '1':
                self.action_init_project()
            elif choice == '2':
                self.action_strategy_prompt()
            elif choice == '3':
                self.action_record_strategy()
            elif choice == '4':
                self.action_context_prompt()
            elif choice == '5':
                self.action_kitchen_prompt()
            elif choice == '6':
                self.action_production_prompt()
            elif choice == 'q':
                print("Goodbye!")
                sys.exit(0)
            else:
                pass

if __name__ == "__main__":
    app = KitchenAssistant()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
