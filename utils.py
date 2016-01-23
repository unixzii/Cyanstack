__VERBOSE_ENABLED = False
__DEBUG_ENABLED = True


def warn(msg):
    print("\033[1;33;40mWARN: %s\033[0m" % msg)


def err(msg):
    print("\033[1;31;40mERR: %s\033[0m" % msg)


def debug(msg):
    global __DEBUG_ENABLED
    if __DEBUG_ENABLED:
        print("\033[1;34;40mDEBUG: %s\033[0m" % msg)


def verbose(msg):
    global __VERBOSE_ENABLED
    if __VERBOSE_ENABLED:
        print(msg)


def set_verbose_enabled(b):
    global __VERBOSE_ENABLED
    __VERBOSE_ENABLED = b


def set_debug_enabled(b):
    global __DEBUG_ENABLED
    __DEBUG_ENABLED = b
