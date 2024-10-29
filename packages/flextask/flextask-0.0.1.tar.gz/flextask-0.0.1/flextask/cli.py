# Flex Task CLI
#
# Written by Grigori Fursin

import cmind
import sys

############################################################
def run_flex_task(argv = None):
    """
    """

    # Access CMX
    if argv is None:
        argv = sys.argv[1:]

    r = cmind.x(['run', 'flex.task'] + argv)

    return r

###########################################################################
if __name__ == "__main__":
    run_flex_task()
