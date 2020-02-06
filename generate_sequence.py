from datetime import datetime
from optparse import OptionParser


def log(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("{0} {1}".format(current_time, msg))


def p1_win(start, n):
    (p1, p2) = (start, start)
    while p1 % n != 0 and p2 % n != 0:
        p1 = (p1 + p2) % n
        p2 = (p1 + p2) % n
    return p1 != 0


def is_seq_member(n):
    if n < 2:
        return False
    first_win = p1_win(1, n)
    for start in range(2, n):
        if p1_win(start, n) != first_win:
            return False
    return True


SEQ_FILE = 'gcs.txt'
MAX_FILE = 'max_calc.txt'

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

parser = OptionParser()
parser.add_option('--end', default=str(max_calced * 2))
(options, args) = parser.parse_args()

end = int(options.end)

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
