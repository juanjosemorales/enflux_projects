import argparse
import pandas as pd

class Analyzer(object):

    def __init__(self, file_name=''):
        self.file_name = file_name
        self._ss = None

    def read_data(self, file_name=None, header=0):
        '''
        This method will read in the specified csv. If none is provided it will assume that a file name was provided
        upon instantiation of the object and attempt to read that instead.
        :param file_name: a csv file in the format <int,int,int>
        :param header: from the pandas documentation - "Row number(s) to use as column names and start of the data"
        '''
        if file_name is None:
            file_name = self.file_name
        try:
            self._ss = pd.read_csv(file_name, header=header, skipinitialspace=True)
        except Exception as e:
            raise Exception('There has been an error while reading the file '+str(e))

    def get_aggregates(self):
        '''
        This method will summarize the total followers of an original post (where repostID = -1).
        Worst Case Performance: O(n) from looping through a dataset with all original posts
        :return dict: a python dictionary in the format { original_post_id : followers }
        '''
        try:
            # set up a copy of the data frame that we will use to count the total number of followers
            copy_ss = self._ss.copy()
            copy_ss.columns = ['id','rID', 'number']
            copy_ss['original_post'] = 0
            # originals contains all of the original posts
            originals = sorted(copy_ss['id'][copy_ss['rID'] == -1])
            if len(originals) < 1:
                return {}
            prev = 0
            # modify our data frame copy to add another field that tells us which post this came from, ie original post
            for next in range(1, len(originals)):
                copy_ss['original_post'][(copy_ss['rID'] < originals[next]) &
                                         (copy_ss['rID'] >= originals[prev])] = originals[prev]
                prev = next
            copy_ss['original_post'][copy_ss['rID'] == originals[prev]] = originals[prev]
            copy_ss['original_post'][copy_ss['rID'] == -1] = copy_ss['id']
            # once we know where each post came from, we can sum up all of the followers and group by original post
            aggregates = copy_ss.groupby(by=[copy_ss['original_post']])['number'].sum()
            return aggregates.to_dict()
        except:
            raise Exception("Unable to aggregate posts. Make sure you provide the "
                            "appropriate csv with columns id:int,rID:int,followers:int")


def main():
    parser = argparse.ArgumentParser(description='Hello. This program summarizes posts from a csv with the following '
                                                 'format <int,int,int> ')

    parser.add_argument('-file_name', type=str, help='the csv file to be analyzed', required=True)
    args = parser.parse_args()
    file_name = args.file_name
    try:
        a = Analyzer(file_name)
        a.read_data()
        aggs = a.get_aggregates()
        for i in aggs:
            print('{}: {}'.format(i, aggs.get(i)))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
