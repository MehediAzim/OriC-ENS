import argparse
import read
import generateFeature
import learning
import numpy as np


def main(args):
    
    X, Y = read.fetchXY(args.fasta, args.label)
    print('\nDatasets fetching done.')

    ############################################################################
    print('Features extraction begins. Be patient! The machine will take some time.')

    T = generateFeature.extract(args, X, Y)

    feature = T[:, :-1]
    label = T[:, -1]
    # print(T.shape)


    X = feature[:, int(args.category1[0]):int(args.category1[1])]  # X = T[:,0:419]
    Y = feature[:, int(args.category2[0]):int(args.category2[1])]  # Y = T[:, 420]
    Z = feature[:, int(args.category3[0]):int(args.category3[1])]  # X = T[:,0:419]

    Label1 = label
    Label2 = label
    Label3 = label
    
    learning.classifiers(X, Y, Z, Label1, Label2, Label3, args)

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from DNA, RNA, and Protein Sequences')

    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='OriC-Data.fsa')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='OriC-Label.txt')

    p.add_argument('-cv', '--nFCV', type=int, help='Number of crossValidation', default=10)

    p.add_argument('-f1', '--category1', nargs='*', help='#s feature inclusive', default=[0, 84])
    p.add_argument('-f2', '--category2', nargs='*', help='#s feature inclusive', default=[84, 148])
    p.add_argument('-f3', '--category3', nargs='*', help='#s feature inclusive', default=[148, 212])

    args = p.parse_args()

    main(args)


