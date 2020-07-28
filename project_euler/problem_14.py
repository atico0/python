m_seq = []
m_num = 0
for z in range(999999, 0, -1):
    num = z
    seq = []
    print(num)
    while num != 1:
        seq.append(num)
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
    print(seq,len(seq))
    if len(list(m_seq)) < len(list(seq)):
        m_seq = []
        m_seq = seq[:]
        m_num = z
print(m_seq)
print(m_num)
