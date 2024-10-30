import os
import sys
import glob
from datetime import datetime
import fnmatch
import logging

logger: logging.Logger = None


def setup_logging(log_level_str="INFO"):
    """
    Setup logging configuration
    """
    # Mapping delle stringhe di log level ai livelli effettivi
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    # Converti la stringa del level in uppercase e prendi il livello corrispondente
    # defaulta a INFO se il level non è valido
    log_level = log_levels.get(log_level_str.upper(), logging.INFO)

    # Configura il logging
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)
    return logger


def get_hyperlisa_dir():
    """
    Returns the hyperlisa directory path. The directory should be in the project root.
    """
    app_root = os.getcwd()  # Get the current working directory (project root)
    hyperlisa_dir = os.path.join(app_root, "hyperlisa")
    if not os.path.exists(hyperlisa_dir):
        os.makedirs(hyperlisa_dir)
    return hyperlisa_dir


def matches_pattern(path, patterns):
    """
    Determine if a path matches any pattern in a given list
    """
    global logger
    logger.debug(f"Checking path: {path} against patterns: {patterns}")
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def get_files_by_depth(repo_dir, includes, excludes):
    """
    Retrieve files, filtering based on include and exclude patterns
    """
    global logger
    logger.debug(f"Searching files in directory: {repo_dir}")
    files_by_depth = []
    for root, dirs, files in os.walk(repo_dir):
        # Apply excludes to directories and files
        dirs[:] = [d for d in dirs if not matches_pattern(d, excludes)]
        relative_root = os.path.relpath(root, repo_dir)

        # Check if the current directory should be excluded
        if matches_pattern(relative_root, excludes):
            continue  # Skip this directory and its contents

        for file in files:
            # Only include files matching the includes list and not in an excluded directory
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, repo_dir)

            if matches_pattern(relative_file_path, includes) and not matches_pattern(
                relative_file_path, excludes
            ):
                files_by_depth.append((relative_root, file_path))

    # Sort files by depth
    files_by_depth.sort(key=lambda x: (x[0].count(os.sep), x[1]))
    return files_by_depth


def remove_old_combined_files(hyperlisa_dir, output_name):
    """
    Remove old combined files that match the output name pattern
    """
    print("Removing old combined files...")
    for file_name in os.listdir(hyperlisa_dir):
        if file_name.startswith(output_name) and file_name.endswith(".txt"):
            print(f"Removing file {file_name}")
            os.remove(os.path.join(hyperlisa_dir, file_name))
    print("Old files removed")


def main():
    global logger
    print("File generation started")

    # Get hyperlisa directory
    hyperlisa_dir = get_hyperlisa_dir()

    # Default output name is the current directory name in uppercase
    app_root = os.getcwd()
    default_output_name = os.path.basename(app_root).upper()
    output_name = default_output_name

    # Check if user provided a custom output name or configuration file path
    config_path = None
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_name = sys.argv[i + 1]
        elif sys.argv[i] == "--config" and i + 1 < len(sys.argv):
            config_path = sys.argv[i + 1]
            break

    if not config_path:
        # Use config.yaml from hyperlisa directory by default
        config_path = os.path.join(hyperlisa_dir, "config.yaml")
        if not os.path.exists(config_path):
            print("Configuration file not found in hyperlisa directory.")
            sys.exit(1)

    # Load configuration from config.yaml
    includes = []
    excludes = []

    try:
        with open(config_path, "r") as f:
            current_section = None
            log_level = "INFO"  # default
            for line in f:
                line = line.strip()
                # Ignore comments and empty lines
                if not line or line.startswith("#"):
                    continue

                if line.startswith("log_level:"):
                    log_level = line.split(":")[1].strip()
                elif line.lower() == "includes:":
                    current_section = "includes"
                    continue
                elif line.lower() == "excludes:":
                    current_section = "excludes"
                    continue

                # Parse list items (assumes each item starts with "- ")
                if line.strip().startswith("- "):
                    item = (
                        line[2:].strip().strip('"')
                    )  # Remove "- ", quotes and any surrounding whitespaceng whitespace
                    if current_section == "includes":
                        includes.append(item)
                    elif current_section == "excludes":
                        excludes.append(item)

        # Setup logging with configured level
        logger = setup_logging(log_level)

        logger.debug("Configuration loaded:")
        logger.debug(f"Log level: {log_level}")
        logger.debug(f"Include patterns: {includes}")
        logger.debug(f"Exclude patterns: {excludes}")

    except FileNotFoundError:
        print(f"Configuration file not found at {config_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading configuration file: {str(e)}")
        sys.exit(1)

    # Check if the "--clean" option was passed
    clean_data = "--clean" in sys.argv

    # Generate output file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = os.path.join(hyperlisa_dir, f"{output_name}_{timestamp}.txt")

    # If "--clean" is passed, remove old combined files
    if clean_data:
        remove_old_combined_files(hyperlisa_dir, output_name)

    # Define separators for file content
    separator = "#" * 40
    file_separator = "+" * 50

    try:
        # Open the output file and write contents of each file, adding separators for readability
        with open(output_file, "w", encoding="utf-8") as outfile:
            for relative_root, file_path in get_files_by_depth(
                app_root, includes, excludes
            ):
                relative_file_path = os.path.relpath(file_path, app_root)
                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        # Add separators and file path for clarity
                        outfile.write(
                            f"{separator}\n#\n#\n# {file_separator}\n# {relative_file_path}\n# {file_separator}\n#\n#\n{separator}\n"
                        )
                        outfile.write(infile.read())
                        outfile.write("\n\n")
                except Exception as e:
                    print(f"Warning: Could not read file {file_path}: {str(e)}")
                    continue

        print(f"All code files have been combined into {output_file}")
    except Exception as e:
        print(f"Error writing output file: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
