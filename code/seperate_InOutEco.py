prefix = '/da4_data/play/Ember_ECO_data/'

file1 = 'direct_downstream'
file2 = 'direct_upstream'
file3 = 'recursive_downstreams'
file4 = 'recursive_upstreams'

file_eco = 'all_packages.ember.list'

ECO_pkgs = set()

with open(prefix + file_eco, 'r') as feco:
    for line in feco:
        ECO_pkgs.add(line.strip())


def seperate_Inout(filename):
    f = open(filename, 'r')
    Inf = open(filename + '.In', 'w')
    Outf = open(filename + '.Out', 'w')
    for line in f:
        items = line.strip().split(';')
        if items[1] == '':
            Inf.write(items[0] + ';\n')
            Outf.write(items[0] + ';\n')
            continue
        Inf.write(
            items[0] + ';' + ','.join(filter(lambda x: x in ECO_pkgs, items[1].split(','))) + '\n')
        Outf.write(
            items[0] + ';' + ','.join(filter(lambda x: x not in ECO_pkgs, items[1].split(','))) + '\n')
    f.close()
    Inf.close()
    Outf.close()


map(seperate_Inout, [prefix + file1, prefix +
                     file2, prefix + file3, prefix + file4])
