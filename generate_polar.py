# pip install matplotlib

from math import log
import matplotlib.pyplot as plt
from optparse import OptionParser


def save_pattern(seq, end):
    """ Saves a polar graph of the GCS sequence, up to a specified stopping point in the sequence

    @param seq (list[int]) - the generalized chopstick sequence
    @param end (int) - only GCS numbers less than or equal to `end` are included in the graph
    """
    size = round(log(end)) * 2
    fig = plt.figure(figsize=(size, size))
    trunc_seq = [n for n in seq if n <= end]
    for n in trunc_seq:
        plt.polar(n, n, 'b.')
    fig.savefig('./img/polar/gcs_polar_{0}.png'.format(end))


SEQ_FILE = 'gcs.txt'

with open(SEQ_FILE) as f:
    seq = [int(line.strip()) for line in f.readlines() if line != '']
    max_calced = max(seq)

# set the limit on how much of the GCS sequence we want in our graph
# if user does not specify a limit, default to the largest number we've checked
parser = OptionParser()
parser.add_option('--end', default=str(max_calced))
(options, args) = parser.parse_args()

# save polar graph to file
save_pattern(seq, int(options.end))
