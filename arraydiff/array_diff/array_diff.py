import argparse


def calculate_difference_list(current=None, target=None):
    '''
    Function to calculate the array difference. This will calculate the differences in individual elements.
    The lists are not treated as mathematical sets.
    Worst Case Performance: O(n*m) from iterating through the lengths of current and target and then through _adds + _deletes
    :param: current - original list
    :param: target - output list
    :returns: diffs - dictionary with two lists additions:[ ] and deletes:[ ]
    '''
    if current is None:
        current = []
    if target is None:
        target = []
    _adds = []
    _deletes = []
    while len(current) > 0 and len(target) > 0:
        a = current.pop(0)
        b = target.pop(0)
        if a != b:
            _adds.append(b)
            _deletes.append(a)
    if len(current) > len(target):
        _deletes += current
    else:
        _adds += target
    for e in _adds + _deletes:
        if e in _adds and e in _deletes:
            _adds.remove(e)
            _deletes.remove(e)
    return {'additions': _adds, 'deletions': _deletes}


def calculate_difference_set(current: list=None, target: list=None):
    '''
    Function to calculate the array difference. This will calculate the differences in individual elements.
    The lists are not treated as mathematical sets.
    Worst Case Performance: O(n*m) from converting the lists into sets
    :param: current - original list
    :param: target - output list
    :returns: diffs - dictionary with two lists additions:[ ] and deletes:[ ]
    '''
    if current == None:
        current = []
    if target == None:
        target = []
    adds = list(set(target) - set(current))
    deletes = list(set(current) - set(target))
    return {'additions': adds, 'deletions': deletes}


def main():
    parser = argparse.ArgumentParser(description='Hello. This program will calculate array differences')
    parser.add_argument('-current', type=int, nargs='+', help='the current list in the following format int, int, int ...', required=True)
    parser.add_argument('-target', type=int, nargs='+', help='the target list in the following format int, int, int ...  ', required=True)
    parser.add_argument('-assume_sets', type=int, help='If >= 1, then it will treat both lists as sets and '
                                                        'assume every element in current and target is unique. '
                                                       '\nIf < 1, then it will treat both lists as python lists')
    args = parser.parse_args()
    current = sorted(args.current)
    target = sorted(args.target)
    assume_set = args.assume_sets
    if assume_set is None:
        assume_set = 0
    if assume_set >= 1:
        diffs = calculate_difference_set(current, target)
    else:
        diffs = calculate_difference_list(current, target)
    for i in diffs:
        print('{}: {}'.format(i, diffs.get(i)))


if __name__ == '__main__':
    main()
