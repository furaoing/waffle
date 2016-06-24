def linux_line_sep(s):
    s = s.replace("\r\n", "\n")
    s = s.replace("\r", "\n")
    return s


def win_line_sep(s):
    s = s.replace("\n", "\r\n")
    s = s.replace("\r", "\r\n")
    return s


def mac_line_sep(s):
    s = s.replace("\r\n", "\r")
    s = s.replace("\n", "\r")
    return s