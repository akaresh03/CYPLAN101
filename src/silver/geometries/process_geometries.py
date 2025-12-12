"""
Master script to process all geometry files from bronze to silver layer.

This script automatically discovers and runs all processor files in this directory.
"""

import importlib
from pathlib import Path


def main():
    """Run all geometry processors."""
    # print("="*60)
    # print("SILVER LAYER: PROCESSING ALL GEOMETRIES")
    # print("="*60)

    # # Get current directory
    # current_dir = Path(__file__).parent

    # # Find all .py files
    # processor_files = current_dir.glob("*.py")

    # # Files to skip
    # skip_files = {"_utilities.py", "process_geometries.py", "__init__.py"}

    # # Track results
    # processors_run = []
    # errors = []

    # for file in processor_files:
    #     # Skip utility files and this file
    #     if file.name in skip_files:
    #         continue

    #     # Get module name (filename without .py)
    #     module_name = file.stem

    #     try:
    #         # Import the module
    #         module = importlib.import_module(module_name)

    #         # Check if it has a process() function
    #         if hasattr(module, 'process'):
    #             print(f"\n{'='*60}")
    #             print(f"Running: {module_name}")
    #             print(f"{'='*60}")

    #             # Run the process function
    #             module.process()

    #             processors_run.append(module_name)
    #         else:
    #             print(f"⚠ Skipping {module_name}: No process() function found")

    #     except Exception as e:
    #         error_msg = f"✗ Error in {module_name}: {e}"
    #         print(f"\n{error_msg}")
    #         errors.append(error_msg)

    # # Summary
    # print("\n" + "="*60)
    # print("PROCESSING COMPLETE")
    # print("="*60)
    # print(f"Processors run: {len(processors_run)}")
    # for proc in processors_run:
    #     print(f"  ✓ {proc}")

    # if errors:
    #     print(f"\nErrors: {len(errors)}")
    #     for error in errors:
    #         print(f"  {error}")
    # else:
    #     print("\n✓ All processors completed successfully!")



    # I want this to run all of the .py files in this directory except for _utilities.py and this file.
    print("This is a placeholder for the main processing function.")
    # Get current directory
    current_dir = Path(__file__).parent

    # Find all .py files
    processor_files = current_dir.glob("*.py")

    # Files to skip
    skip_files = {"_utilities.py", "process_geometries.py", "__init__.py"}

    # Track results
    processors_run = []
    errors = []

    for file in processor_files:
        # Skip utility files and this file
        if file.name in skip_files:
            continue

        # Get module name (filename without .py)
        module_name = file.stem

        try:
            # Import the module
            module = importlib.import_module(module_name)

            # Check if it has a process() function
            if hasattr(module, 'process'):
                print(f"\n{'='*60}")
                print(f"Running: {module_name}")
                print(f"{'='*60}")

                # Run the process function
                module.process()

                processors_run.append(module_name)
            else:
                print(f"⚠ Skipping {module_name}: No process() function found")

        except Exception as e:
            error_msg = f"✗ Error in {module_name}: {e}"
            print(f"\n{error_msg}")
            errors.append(error_msg)

    # Summary
    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)
    print(f"Processors run: {len(processors_run)}")
    for proc in processors_run:
        print(f"  ✓ {proc}")

    if errors:
        print(f"\nErrors: {len(errors)}")
        for error in errors:
            print(f"  {error}")
    else:
        print("\n✓ All processors completed successfully!")

if __name__ == "__main__":
    main()
