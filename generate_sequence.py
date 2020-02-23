from datetime import datetime
from optparse import OptionParser


def log(msg):
    """ Logs a message with the timestamp of when it occurred

    @param msg (string) - message to be logged
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("{0} {1}".format(current_time, msg))


def p1_win(i, n):
    """ Returns whether or not the first player to get hit wins the game

    @param i (int) - number of fingers each player starts with
    @param n (int) - total number of fingers on a hand

    @return (boolean)
    """
    (p1, p2) = (i, i)
    while p1 % n != 0 and p2 % n != 0:
        p1 = (p1 + p2) % n
        p2 = (p1 + p2) % n
    return p1 != 0


def is_seq_member(n):
    """
    Returns whether or not a number `n` is a member of the generalized chopstick sequence.
    A number `n` is a sequence member iff the same player either wins or loses every round
    for all values of `i` (0 < i < n) where `i` is the number of fingers each player starts with

    @param n (int) - total number of fingers on a hand

    @return (boolean)
    """
    if n < 2:
        return False
    first_win = p1_win(1, n)
    for start in range(2, n):
        if p1_win(start, n) != first_win:
            return False
    return True


# files used for storing and calculating the generalized chopstick sequence
SEQ_FILE = 'gcs.txt'
MAX_FILE = 'max_calc.txt'

# determine where we need to resume calculating the sequence from
try:
    with open(SEQ_FILE) as f:
        seq = [int(line.strip()) for line in f.readlines() if line != '']
        max_calced = max(seq)
except FileNotFoundError:
    with open(SEQ_FILE, 'w') as f:
        f.write('')
    seq = []
    max_calced = 0

try:
    with open(MAX_FILE) as f:
        num = int(f.readline())
        max_calced = max(max_calced, num)
except FileNotFoundError:
    with open(MAX_FILE, 'w') as f:
        f.write(str(max_calced))

# determine when to stop calculating the sequence (user input or default)
parser = OptionParser()
parser.add_option('--end', default=str(max_calced + 5000))
(options, args) = parser.parse_args()

end = int(options.end)

# generate GCS sequence numbers and save them to a file
log('Processing until {0}'.format(end))

for n in range(max_calced + 1, end + 1):
    if n % 10 == 0:
        log('n = {0}'.format(n))
    if is_seq_member(n):
        with open(SEQ_FILE, 'a') as f:
            f.write(str(n) + '\n')
    with open(MAX_FILE, 'w') as f:
        f.write(str(n))

log('Done processing up to {0}'.format(end))
input()
