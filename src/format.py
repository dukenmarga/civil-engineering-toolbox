
def float(x, decimal=2):
    dec ='{0:.' + str(decimal) + 'f}'
    return float(dec.format(x))