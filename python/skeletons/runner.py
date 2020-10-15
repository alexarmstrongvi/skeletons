#!/usr/bin/env python3
"""
TODO: Brief synopsis

Examples:
    TODO: $ ./runner.py foo.txt --bar
"""
# Standard library
import argparse
import logging
import os
import sys
from time import time
from typing import List, Any

# Local
import skeletons

# Globals
logger = logging.getLogger(__name__)

################################################################################
def main():
    """ Main Function """
    start_time = time()
    args = parse_args(sys.argv[1:])
    setup_logging(args.log_level.upper())

    logger.debug(">"*40)
    logger.debug("Running %s", " ".join(sys.argv[1:]))

    check_environment()
    check_args(args)

    # Main logic of script
    var1, var2 = 3, 2
    results = []
    results.append(skeletons.add(var1, var2))
    logger.info("%d + %d = %d", var1, var2, results[0])
    results.append(skeletons.subtract(var1, var2))
    logger.info("%d - %d = %d", var1, var2, results[1])

    # Save output
    save(args.ofile_name, results)

    run_time = (time() - start_time)
    logger.debug("TOTAL TIME: %fs", run_time)
    logger.debug("<"*40)

################################################################################
# Setup Functions
def parse_args(argv : List[str]) -> argparse.Namespace:
    """ Parse user input

    Arguments:
        argv : User input arguments split into list

    Returns:
       Parsed user inputs
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ifile-name",
                        help="Input file name")
    parser.add_argument("-o", "--ofile-name",
                        help="Output file name")
    parser.add_argument("-l", "--log-level",
                        default="INFO",
                        help="Logging level")

    return parser.parse_args(argv)

def setup_logging(log_level : str):
    """ Configure module-level logger

    Arguments:
        log_level: Output level for logger
    """
    # Configuration
    log_format = "%(levelname)8s :: %(message)s"
    #log_format = ("%(levelname)8s :: "
    #              +"(%(filename)s:%(funcName)s:L%(lineno)d) "
    #              +"%(message)s") # Useful for debugging
    log_stream = sys.stderr

    # Setup
    formatter = logging.Formatter(log_format)
    handler = logging.StreamHandler(stream=log_stream)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)

def check_environment():
    """ Check if the runtime environment is setup as expected """
    if not os.environ.get("PYTHONPATH"):
        logger.error("PYTHONPATH environment variable not defined")
        sys.exit(1)

def check_args(args : argparse.Namespace):
    """ Check the input arguments are as expected

    Arguments:
        args : parsed user inputs
    """
    if args.ifile_name and not os.path.exists(args.ifile_name):
        logger.error("Cannot find input file: %s", args.ifile_name )
        sys.exit(1)
    logger.debug("Reading in %s", args.ifile_name)

    # Check if output file exists
    # If so, check with user if they want to overwrite it
    if args.ofile_name and os.path.exists(args.ofile_name):
        logger.warning("Output file already exists: %s", args.ofile_name)
        usr_msg = "\tWould you like to overwrite it? [Y/N] "
        overwrite_op = input(usr_msg)

        # Only accept Y or N
        while overwrite_op not in ["Y","N"]:
            logger.error("Unacceptable answer: %s", overwrite_op)
            usr_msg = "Would you like to overwrite it? [Y/N] "
            overwrite_op = input(usr_msg)

        if overwrite_op == "N":
            print("Try using a different output file name, "
                  "deleting the old file, or "
                  "changing the name of the old file.")
            sys.exit(0)

def save(ofile_name : str, results : List[Any]):
    """ Save output

    Arguments:
        ofile_name : name of output file
        results : results to be printed into output file
    """
    if ofile_name:
        write_str = "Hello World\n"
        write_str += "Results = " + str(results) + "\n"
        with open(ofile_name, "w") as ofile:
            ofile.write(write_str)

################################################################################
if __name__ == "__main__":
    main()
