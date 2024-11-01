import os
from types import MappingProxyType

try:
    _tw_dict = {}
    _sc_dict = {}
    _scp_set = set()
    # Load and merge SC characters from TW variants, as the BERT model was trained on zh_TW data mostly
    with open(f'{os.path.dirname(__file__)}/TWVariants.txt', 'r', encoding='utf-8') as tw:
        for line in tw:
            k, v = line.strip().split('\t')
            _tw_dict[k] = v
    with open(f'{os.path.dirname(__file__)}/STCharacters.txt', 'r', encoding='utf-8') as sc:
        for line in sc:
            k, v = line.strip().split('\t')
            tc_list = []
            tc = v.split(' ')
            for t in tc:
                if t in _tw_dict:
                    t = _tw_dict[t]
                if not t in tc_list:
                    tc_list.append(t)
            if len(tc_list) == 1 and tc_list[0] == k:
                continue
            _sc_dict[k] = tc_list
    with open(f'{os.path.dirname(__file__)}/STPhrases.txt', 'r', encoding='utf-8') as sp:
        pd = {}
        for line in sp:
            k, v = line.strip().split('\t')
            pairs = zip(k, k[1:])
            for i, pair in enumerate(pairs):
                if pair[0] in _sc_dict and pair[1] in _sc_dict:
                    p1 = _sc_dict[pair[0]]
                    p2 = _sc_dict[pair[1]]
                    if len(p1) > 1 and len(p2) > 1:
                        pk = ''.join(pair)
                        if not pk in pd:
                            pd[pk] = set()
                        pd[pk].add(v[i:i+2])
        for k, v in pd.items():
            if len(v) > 1:
                repeated = True
                uc = set()
                for vv in v:
                    if vv[0] != vv[1]:
                        repeated = False
                    uc.add(vv[0])
                    uc.add(vv[1])
                if not repeated and len(uc) > 3:
                    _scp_set.add(k)
except FileNotFoundError as e:
    print(f"Dictionary file not found: {e}")
    raise

tw_dict = MappingProxyType(_tw_dict)
sc_dict = MappingProxyType(_sc_dict)
scp_set = frozenset(_scp_set)
sc_char = frozenset(set([k for k, v in sc_dict.items() if k not in v]))
sc_tc_variants = frozenset(set([t for tc_list in sc_dict.values() if len(tc_list) > 1 for t in tc_list]))
