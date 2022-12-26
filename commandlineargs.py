import argparse
parser=argparse.ArgumentParser(description='find the average')
parser.add_argument('integers',nargs='+',type=float,help='an integers required')
parser.add_argument('sum',action='store_const',const=sum,help='calculate sum')
parser.add_argument('len',action='store_const',const=len,help='calculate length')
args=parser.parse_args()
add=args.sum(args.integers)
length=args.len(args.integers)
avg=add/length
print(avg)




